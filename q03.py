#!/usr/bin/python
import re

ssn = raw_input("Enter SSN:")

print "By strict SSN rules:",("SSN Valid" if re.match(r"^(?!(000|666|9))\d{3}-(?!00)\d{2}-(?!0000)\d{4}$",ssn) else "SSN Invalid")

print "By SSN pattern:",("SSN Valid" if re.match(r"^(\d{3}-?\d{2}-?\d{4}|XXX-XX-XXXX)$",ssn.upper()) else "SSN Invalid")

