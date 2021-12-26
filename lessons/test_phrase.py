class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase: ")
        assert 15 > len(phrase)