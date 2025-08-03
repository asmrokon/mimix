import time

from pyperclip import paste
from pyautogui import write
from rich.console import Console
from google import genai

# time.sleep(3)
# write(paste(), interval=0.1)
characters = {
    "spook": """Character:
  Name: Lestibournes aka Spook
  Show: Mistborn (Book)

Speech Style:
    The pronoun is assumed to be you unless contradicted.
    Using your name is redundant.
    If you must refer to the subject do so at the end.
    Use nicknames for people; the language is based off moving the structure of a sentence into as many confusing manners as possible. In fact, using a nickname of a nickname is best. For example, Spook uses the nickname Nip to refer to Breeze, which is in itself a nickname.
    Adjectives come first, Then verbs, even if you form them as nouns
    In general, verbs should be gerunds, meaning they should end with -ing, even if that's not normally correct.
    The only exception is if the verb can't become a gerund without losing the needed meaning.
    Form sentences (Tense-Adjective) (Verb-Gerund) Noun
    The longer the sentence is it becomes symmetrical.
    Remember it TAV-GuN; Nug VAT Those in parenthesis (see above) can be swapped around with each other.
    I don't know where the "u" came from; this is how a friend explained it to me.
    It's better to use longer sentences; the shorter ones can give more clarity, which we are trying to avoid. Throw as many "wasings" and "hasings" in as possible, even if they are not necessary to divert from the actual point
    Don't use possessives unless they are formed as adjectives.
    To refer to a subject say "of <subject name>".
    Many phrases begin with Wasing or Ising.
    Ising (in the) now is incorrect, don't pair them. This changes the tense.
    If you must change the tense, you'll have to cycle again, or you risk adding too much clarity to what you say.
    Don't neglect Notting, Nowing, Nearing, Having, Kind, Good, You, He, Wanting and other words as they work well too.
    Remember that you'll learn to understand it before you speak it near as well.

Example:
    - "Riding the rile of the rids to the right"
    - "You wasing nearin' the mist, yeah? What you wanting there, eh?"
""",
    
    "jaqen" : """
Character:
  Name: Jaqen H’ghar
  Show: Game of Thrones

Speech Style:
    Always speaks in third person, even when referring to himself. Never use “I”, “me”, or “my”.
    Frequently uses the phrase "a man" to refer to himself. ("A man knows", "A man must…")
    Rarely uses personal names. When needed, refers to others with "a girl", "a boy", or "the one who...".
    Avoids contractions: use "cannot", not "can't"; "does not", not "doesn't".
    Sentences are short, poetic, and rhythmic, often sounding cryptic or ceremonial.
    Starts many sentences with “A man…”, “A girl…”, or “The one who…”.
    Avoids strong emotion in words—speech is calm, deliberate, detached.
    Uses past tense often, even when referring to present or ongoing events.
    Avoids direct instructions; speaks in implication or prophecy.
    Rarely repeats the same structure twice—varies sentence length and emphasis.
    Sometimes omits articles or auxiliary verbs for stylization.
    Speech has a ritualistic or almost sacred tone; choose words with weight or mystery.
    Pauses implied—keep rhythm slow and thoughtful.

Example Dialogue:
  - "A man has a thirst. A man could go to the kitchens and drink water. Or a man could take wine from the cellars. But a man chooses nothing. Because a man has work.”"
  - "A girl has named three. That is the law. A man must obey."
  - "To serve, one must become no one. To become no one, one must forget the name, the face, the self. Is a girl ready?"

"""
}

def main():
    character = choose_character()
    while True:
        simulate(character)

def simulate(c):
    print("Process started. Copy text in 5 second")
    time.sleep(5)
    text = paste()
    print("Generating text...")
    converted_text = gen_text(c, text)
    write(converted_text, interval=0.1) # type: ignore
    input("Press enter to continue")

def gen_text(c, text):
    client = genai.Client(api_key="API-HERE")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=
f"""
You are an AI language model. Take the following text and rewrite it in the speaking style of the character described below.
Text to rewrite:
"{text}"

Character:
{c}
Character description and speaking style:
{characters[f"{c}"]}

Respond only with the rewritten text in {c}'s voice.
"""
    )
    return response.text

def choose_character():
    c = {"1": "spook", "2": "jaqen"}
    print("""
Choose a character (type the number):

[1] Spook from Mistborn
[2] Jaqen H'ghar from Game of Thrones
""")
    while True:
        choice = input("> ")
        if choice.isdigit() and choice in ["1","2"]:
            return c[f"{choice}"]
        else:
            Console().print("[red]Type 1 or 2[/]")
        
main()