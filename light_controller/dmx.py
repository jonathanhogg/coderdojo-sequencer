#!/usr/bin/python

import sys
import serial
import glob
from traits.api import (HasTraits, Int, Str, List, Float, Instance, Bool, Tuple, 
                        Either, Range, Property, ReadOnly, cached_property, on_trait_change)


class Fixture(HasTraits):
    base = ReadOnly
    slots = Property(depends_on='-ignore', ignore=True)

class DimmableColor(Fixture):
    red = Property(lambda self: self.color[0])
    green = Property(lambda self: self.color[1])
    blue = Property(lambda self: self.color[2])
    color = Tuple(Float, Float, Float)
    intensity = Float

class MovingHead(Fixture):
    pan = Float
    tilt = Float
    speed = Float(1)

class Gobo(Fixture):
    gobo = Int
    shake = Float

class Strobe(Fixture):
    strobe = Float


class DMXController(HasTraits):
    port = Either(None, Str)
    tty = Property(depends_on='port')
    fixtures = List(Instance(Fixture))
    enabled = Bool
    debug = Bool
    channels = Range(value=128, low=1, high=512)
    _slots = List(Int)
    slots = Property(lambda self: self._slots)

    def _port_default(self):
        ports = glob.glob('/dev/tty.usb*') + glob.glob('/dev/ttyACM*')
        if ports:
            return ports[0]

    @cached_property
    def _get_tty(self):
        if self.port:
            return serial.Serial(self.port, 115200)

    def write(self, *args):
        command = ''.join(str(arg) for arg in args) + '\r\n'
        if self.debug:
            sys.stdout.write(command)
        if self.tty:
            self.tty.write(command)
            self.tty.flush()

    def _channels_changed(self):
        self.write('m', self.channels)

    @on_trait_change('enabled,fixtures,fixtures_items,fixtures:slots')
    def _update(self, obj, name, old, new):
        if name == 'enabled':
            self.write('e', 1 if self.enabled else 0)
            self._slots = []
        if self.enabled:
            slots = [0] * 512
            max_channel = 0
            for fixture in self.fixtures:
                for i, value in enumerate(fixture.slots):
                    channel = fixture.base + i
                    slots[channel - 1] = min(255, max(0, value))
                    if channel > max_channel:
                        max_channel = channel
            if max_channel > self.channels:
                self.channels = max_channel
            old_slots = self._slots or [0] * 512
            for channel, value in enumerate(slots):
                if value != old_slots[channel]:
                    self.write('c', channel + 1)
                    self.write('w', value)
            self._slots = slots


class EuroliteMovingHeadWash(MovingHead, Strobe, DimmableColor):
    def _get_slots(self):
        pan = int((self.pan + 270.) / 540. * 65535)
        tilt = int((self.tilt + 90.) / 180. * 65535)
        strobe = 31 + int(self.strobe * 169) if self.strobe else 255
        return [pan >> 8, tilt >> 8, int((1. - self.speed) * 255),
                int(self.red * 255), int(self.green * 255), int(self.blue * 255),
                0, strobe, int(self.intensity * 255), pan & 255, tilt & 255]

class VarytecMovingHeadSpot(MovingHead, Strobe, DimmableColor, Gobo):
    def _get_slots(self):
        pan = int((self.pan + 270.) / 540. * 65535)
        tilt = int((self.tilt + 105.) / 210. * 65535)
        if self.strobe:
            dimmer = 135 + int(self.strobe * 104)
        else:
            dimmer = 0 if self.intensity < (1./127) else 135 - int(self.intensity * 127)
        return [pan >> 8, pan & 255, tilt >> 8, tilt & 255, int((1. - self.speed) * 255),
                dimmer, int(self.red * 255), int(self.green * 255), int(self.blue * 255),
                0, 0, 0, self.gobo * 8 if not self.shake or not self.gobo else 65 + self.gobo * 15 + int(self.shake * 14)]


if __name__ == '__main__':
    wash = EuroliteMovingHeadWash(base=1, color=(1, 0, 0.5), intensity=1)
    controller = DMXController(debug=True, fixtures=[wash])
    controller.enabled = True

