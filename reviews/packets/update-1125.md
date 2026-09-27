<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1125.txt",
      "sha256": "a29bb8ff198dd7eca7156dfe5079d8718e9aaebfb6bb37f0f5a7aa4f0664e976",
      "bytes": 12407
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bbdcc391bddd1797742a58c722a84fe5ab7ca9d2acf82f853175520ce3c6872f",
      "bytes": 1202
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "307189767337c5394589bdcaa7f59f3e28cdf1da9d380fecae4d63447025be4b",
      "bytes": 245178
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "129d2e50a0f0ad11e1847b77892271c7022e045b5d7b67155d27e3ba89a18349",
      "bytes": 936
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "35a766baec3322df2e0d6bce307cd0e6c8e6721acb6f627a9042f2757f08719e",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f38a7fde3d4f6def87c4395bd92dd26e3a0512404f82926d0ec0aefa19798e9a",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "87a9549a12906242c589a2cb88230c84b83ea6c7fe73d1524e42e5dcef89be69",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "12245b2ab67d65b4c0922532fd3a1f1df55014cd9527bd4f0993e5dc9a975347",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "547a37dc1c5d6e14beb7ef52d5a661ae4ad66facbffc5c701872dfecf4cca8d5",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fbe26e0ec5f89ce57df0b052ec3ff3869882eaa7728f4db5939e2d5122fb744c",
      "bytes": 289919
    }
  ],
  "estimated_tokens": 10650
}
-->

# Durable State Update — Chapter 1125

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
1 and safe_through 1125. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1125. Profile updates may replace only one
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
  "chapter": 1125,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1125,
    "continuity_sources": [1125],
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
    "The Inner City battlefield remains under siege.",
    "The quest timer begins counting down from five minutes as Taekyung confronts the Blood Lord.",
    "Taekyung is critically injured but evades the Blood Lord’s attacks with unexplained precision.",
    "Jeok Cheongang and Cheongpung fight beside Taekyung; Cheongpung is injured and Jeok is knocked away.",
    "The Blood Lord absorbs blood to replenish his strength; a wound in his palm remains unhealed.",
    "Taekyung’s spear pierces the Blood Lord’s wounded palm; the outcome is unresolved.",
    "Taekyung believes Hyuk Mujin is dead, though he did not witness his fate.",
    "Taekyung remembers an unfulfilled promise to Ju Hwaran."
  ],
  "continuity_sources": [
    1124
  ],
  "open_questions": [
    "Will Taekyung survive the remaining quest time and defeat the Blood Lord?",
    "Why can Taekyung evade the Blood Lord’s attacks with such precision?",
    "What effect will Taekyung’s spear thrust have on the Blood Lord?",
    "What happened to Hyuk Mujin?",
    "Will Taekyung ever fulfill his promise to Ju Hwaran?"
  ],
  "safe_through": 1124,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 일격     | **One Strike**                         |
| 화산     | **Huashan**            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 수강 | **Palm Force** | Force generated through a palm technique. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 무아 | **No-self** | The brief self-forgetting state the disciple mistakes for a breakthrough. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1124
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality; after killing the Grand Mage, he claims command of the Dark Heaven army.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; newly unrestrained, he defies the Lord of Heaven’s will and seizes command for himself.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He has served the Lord of Heaven but now openly defies his will; he is fixated on killing Jin Taekyung, killed the Grand Mage, and recognizes Cheongpung from his connection to Sword Saint Mae Jonghak.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1124
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1124
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1124
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1124
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1124
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃1125화



콰드드드득!

섬뜩한 파육음이 울려 퍼진 그 순간, 혈주는 불현듯 세상이 멈춘 듯한 착각에 휩싸였다.

‘아.’

뜨겁다. 아득하다.

흔들리는 시야와 멀게만 느껴지는 소음들.

어쩌면 지금까지의 일들이 꿈은 아니었을까, 싶을 정도로 주위를 둘러싼 모든 것이 낯설게만 느껴졌다.

만약 살과 뼈를 불사르는 이 끔찍한 열기가 없었다면, 혈주는 진정 그리 생각했을지도 몰랐다.

아니.

화염으로 인한 매캐한 연기와 아지랑이 너머로 보이는 누군가의 얼굴이 아니었다면.

쿨럭.

입술을 비집고 흘러넘치는 선혈.

눈앞을 새하얗게 물들이는 작열통(灼熱痛) 속, 내장 조각이 섞인 핏물을 울컥 토해 낸 혈주는 눈앞의 청년을 바라보았다.

어느덧 한 자루의 창으로 자신과 이어져 있는, 젊고도 무모한 부나방을.

동시에 문득, 피에 젖은 입술을 열었다.

“도대체 어떻게?”

순수한 의문이 담긴 눈빛.

짧지만 많은 뜻이 담겨 있는 그 물음에, 진태경이 대답했다.

“몰라, 나도.”

“뭐?”

“단지…… 당연하게 알 수 있었다.”

놀라우리만치 담담한 음성으로, 진태경은 말을 이었다.

“네 모든 움직임을. 그리고 내가 어떻게 해야 하는지.”

“……!”

“그뿐이야.”

일순간, 혈주는 자신도 모르게 눈을 부릅떴다.

타들어 가는 듯한 고통 때문에?

틀렸다.

손바닥을 관통한 것으로도 모자라 몸속 깊숙이 파고들어 열기를 퍼트리는 이 빌어먹을 창날도, 지금 그가 느끼고 있는 충격에 비하면 아무것도 아니었다.

‘알 수 있었다고? 내 모든 것을?’

촌각 전에 들었다면 코웃음을 쳤을, 말도 안 되는 헛소리였다.

한계마저 넘어선 자신의 권능은 실로 강대했고, 상대와의 격차는 가능성이라는 단어조차 무의미하게 만들 정도였으니까.

하지만.

‘거짓도, 허풍도 아니다.’

진태경과 시선이 맞닿은 그 순간, 혈주는 본능적으로 깨달을 수 있었다.

그에게는 너무나도 잔인한 한 가지 진실을.

더불어 혈주 자신이 그 진실을 애써 부정하고 있었다는 것을.

“처음부터…… 물어볼 필요도 없었군.”

“그래.”

작게 고개를 끄덕인 진태경이, 흐릿한 음성으로 덧붙였다.

“적어도 그 순간만큼은, 내가 너보다 강했다.”

마침내 적의 입술 사이로 흘러나온, 인정할 수밖에 없는 진실에 혈주의 등골이 찌르르 울렸다.

고통마저 뒤덮으며 전신을 휩쓰는 무수한 감정들.

그것은 뼈저린 패배감이요, 이해할 수 없는 불가해(不可解)로부터 비롯된 두려움인 동시에 그와는 전혀 상반된 무언가이기도 했다.

깊은 안도와 기쁨.

지금 이 순간, 그는 스스로의 선택이 옳았음을 온몸으로 깨닫고 있었다.

‘천주시여, 경애하는 나의 주인이시여. 보고 계십니까. 듣고 계십니까.’

혈주는 문득 하늘을 올려다보았다.

끊이지 않는 빗줄기와 먹구름에 가려진, 자신의 하늘을 향해 속삭였다.

‘제 선택은, 결코 틀리지 않았나이다.’

사실 혈주의 마음 한구석에는 불안감이 꿈틀거리고 있었다.

진태경의 제거는 확고부동한 충심(忠心)만으로 결심한 것이 아니었으니까.

서운했다. 원망스러웠다.

목숨 바쳐 충성을 다하는 종복들의 안위 따위는 염두에도 두지 않는 듯한 주인의 모습에.

동시에, 우습게도 질투했다.

그런 주인에게 애정에 가까운 관심을 한 몸에 받고 있는 진태경을.

하여 죽이고자 했다.

번번이 암천의 앞길을 가로막는 걸림돌을 치운다는 명분을 내세우고, 충성심이라는 세 글자로 덮어 애써 합리화했다.

하지만 이제는 그럴 필요조차 없게 되었다.

반드시 진태경이 죽어 사라져야 하는 이유를, 오늘 이 자리에서 스스로 직접 증명해 보였으니까.

그리고, 반드시 그리될 테니까.

“열화신룡(烈火神龍) 진태경. 인정하마. 너는 분명 신룡이라 불릴 자격이 충분해.”

혈주는 진태경을 향해 속삭였고, 그것은 한 치의 거짓도 섞여 있지 않은 진심이었다.

아니, 오히려 신룡이라는 표현조차 부족하게 느껴졌다.

죽음의 문턱에 다다른 와중에도 무아지경(無我之境)에 휩싸인 채, 더 높은 깨달음을 향해 가까워지던 그 모습은 다시 떠올려보아도 소름이 끼칠 정도였으니까.

“그래, 네놈의 말이 옳다. 그 순간의 너는 분명 무서우리만치 강했지. 나로서도 막을 수 없을 만큼.”

진태경이 얼마나 대단한 깨달음을 얻었는지는 모른다.

생사가 경각에 달한 상황에서 어찌 저렇게 분투할 수 있는지도 모른다.

고작 한 줌에 불과한 기운이 실린 창날로, 어떻게 그의 막강한 강기(罡氣)를 파훼했는지도.

그러나.

“그런 것 따위, 아무런 의미도 없지.”

어느덧 혈주는 웃고 있었다.

패배자라면 결코 보일 수 없는, 환한 미소를 띤 채 자신의 몸속 깊숙이 박힌 창날을 붙잡았다.

정확히는, 가슴에서 한 뼘 차이로 벗어난 백염의 창날을.

푸욱. 투두둑.

섬뜩한 파육음과 함께 터져 나오는 핏물.

혈주는 짙은 수강(手罡)에 휩싸인 손으로 창날을 뽑아내며 뇌까렸다.

“죽었다고 생각했다. 그 순간만큼은 분명히.”

진태경이 혼신을 다해 내뻗은 마지막 공격은, 혈주로서도 도저히 막을 수 없는 일격이었다.

만약 때맞춰 진태경의 공력이 고갈되지만 않았다면. 

그로 인해 힘을 잃은 창날의 방향이 빗나가지만 않았다면 분명 그랬을 터다.

하지만 아니었다.

“이것이 하늘의 뜻이다.”

혈주는 몸속 깊은 곳에서 차오르는 환희를 느꼈다.

저 드높은 하늘은, 결국 진태경이 아닌 자신의 손을 들어 주었다.

“네놈이 믿는 그 알량한 하늘이 아닌, 내가 섬기는 진정한 하늘의 뜻이란 말이다!”

바로 그 순간.

고통 따위는 단숨에 잊어버릴, 벼락과도 같은 전율과 함께 관통당한 손마저 빼낸 혈주가 창대를 비틀었다.

쉬릭, 콰드드득!

무시무시한 힘을 이기지 못하고 맹렬하게 회전하는 창대.

백염이라는 이름을 지닌 그것은 마지막까지 애병(愛兵)을 놓치지 않기 위해 단단히 묶어놓았던 옷깃을 단숨에 끊어 내고, 이내 주인의 손아귀를 피투성이로 물들이기에 충분했다.

철퍽.

힘을 이기지 못하고 밀려 나가는 몸뚱어리.

신형조차 제대로 가누지 못한 채 쓰러진 진태경을 향해, 혈주는 망설임 없이 걸음을 내디뎠다.

정확히는, 내디디려 했다.

다음 순간, 연못이 아닌 화산(華山)의 산기슭에서 성장한 또 하나의 신룡이 포효와 함께 달려들기 전까지는.

“안 돼!”

쐐애애액!

어둠 너머로 노을이 번진다. 줄기줄기 금이 간 검신을 따라 피어난 강기가 서른여섯 개의 꽃잎이 되어 흩날렸다.

보는 이로 하여금 탄성을 자아내게 할 만큼 아름다운 검격(劍擊).

하지만 그 안에 실린 감정은 어느 때보다 처절했고, 그렇기에 더욱더 안타까울 수밖에 없었다.

후우웅!

곧이어 공간을 뒤덮은 핏빛 강기는, 꽃잎이 아닌 숲마저 송두리째 베어 가를 만큼 강맹했으니까.

콰아아앙!

굉음과 함께 뒤흔들리는 지축.

세찬 빗줄기마저 가라앉히지 못한 먼지구름 너머로, 비틀거리며 일어난 인영이 쓰러진 진태경의 앞을 가로막았다.

하나가 아닌, 둘이 되어.

“어딜, 쿨럭. 가려 하느냐.”

혈인(血人)이나 다름없는 몰골로 다시 일어나 앞길을 가로막은 적천강과 청풍의 모습에, 핏빛 눈동자가 깊게 가라앉았다.

“북망산(北邙山).”

이제는 자신의 것이 된 창을 비스듬히 치켜세우며. 괴물이 덧붙였다.

“물론, 가는 건 네놈들이지.”

우우웅.

주인을 잃은 창날이, 구슬픈 울음소리를 토해 냈다.



* * *



솨아아아.

하염없이 쏟아져 내리는 빗줄기 너머, 끝없이 펼쳐진 어두컴컴한 하늘을 나는 멍하니 바라보았다.

‘이것이 하늘의 뜻이다.’

지금 이 순간에도 귓가에 남아 메아리치는, 혈주의 목소리를 들으며.

‘네놈이 믿는 그 알량한 하늘이 아닌, 내가 섬기는 진정한 하늘의 뜻이란 말이다!’

환희로 들끓던 그 핏빛 눈동자를 떠올리며, 마음속으로 뇌까렸다.

‘그래, 어쩌면 그럴 수도 있겠지.’

나는 분명 최선을 다했다.

아니, 나를 포함한 모두가 혼신(渾身)을 다해 싸웠다.

더는 쏟아낼 것조차 남지 않을 만큼.

그 어떤 후회도, 분노도 느껴지지 않을 만큼.

하지만…….

‘하늘의 뜻 따위, 따른 적도 없었다.’

나는 조용히, 동시에 필사적으로 몸부림쳤다.

촤륵.

온통 짓이겨지고 부러진 손아귀로, 핏물이 뒤섞인 검붉은 흙덩이를 있는 힘껏 그러쥐며 몸을 일으켜 세웠다.

그래야만 했고, 그럴 수밖에 없었다.

지금 이 순간에도 피를 흩뿌리며 쓰러지는 사람들을 위해서라도.

혈주가 비웃었던, 내 알량한 하늘이 바로 저들이었으므로.

퍼어엉!

맹렬한 파공성이 공간을 터트린다.

비틀거리며 무릎을 꿇는 적천강의 모습이, 포탄처럼 튕겨 나가 바닥을 구르는 청풍의 신형이 흐릿한 시야에 담긴다.

마침내 자신을 막아서는 모든 걸림돌을 허물어트린 채, 나를 향해 다가오는 괴물의 발걸음도 함께.

철벅.

한 걸음, 또 한 걸음.

가까워지는 거리만큼 선명해지는 핏빛 안광(眼光)을 바라보며, 나는 온 힘을 다해 몸을 일으켜 세웠다.

기억도 나지 않는 갓난아이 시절처럼 몸뚱어리를 뒤집고, 두 팔과 다리로 땅을 짚었으며, 힘없이 휘청거리는 육신을 가까스로 일으켜 세웠다.

그리고 어느덧 태양처럼 붉게 타오를 만큼 가까워진, 혈주의 두 눈동자와 마주한 그 순간.

‘인벤토리 오픈, 소환.’

이 광활한 천하에서 오직 내게만 허락된 무한의 창고 속에서, 잘 벼려진 단검을 꺼내어 내질렀다.

그와 동시에 귓가를 파고든, 나직한 조소(嘲笑)를 들으며,

“역시.”

콰득.

고통은 느껴지지 않았으나, 소리만으로도 알 수 있었다.

혈주가 섬광처럼 움켜쥔 내 손목이, 두 번 다시 회복될 수 없을 만큼 산산이 으스러졌다는 사실을.

하지만 상대를 예측한 건, 혈주만이 할 수 있는 일이 아니다.

스륵, 툭.

회광반조(回光返照)로 인해 지워진 고통을 뒤로한 채, 나는 손아귀에서 떨어져 내리던 단검의 칼자루를 발끝으로 후려쳤다.

푹.

“……!”

서늘한 파육음과 함께 살갗 깊숙이 파고드는 단검.

일순간 크게 뜨인 두 눈으로 자신의 정강이에 틀어박힌 날붙이를 바라본 혈주가 입술을 핥았다.

“대단하군. 정말 대단해. 허나 그 때문에…….”

그리고 한 치의 망설임도 없이, 남은 한 다리를 채찍처럼 휘둘렀다.

“네놈을 결코 살려둘 수 없는 것이다.”

콰드드득!

짓뭉개진 살갗 사이로 튀어나오는 새하얀 뼈마디.

한쪽 팔에 이어, 두 다리마저 불구로 만든 혈주가 벼락처럼 손을 뻗어 내 목을 움켜잡았다.

우득.

뼈 어긋나는 소리와 함께 어두워지는 시야.

숨을 헐떡이는 내 귓가로 깊게 가라앉은 혈주의 음성이 흘러들어왔다.

“기나긴 악연이었다. 열화신룡 진태경.”

그 순간.

화아아악.

지나온 삶을 반추하는 마지막 촛불처럼, 칠흑과도 같은 어둠 속으로 굴러떨어지던 시야가 새하얗게 물들었다.

아니.

어쩌면 노을보다도 붉고 짙은 색으로.

서걱.
```

## Final English reading copy

```markdown
# Chapter 1125

KRRRCH!

At the moment a ghastly sound of flesh being torn apart rang out, the Blood Lord was suddenly overcome by the illusion that the world had stopped.

*Ah.*

Hot. Distant.

His vision wavered, and the noise around him seemed impossibly far away.

Everything surrounding him felt so unfamiliar that he wondered if perhaps everything that had happened until now had been a dream.

If not for the terrible heat scorching his flesh and bones, he might truly have thought so.

No.

If not for the face he could see beyond the acrid smoke and shimmering haze of the flames.

*Cough.*

Fresh blood spilled past his lips.

Amid the searing pain that turned his vision white, the Blood Lord coughed up blood mixed with bits of his innards and looked at the young man before him.

The reckless young moth, now joined to him by a single spear.

Then, suddenly, he parted his blood-soaked lips.

“How?”

His eyes held genuine confusion.

Jin Taekyung answered the brief question, laden with meaning.

“I don’t know either.”

“What?”

“I just… knew, as if it were the most natural thing in the world.”

His voice astonishingly calm, Jin Taekyung continued.

“Every move you’d make. And what I had to do.”

“……!”

“That’s all.”

For an instant, the Blood Lord’s eyes widened before he even realized it.

Was it because of the pain, as if he were burning alive?

Wrong.

The accursed spearhead had pierced his palm and driven deep into his body, spreading heat through him. But compared to the shock he felt now, that was nothing.

*He knew? Everything I’d do?*

If he’d heard those absurd words a moment ago, he would have scoffed.

His power had grown beyond its limits, and the gulf between them was so vast that even the word *possibility* had become meaningless.

But—

*He isn’t lying. He isn’t boasting.*

The moment their eyes met, the Blood Lord understood instinctively.

A single truth, unbearably cruel to him.

And that he had been desperately denying it.

“So there was no point in asking from the start.”

“Yeah.”

Jin Taekyung gave a small nod, then added in a faint voice,

“At least in that moment, I was stronger than you.”

At last, the enemy’s lips gave voice to a truth he could no longer deny. A shiver ran down the Blood Lord’s spine.

Countless emotions swept through him, overwhelming even the pain.

Bitter defeat. Fear born of something impossible to understand. And, at the same time, something entirely opposed to those feelings.

Deep relief and joy.

In this moment, his whole body knew he had made the right choice.

*Lord of Heaven, my revered master. Are you watching? Can you hear me?*

The Blood Lord suddenly looked up at the sky.

He whispered to his own heavens, hidden behind the unceasing rain and dark clouds.

*My choice was never wrong.*

Truthfully, a thread of anxiety had been stirring in a corner of the Blood Lord’s heart.

He hadn’t resolved to eliminate Jin Taekyung out of unwavering loyalty alone.

He’d been disappointed. Resentful.

His master seemed to have no thought for the welfare of his servants, who gave their lives in service.

And, absurdly, he’d been jealous.

Jealous of Jin Taekyung, who had all but monopolized that same master’s almost affectionate attention.

So he’d wanted to kill him.

He’d claimed it was to remove an obstacle that kept standing in Dark Heaven’s way, and forced himself to rationalize it beneath those three words: *loyalty to his master.*

But now there was no need.

Here, today, Jin Taekyung had proved with his own actions why he absolutely had to die and disappear.

And he would. Without fail.

“Blazing Flame Divine Dragon Jin Taekyung. I’ll admit it. You truly deserve to be called a Divine Dragon.”

The Blood Lord whispered to Jin Taekyung, and there wasn’t a trace of falsehood in his words.

No—the title *Divine Dragon* even seemed insufficient.

Even as he stood at death’s door, he’d been swept into a trance, drawing closer to a higher enlightenment. The memory of it still sent a chill through the Blood Lord.

“Yes, you were right. In that moment, you were terrifyingly strong. Strong enough that even I couldn’t stop you.”

He didn’t know what profound enlightenment Jin Taekyung had gained.

He didn’t know how he could fight so desperately when his life was hanging by a thread.

He didn’t know how a spearhead carrying no more than a trace of energy had broken through his formidable Force.

But—

“That means nothing.”

By then, the Blood Lord was smiling.

With a bright smile no defeated man could wear, he grasped the spearhead buried deep inside him.

More precisely, the spearhead of White Flame, embedded a handspan from his heart.

*Squish. Crack.*

Blood burst out with a ghastly sound of torn flesh.

The Blood Lord pulled out the spearhead with a hand wrapped in dense Palm Force and muttered,

“I thought I was dead. In that moment, I certainly did.”

Jin Taekyung’s final attack, thrown with all his strength, had been a strike the Blood Lord could not possibly have stopped.

If Jin Taekyung’s internal energy hadn’t run dry at just the right moment—

If the weakened spearhead hadn’t veered off course because of it—then that would have been the end.

But it hadn’t happened.

“This is Heaven’s will.”

The Blood Lord felt joy welling up from deep within him.

The heavens above had, in the end, chosen him—not Jin Taekyung.

“Not that paltry heaven you believe in. This is the will of the true Heaven I serve!”

Right then.

With a shudder like a bolt of lightning, powerful enough to make him forget the pain in an instant, the Blood Lord pulled his pierced hand free and twisted the spear shaft.

SHWIK—KRRRCH!

The spear shaft spun violently, driven by a force too great to resist.

White Flame, as it was called, snapped through the collar of the garment that had been tightly tied to keep its owner from losing his beloved weapon. It was more than enough to leave its owner’s grasp bloodied.

*Splatter.*

Jin Taekyung was shoved backward, unable to withstand the force.

He fell, unable even to keep his body upright.

The Blood Lord stepped toward him without hesitation.

Or rather, he tried to.

Until another Divine Dragon—one who had grown up on the slopes of Mount Huashan, not beside a pond—charged in with a roar.

“No!”

SHWAAAAK!

Sunset spread through the darkness. Force bloomed along the sword’s blade, cracked from end to end, then scattered in thirty-six petals.

A sword strike beautiful enough to draw gasps from anyone who saw it.

But the feelings behind it were more desperate than ever, and that made it all the more heartbreaking.

FWOOM!

Then the blood-red Force that engulfed the space was so powerful it could cut down not only the petals, but an entire forest.

KWA-BOOOOM!

The earth shuddered with a deafening crash.

Beyond the cloud of dust that even the pounding rain couldn’t settle, a figure staggered to his feet and stood in front of Jin Taekyung’s fallen body.

Not one, but two.

“Where do you think you’re going? *Cough.*”

At the sight of Jeok Cheongang and Cheongpung, their bodies no better than blood-soaked men, rising once more to block his path, the Blood Lord’s red eyes sank into a cold glare.

“Mount Beimang.”

Raising the spear that now belonged to him at an angle, the monster added,

“Of course, you’re the ones going there.”

*Hummm.*

The spearhead, separated from its master, let out a sorrowful hum.

* * *

*Shhhhh.*

Beyond the rain pouring without end, I stared blankly at the dark sky stretching endlessly above me.

*This is Heaven’s will.*

Listening to the Blood Lord’s voice echoing in my ears even now.

*Not that paltry heaven you believe in. This is the will of the true Heaven I serve!*

Remembering those blood-red eyes, boiling with joy, I muttered to myself,

*Yeah. Maybe it is.*

I’d certainly done everything I could.

No—every one of us had fought with all we had.

Until there was nothing left to give.

Until there was no room for regret or anger.

But…

*I never followed some will of Heaven.*

Quietly, desperately, I struggled.

*Crunch.*

With a hand crushed and broken all over, I gripped a clod of dark red earth mixed with blood as hard as I could and pushed myself up.

I had to. There was no other choice.

For the people even now collapsing, their blood scattering around them.

The paltry heaven the Blood Lord had mocked—that was these people.

*BOOM!*

A fierce crack of air burst through the space.

Jeok Cheongang, staggering as he dropped to one knee. Cheongpung’s figure, flung like a cannonball and rolling across the ground. Both came into my blurred vision.

And the monster’s steps, as he came toward me after tearing down every last obstacle in his way.

*Splash.*

One step, then another.

As the distance closed, the Blood Lord’s red eyes grew clearer. I used every bit of strength I had to get up.

Like a baby turning over for the first time, I rolled onto my front, braced myself on my hands and knees, and somehow got my unsteady body to its feet.

And at the moment I met the Blood Lord’s eyes, now close enough to blaze red like the sun—

*Inventory open. Summon.*

From the boundless storehouse granted to me alone in this vast world, I drew a finely sharpened dagger and thrust it forward.

At the same time, I heard a quiet sneer cut into my ears.

“As expected.”

*Crack.*

I felt no pain, but the sound alone told me what had happened.

The Blood Lord had snatched my wrist in a flash and crushed it beyond any hope of recovery.

But the Blood Lord wasn’t the only one who could predict his opponent.

*Slip. Tap.*

Ignoring the pain erased by my final rally, I kicked the dagger’s hilt with my toe as it fell from my grasp.

*Thud.*

“……!”

With a cool, tearing sound, the dagger sank deep into flesh.

The Blood Lord’s eyes flew wide as he looked down at the blade buried in his shin. He licked his lips.

“Impressive. Truly impressive. But because of that…”

Without a moment’s hesitation, he whipped his remaining leg like a lash.

“You can never be allowed to live.”

KRRRCH!

White bones burst through mangled flesh.

After crippling one arm and both legs, the Blood Lord shot out his hand like lightning and grabbed me by the throat.

*Crack.*

My bones shifted with a crunch, and my vision darkened.

The Blood Lord’s voice, sunk deep and low, reached my ears as I gasped for breath.

“This has been a long and bitter connection. Blazing Flame Divine Dragon Jin Taekyung.”

At that moment—

*FWOOSH.*

Like the last candle recalling the life that had come before, my vision, tumbling into pitch-black darkness, turned white.

No.

Perhaps it was a shade deeper and redder than sunset.

*Slash.*
```
