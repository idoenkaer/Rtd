import random

responses = [
    "A new path will reveal itself when you least expect it; be ready to walk it.",
    "The whispers of the past hold a clue to your greatest triumph.",
    "A chance encounter with a stranger will change the course of your next year.",
    "The answer you seek lies not in words, but in the silence between them.",
    "What you have lost will be returned to you in a different, more valuable form.",
    "The smallest act of kindness you perform today will echo in your future.",
    "A decision you make tomorrow will lead to a new beginning.",
    "Do not fear the darkness, for it is there you will find a hidden light.",
    "The strength you need is already within you, waiting to be awakened.",
    "A long-held dream is closer to fruition than you believe.",
    "A challenge you face now is but a test, preparing you for a greater victory.",
    "The key to unlocking your destiny is found in forgiving someone.",
    "Prosperity will come to you through an unexpected source.",
    "Trust your intuition, for it will guide you through a confusing time.",
    "A journey is ahead of you, one that will change your perspective entirely.",
    "The truth you have been searching for will be revealed in a flash of insight.",
    "A beautiful friendship will blossom from an unlikely connection.",
    "The stars align to favor a bold move you are contemplating.",
    "Your future is not set in stone; your choices shape the path.",
    "The Shadow on the Wall: You are looking at the shadow and not the object that casts it. The answer you seek is not in the form of a simple confirmation or denial, but in understanding the true nature of the question's source. To receive clarity, you must turn to face the light that projects the shadow. Your current path is a reflection of a deeper desire, and the resolution lies in acknowledging that unvoiced need.",
    "The Fated Crossroads: You stand at a crossroads where all three paths are fated for you. The path to the left leads to a resounding yes, but through hardship. The path to the right leads to an immediate no, but with an unexpected blessing. The path straight ahead is the maybe, where you must forge your own destiny without the guidance of prophecy. The choice is not about the outcome, but the journey you wish to endure.",
    "The Shifting Sands of Time: Do not mistake the shifting of the sands for the final count. What appears to be an affirmation today may be revealed as a postponement tomorrow, and a denial may be the beginning of a greater opportunity in the long run. The answer you seek is a living, breathing thing, changing and evolving with the universe. It is not static, and its final form has not yet been decided.",
    "The Unspoken Word: The answer is a word that cannot be spoken, a truth that must be felt. Trying to categorize it as 'yes' or 'no' is like trying to hold water in a net. It is a feeling of knowing, a quiet certainty that will settle upon you when you cease to search for a definitive verbal response. This is not a matter of logic, but of intuition, and the universe is guiding you toward this silent realization."
]

question = input("Ask the Magic 8-Ball a question: ")
print(random.choice(responses))
