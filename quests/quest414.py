from difflib import SequenceMatcher


def steps_to_convert(*lines):
    seq = SequenceMatcher(None, *sorted(lines, key=len))
    return sum(stop - start for diff, _, _, start, stop in seq.get_opcodes()
               if diff in ['replace', 'insert'])
