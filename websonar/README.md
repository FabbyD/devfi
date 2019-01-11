Websonar
--------------------

Web Browser Controller with hand gestures using a sonar and Arduino! Because fun?

Very simple hand gestures are supported obviously since a sonar is not that precise.

### Gestures

All gestures are detected by zones. The area in front of the sonar is divided in three zones in order to simplify gesture detection.

```
                                                                                            _.-._
                                                                                           | | | |_ 
  /|                                                                                       | | | | |
 | | |------- Zone 0 -------|------- Zone 1 -------|------- Zone 2 -------|              _ |  '-._ |
  \|                     |~~~~~|                |~~~~~|                |~~~~~|           \`\`-.'-._;
(Sonar)                                                                                   \    '   |
                                                                                           \  .`  /
                                                                                            |    |
```

The wiggly areas under zone boundaries indicate a tolerance I set so the user does not swap zones involuntarily when close to boundaries. In order to actually enter a new zone, you have to go over that tolerance.

| Gesture     | Description                  |
|:------------|:-----------------------------|
| Tap (zone)  | Quick detection in a zone    |
| Hold (zone) | Long detection in a zone     |
| Swipe in    | Detection of the zones 2,1,0 |
| Swipe out   | Detection of the zones 0,1,2 |
| Wiggle      | Detection of the zones 0,1,0 |

Very simple noise filtering was used on the sonar data: average of the last 10 readings.

Here is a summary of what browser actions are supported and their associated hand gestures. You may swap tools at any time by doing the wiggle hand gesture.

### Browser tool

This is the main tool used to move around in a web browser.

| Action      | Gesture (Zone) |
|:------------|:--------------:|
| Enter       |    Tap (0)     |
| Shift-tab   |    Tap (1)     |
| Scroll down |    Hold (0)    |
| Tab         |    Hold (1)    |
| Scroll Up   |    Hold (2)    |
| Go Forward  |    Swipe in    |
| Go Back     |    Swipe out   |

### Keyboard tool

When using this tool, a virtual keyboard pops up (only available in Linux) in order to type in input fields.

| Action            | Gesture (Zone) |
|:------------------|:--------------:|
| Move cursor right |    Hold (0)    |
| Move cursor left  |    Hold (2)    |
| Move cursor up    |    Swipe in    |
| Move cursor down  |    Swipe out   |
| Type              |    Tap         |

