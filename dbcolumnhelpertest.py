import unittest

import dbcolumnhelper

class TestDBColumnHelper(unittest.TestCase):
  
  def test_classExists(self):
    self.assertIsNotNone(dbcolumnhelper)

  def test_counts0Phrases(self):
    rtn = dbcolumnhelper.Parse([""])
    self.assertEqual(rtn[0].Count, 0)

  def test_counts1Phrase(self):
    rtn = dbcolumnhelper.Parse(["Phrase"])
    self.assertEqual(rtn[0].Count, 1)

  def test_counts2Phrases(self):
    rtn = dbcolumnhelper.Parse(["Phrase", "Phrase"])
    self.assertEqual(rtn[0].Count, 2)
  
  def test_counts2DifferentPhrases(self):
    rtn = dbcolumnhelper.Parse(["Phrase1", "Phrase2"])
    self.assertEqual(rtn[0].Count, 1)
    self.assertEqual(rtn[1].Count, 1)

  def test_records2DifferentPhrases(self):
    rtn = dbcolumnhelper.Parse(["Phrase1", "Phrase2"])
    self.assertEqual(rtn[0].Phrase, "Phrase1")
    self.assertEqual(rtn[1].Phrase, "Phrase2")

  def test_splitsString(self):
    rtn = dbcolumnhelper.Parse(["Phrase1; Phrase2"])
    self.assertEqual(rtn[0].Count, 1)
    self.assertEqual(rtn[1].Count, 1)

  def test_splitRemovesWhitespaceBetweenSemicolons(self):
    rtn = dbcolumnhelper.Parse(["Phrase1; Phrase2"])
    self.assertEqual(rtn[0].Phrase, "Phrase1")
    self.assertEqual(rtn[1].Phrase, "Phrase2")

  def test_stringsCaseInsensitive(self):
    rtn = dbcolumnhelper.Parse(["Phrase1", "phrase1"])
    self.assertEqual(rtn[0].Phrase, "Phrase1")
    self.assertEqual(rtn[0].Count, 2)

  def test_stringsCaseInsensitiveMuliplePhrases(self):
    rtn = dbcolumnhelper.Parse(["Phrase1; phrase2", "phrase1; Phrase2"])
    self.assertEqual(rtn[0].Phrase, "Phrase1")
    self.assertEqual(rtn[0].Count, 2)
    self.assertEqual(rtn[1].Phrase, "Phrase2")
    self.assertEqual(rtn[1].Count, 2)

  def test_trimsWhitespaceAroundPhrases(self):
    rtn = dbcolumnhelper.Parse(["  Phrase1 ; Phrase2     "])
    self.assertEqual(rtn[0].Phrase, "Phrase1")
    self.assertEqual(rtn[0].Count, 1)
    self.assertEqual(rtn[1].Phrase, "Phrase2")
    self.assertEqual(rtn[1].Count, 1)

  def test_displaysDataFromGreatestCountToLeast(self):
    rtn = dbcolumnhelper.Parse(["Phrase1; Phrase2", "Phrase2"])
    self.assertEqual(rtn[0].Phrase, "Phrase2")
    self.assertEqual(rtn[0].Count, 2)
    self.assertEqual(rtn[1].Phrase, "Phrase1")
    self.assertEqual(rtn[1].Count, 1)

  def test_countsPhraseInRowOnlyOnce(self):
    rtn = dbcolumnhelper.Parse(["Phrase1; Phrase1", "Phrase1"])
    self.assertEqual(rtn[0].Phrase, "Phrase1")
    self.assertEqual(rtn[0].Count, 2)
