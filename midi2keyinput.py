import sys
import keyboard
import pygame
import pygame.midi

# 以下のキーは好みに応じて変更することが出来ます
midi_to_key = {
    47: 'a',
    48: 's',
    50: 'd',
    52: 'SPACE',
    53: 'g',
    54: 'y',
    55: 'h',
    56: 'u',
    57: 'j',
    58: 'i',
    59: 'k',
    60: 'l',
    45: 'SHIFT',
    49: 'w',
    51: 'f',
    46: 'ESCAPE',
    44: 'TAB',
    43: 'e',
    42: 'q',
    61: 'o',
    63: 'n',
}

def midi_to_keyboard():
    pygame.init()
    pygame.midi.init()

    try:
        input_device_id = 1 # デバイスIDは合うものに変えてください
        midi_input = pygame.midi.Input(input_device_id)

        while True:
            if midi_input.poll():
                midi_events = midi_input.read(10)
                for midi_event in midi_events:
                    status, note, velocity, _ = midi_event[0]

                    if status & 0xF0 == 0x90 and velocity > 0:
                        if note in midi_to_key:
                            key = midi_to_key[note]
                            keyboard.press(key)
                            print(f"MIDI Note On: {note}, Key Down: {key}")

                    elif status & 0xF0 == 0x80 or (status & 0xF0 == 0x90 and velocity == 0):
                        if note in midi_to_key:
                            key = midi_to_key[note]
                            keyboard.release(key)
                            # print(f"MIDI Note Off: {note}, Key Up: {key}")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    finally:
        pygame.midi.quit()
        pygame.quit()

if __name__ == "__main__":
    midi_to_keyboard()
