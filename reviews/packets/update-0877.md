<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0877.txt",
      "sha256": "d46cc787490b22a351a92adbb98e64b5fe09a4da4a3646d2a6744270aa6f3255",
      "bytes": 13142
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "29489f2cdfe0319533f71686539f46196be6358ce735568e5d392a127f5ae59f",
      "bytes": 1708
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3de1f8e5a93c04e8a977dadc6905f5851ff36752f5559f9e89cbdbe61f3583b0",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "e93f09e2ef790eb250d649f2e95419fdd684419d0e503f4ed665fd355239e149",
      "bytes": 854
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "918925b4e066cc88460a76808b6b79048b892813f22abf9986d0f8d48c01222a",
      "bytes": 1432
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ee193969d589fe329600501d530b77745a9d0e70a90fecafb43c486014cbfd7c",
      "bytes": 1511
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "73d85108fce06b92873109acf8db60adede7b3bf586f8168d15e12553c773a01",
      "bytes": 765
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "26fe1f73b1cbb54f47b0de22b083425220feac895f12042268879eef59ad1613",
      "bytes": 554
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "811e9bbf9b17eed4a564a962f2c6bdbfe410b7c2cf24d2a1853578d647fd108b",
      "bytes": 952
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d9384e9ac1b5e8435b4526eb3ad43743df747a3184af7f49792e9027db164ec5",
      "bytes": 258472
    }
  ],
  "estimated_tokens": 11412
}
-->

# Durable State Update — Chapter 877

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
1 and safe_through 877. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 877. Profile updates may replace only one
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
  "chapter": 877,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 877,
    "continuity_sources": [877],
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
    "Prince Shangshan remains in the imperial capital under the care of palace attendants led by So Gyo; Taekyung gave him the Myriad-Poison Ring for protection against poisoning.",
    "The palace attendants assigned to Shangshan are First Rate martial artists who carry flexible swords.",
    "The Emperor has a concealed Supreme Peak assassin, No Shadow.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "Qianqing Palace is defended by mechanisms and formations, at least three Supreme Peak masters, and more than a hundred elite assassins.",
    "Taekyung heard Aehyang’s voice in a restricted part of Qianqing Palace and recognized her as the concubine the City Lord of Sichuan Province lost to the Emperor.",
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him.",
    "Hong Jin and Taekyung conclude Aehyang is pregnant; they suspect the Emperor may intend her child to replace Shangshan as heir."
  ],
  "continuity_sources": [
    875,
    876
  ],
  "open_questions": [
    "What does the Emperor intend for Shangshan, and what are the palace attendants’ true orders?",
    "What is Aehyang’s situation in the restricted part of Qianqing Palace, and is she pregnant?",
    "What is the nature of the Emperor’s connection to Dark Heaven?"
  ],
  "safe_through": 876,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 암천     | **Dark Heaven**                  |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 사성 | **Four Saints** | Rank the Blood Lord says Jeok Cheongang might have attained if the Great Faction War had continued another year. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 애향이 | **Aehyang** | Personal name of the Sichuan City Lord's favorite concubine. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 애향 | **Aehyang** | The City Lord’s favored concubine. |
| 혈혼고 | **Blood Soul Gu** | Rare gu poison found deep in Nanman. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 사천성주 | 애향이 | lord_to_favorite_concubine | Aehyang | affectionate-familiar | The City Lord uses her personal name while discussing the visitors. |
| 애향이 | 사천성주 | favorite_concubine_to_city_lord | My lord | seductive-deferential | Aehyang repeatedly addresses the City Lord as 대인 while persuading him to receive Taekyung. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 혁무진 | 홍진 | martial artist addressing a senior official and political ally | Comrade Hong | casual and coaxing | Hyuk Mujin addresses Hong Jin as 홍 동지님 while trying to calm him and de-escalate the confrontation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 876
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 876
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he left the palace to serve the prince, while his longtime friend and former East Depot cohort Ma Sanbao stayed behind.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 876
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 875
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 876
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 875
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 876
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

## Korean source

```text
＃877화



애초에 말도 안 되는 일이었다.

명색이 황족씩이나 되는 인간들이 옆집 춘식이네도 아닌데 건청궁에 모여 다 함께 오순도순 사는 게 말이 되나.

게다가 직접 탐방하고 온 입장에서 말하자면, 그곳은 황제가 먹고 자는 생활공간이라기보다는 요새나 미궁에 가까웠다.

부산의 연산 로터리마냥 이리저리 뒤얽힌 길을 지나다가 미노타우로스를 마주쳐도 딱히 놀랍지 않은 그런 느낌.

그뿐인가.

중국 바퀴벌레 같은 살수들이 사방에 득실거리고, 혹시 모를 불청객을 대비한 기관진식까지 설치되어 있다.

이 정도면 어느 영국 마법 학교의 지하 감옥 기숙사가 5성급 호텔로 보이는 수준.

그러나 황제가 단순히 미친놈이라서 이처럼 꿈도 희망도 없는 환경을 조성한 것은 아닐 것이다.

그에게는 분명한 목적이 있었다.

말 그대로 철통같은 보안.

어떤 암살자도 뚫지 못할 강력한 전력을 갖추고, 믿을 만한 충복들로 건청궁을 채운 건 바로 그런 이유에서였을 것이다.

그리고 그 목적은 지금까지 훌륭하게 유지되어 왔다.

바로 오늘, 무림에서 굴러먹다 온 웬 젊은 무뢰배가 애향의 존재를 알아차리기 전까지는.

어쩌면 황제가 숨기고자 했던 가장 비밀 중 하나를 짐작해 내기 전까지는.

‘임신이라니.’

마치 쇠망치로 뒤통수를 얻어맞은 기분이다. 탁자 하나를 사이에 두고 마주 앉은 홍진과 혁무진의 표정 역시 다르지 않았다.

“회임……이요? 그게 진짭니까?”

“아직 확신할 수는 없지만 그럴 가능성이 농후해요.”

넋 나간 목소리로 물어오는 혁무진을 향해 대답한 홍진이 나직하게 덧붙였다.

“이 모든 게 말도 안 되는 헛소리라면 가장 좋겠지만.”

나도 무겁게 고개를 끄덕였다.

피붙이 간의 정이고 나발이고, 일가친척의 피로 반신욕을 하다시피 하며 권좌를 탈취한 황제다.

그런데 이런 상황에서 자신의 피를 이은 자식이 탄생한다면, 머지않아 상산왕에게 닥칠 상황은 뻔했다.

참초제근(慘草除根).

강보에 싸여 쫓기듯 황궁을 떠나야 했던 어린아이는 이제 어엿한 소년이 되었고, 한 뿌리에서 난 거목(巨木)의 씨앗은 싹이 되어 잘 영글었다.

의심 많은 황제가 상산왕을 제거할 이유는 그것으로도 차고 넘친다.

‘후계 정리.’

하늘에 두 개의 태양이 있을 수는 없듯이, 천자라는 존재도 마찬가지다.

지금의 황제는 조정과 백성의 불만을 억제하며 군림하고 있으나 폭군이자 반역자라는 본질은 변하지 않는다.

아니, 그의 혈관에 흐르는 피처럼 새로운 후계자에게 이어질 것이다.

반역자의 자식이라는 꼬리표와 함께.

그리고 황제에 대한 반발심을 애써 억누르고 있는 권력자들은 그 상황을 썩 달갑게 여기지 않을 것이 틀림없었다.

당장 연판장(連判狀)이라는 이름의 롤링페이퍼를 작성한 이들에게는 상산왕이라는 훌륭한 대안이 있었으니까.

‘바로 그 상산왕이 세상에서 사라진다면, 황제에게는 더할 나위 없는 호재일 테고.’

모두가 나와 같은 생각을 하는 듯, 전각 안의 공기는 무겁고 냉랭했다.

깊게 가라앉은 눈빛으로 허공을 응시하던 홍진이 불쑥 입을 연 것은 한참이나 침묵이 흐르던 그때였다.

“어떻게 그 사실을 짐작할 수 있었던 거죠?”

“무슨 뜻입니까?”

“저야 황궁의 사정에 대해 어느 정도 알고 있다지만, 진 공자께서는 단순히 그 애향이라는 여인이 건청궁에 머무른다는 사실만으로는 쉽게 추측할 수 없었을 텐데.”

잠시 그때 상황을 떠올린 내가 대답했다.

“단순히 소리만으로는 짐작할 수 없었습니다. 한 가지가 더 있었죠.”

“그게 뭔가요?”

“냄새.”

“냄새?”

“예. 희미하지만 분명한 약재 냄새를 맡았습니다. 정확히는 탕약이요.”

“탕약이라…….”

“솔직히 제 주위에 그 방면으로 잘나가는 분들이 계시긴 하지만, 정확히 어떤 약재를 썼고 탕약의 재료가 뭔지는 모릅니다. 하지만 단순히 생각해 보니 대강의 답이 나오더라고요.”

나는 천천히 말을 이었다.

“탕약이란 게 결국 병자나 보신(補腎)이 필요할 때 쓰이는 건데, 지금 이 상황에서 황제가 애향에게 탕약을 먹이는 이유가 뭘까. 단순히 아프니까 걱정이 돼서? 아니면 다른 이유가 있어서?”

주어진 모든 상황과 단서를 짜 맞추면 밑그림이 그려진다.

이번에도 역시 마찬가지였다.

적어도 내가 파악한 황제는 사랑꾼과는 거리가 먼 인물이었고, 건청궁은 그만큼 특수한 곳이었으니까.

“저로서도 설마 했습니다. 그래서 최대한 빨리 돌아온 거였고요.”

홍진이 침음성을 흘렸다.

“진 공자는 이 이야기가 사실일 가능성이 얼마나 될 것 같아요?”

“냉정하게?”

“네. 냉정하게.”

“최소 구 할 이상.”

“……!”

“죄송합니다. 하지만 제가 보기에는 모든 게 너무 정확하게 맞아떨어져요.”

빌어먹을 현실이지만 인정할 건 해야 한다.

십 년이 넘도록 수수방관하던 황제가 갑작스럽게 상산왕을 황도로 부른 이유. 반강제에 가깝게 건청궁에 묶어 둔 이유.

그리고…… 상산왕을 해할 만한 이유.

그 모든 의문에 대한 답이 저 하나로 해결된다.

‘새로운 후계자.’

홍진도 그 사실을 모르지는 않을 것이다.

아니, 아마도 누구보다 확신하고 있을 것이 틀림없었다.

전날 밤 찾아온 마삼보조차 이런 중요한 정보에 대하여 일언반구도 없었다는 것은, 황제가 동창의 눈조차 속이며 애향의 상태를 철저히 함구해 왔다는 뜻.

이 사실이 무엇을 의미하는지, 동창 내에서도 상당한 고위직이었던 홍진이 모를 리 없었다.

짐작이라 쓰고 확신이라 읽을 뿐.

애향의 배 속에 황제의 씨앗이 들어 있다는 것은 이미 기정사실이나 다름없었다.

‘다만 부정하고 싶은 거지.’

마음속으로 뇌까린 나는 조용히 홍진을 응시했다. 그리고 아직 해결되지 않았던 의문 중 하나를 꺼내 들었다.

“이런 말씀 드리기에는 시기가 좋지 않지만, 한 가지 여쭤봐도 됩니까?”

홍진이 가라앉은 목소리로 대답했다.

“뭐든지.”

“황제는 왜 진작 상산왕 전하를. 어. 그러니까…….”

“제거하지 않았느냐고요?”

내가 묵묵히 고개를 끄덕이자, 홍진이 말을 이었다.

“황제의 속마음까지 정확히 알 수는 없겠지만, 적어도 한 가지는 확실해요. 아직 젖도 다 떼지 못했던 어린 황자마저 해친다면 그 후폭풍이 두려웠겠죠.”

“그러기에는 이미 수많은 사람을 죽이지 않았습니까?”

“숙청은 하루아침에 끝난 게 아니에요. 특히 황족들은.”

“더 자세히.”

“사 황자의 반란이 성공적으로 마무리된 직후, 선황 폐하를 비롯한 직계 황족들은 유폐되어 철저한 감시를 받았죠. 그리고 일 년이라는 시간 동안 마치 약속이라도 한 것처럼 차례차례 숨을 거두었고. 참 희한하지 않아?”

목소리는 담담하지만, 아직 가시지 않은 충격과 두려움마저 숨길 수는 없다.

떨리는 손으로 품에서 곰방대를 꺼낸 홍진이 불을 붙였다.

후우.

깊은 심호흡과 함께 뿜어지는 희끄무레한 연기.

나는 문득 어디선가 맡아 본 냄새라고 생각하며, 이어지는 이야기에 귀를 기울였다.

“동창의 역량을 총동원해 선황 폐하를 비롯한 황족들을 구출하려고 했지만, 모두 보기 좋게 실패했어요. 나는 이미 일거수일투족을 감시당하고 있었고, 당장 내일 형옥(刑獄)에 갇혀도 이상하지 않을 상황이었지.”

“하지만 결과적으로 황제에게 죽임을 당하진 않았고요.”

“맞아요. 묵은 인연 때문인지, 혹은 단순한 변덕 때문인지는 몰라도 사 황자는 나를 살려 뒀지.”

“묵은 인연?”

“내가 황궁에 몸담은 세월만 수십 년이에요. 선황 폐하를 가까이에서 모셨던 만큼 사 황자와도 적지 않게 마주쳤지. 여러모로 뛰어나고 명석한 소년이었어요. 적어도 그때에는.”

희뿌옇게 천장 위로 솟구치는 연기를 바라보는 홍진의 눈동자는 공허했다.

“어찌 되었건 나는 살아남았고, 선황 폐하께서 붕어하시기 직전에야 그분을 알현할 수 있게 됐어요. 마치 광증(狂症)에 걸린 사람처럼 정신이 혼미하신 와중에도 내게 상산왕 전하를 부탁하셨지.”

“잠깐, 광증이요?”

“응. 그런데 그게 왜…… 아.”

내가 하려는 말을 알아차린 홍진이 혼란스러운 얼굴로 되물었다.

“설마?”

“가능성은 있습니다. 정확히 증상이 어땠습니까?”

“일각도 되지 않을 만큼 짧아서 뭐라 말하기 힘들어요. 그 나이에 후사(後嗣)를 보셨을 만큼 정정하셨던 건 사실이지만 이미 연로하셨고.”

“압니다. 역모에 유폐까지 겹쳤으니 충격이 크셨겠죠. 하지만 최대한 본 것 그대로 말씀해 주셔야 합니다. 그래야…….”

“사천성주와의 유사성을 찾을 수 있을 테니까?”

“……!”

마른침을 삼키며 듣고 있던 혁무진이 눈을 부릅떴고, 나는 조용히 고개를 끄덕였다.

암천(暗天)이라는 두 글자와 함께, 불과 보름 전쯤 보았던 그 저주받은 생물을 떠올리며.

‘혈혼고(血魂蠱).’

사천 땅의 내로라하는 명의들조차 흔적을 찾지 못했던 독물.

전무하다시피 할 만큼 아무런 흔적도 남기지 않고 숙주를 죽음으로 몰아가는 그것은 수백여 년 전 남만의 오독문에서 탄생했고, 이제는 산 사람이 아니게 된 사천성주의 시신에서 발견되었다.

‘그리고 사천성주는 몇 달 전 황도에서 돌아오는 길에서부터 이상 증세를 보이기 시작했지.’

이게 과연 단순한 우연일까?

나는 이루 말할 수 없을 만큼 딱딱하게 굳은 홍진의 표정에서 그 답을 찾을 수 있을 것 같았다.

“가능성이 얼마나 되리라 보십니까?”

침묵하던 홍진이 대답했다.

“지금으로서는 일 할. 아니, 이 할.”

“당시에 유폐되었던 다른 황족분들이 어떻게 돌아가셨는지는 압니까?”

“알려지지 않았어요. 그렇게 잊혔고.”

“그렇다면…….”

“늦어도 오늘 밤 마 태감에게 연락을 취할 생각이에요. 전하의 목숨이…… 경각에 달했을지도 몰라요.”

맞다.

정말 몇 달 전 사천성주에게, 십여 년 전 선황에게 혈혼고를 심은 것이 황제라면. 혹은 그와 손잡은 암천이라면 상산왕은 이미 죽은 목숨이나 다름없다.

하지만…….

“제가 따로 지니고 있던 귀물(貴物)을 전하께 맡겼으니 당장은 크게 걱정하지 않아도 될 겁니다.”

만독지환.

비록 심각한 부상을 입었다고는 하나, 화왕 적천강이라는 거인마저 쓰러트린 무형지독을 해독한 사천당문의 신물(神物).

혈혼고도 결국은 오독문의 손을 거쳐 탄생한 독물인 만큼, 만독지환의 효능을 벗어날 수는 없을 것이다.

아니, 반드시 그래야 한다.

“그리고 하나 더. 개인적으로 마 태감께 부탁할 것이 있습니다.”

뒤이어 이어진 내 말에, 홍진의 두 눈이 크게 뜨였다.



* * *



절강성, 그중에서도 항주(杭州)는 황실이 이전해 오기 전부터 천하에서 둘째가라면 서러운 향락의 도시였다.

수많은 명승고적과 아름다운 경치. 운하를 따라 막대한 자원과 재물이 오가고, 깊은 밤에도 환하게 밝혀진 거리는 늘 사람들로 북적였다.

말 그대로 불야성(不夜城).

그리고 온갖 점포들이 자리 잡은 이 황도의 대로변에서, 밤늦게 손님이 찾아온 것은 그리 이상한 일이 아니었다.

그 손님을 대하는 종업원의 태도는 조금 이상했지만.

“어디 한 번 둘러보쇼. 마음에 들면 그때 물어보시고.”

귀찮아 죽겠다는 얼굴. 퉁명스러움이 뚝뚝 묻어 나오는 중년의 종업원을 물끄러미 바라보던 손님이 입술을 달싹인 것은 그때였다.

- 열화신룡(烈火神龍)의 전언을 가져왔소.

“……!”

혁가포목점이라 적힌 현판 아래, 중년의 종업원. 아니 화왕 적천강은 눈을 부릅떴다.
```

## Final English reading copy

```markdown
# Chapter 877

It had never made any sense in the first place.

These were members of the imperial family, for crying out loud. These were members of the imperial family, not Chunshik’s family next door. Why would they all gather in Qianqing Palace and live together like one big happy family?

Besides, having been there myself, I could say the place was closer to a fortress or a labyrinth than to the Emperor’s living quarters.

The kind of place where you could wander through roads as tangled as the Yeonsan Rotary in Busan and run into a Minotaur without finding it particularly surprising.

And that wasn’t all.

Assassins swarmed everywhere like Chinese cockroaches, and mechanisms and formations had been set up to deal with any unwelcome visitors.

At this point, even the dormitory dungeons beneath some British school of magic would look like a five-star hotel.

But the Emperor couldn’t have created an environment this hopeless simply because he was crazy.

He had a clear purpose.

Security, quite literally as solid as iron.

He must have surrounded Qianqing Palace with enough force to stop any assassin from breaking through, then filled it with loyal servants he could trust. That was why.

And until now, he’d carried out that purpose perfectly.

Right up until today, when some young ruffian who’d spent his life scraping by in Murim realized Aehyang was there.

Or perhaps until he guessed one of the Emperor’s most closely guarded secrets.

*Pregnant?*

It felt like I’d been hit in the back of the head with a sledgehammer. Hong Jin and Hyuk Mujin, sitting across the table from me, looked just as stunned.

“Pregnant…? Is that true?”

“I can’t be certain yet, but it’s highly likely.”

Hong Jin answered Hyuk Mujin’s dazed question, then added quietly,

“It would be best if all of this were utter nonsense.”

I nodded heavily.

To hell with family ties—the Emperor had seized the throne after practically bathing in his relatives’ blood.

If a child of his own blood were born under these circumstances, it was obvious what would soon happen to Prince Shangshan.

*Pulling up the weeds by the roots.*

The child who’d once had to leave the imperial palace in a rush, wrapped in swaddling cloth, had now grown into a proper young boy. And the seed of a towering tree, sprung from the same root, had taken hold and flourished.

That was more than enough reason for a suspicious Emperor to eliminate Prince Shangshan.

*Clearing the line of succession.*

Just as there couldn’t be two suns in the sky, there couldn’t be two Sons of Heaven.

The current Emperor ruled over the court and the people, suppressing their discontent, but he was still a tyrant and a traitor at heart.

No—like the blood running through his veins, that nature would be passed on to his new successor.

Along with the label of a traitor’s child.

And the powerful men who were forcing down their resentment toward the Emperor certainly wouldn’t welcome that.

The people who’d put together that petition—basically a rolling paper for signatures—already had an excellent alternative in Prince Shangshan.

*If that very prince disappeared from the world, it would be the best possible news for the Emperor.*

The air in the pavilion was heavy and cold, as if everyone were thinking the same thing I was.

Hong Jin had been staring into space, his gaze sunk deep, and a long silence had passed before he suddenly spoke.

“How did you guess?”

“What do you mean?”

“I know a fair amount about the imperial palace, but Young Master Jin couldn’t have made that guess just from knowing that a woman named Aehyang was staying in Qianqing Palace.”

I thought back to the situation and answered.

“I couldn’t have guessed from the sound alone. There was one other thing.”

“What was it?”

“The smell.”

“The smell?”

“Yes. It was faint, but I could clearly smell medicinal herbs. More precisely, a decoction.”

“A decoction…”

“To be honest, I do have people around me who know a lot about that sort of thing, but I don’t know exactly which herbs were used or what went into it. Still, when I thought about it, I could work out the general answer.”

I went on slowly.

“A decoction is ultimately used when someone is sick, or when they need to restore their health. So, given the circumstances, why would the Emperor be giving Aehyang one? Simply because she was ill and he was worried? Or was there another reason?”

When you fitted every circumstance and clue together, a picture began to emerge.

This time was no different.

At least as far as I could tell, the Emperor was far from a lovesick romantic, and Qianqing Palace was an unusual place for a reason.

“I couldn’t believe it myself. That’s why I came back as quickly as I could.”

Hong Jin let out a low groan.

“How likely do you think it is that this is true, Young Master Jin?”

“Do you want the cold, hard answer?”

“Yes. The cold, hard answer.”

“At least ninety percent.”

“……!”

“I’m sorry. But everything fits together too perfectly, as far as I can tell.”

It was a damnable reality, but I had to acknowledge what I saw.

The reason the Emperor, who’d left Prince Shangshan alone for over a decade, had suddenly summoned him to the imperial capital. The reason he’d practically forced him to stay in Qianqing Palace.

And… the reason he might want to harm Prince Shangshan.

One answer resolved every question.

*A new heir.*

Hong Jin couldn’t have missed that, either.

No—he was probably more certain of it than anyone.

Even Ma Sanbao, who’d come to visit the night before, hadn’t said a word about such important information. That meant the Emperor had kept Aehyang’s condition completely secret, even from the East Depot.

Hong Jin, who’d held a fairly high position within the East Depot, couldn’t fail to understand what that meant.

Call it a guess, but read it as certainty.

It was all but a foregone conclusion that the Emperor’s seed was growing inside Aehyang.

*He just wants to deny it.*

I muttered to myself and watched Hong Jin in silence. Then I brought up one of the questions that still hadn’t been answered.

“I know this isn’t the best time to ask, but may I ask you something?”

Hong Jin answered in a subdued voice.

“Anything.”

“Why didn’t the Emperor eliminate Prince Shangshan sooner? I mean…”

“Why didn’t he kill him?”

I nodded silently, and Hong Jin continued.

“I can’t know exactly what was in the Emperor’s heart, but one thing is certain. He was probably afraid of the backlash if he killed even a young prince who hadn’t been weaned yet.”

“Hadn’t he already killed countless people?”

“The purge didn’t end overnight. Especially when it came to the imperial family.”

“Tell me more.”

“Right after the Fourth Prince’s rebellion was successfully concluded, the late Emperor and the other members of the direct imperial family were confined and placed under strict surveillance. Then, over the course of a year, they died one after another, as if they’d all made some kind of agreement. Strange, isn’t it?”

His voice was calm, but he couldn’t hide the shock and fear that still lingered.

Hong Jin drew a long-stemmed tobacco pipe from inside his robe with a trembling hand and lit it.

Whoosh.

He exhaled a pale plume of smoke with a deep breath.

For a moment, I thought I recognized the smell from somewhere. Then I turned my attention back to his story.

“I mobilized the East Depot’s full strength to rescue the late Emperor and the other royals, but every attempt failed miserably. I was already being watched in everything I did. It wouldn’t have been strange if I’d been thrown in prison the very next day.”

“But in the end, the Emperor didn’t kill you.”

“That’s right. Maybe because of our old ties, or maybe out of simple caprice, the Fourth Prince let me live.”

“Old ties?”

“I served in the imperial palace for decades. I was close to the late Emperor, so I also crossed paths with the Fourth Prince quite a few times. He was a talented, sharp-minded boy in many ways. At least back then.”

Hong Jin’s gaze was empty as he watched the smoke drift toward the ceiling.

“Regardless, I survived, and I was finally allowed to see the late Emperor shortly before he passed away. Even though his mind was clouded, almost as if he’d gone mad, he entrusted Prince Shangshan to me.”

“Wait. He’d gone mad?”

“Yes. But why would that—oh.”

Hong Jin realized what I was getting at and asked, his face confused,

“Surely not?”

“It’s possible. What exactly were his symptoms like?”

“I saw him for less than fifteen minutes, so it’s hard to say. He was already old, though he’d been healthy enough to father a child at that age.”

“I know. The rebellion and confinement must have been a terrible shock. But you need to describe exactly what you saw. That’s the only way we can…”

“Find a similarity to the City Lord of Sichuan Province?”

“……!”

Hyuk Mujin, who’d been listening with a dry swallow, widened his eyes. I nodded quietly.

At the words *Dark Heaven*, I remembered that cursed creature I’d seen only about two weeks ago.

*Blood Soul Gu.*

A venomous creature whose traces even the most renowned physicians in Sichuan couldn’t find.

It left almost no trace at all, driving its host to death. It had been created centuries ago by the Five Poisons Sect of Nanman, and had been discovered in the corpse of the City Lord of Sichuan Province, who was no longer among the living.

*And the City Lord of Sichuan Province started showing strange symptoms months ago, on his way back from the imperial capital.*

Could this really be a coincidence?

I thought I could find the answer in Hong Jin’s expression, rigid with unspeakable tension.

“How likely do you think it is?”

Hong Jin answered after a silence.

“Ten percent. No… twenty.”

“Do you know how the other royals who were confined back then died?”

“It was never made public. They were forgotten.”

“Then…”

“I’m going to contact Eunuch Ma tonight at the latest. His Highness’s life… may be in immediate danger.”

Right.

If it really was the Emperor—or Dark Heaven working with him—who had implanted Blood Soul Gu in the City Lord of Sichuan Province a few months ago, and in the late Emperor more than a decade ago, then Prince Shangshan was as good as dead already.

But…

“I entrusted His Highness with a precious artifact I’d been carrying, so there’s no need to worry too much for now.”

The Myriad-Poison Ring.

Though he’d suffered a serious injury, it had detoxified the Formless Ultimate Poison that had even brought down Jeok Cheongang, the giant known as the Fire King. It was the Sichuan Tang Clan’s divine artifact.

Blood Soul Gu was ultimately a venomous creature created by the Five Poisons Sect. It couldn’t escape the Myriad-Poison Ring’s power.

No—it had to work.

“And one more thing. There’s something I’d like to ask Eunuch Ma to do for me personally.”

Hong Jin’s eyes widened at what I said next.

* * *

Hangzhou, in Zhejiang Province, had been one of the most extravagant cities under heaven even before the imperial court moved there.

It had countless scenic landmarks and beautiful views. Vast quantities of goods and wealth passed along its canals, and even late into the night, its brightly lit streets bustled with people.

A city that never slept, in every sense.

And it wasn’t unusual for customers to arrive late at night on the main road of this imperial capital, lined with all kinds of shops.

Though the shopkeeper’s attitude toward this particular customer was a little unusual.

“Go on, take a look around. If you like anything, ask me then.”

The middle-aged employee looked bored to death, his manner dripping with brusqueness. The customer studied him for a moment, then parted his lips.

“I’ve brought a message from the Blazing Flame Divine Dragon.”

“……!”

Beneath a sign that read *Hyuk Family Textile Shop*, the middle-aged shopkeeper—no, Jeok Cheongang, the Fire King—opened his eyes wide.
```
