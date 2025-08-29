# BeNative

become a native speaker with AI on your device

```
+-------------------------------------------------------+
|                    BeNative (Desktop)                 |
+-------------------------------------------------------+

 UI Layer (Electron/JS)
 --------------------------------------------------------
 | - Tampilan percakapan (chat UI, mic button, text box)|
 | - Audio capture (mic)                                |
 | - Audio playback (speaker)                           |
 | - Komunikasi IPC (spawn python, kirim JSON)          |
 --------------------------------------------------------
                      |
                      | JSON Message (IPC)
                      v
 Core Engine (Python)
 --------------------------------------------------------
 | Application Layer (Controller)                       |
 |  - Mengatur alur: STT -> LLM -> Grammar -> TTS       |
 |                                                      |
 | Domain Layer (Interfaces)                            |
 |  - SpeechToText                                      |
 |  - ConversationalAgent                               |
 |  - GrammarChecker                                    |
 |  - TextToSpeech                                      |
 |                                                      |
 | Infrastructure Layer (Implementasi)                  |
 |  - WhisperSTT (offline)                              |
 |  - Phi3Agent / MistralAgent (offline LLM)            |
 |  - GrammarCorrector (pakai LLM juga)                 |
 |  - CoquiTTS (offline TTS)                            |
 |                                                      |
 | Plugin System                                        |
 |  - Folder plugins/ untuk modul baru                  |
 --------------------------------------------------------
```

## Struktur folder

```
BeNative/
├── ui/                         # Electron (UI)
│   ├── src/
│   │   ├── components/         # Chat UI, mic button, dsb
│   │   ├── ipc.js              # Modul komunikasi dengan Python
│   │   └── ...
│   └── package.json
│
├── core/                       # Python AI Core
│   ├── app/                    # Application layer (controller)
│   │   └── main_controller.py
│   ├── domain/                 # Interfaces
│   │   ├── stt.py
│   │   ├── llm.py
│   │   ├── grammar.py
│   │   └── tts.py
│   ├── infrastructure/         # Implementasi nyata
│   │   ├── whisper_stt.py
│   │   ├── phi3_agent.py
│   │   ├── grammar_corrector.py
│   │   ├── coqui_tts.py
│   │   └── ...
│   ├── plugins/                # Tempat modul
│   ├── ipc_server.py           # Script listener IPC (stdin/stdout)
│   └── requirements.txt
│
├── docs/                       # Dokumentasi
└── README.md
```
