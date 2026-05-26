# =====================================================
# IMPORTS
# =====================================================

from youtube_transcript_api import (

    YouTubeTranscriptApi,

    TranscriptsDisabled
)

# =====================================================
# VIDEO ID
# =====================================================

video_id = "Gfr50f6ZBvo"

# =====================================================
# FETCH TRANSCRIPT
# =====================================================

try:

    transcript_list = YouTubeTranscriptApi.get_transcript(

        video_id,

        languages=["en"]
    )

    # =================================================
    # CONVERT LIST OF CHUNKS INTO SINGLE TEXT
    # =================================================

    transcript = " ".join(

        chunk["text"]

        for chunk in transcript_list
    )

    print(transcript)

except TranscriptsDisabled:

    print("No captions available.")