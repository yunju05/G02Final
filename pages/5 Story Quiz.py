import streamlit as st
import random
from gtts import gTTS
import os
import pandas as pd

# 데이터
sentences = [
    ["Leo", "and", "his", "friends", "discovered", "a", "path", "leading", "to", "the", "Whispering", "Woods", ",", "known", "for", "the", "trees", "that", "could", "talk"],
    ["The", "locals", "avoided", "it,", "saying", "it", "was", "bewitched", ",", "but", "the", "adventurous", "teens", "couldn’t", "resist", "exploring"],
    ["As", "they", "walked", "deeper", "into", "the", "woods", ",", "the", "trees", "started", "whispering"],
    ["Each", "tree", "told", "stories", "of", "ancient", "times", ",", "of", "battles", "fought", "and", "lovers", "separated"],
    ["The", "trees", "also", "warned", "them", "about", "the", "dangers", "of", "forgetting", "the", "past", "and", "the", "importance", "of", "nature"],
    ["Moved", "by", "these", "stories", ",", "the", "friends", "promised", "to", "protect", "the", "woods", "and", "share", "their", "knowledge"],
    ["They", "left", "the", "woods", "wiser", ",", "with", "a", "deeper", "respect", "for", "nature", "and", "its", "untold", "stories", ",", "ready", "to", "advocate", "for", "its", "preservation"]
]

translations = [
    "리오와 그의 친구들은 속삭이는 숲으로 이어지는 길을 발견했다.",
    "현지인들은 그 숲이 마법에 걸렸다고 해서 피했지만, 모험심 강한 십대들은 탐험을 멈추지 않았다.",
    "그들이 숲 속으로 더 깊이 들어가자, 나무들이 속삭이기 시작했다.",
    "각 나무는 오래전의 전쟁과 이별 이야기를 들려주었다.",
    "나무들은 과거를 잊지 말고 자연을 소중히 하라고 경고했다.",
    "그 이야기에 감동한 친구들은 숲을 보호하고 이야기를 전하기로 약속했다.",
    "그들은 자연과 그것의 숨겨진 이야기들에 대한 깊은 존경심을 가지고 숲을 떠났다."
]

important_indices = {
    "Easy": [
        [4, 6, 7],
        [2, 6, 7],
        [2, 3],
        [2, 3],
        [3, 4],
        [7, 8],
        [4, 8]
    ],
    "Hard": [
        [6, 7, 10, 11, 17, 18, 19],
        [2, 6, 7, 13, 14, 15],
        [2, 3, 10, 11],
        [2, 3, 9, 10, 12, 13],
        [2, 3, 4, 7, 8, 9],
        [1, 2, 3, 8, 9, 10, 14],
        [4, 8, 9, 13, 14, 15, 17, 18, 22]
    ]
}

# 이하 코드는 동일하며 변경할 필요 없음
