<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1136.txt",
      "sha256": "8256b80aeeac6c565612bfb3247d2d2898095c428532d7bf248e4d01b3d77c3f",
      "bytes": 11349
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4e801014001a6d159abee4f5cd51cf63ef30a8910f4e4b1d7b8b0d732c009f8e",
      "bytes": 584
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a748a23dd04ae8f0d0c8056ba9e2d3b28b4a655e79077f108552bb0f78f6c332",
      "bytes": 245483
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "3fd7aa5edf01f4b7da6c2701a2d9c1a62c482cac170e46e4158773cb5ed2675f",
      "bytes": 951
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f977cd756e43bba0976ff168a80ad208ac4fe1850631422b30b0fe55a9bd93a9",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "0dc15d4f2d211b30aa0374e5fe19a865e6f3acc2593dcd563a960bba679f76bf",
      "bytes": 668
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "46c59282e45ae9d17a8adc87d298b220da0d388f8c1cc2da89893c04a0136a37",
      "bytes": 1929
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "30dcffc3440f831e883e86625ecf8bfbfeb0deb5a1aa9a7264a729bc79d0a663",
      "bytes": 623
    },
    {
      "path": "characters/Son of Heaven.md",
      "sha256": "1640e8f5a3cb4518a34f54bbca1e64c0febb918c0674e2b1af8d8a860b88ff9b",
      "bytes": 642
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "ac214432c0b648eb8d14db773cbda9e79e192e0bc8c9d0d760e5f89fe9b93954",
      "bytes": 650
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5895951d60d69a56331fdfdc592502035283d3a48acfa6cb07fdeb7d2eb418c2",
      "bytes": 291096
    }
  ],
  "estimated_tokens": 9758
}
-->

# Durable State Update — Chapter 1136

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1136. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1136. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 1136,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1136,
    "continuity_sources": [1136],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Son of Heaven used the White Illusion Jiangshi Art given by Jin Taekyung to remain with Zhu Bao after Zhu Bao asked him to live a thousand years as family.",
    "Ma Sanbao is dead; his forces were trapped and defeated.",
    "The Murim Alliance and its allies secretly located and neutralized Moving Formations."
  ],
  "continuity_sources": [
    1135
  ],
  "open_questions": [
    "What are the consequences of the Son of Heaven using the White Illusion Jiangshi Art?"
  ],
  "safe_through": 1135,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 내공     | **internal energy**                              |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 도사      | **Daoist**                                                      |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 괴공절학 | **monstrous martial arts and supreme techniques** | Bizarre arts associated with the Demonic Cult. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 대역 | **stand-in** | Jin's term for the substitute Go Jun used to fake Song Cheonwoo's departure. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 백환강시공 | **White Illusion Jiangshi Art** | Martial art named on the old bamboo slip. |
| 강시공 | **Corpse Art** | Wei Zhong’s technique for creating or controlling jiangshi. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 제갈풍 | 천자 | Zhuge Clan Family Head addressing the Emperor | Your Majesty | formal and deferential | Apologizes for his discourtesy after joking with the Emperor. |
| 천자 | 제갈풍 | Emperor addressing the Zhuge Clan Family Head | you | familiar and permissive | Uses 자네 while forgiving Zhuge Feng's discourtesy. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 1135
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a martial arts instructor to the Emperor, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, Baek Yeon prioritizes the Great Nation and its people over Murim’s interests, and is willing to dismantle Murim if it becomes a threat to them.
- **Voice:** Baek Yeon speaks with measured formality in public, but with the Emperor he shifts easily into familiar teasing and earnest, eloquent praise.
- **Relationships:** Baek Yeon is the Emperor’s trusted confidant and former martial arts instructor, and he is entrusted with protecting Zhu Bao; he commands the Embroidered Uniform Guard and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1135
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1120
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1135
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; the Helper first taught Taekyung to circulate qi; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1135
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Son of Heaven.md

# Son of Heaven (천자)

- **Safe through:** Chapter 1135
- **Aliases:** Emperor, Zhu Di
- **Role:** The Son of Heaven is the Emperor and Zhu Bao’s elder brother, and used the White Illusion Jiangshi Art given to him by Jin Taekyung to extend his life.
- **Personality:** Coldly strategic and imperious, he is willing to break taboos to remain with his younger brother.
- **Voice:** Calm and commanding, with dry, understated humor.
- **Relationships:** Zhu Bao is his younger brother and heir; Jin Taekyung gave him the White Illusion Jiangshi Art; he killed Ma Sanbao.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 1135
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃1136화



심장이 으스러지고도 살아남을 수 있는 사람은 없다.

그리고 이 간단명료한 사실은, 천하의 온갖 괴공절학 중에서도 첫 손에 꼽히는 백환강시공(魄環僵尸功)을 익혔다 하더라도 피할 수 없는 진리였다.

털썩.

썩은 고목 나무처럼 허물어지는 신형.

마침내 최후를 맞이한 대역 죄인의 모습을 말없이 내려다보던 천자는, 이내 그의 가슴 깊숙이 박혀 있던 손을 뽑으며 입을 열었다.

“지휘사.”

비록 아무런 내용도 없는 짤막한 부름.

그러나 금의위 지휘사 백연에게는 그것만으로도 충분했다.

“존명(尊命).”

물 흐르듯 자연스러웠다.

당신의 손으로 직접 역적을 처단한 천자를 향한 경의도.

그와 동시에 한 줄기 섬광이 되어 떨어져 내리는 언월도(偃月刀) 역시도.

서걱!

서늘한 절삭음과 함께 분리되는 살과 뼈.

단숨에 참수형(斬首刑)을 집행한 백연은 언월도의 끝으로 잘려 나간 목을 꿰어 바로 세웠다.

채 감기지 못하고 부릅뜬 채 굳어 버린 죄인의 두 눈이, 언덕 아래에 펼쳐진 광경을 끝까지 지켜볼 수 있도록.

쉬쉬쉬쉬쉭!

문득 하늘이 어두워졌다고 느낀 것은, 비단 누구 한 사람만의 착각이 아니었다.

천자의 이름에 걸맞게 정예만 가려 뽑은 수천의 금위군.

그들이 일시에 내공을 실어 쏘아 보내는 강궁(强弓)이 실로 강맹한 속도와 위력으로 하늘을 뒤덮으며 쏟아져 내리고 있었다.

수십여 장 밖, 야트막한 분지에서 죽을 힘을 다해 몸부림치는 적들을 향해.

푸푸푸푹!

“크아아악!”

끊임없이 터져 나오는 핏물과 비명.

본격적인 전투의 시작과 동시에 잠력단을 복용한 상당수의 광신도가 검기(劍氣)를 휘두르며 거리를 좁혔으나, 사력을 다한 그들의 발걸음은 결코 언덕에 다다를 수 없었다.

“개(開).”

화아아악.

제갈풍의 나직한 명령에 따라, 대기를 떠돌던 기이한 기운이 아지랑이처럼 피어올랐다.

삽시간에 짙은 안개에 휘감긴 언덕 밑.

지금껏 본 적 없는 환영을 맞닥트린 광신도들이 혼란에 휩싸인 순간, 두 번째 명령이 울려 퍼졌다.

“폐(閉).”

철컥.

차가운 쇳소리와 함께 곳곳에서 무수한 암기와 화살촉이 고개를 내밀었다.

천하 일절이라 평가받는 제갈세가의 기관진식(機關陣式)이 비로소 모습을 드러낸 것이다.

그리고 그 결과는, 곧 끔찍한 죽음으로 이어졌다.

쐐애애액, 퍼걱!

안개가 붉게 물들었다.

그 안의 모든 것이 꿰뚫리고, 베이고, 박살났다.

바위 틈새에서, 땅 밑에서, 또 나무 옹이에서.

생각지도 못한 틈새 사이사이에서 발동된 함정은 그들을 순식간에 죽음으로 몰아넣었다.

아군의 시체를 방패 삼아 기적적으로 살아남은 일부 광신도가 가까스로 안개를 벗어났지만, 제갈풍이 준비해 둔 것은 그뿐만이 아니었다.

솨아아악!

고작 일백에 불과한 제갈세가의 가솔들, 하지만 그들의 손에 들린 제갈노(諸葛弩)의 무시무시한 연사력은 적은 머릿수를 상쇄하기에 충분했다.

아니, 그 이상이었다.

콰드드득!

눈 깜짝할 새에 벌집이 되어 쌓여 가는 시체들.

깊은 밤 속에서 시작된 전투는 지금 이 순간에도 계속 이어지고 있었으나, 모두의 눈 앞에 펼쳐진 광경은 전투라는 단어조차 무색하게 만들었다.

이토록 일방적인 학살은 전투라 부를 수 없으니까.

더불어 이와 같은 지옥도(地獄道)는, 비단 하남에서만 벌어지고 있는 일이 아닐 터였다.

“제법 긴 밤이 되겠군.”

불현듯 흘러나온 천자의 뇌까림에, 제갈풍이 대답했다.

“그리고 곧 날이 밝겠지요.”

맞다.

밤이 아무리 길어도 날은 밝아올 것이다.

평소와 다름없는, 아니 더욱 밝아진 태양 아래에 또 한 번의 하루가 시작될 것이다.

오늘 밤, 중원을 위협하던 커다란 우환 하나를 제거하게 될 테니.

“비록 지자(智者)에게 있어 확신은 금물이나…… 이 제갈 모는 믿어 의심치 않습니다.”

그만큼 사력을 다해 세운 계획이었다.

짧지 않은 시간 동안 적뿐만 아니라 아군의 눈까지 속이면서까지 기다려왔던 제갈풍이다.

바로 오늘, 지금 이 순간을 위해.

“역도(逆徒)들이 어디로 향하든, 죽음을 피할 수 없을 겁니다.”

제갈풍은 확신에 찬 음성으로 입을 열었다.

지금껏 찾아낸 모든 이동진에 각 성의 정예들을 모조리 집결시켰다. 암천의 비수가 어디로 향하든, 오늘 밤이 지나면 그들은 모조리 불귀의 객이 되어 있을 것이다.

특히, 제갈풍이 하남과 더불어 적들이 노릴 가장 유력한 장소로 점쳤던 산서(山西)는 말할 것도 없었다.

그곳에는 창천검왕(蒼天劍王)이라는 거인이 진두지휘하고 있었으니.

“모든 것이 폐하께서 도와주신 덕분입니다.”

“그런가?”

실로 공손한 제갈풍의 감사 인사에, 문득 실소를 흘린 천자가 입을 열었다.

“지휘사도 그리 생각하는지 궁금하군.”

곁에 서 있던 백연이 한 치의 망설임도 없이 대답했다.

“그럴 리가 있겠습니까. 큰일은 저들이 다했고, 황실이야 마지막에 한 손 거든 것뿐이지요.”

생각지도 못한 답에 제갈풍은 입을 딱 벌렸지만, 천자의 입가에 걸린 미소는 더욱 짙어졌다.

“어째서?”

“괜히 묻지 마십시오. 폐하께서도 잘 아시지 않습니까.”

“말투가 참 불경하군. 조금 전에는 대역죄인도 제대로 막지 못했으면서.”

천자의 지적에 백연이 눈살을 찌푸렸다.

“그건 앞서 폐하께서 직접 놈을 처단하시겠다고 신신당부하신 탓이지요. 왜, 삭탈관직(削奪官職)이라도 하시렵니까?”

“곤란해. 짐에게는 아직 그대가 필요하거든.”

“폐하의 혜안이 날로 갈수록 깊어지시니, 신으로서는 참으로 기쁠 따름입니다. 고생하는 것에 비해 몇 년째 제자리걸음만 하는 녹봉이 아쉽지만 말입니다.”

“저런. 명색이 금의위 지휘사가 그러면 쓰나. 역도들에게서 회수한 재물도 있으니, 이참에 녹봉을 두 배로 올려 주지.”

“신도 늙은 모양인지, 오늘따라 갑옷이 무겁습니다.”

“세 배.”

“황은이 망극하옵니다. 폐하.”

절도있게 군례를 취한 백연은 슬쩍 고개를 들어 천자를 마주했다.

그리고 약속이라도 한 듯, 두 군신(君臣)은 동시에 웃음을 터트렸다.

이 말도 안 되는 상황을 눈앞에서 지켜보던 제갈풍이 할 말을 잃을 정도로 시원한 웃음을.

하지만 천하에서 가장 고귀한 혈통을 이어받은 사내는 조금도 개의치 않았다.

수십여 년간 황실을 지켜온 노장에게는 저런 말을 할 자격이 충분했고, 이를 떠나 그의 말은 전부 틀림없는 사실이었으니.

“그래, 지휘사의 말이 실로 옳다. 짐이야 마지막에 한 손 거든 것뿐, 이 정도로는 지금껏 진 빚의 십 분지 일도 갈음하지 못할 것이다.”

천자는 얼빠진 시선으로 자신을 바라보는 제갈풍을 향해 미소지었다.

살얼음과 같던 과거, 사방에 도사린 위협과 병마에 맞서 싸우던 시절의 그에게는 허락되지 않았던 웃음이었으나 이제는 다르다.

아니, 달라지게 만들었다.

바로 그가, 진태경이 모든 것을 뒤바꾸고 오래전 잃어버렸던 웃음을 되찾아 주었다.

그런 사실을 누구보다 잘 알고 있는 천자이기에, 형식적으로라도 제갈풍의 공치사를 받아들일 수 없었다.

자신이 살아 있을 수 있는 이유도, 천하가 다시 한번 위기를 헤쳐 나갈 수 있었던 것도 모두 그의 덕분이었으니까.

“고민이군. 자꾸만 늘어나는 이 빚을 어떻게 갚아야 하는지.”

쓴웃음이 담긴 천자의 뇌까림에, 어느덧 눈빛을 가라앉힌 제갈풍이 대답했다.

“아마도…… 모두가 같은 고민을 하고 있을 겁니다.”

그들은 문득 고개를 돌려 서쪽을 바라보았다.

비록 아무것도 보이지 않지만, 세 사람의 눈에는 수천 리 밖에 어딘가에 있을 한 사람의 모습이 비쳐 오는 듯했다.

지금 이 순간, 그들의 어깨너머로 어렴풋이 번지는 흐릿한 빛처럼.

“해가 떴군.”

“예. 날이 밝아 오고 있습니다.”

천자는 처음으로 빛을 마주한 사람처럼 눈을 깜빡였다.

기분 탓일까.

어느새 정적과 피 웅덩이에 잠긴 분지 위, 산처럼 쌓인 수천의 시체를 뒤덮으며 다가오는 햇빛은 그 어느 때보다 눈부셨다.

“명(明).”

밝다.

어둠이 흩어지고, 빛이 타오른다.

앞으로 이어질 수많은 나날 또한 이러하길, 천자는 간절히 바랐다.

분명 또다시 자신의 모든 것을 내던지며 생사의 기로에 놓여 있을 진태경의 운명 역시도.

“대명(大明).”

모두의 앞날을 밝혀 줄 새로운 국호(國號)와 함께, 대명제국의 천자는 터질 듯이 부풀어 오른 숨을 내뱉었다.

“백연.”

“하명하시옵소서.”

“그대의 녹봉을 네 배로 올려 줘야 할 것 같구나. 제법 고난한 일이 될 터이니.”

“그 말씀은.”

“짐은 환궁(還宮)하지 않을 것이다.”

“……!”

“천하의 만백성에게 전하라. 사막 너머에 도사린 저 극악무도한 역도들을 뿌리 뽑지 않는 한, 짐이 옥좌에 앉을 일은 없을 것이라고.”

크게 뜨인 눈으로 천자를 바라보던 노장이 미소와 함께 한쪽 무릎을 꿇었다.

“신, 금의위 지휘사 백연. 지엄하신 황명을 받드나이다.”

그날, 수많은 전서구와 파발마가 천하의 땅과 하늘을 가로질렀다.



* * *



말발굽과 날개를 타고 전해진 황명(皇命)은 불과 며칠 만에 온 천하를 뒤덮었다.

아니, 뒤흔들었다.

무림과 민간, 더불어 관부까지도.

“황명이오!”

천하 각지로 향한 전령들은 황실의 인장이 새겨진 방을 곳곳에 내걸었고, 마침내 모든 이가 알게 되었다.

자신들의 턱 끝까지 다가와 있던 칼날의 존재를.

그리고 단 하룻밤 사이에 시작되고 끝난, 일방적이면서도 위대한 승리를.

하지만 천자가 전하고자 한 것은 비단 승전보뿐만이 아니었다.

친정(親征).

사 황자라 불리던 시절, 이미 정복 군주의 그릇으로 평가받던 천자는 대명이라는 새로운 국호 아래 금위군의 집결을 명령했고 그의 목적지는 모두가 짐작했던 대로였다.

신강(新疆).

열사의 사막 너머 존재하는 옛 마교의 본거지.

광오하게도 스스로를 천주(天主)라 칭하는 역도들의 우두머리를 향해, 온 천하의 창끝이 겨누어지고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1136

No one could survive having their heart crushed.

And this simple, clear fact was no exception—not even for someone who had mastered the White Illusion Jiangshi Art, one of the foremost among the countless monstrous martial arts and supreme techniques in the world.

Thud.

His body crumpled like a rotten old tree.

The Son of Heaven silently looked down at the traitor who had finally met his end. Then he pulled his hand from deep inside the man’s chest and spoke.

“Commander.”

It was a brief call, without a single detail.

But it was enough for Baek Yeon, Commander of the Embroidered Uniform Guard.

“At your command.”

It was as natural as water flowing.

So was the reverence for the Son of Heaven, who had personally executed the traitor with his own hand.

And so was the crescent-bladed polearm that flashed down in a streak of light.

*Shhk!*

Flesh and bone parted with a chilling slice.

Baek Yeon carried out the beheading in a single stroke, then lifted the severed head on the tip of his polearm.

The traitor’s eyes were still wide open, frozen before they could close. He would watch to the very end the scene spread out below the hill.

*Shh-shh-shh-shh-shhk!*

The sudden feeling that the sky had darkened was no one person’s mistake.

Thousands of Imperial Guards, each an elite chosen to match the Son of Heaven’s name.

With internal energy behind each shot, arrows from their powerful bows filled the sky and rained down with astonishing speed and force.

They fell upon enemies struggling with all their might in the shallow basin hundreds of feet away.

*Thwup-thwup-thwup!*

“Gaaah!”

Blood and screams burst forth without pause.

At the very start of the battle, many of the fanatics had taken Temporary Strength Pills and swung Sword Energy as they closed the distance. But even their desperate strides could never reach the hill.

“Open.”

*Fwoosh.*

At Zhuge Feng’s quiet command, a strange energy drifting through the air rose like heat haze.

The base of the hill was instantly swallowed by thick fog.

As the fanatics were thrown into confusion by an illusion unlike anything they had ever seen, a second command rang out.

“Close.”

*Clack.*

With the cold sound of metal, countless hidden weapons and arrowheads emerged from all around them.

The Zhuge Clan’s mechanisms and formations, hailed as the finest in the world, had finally revealed themselves.

And the result was a horrible death.

*Fwoosh, splat!*

The fog turned red.

Everything inside was pierced, cut, and smashed to pieces.

From between rocks, from beneath the earth, from the knots in trees.

The traps, triggered in unexpected gaps all around them, sent the fanatics to their deaths in an instant.

A few fanatics managed to escape the fog by using the corpses of their allies as shields, but Zhuge Feng had prepared more than that.

*Fwoosh!*

The Zhuge Clan retainers numbered a mere hundred, but the terrifying rate of fire of the Zhuge Repeating Crossbows in their hands more than made up for their small numbers.

No—their firepower was greater still.

*Crack-crack-crack!*

In the blink of an eye, bodies piled up, riddled with holes.

The battle that had begun in the dead of night still raged on, but the scene before everyone’s eyes made even the word “battle” seem inadequate.

A slaughter this one-sided could hardly be called a battle.

And this hellscape wasn’t unfolding only in Henan.

“Looks like it’ll be a long night.”

At the Son of Heaven’s sudden murmur, Zhuge Feng answered.

“And soon, the sun will rise.”

That was right.

No matter how long the night, day would dawn.

Another day would begin beneath a sun as bright as ever—or brighter.

Tonight, they would eliminate one of the great threats hanging over the Central Plains.

“Though certainty is a dangerous thing for a wise man…… I, Zhuge, have no doubt.”

He had built the plan with all his might.

Zhuge Feng had waited a long time, deceiving not only the enemy but even his own allies.

All for today. For this very moment.

“Wherever the traitors go, they won’t escape death.”

Zhuge Feng spoke with conviction.

They had gathered the elite of every province at every Moving Formation they had found. No matter where Dark Heaven’s dagger went, once tonight was over, they would all be dead, never to return.

That went especially for Shanxi, which Zhuge Feng had judged—alongside Henan—to be the enemy’s most likely target.

A giant called the Azure Sky Sword King was leading the forces there.

“It is all thanks to Your Majesty’s help.”

At Zhuge Feng’s most respectful expression of gratitude, the Son of Heaven let out a quiet laugh.

“Is that so?”

Then he spoke.

“I wonder if the Commander thinks so, too.”

Baek Yeon, standing beside him, answered without the slightest hesitation.

“Of course not. They did all the hard work. The Imperial House only lent a hand at the end.”

Zhuge Feng’s mouth fell open at the unexpected answer, but the Son of Heaven’s smile only deepened.

“Why?”

“Don’t ask when you already know, Your Majesty.”

“That’s a rather irreverent way to speak. You couldn’t even stop the traitor just now.”

Baek Yeon frowned at the Son of Heaven’s remark.

“That was because Your Majesty repeatedly insisted that you would deal with him yourself. What, are you going to strip me of my office?”

“That would be inconvenient. I still need you.”

“Your Majesty’s wisdom grows deeper by the day. This servant can only be glad. Though I do regret that my salary has been stuck in place for years, despite all the trouble I go through.”

“My, my. Is that any way for the Commander of the Embroidered Uniform Guard to speak? We’ve recovered the traitors’ wealth, so I’ll double your salary.”

“Perhaps I’m getting old. My armor feels heavy today.”

“Triple it.”

“I am overwhelmed by Your Majesty’s grace.”

Baek Yeon gave a crisp salute, then glanced up at the Son of Heaven.

And as if on cue, the two sovereign and subject burst out laughing.

It was such a hearty laugh that Zhuge Feng, watching this absurd scene unfold before his eyes, was left speechless.

But the man born of the most noble bloodline in the world didn’t mind in the slightest.

The old general who had guarded the Imperial House for decades had every right to speak that way. And apart from that, everything he had said was true.

“Yes. The Commander is absolutely right. I only lent a hand at the end. That’s nowhere near enough to repay even a tenth of what I’ve owed all this time.”

The Son of Heaven smiled at Zhuge Feng, who was staring at him in bewilderment.

In the past, when danger lurked on every side and he fought against illness, laughter like this had been denied him.

But now it was different.

No—Jin Taekyung had made it different. He had changed everything and given the Son of Heaven back the laughter he’d lost long ago.

The Son of Heaven knew that better than anyone. He couldn’t accept Zhuge Feng’s formal praise, even as a courtesy.

The reason he was still alive, the reason the world had overcome another crisis, was all thanks to him.

“It’s troubling. How am I supposed to repay this debt that keeps growing?”

At the Son of Heaven’s rueful murmur, Zhuge Feng’s eyes had grown serious.

“Perhaps…… we’re all wondering the same thing.”

They turned and looked west.

Though nothing could be seen, the three of them seemed to glimpse the figure of one man somewhere thousands of miles away.

Like the faint light spreading dimly over their shoulders at this very moment.

“The sun’s risen.”

“Yes. Day is breaking.”

The Son of Heaven blinked as if he were seeing the light for the first time.

Perhaps it was only his imagination.

On the basin, now steeped in silence and pools of blood, the sunlight advancing over mountains of thousands of corpses shone brighter than ever.

“Bright.”

Darkness scattered. Light blazed.

The Son of Heaven fervently hoped that the countless days ahead would be the same.

And that Jin Taekyung’s fate, which would surely once again leave him standing at the edge of life and death, casting everything he had aside, would be bright as well.

“Great Ming.”

With the new name of the nation that would light the way for everyone’s future, the Son of Heaven of the Great Ming Empire let out a breath that had been swelling in his chest.

“Baek Yeon.”

“Your orders, Your Majesty?”

“I think I’ll have to quadruple your salary. This is going to be a difficult undertaking.”

“What do you mean……?”

“I will not return to the palace.”

“……!”

“Tell all the people of the realm: I will not sit on the throne until those vile traitors lurking beyond the desert have been rooted out.”

The old general stared at the Son of Heaven, eyes wide. Then, smiling, he lowered one knee to the ground.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard, accept Your Majesty’s imperial decree.”

That day, countless messenger pigeons and mounted couriers crossed the land and skies of the realm.

* * *

The imperial decree, carried by hooves and wings, spread across the realm in just a few days.

No—it shook it to its core.

Murim, the common people, and even the government.

“By imperial decree!”

The messengers sent across the realm hung notices bearing the Imperial Seal everywhere they went. At last, everyone learned of the blade that had been closing in on their throats.

And of the one-sided, momentous victory that had begun and ended in a single night.

But victory was not all the Son of Heaven wished to announce.

A personal expedition.

Back when he was known as the Fourth Prince, the Son of Heaven had already been judged to have the makings of a conqueror. Now, under the new name of Great Ming, he ordered the Imperial Guards to assemble, and his destination was exactly what everyone had expected.

Xinjiang.

The former stronghold of the Demonic Cult, beyond the scorching desert.

The spearheads of the whole realm were aimed at the leader of the traitors, who dared to call himself the Lord of Heaven.
```
