import language_tool_python


def correct_mistakes(text):
    tool = language_tool_python.LanguageTool("en-US")

    # text = """LanguageTool offers spell and grammar checking.
    # Just paste your text here and click the 'Check Text' button.
    # Click the colored phrases for details on potential errors.
    # or use this text too see an few of of the problems that
    # LanguageTool can detecd. What do you thinks of grammar checkers?
    # Please not that they are not perfect. Style issues get a blue marker:
    # It's 5 P.M. in the afternoon. The weather was nice on Thursday, 27 June 2017"""

    matches = tool.check(text)

    corrections = []
    mistakes = []
    errorStartPosition = []
    errorEndPosition = []

    for match in matches:
        # To check if there are any correct replacement available
        if len(match.replacements) > 0:
            errorStartPosition.append(match.offset)
            errorEndPosition.append(match.offset + match.errorLength)
            mistakes.append(text[match.offset : match.offset + match.errorLength])
            corrections.append(match.replacements[0])

    # Converting our originaltext into list
    newText = list(text)

    for i in range(len(errorStartPosition)):
        for j in range(len(text)):
            newText[errorStartPosition[i]] = corrections[i]
            if j > errorStartPosition[i] and j < errorEndPosition[i]:
                newText[j] = ""

    # Joining our list to convert to string
    newText = "".join(newText)

    return newText
