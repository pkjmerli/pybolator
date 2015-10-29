from random import randint
from time import sleep
import sys


_LEDS_AMOUNT = 4


class _Accel:

    def x(self):
        sys.stderr.write("ACCEL:\n")
        sys.stderr.write("\tx\n")

        return randint(0, 10)

    def y(self):
        sys.stderr.write("ACCEL:\n")
        sys.stderr.write("\ty\n")

        return randint(0, 10)

_accel = _Accel()


class _LED:

    state = False
    intensity_value = 0

    def __init__(self, led):
        self.led = led

    def on(self):
        self.state = True
        sys.stderr.write("LED %s:\n" % self.led)
        sys.stderr.write("\t on\n")

    def off(self):
        self.state = False
        sys.stderr.write("LED %s:\n" % self.led)
        sys.stderr.write("\t off\n")

    def toggle(self):
        if self.state:
            return self.off()
        return self.on()

    def intensity(self, value):
        self.intensity_value = value
        sys.stderr.write("LED %s:\n" % self.led)
        sys.stderr.write("\t intensity %s\n" % self.intensity_value)


_leds = [_LED(i) for i in range(_LEDS_AMOUNT)]


class _Switch:

    status = False
    callable = None

    def __call__(self):
        sys.stderr.write("SWITCH:\n")
        sys.stderr.write("\t call > %s\n" % self.status)

        return self.status

    def callback(self, callable):
        self.callable = callable
        sys.stderr.write("SWITCH:\n")
        sys.stderr.write("\t callback %s\n" % self.callable)

    def _down(self):
        self.status = True
        self.callable()

    def _up(self):
        self.status = False


_switch = _Switch()


def _run_code():
    def target():
        import os
        MAIN_FILENAME = os.environ.get("PYBOLATOR_MAIN", "main.py")
        obj = compile(open(MAIN_FILENAME).read(), MAIN_FILENAME, 'exec')
        exec(obj, globals())

    import threading
    thread = threading.Thread(target=target)
    thread.start()


### pyb method and classes

def Accel():
    return _accel


def ADC(pin):
    """http://docs.micropython.org/en/latest/library/pyb.ADC.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def ADCAll(resolution):
    """http://docs.micropython.org/en/latest/library/pyb.ADC.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def CAN(bus):
    """http://docs.micropython.org/en/latest/library/pyb.CAN.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def DAC(port, bits=8):
    """http://docs.micropython.org/en/latest/library/pyb.DAC.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def ExtInt(pin, mode, pull, callback):
    """http://docs.micropython.org/en/latest/library/pyb.ExtInt.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def I2C(bus):
    """http://docs.micropython.org/en/latest/library/pyb.I2C.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def LCD(skin_position):
    """http://docs.micropython.org/en/latest/library/pyb.LCD.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def LED(number):
    return _leds[number - 1]


def Pin(id):
    """http://docs.micropython.org/en/latest/library/pyb.Pin.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


# http://docs.micropython.org/en/latest/library/pyb.Pin.html#class-pinaf-pin-alternate-functions


def RTC():
    """http://docs.micropython.org/en/latest/library/pyb.RTC.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def Servo(id):
    """http://docs.micropython.org/en/latest/library/pyb.Servo.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def SPI(bus, mode, **kwargs):
    """http://docs.micropython.org/en/latest/library/pyb.SPI.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def Timer(id, **kwargs):
    """http://docs.micropython.org/en/latest/library/pyb.Timer.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def UART(bus, baudrate):
    """http://docs.micropython.org/en/latest/library/pyb.UART.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def USB_VCP():
    """http://docs.micropython.org/en/latest/library/pyb.USB_VCP.html"""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def Switch():
    return _switch


def delay(miliseconds):
    sys.stderr.write("PYB:\n")
    sys.stderr.write("\tdelay %s\n" % miliseconds)
    sleep(miliseconds / 1000)


def udelay(us):
    """Delay for the given number of microseconds."""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def millis():
    """Returns the number of milliseconds since the board was last reset.

    The result is always a micropython smallint (31-bit signed number), so
    after 2^30 milliseconds (about 12.4 days) this will start to return
    negative numbers.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def micros():
    """Returns the number of microseconds since the board was last reset.

    The result is always a micropython smallint (31-bit signed number), so
    after 2^30 microseconds (about 17.8 minutes) this will start to return
    negative numbers.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def elapsed_millis(start):
    """Returns the number of milliseconds which have elapsed since ``start``.

    This function takes care of counter wrap, and always returns a positive
    number. This means it can be used to measure periods upto about 12.4 days.

    Example::

        start = pyb.millis()
        while pyb.elapsed_millis(start) < 1000:
            # Perform some operation
    """


def elapsed_micros(start):
    """Returns the number of microseconds which have elapsed since ``start``.

    This function takes care of counter wrap, and always returns a positive
    number. This means it can be used to measure periods upto about 17.8 minutes.

    Example::

        start = pyb.micros()
        while pyb.elapsed_micros(start) < 1000:
            # Perform some operation
            pass
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def hard_reset():
    """Resets the pyboard in a manner similar to pushing the external RESET
    button.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def bootloader():
    """Activate the bootloader without BOOT\* pins."""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def disable_irq():
    """Disable interrupt requests.
    Returns the previous IRQ state: ``False``/``True`` for disabled/enabled IRQs
    respectively.  This return value can be passed to enable_irq to restore
    the IRQ to its original state.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def enable_irq(state=True):
    """Enable interrupt requests.
    If ``state`` is ``True`` (the default value) then IRQs are enabled.
    If ``state`` is ``False`` then IRQs are disabled.  The most common use of
    this function is to pass it the value returned by ``disable_irq`` to
    exit a critical section.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def freq(sysclk=None, hclk=None, pclk1=None, pclk2=None):
    """If given no arguments, returns a tuple of clock frequencies:
    (sysclk, hclk, pclk1, pclk2).
    These correspond to:

        - sysclk: frequency of the CPU
        - hclk: frequency of the AHB bus, core memory and DMA
        - pclk1: frequency of the APB1 bus
        - pclk2: frequency of the APB2 bus

    If given any arguments then the function sets the frequency of the
    CPU, and the busses if additional arguments are given.
    Frequencies are given in Hz.  Eg freq(120000000) sets sysclk (the
    CPU frequency) to 120MHz.  Note that not all values are supported
    and the largest supported frequency not greater than the given
    value will be selected.

    Supported sysclk frequencies are (in MHz): 8, 16, 24, 30, 32, 36,
       40, 42, 48, 54, 56, 60, 64, 72, 84, 96, 108, 120, 144, 168.

    The maximum frequency of hclk is 168MHz, of pclk1 is 42MHz, and of
    pclk2 is 84MHz.  Be sure not to set frequencies above these
    values.

    The hclk, pclk1 and pclk2 frequencies are derived from the sysclk
    frequency using a prescaler (divider).  Supported prescalers for
    hclk are: 1, 2, 4, 8, 16, 64, 128, 256, 512.  Supported prescalers
    for pclk1 and pclk2 are: 1, 2, 4, 8.  A prescaler will be chosen
    to best match the requested frequency.

    A sysclk frequency of 8MHz uses the HSE (external crystal)
    directly and 16MHz uses the HSI (internal oscillator) directly.
    The higher frequencies use the HSE to drive the PLL (phase locked
    loop), and then use the output of the PLL.

    Note that if you change the frequency while the USB is enabled
    then the USB may become unreliable.  It is best to change the
    frequency in boot.py, before the USB peripheral is started.  Also
    note that sysclk frequencies below 36MHz do not allow the USB to
    function correctly.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def wfi():
    """Wait for an internal or external interrupt.

       This executes a ``wfi`` instruction which reduces power
       consumption of the MCU until any interrupt occurs (be it
       internal or external), at which point execution continues.
       Note that the system-tick interrupt occurs once every
       millisecond (1000Hz) so this function will block for at most
       1ms.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def stop():
    """Put the pyboard in a "sleeping" state.

       This reduces power consumption to less than 500 uA.  To wake
       from this sleep state requires an external interrupt or a
       real-time-clock event.  Upon waking execution continues where
       it left off.

       See :meth:`rtc.wakeup` to configure a real-time-clock wakeup
       event.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def standby():
    """Put the pyboard into a "deep sleep" state.

       This reduces power consumption to less than 50 uA.  To wake
       from this sleep state requires a real-time-clock event, or an
       external interrupt on X1 (PA0=WKUP) or X18 (PC13=TAMP1).  Upon
       waking the system undergoes a hard reset.

       See :meth:`rtc.wakeup` to configure a real-time-clock wakeup
       event.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def have_cdc():
    """Return True if USB is connected as a serial device, False otherwise.

       This function is deprecated.  Use pyb.USB_VCP().isconnected()
       instead.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def hid(buttons, x, y, z):
    """Takes a 4-tuple (or list) and sends it to the USB host (the PC) to
    signal a HID mouse-motion event.

    This function is deprecated.  Use pyb.USB_HID().send(...) instead.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def info(dump_alloc_table=None):
    """Print out lots of information about the board."""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def main(filename):
    """Set the filename of the main script to run after boot.py is
    finished.  If this function is not called then the default file
    main.py will be executed.
    
    It only makes sense to call this function from within boot.py.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def mount(device, mountpoint, *args, readonly=False, mkfs=False):
    """Mount a block device and make it available as part of the
       filesystem.  ``device`` must be an object that provides the
       block protocol:

        - ``readblocks(self, blocknum, buf)``
        - ``writeblocks(self, blocknum, buf)`` (optional)
        - ``count(self)``
        - ``sync(self)`` (optional)

       ``readblocks`` and ``writeblocks`` should copy data between
       ``buf`` and the block device, starting from block number
       ``blocknum`` on the device.  ``buf`` will be a bytearray with
       length a multiple of 512.  If ``writeblocks`` is not defined
       then the device is mounted read-only.  The return value of
       these two functions is ignored.

       ``count`` should return the number of blocks available on the
       device.
       ``sync``, if implemented, should sync the data on the device.

       The parameter ``mountpoint`` is the location in the root of the
       filesystem to mount the device.  It must begin with a
       forward-slash.

       If ``readonly`` is ``True``, then the device is mounted
       read-only, otherwise it is mounted read-write.

       If ``mkfs`` is ``True``, then a new filesystem is created if
       one does not already exist.

       To unmount a device, pass ``None`` as the device and the mount
       location as ``mountpoint``.
    """
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def repl_uart(uart):
    """Get or set the UART object where the REPL is repeated on."""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def rng():
    """Return a 30-bit hardware generated random number."""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def sync():
    """Sync all file systems."""
    raise NotImplementedError("Contribute on github.com/alej0varas/pybolator")


def unique_id():
    """Returns a string of 12 bytes (96 bits), which is the unique ID of
    the MCU.
    """
