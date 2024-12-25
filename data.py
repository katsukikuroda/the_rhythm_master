A = "A"
N = None

music_a = {
    "score": [
        A, N, A, N, A, A, A, N,
        A, N, A, N, A, A, A, N,
    ],
    # lesson4 音楽の再生 で変更
    "fps": 60000 / 121 / 5,
    "bpm": 121,
    #
    "title": "sample A",
    # lesson4 音楽の再生 で追加
    "music": 'sounds/MusMus-CT-NV-TT.mp3',
    #
    # lesson4 音楽の再生 で追加
    "delay": 1630,
    #
    # lessson4 画面の作成 で追加
    "time": 75000,
    #
}

music_b = {
    "score": [],
    "fps": 125,
    "bpm": 96,
    "title": "sample B",
}

music_list = [
    music_a,
    music_b,
]