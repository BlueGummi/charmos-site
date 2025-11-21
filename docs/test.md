# Big Idea: Turnstiles (EXPERIMENTAL)
**Credits:** Eleanor Semaphore

# Alerts
This is still EXPERIMENTAL. Be wary of bugs that may be from this component.

# Audience
Synchronization subsystem authors and others interested. not necessary to read.

# Overview
Turnstiles give us pointer sized adaptive mutexes (see "Locking Philosophy" [^1])...

# Background
Turnstiles were invented by Solaris, and are used in FreeBSD and XNU...

# Summary
Turnstiles give us a unified structure with functionalities... this functionality is provided by turnstile_block()...

# API
Turnstiles expose these functions, use them like such...

# Interactions
Turnstiles are used in our mutex implementation and are not to be used on their own outside of tests...

# Constraints
Turnstiles must be efficient and avoid taking the slow blocking path too frequently...

# Errors
Turnstiles don't "fail", but these things can... [`reference()`](https://github.com/bluegummi/charmos/blob/main/test.c#L33)

[#67](https://github.com/bluegummi/charmos/issues/67)

# Rationale
Turnstiles spin when the owner is running because it avoids a slowpath...

# Diagrams

-- note: diagrams should have the 3 grave stones preceding and following them. this is omitted
here because this document is also in markdown and that would interfere with this.
```
                 Diagram A: Turnstile Donation

             turnstile       ┌────────────┐      no existing
             ┌─exists────────│   Block    │───────turnstile┐
             │               └────────────┘                │
             │                                             │
             │                                             │
             │                                             │
             ▼                                             ▼
 ┌─────────────────────────┐                      ┌──────────────────┐
 │Add Turnstile to freelist│                      │ Donate Turnstile │
 └─────────────────────────┘                      └──────────────────┘
```

# Bugs
  Issue [#44](https://github.com/bluegummi/charmos/issues/44) "missed wakeup"


# Tests
  [`./kernel/tests/turnstile.c`](https://github.com/bluegummi/charmos/blob/main/./kernel/tests/turnstile.c) - general turnstile tests
  [`./kernel/tests/mutex.c`](https://github.com/bluegummi/charmos/blob/main/./kernel/tests/mutex.c) - general mutex tests that use turnstiles

# References
[^1] "Locking Philosophy" [`./docs/locking_idea.md`](https://github.com/bluegummi/charmos/blob/main/./docs/locking_idea.md)

# Changelog
  09/02/2005 - Eleanor Semaphore: Added second queue for rwlocks (commit 0b4e)
  09/01/2005 - Eleanor Semaphore: Created Idea (commit 62ef)

# Notes
  Here is some stuff you might be interested in reading regarding the history of turnstiles

/

## Functions
- [`reference()`](https://github.com/bluegummi/charmos/blob/main/test.c#L33)
