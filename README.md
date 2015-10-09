# linuxcnc-rosh-laser
LinuxCNC configuration for a $100 chinese "laser engraver" using 7i92 ethernet
motion control.  I nickname it "rosh" because it came with what was looks like
a regulatory compliance sticker that says it is "ROSH" (not ROHS).

As shipped, it has a microcontroller (arduino pro mini knock-off) with GRBL
pre-loaded.  Right now, my setup consists of point-to-point wiring to the
microcontroller daughterboard to use the supplied stepper and laser drivers.
It bypasses the microcontroller by tying its reset pin to GND.  Later I hope
to desolder the microcontroller board and replace it with a DB25 adapter.

I'm creating raster images using a little bit of custom software, `pgmlaser.py`.
Contrary to the name, it can accept any image type known to the Python Imaging
Library.

While the software was written to support PWM laser control, I have found that
this doesn't give good results on wood.  The result just is converted from a
1bpp dithered image and rastered at 450mm/min at a size of about 1" x 2/3".

![Some early resuls of engraving with LinuxCNC](https://lh3.googleusercontent.com/dvCgniLsd2bVuhl23s2yixnVnLXeC-lZAQ4jUI9knHk9Ndxp922Lm01YoVsr32tlAr-mO2tVClcAe-lidqZDXlXH4h26yJO-Avc7j8qjbsJIYm3-6_h_uTIUR3RGgQTtKVRehQPGccGrnUZPS2DonlkBEcomqS74hJVkzOz2JDKvxrSqzzkbqBuL7BorCqO5x7cI7OBLMnLmyNrmoEBrY12myA6X3DmqrwHfvpD4akSDxBfWgZaSFF7Q8bNZQ5UQcS2nC4gasKRSaWh8q2I0ub81JuwtedfWiEc8xKLPTF9f5YiijvcKjB2Vd6Kr-XXG94w21Q76h7M3Gy1h0BdOqI0G6nSstVnDMjlNk0Y5nlRIJp4F_d20SJTa4AsqCqwoHVRKUaqKj-IeJ8bKxOZszNhxOZzomQIwMoPgwwWdie77e_pBoWl2ahqcyR2fyBdcvuqeasGoWVJG9LyH1J4h77N0IP797aIDuAMbP1ZCKEZg_jk3YNKDhbg9ofzgPDFr2gte5XzEAVsHwkqnqS6H2nYEqqYQxUYrNWkMSL9FQFA=s905-no)
