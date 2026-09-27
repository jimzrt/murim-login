<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1086.txt",
      "sha256": "3f808dad6ab203777668160fe2c54a535b0842b4b0975a71fa744bcfdebd5e52",
      "bytes": 11539
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "00acc98b056a2859ad3d644e42b0964ce6a7b29533c19482de60bfc4aaa8818b",
      "bytes": 1124
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1004ef74185869d3443d7c03af7ca2ad564e5ecc02ba7ebfa5360f6bbb22bb7e",
      "bytes": 243655
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4943f4b6129bd87a87bc2eac03864ff1a718ed341c640a6b5d81b87c36aaa885",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "b349485788e21de1857e2cf09694bd38be686973b5cd6c8bcc0bd2a271210d38",
      "bytes": 554
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "61d8066e933f2bba48486e7b4080c8cebcb5b96244cf7b1cf2fc5318867a1f25",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6e1bf0a6acbd63070fe82658b335d4f55e75fb7eb96926d90b13793c2f224672",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "e2584dcbd3eb482412e94c8f05aa6ec748ac88fbca7c7a1260f025a5f6afbb69",
      "bytes": 1084
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "c12e2eabe603a3c9b6a0f61bc612344d92961e2dce23cbd2bfc942a344ab1782",
      "bytes": 768
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "b183b7ecf7a50a40c65b1c083eff472c43d11fb28a096a7637642b0e26fc5b84",
      "bytes": 650
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c4a0e6a83aedc85b5783bb09dd09c0203fec4ce272e8879854936f6a4d11be19",
      "bytes": 286755
    }
  ],
  "estimated_tokens": 10447
}
-->

# Durable State Update — Chapter 1086

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
1 and safe_through 1086. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1086. Profile updates may replace only one
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
  "chapter": 1086,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1086,
    "continuity_sources": [1086],
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
    "The Yangtze River Channel League and Green Forest Alliance are advancing west in a large combined force.",
    "Dark Heaven reinforcements are joining the forces through Moving Formations, whose locations remain unknown.",
    "Green Forest forces crossed Tongsan with an estimated five thousand men; additional troops have joined from scattered strongholds.",
    "The orthodox factions have suffered severe losses, and some local leaders refuse to risk their families in a confrontation.",
    "Zhuge Feng has located the concealed Alliance Leader in the Zhuge Clan’s Inner Hall garden."
  ],
  "continuity_sources": [
    1085
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who is the black-robed man beside Pa Ryun?"
  ],
  "safe_through": 1085,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 하오문    | **Lower District Sect**          |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 가주     | **Family Head**                              |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 본가      | **our family / this family**                                    |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 가주전 | **Family Head's Hall** | Hall where the Tang Family Head receives visitors. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 전도 | **complete map of the realm** | Mae Jonghak's map marking terrain, place names, and sect locations. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 화원 | **Fire Courtyard** | Courtyard associated with Jin Taekyung and Ju Hwaran's final walk before leaving Sichuan. |
| 진화 | **evolution** | The transformation the Southern Heaven Demon Empress claims the rift will produce. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |
| 천면호리 | 매종학 | intelligence_chief_to_alliance_leader | Alliance Leader | formal and deferential | Requests that Mae move elsewhere with the others before he reports further. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 매종학 | 천면호리 | Alliance Leader to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | casual-but-commanding | Asks Song Ho's view of Taekyung's suspected target. |
| 매종학 | 제갈풍 | Alliance Leader to Zhuge Clan Family Head | Family Head Zhuge | formal and familiar | Mae Jonghak asks whether Zhuge Feng completed his assignment. |
| 제갈풍 | 송호 | Zhuge Clan Family Head to Hidden Shadow Pavilion Chief | Chief of the Hidden Shadow Pavilion | formal and playfully accommodating | Zhuge Feng jokes that he would overlook Song Ho’s conduct if the amount were reasonable. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |
| 제갈풍 | 맹주 | Zhuge Clan Family Head to Murim Alliance Leader | Alliance Leader | polite | Zhuge Feng addresses the concealed Alliance Leader in the Zhuge Clan garden. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1083
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1081
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1084
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1084
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1027
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 1085
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 1085
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
1086화




좋게 말하면 서글서글하고, 나쁘게 말하자면 일면식이 있더라도 금세 잊을 법한 흔한 인상의 청년이었다.

그리 크지도, 작지도 않은 체격과 어느 곳에 있어도 쉽게 녹아들 것 같은 자연스러운 분위기를 풍기는.

아마도 그래서였을 것이다.

제법 긴 외유를 끝마치고 가문으로 복귀한 제갈풍의 곁에 있던 어느 청년의 모습에서, 그 누구도 검성(劍星)이라는 별호를 떠올리지 못했던 것은.

“오, 자네로군.”

그제야 뒤돌아선 매종학이 제갈풍을 향해 빙긋 웃었다.

깊으면서도 맑은 눈동자와 보는 것만으로도 마음이 편안해지는 듯한 미소.

극심한 혼란과 불안에 휩싸인 천하와 달리, 그들 중 누구보다 막중한 책임감을 짊어지고 있어야 할 무림 맹주는 천진난만한 어조로 말을 이었다.

“여기저기 돌아다니다 보니 심심해져서 말일세. 어느 순간 그저 이끌리는 대로 걸음을 옮기다 보니 이곳이지 뭔가.”

“어디인지도 모르고 오셨단 말입니까?”

“그렇네만.”

“이 화원을 중심으로 일백여 장이 전부 가주전(家主殿)입니다. 본가의 직계들도 제 허락이 있어야 들어올 수 있지요.”

“그랬나? 어쩐지 좀 이상하다고는 생각했지. 이곳저곳 숨어 있는 인기척도 인기척이지만, 온갖 잡다한 기관진식에 진법(陳法)도 제법 깔려 있길래.”

매종학의 대답을 들은 제갈풍은 헛웃음을 흘릴 수밖에 없었다.

“무슨 좋은 일이라도 있나?”

“그럴 리가요. 그냥 웃겨서 그렇습니다.”

천하에서 내로라하는 대도(大盜)들도 감히 함부로 넘볼 수 없는 곳이 바로 제갈세가다.

오죽하면 하늘도 훔칠 수 있다던 천도객(天盜客)이 간 크게도 제갈세가의 가주전에 침입, 직후 기관진식에 갇혀 달포를 넘게 헤매었을까.

당시 천하제일의 대도였던 그는 결국 자비로운 선대 가주의 명에 따라 제갈세가의 무인들에게 구출되었고, 피골이 상접 한 채로 풀려 나오며 이런 말을 남겼다.



‘황궁에 침입하면 고문당하다 죽고, 사천당문은 중독되어 죽지만, 제갈세가는 영혼까지 털려서 서서히 굶어 죽는다.’



후대의 도둑놈들에게 뼈저린 교훈을 남긴 삼금지(三禁地)는 그렇게 탄생했다.

물론 당대 최고의 대도도 아사할 뻔한 제갈세가의 가주전도, 천하제일의 검객 앞에서는 무용지물이었다는 것이 확인되었지만.

“이거 실례했군. 가주전인 줄 알았다면 허락이라도 맡았을 텐데.”

“그때 전 회의 중이었습니다.”

“집주인이 없다고 문이 안 열리나? 숨어 있던 이들에게 부탁하면 되지.”

“만에 하나 부탁하셨더라도, 그 친구들이 ‘어휴, 어디에 있다가 이제야 오셨습니까’ 하고 열어 줬겠습니까?”

“하긴 그도 그렇군. 맹주라고 밝힐 수도 없는 노릇이니.”

뒤통수를 긁적이는 매종학의 모습에, 제갈풍은 고개를 절레절레 내저었다.

그도 세간에서는 제법 괴짜라는 평을 듣지만, 눈앞의 저 사내에 비하면 발끝에도 미치지 못할 것 같았다.

“그래서, 이곳에서 뭘 하시던 중이셨습니까?”

“향을 맡고 있었지.”

“향, 말입니까.”

제갈풍은 고개를 갸웃거렸다.

가주전의 주인이 된 지 한참의 세월이 흘렀음에도, 그가 이 화원을 드나든 적은 손가락으로 헤아릴 수 있을 만큼 드물었다.

제갈풍 자신이 학문과 기관진식의 연구에 대부분의 시간을 할애했기 때문도 있지만, 이곳은 화원(花園)이라 칭하기에 너무 투박했으니까.

“보시다시피 이 화원에는 온통 뽕나무뿐이라, 딱히 경치나 향이 좋지도 않습니다만.”

“그렇지 않네. 세상 만물에는 저마다의 향이 있지. 이 뽕나무 역시 마찬가지일세.”

매종학이 나직이 덧붙였다.

“지금은 손이 닿지 않은 곳에 피어 있을, 매화(梅花) 역시도.”

어렴풋한 그 음성에, 잠시 침묵하던 제갈풍이 조심스럽게 입을 열었다.

“화산으로…… 돌아가고 싶으십니까?”

“언제나 늘 그랬지. 하지만 지금 같은 상황에서는 아닐세. 내가 있어야 할 곳은 정해져 있어.”

“하면.”

“그리울 뿐일세. 평화롭던 그때가. 매화가 흐드러지게 피어난 숲속에서 햇살을 받으며 누워 있던 그 날이.”

매종학은 손을 뻗어 가까이에 있는 뽕나무를 쓰다듬었다.

계절을 무시한 서린 날씨 때문일까, 열매 하나 없이 가지를 늘어트린 그것은 작금의 천하를 닮아 있었다.

“이 뽕나무에도 언젠가 열매가 맺히겠지. 안 그런가?”

“그럴 겁니다. 아니, 반드시 그렇게 만들겠습니다. 제 손으로 직접.”

제갈풍의 힘 있는 대답에 흐릿하게 웃은 매종학이 입을 열었다.

“자네의 손은 귀하니 다른 곳에 쓰게. 이처럼 거친 일에는 나와 같은 검수(劍手)가 나서야 적격이니.”

“……!”

일순간, 매종학의 말에 담긴 의미를 읽어 낸 제갈풍의 눈가가 파르르 떨렸다.

바야흐로 일 년.

짧다면 짧고, 길다면 길었던.

그러나 그 어느 때보다 치열하게 매달려 왔던 일의 결과가 마침내 눈앞으로 다가왔다는 사실이 피부로 전해졌다.

이미 모든 과정과 흐름을 알고 있던 그조차 격동할 만큼.

“맹주, 그 말씀은.”

“언제까지 당하고 있을 수만은 없네. 많은 이들이 참으로 오랫동안 인내하며 기다렸어.”

“그렇다면 드디어?”

매종학이 조용히 고개를 끄덕였다.

“두 번 다시 없을 기회를 놓칠 수는 없지.”

“……!”

“참으로 고생 많았네. 제갈 가주. 자네의 노고가 아니었다면 오늘날의 기회도 없었을 테지.”

가까스로 격동을 가라앉힌 제갈풍이 크게 심호흡한 뒤 대답했다.

“아닙니다. 모두의 크고 작은 희생 덕분입니다.”

그는 아직도 떨림이 완전히 사라지지 않은 자신의 손을 바라보았다.

거칠고 투박했다.

마치 일평생을 수련에 매진해 온 무인의 그것처럼.

그간 일가의 가주로서 갖추어야 할 최소한의 무공만을 익혀왔을 뿐, 굳은살도 서서히 사라져 가던 섬섬옥수는 더는 찾아볼 수 없었다.

암천이라는 암운(暗雲)이 천하에 드리워진 이후부터, 그는 오늘만을 기다려 왔다.

길었던 외유(外遊)의 이유를 증명할 때를.

“남을 자와 떠날 자는 가려졌나?”

“예.”

“자네에게 주어진 임무는 알고 있겠지.”

“그럴 리가 있겠습니까. 줄곧 이 순간만을 기다려 왔습니다.”

“준비는 끝났네. 온 천하의 모두가.”

힘주어 뒷말을 덧붙인 매종학이 품에서 돌돌 말린 종이를 꺼내어 내밀었다.

“이건…….”

“하남을 떠나기 전, 송 각주(閣主)에게 받은 것일세.”

매종학의 부재는 현재 극비에 부쳐진 상태.

은영각의 각주인 천면호리 송호가 썼다는 말에 제갈풍의 눈빛이 깊게 가라앉았다.

“무슨 내용입니까?”

“아직까지도 남아 있는 내부의 세작들. 그리고 자네와 함께할 이들의 명단과 합류할 위치가 적힌 약도지.”

직접 서신을 펼쳐 확인한 제갈풍의 눈에 희열이 떠올랐다.

“역시…….”

“은영각을 중심으로 개방과 하오문을 총동원한 결과일세. 송 각주가 직접 선별한 인원들로 이루어진 일이니, 비밀이 새어 나갈 염려는 없을 걸세.”

“그렇겠지요. 조금의 오차도 없이 행하겠습니다.”

“그간 모두가 열심히 경작해 온 밭이니, 새나 벌레에 쪼아 먹혀선 안 되네.”

“걱정하지 마십시오. 비록 여기까지 오는 과정은 괴롭고 힘겨웠으나, 추수(秋收)는 한 치의 실수 없이 단숨에 끝내겠습니다.”

“믿겠네.”

제갈풍에게서 다시 서신을 넘겨받은 매종학이 손아귀에 공력을 불어넣었다.

화르륵.

삼매진화(三昧眞火)의 불길에 휩싸임과 동시에 흩날리는 잿가루.

혹시 모를 상황을 대비하여 서신까지 불태운 매종학의 모습에, 제갈풍은 지극히 공손한 태도로 양손을 모았다.

자신의 눈앞에 있는 저 천하제일의 검객이 이제는 떠나야 할 때를 맞이했음을, 그는 이미 알고 있었다.

“살펴 가십시오, 맹주(盟主).”

제갈풍은 진심 어린 존경을 담아 허리를 굽혔다.

그리고 그런 그가 다시 고개를 들었을 때, 그곳에 남아 있는 것은 서늘한 바람에 몸을 떠는 수백여 그루의 뽕나무뿐이었다.

“성격도 급하시군. 인사도 없이 그냥 가시다니.”

피식 실소를 흘린 제갈풍은 손을 뻗어 힘없이 늘어져 있는 뽕나무 가지를 매만졌다.

옛 선조인 제갈무후(諸葛武侯)가 손수 심었다고 알려진 이 뽕나무들은 제갈세가의 상징 중 하나였지만, 민초들이 떠들어 대는 그 이야기는 사실 단순한 구설에 불과했다.

‘무후께서는 한의 소열제(昭烈帝)를 따라 파촉 땅에 자리 잡았거늘, 그분께서 손수 심으셨던 뽕나무가 수천 리 밖의 호북에 있을 리 없지.’

이 뽕나무들은 현재의 제갈세가의 반석을 다진 그의 후손들이 심은 것이다.

제갈씨의 명맥을 계속해서 이어 나가고자, 동시에 위대한 선조를 기억하고자.

제갈무후의 죽음 이후, 끝끝내 멸망하고야 말았던 촉한에 남아 있었을 수백여 그루의 뽕나무들이 어떻게 되었는지는 모른다.

그러나, 그 뿌리는 새로운 땅에서 이어져 나가고 있다.

단 하나의 씨앗이라도 남아 있다면, 명맥은 끊어지지 않는다.

“중요한 것은 사람이지, 땅이 아닌 법.”

나직하게 뇌까린 제갈풍은 나뭇가지에 맺힌 서리를 툭툭 털어냈다.

“다시 돌아올 때는, 열매가 맺혀 있길 바라마.”

희미한 미소를 마지막으로, 제갈풍은 망설임 없이 돌아섰다.

그리고 약 촌각 후.

자신들의 가주가 측간에서 암살당했을지도 모른다는 걱정으로 내당을 들쑤시고 있던 이들에게, 대뜸 한마디를 내뱉었다.

“자, 지금부터 짐들 싸게.”

“예? 또 뭘 싸요?”

“아니, 아직도 다 못 쌌던 겁니까?”

생각지도 못한 말을 이해하지 못하고 어리둥절하던 이들에게, 다시 한번 청천벽력 같은 말이 떨어졌다.

“짐 싸라고! 제갈세가는 즉각 이곳을 뜬다!”

그 순간, 몇몇 사람은 생각했다.

저 염병할 가주가, 차라리 측간에서 암살당하는 것이 조금 더 나았을지도 모르겠다고.

하지만 이 엄청난 폭탄을 던져놓은 제갈풍의 입가에는, 이해할 수 없는 웃음마저 맺혀 있었다.

‘부디 무운을 빕니다. 맹주. 그리고…….’

조금만, 부디 조금만 더 버텨 주게.

열화신룡 진태경.

그 간절한 바람을 마음속으로 뇌까린 제갈풍의 시선은, 서쪽 저 너머를 향해 있었다.
```

## Final English reading copy

```markdown
# Chapter 1086

To put it kindly, he had an open, easygoing face. Put it less kindly, and he was the sort of young man you might forget in a moment, even after being introduced.

He was neither tall nor short, and had the kind of natural air that let him blend in wherever he went.

Perhaps that was why no one had thought of the title Sword Saint when they saw the young man beside Zhuge Feng, who had returned to his family after a lengthy absence.

“Oh, there you are.”

Mae Jonghak finally turned around and smiled at Zhuge Feng.

His eyes were deep yet clear, and his smile seemed to put anyone who saw it at ease.

While the world was gripped by turmoil and anxiety, the Murim Alliance Leader—who ought to have borne a heavier burden than anyone else—continued in an almost childlike tone.

“I was wandering here and there and got bored. At some point, I found myself just walking wherever my feet took me, and here I am.”

“You came here without knowing where you were?”

“I did.”

“This garden and everything within roughly a hundred *jang* of it are part of the Family Head’s Hall. Even our family’s direct descendants need my permission to enter.”

“Is that so? I did think something was a little odd. Aside from the people hiding here and there, there were all sorts of mechanisms and formations set up.”

Hearing Mae Jonghak’s answer, Zhuge Feng could only let out a hollow laugh.

“Is something good happening?”

“Not at all. I just found it funny.”

The Zhuge Clan was a place even the greatest thieves in the world wouldn’t dare try to break into.

The Heaven-Stealing Thief, who supposedly could steal even from heaven, had once barged into the Zhuge Clan’s Family Head’s Hall—and wound up trapped in its mechanisms and formations, wandering for over a month.

At the time, he was the greatest thief in the world. In the end, he was rescued by the Zhuge Clan’s martial artists on the merciful order of the previous Family Head. Released in a state of skin and bones, he left these words behind:

> “Break into the imperial palace, and you’ll be tortured to death. Break into the Sichuan Tang Clan, and you’ll be poisoned to death. But break into the Zhuge Clan, and they’ll rob you down to your soul and let you starve to death.”

And so the Three Forbidden Places were born, leaving a painful lesson for the thieves who came after him.

Of course, it had now been proven that even the Zhuge Clan’s Family Head’s Hall—where the greatest thief of the age had nearly starved to death—was powerless before the greatest swordsman in the world.

“My apologies. If I’d known this was the Family Head’s Hall, I would’ve asked permission.”

“I was in a meeting at the time.”

“Does the door stay shut if the homeowner isn’t there? I could’ve asked the people hiding around here to let me in.”

“Even if you had asked, would they really have opened it and said, ‘Goodness, where have you been all this time?’”

“True enough. It’s not as if I could tell them I’m the Alliance Leader.”

As Mae Jonghak scratched the back of his head, Zhuge Feng shook his own.

People did call him a bit of an eccentric, but compared to the man before him, he couldn’t hold a candle to him.

“So, what were you doing here?”

“Smelling the fragrance.”

“The fragrance?”

Zhuge Feng cocked his head.

Though he had been the Family Head for many years, he had visited this garden only a handful of times.

Part of the reason was that he spent most of his time studying and researching mechanisms and formations. But the place was also far too rugged to call a flower garden.

“As you can see, this garden is full of nothing but mulberry trees. There isn’t much to see, and they don’t smell especially nice.”

“That’s not so. Everything in the world has its own fragrance. These mulberry trees are no different.”

Mae Jonghak added quietly,

“And neither are the plum blossoms, blooming somewhere I can’t reach right now.”

At the faintness in his voice, Zhuge Feng fell silent for a moment, then asked carefully,

“Do you… want to return to Huashan?”

“I always have. But not in a time like this. It’s clear where I need to be.”

“Then…”

“I just miss those peaceful days. That day I lay beneath the sunlight in a forest full of plum blossoms.”

Mae Jonghak reached out and stroked a nearby mulberry tree.

Perhaps because of the unseasonably cold weather, its branches hung bare, without a single fruit. It looked much like the world did now.

“One day, this mulberry tree will bear fruit too. Don’t you think?”

“It will. No—I’ll make sure it does. With my own hands.”

Mae Jonghak gave a faint smile at Zhuge Feng’s firm reply.

“Your hands are precious. Use them elsewhere. For rough work like this, a swordsman like me is the right one to step forward.”

“...!”

Zhuge Feng’s eyes trembled as he understood what Mae Jonghak meant.

A year.

Short, if you called it short. Long, if you called it long.

But the result of the work they had pursued more fiercely than ever before was finally within reach. He could feel it down to his skin.

Even he, who already knew every step and turn of the plan, was shaken.

“Alliance Leader, do you mean…”

“We can’t keep taking hits forever. So many people have endured and waited for so long.”

“Then, at last?”

Mae Jonghak nodded quietly.

“We can’t afford to let this chance pass us by. We may never get another.”

“...!”

“You’ve worked hard, Family Head Zhuge. Without your efforts, we wouldn’t have this opportunity today.”

Zhuge Feng finally managed to calm his excitement. After taking a deep breath, he replied,

“No. It’s thanks to everyone’s sacrifices, great and small.”

He looked down at his hand, still trembling.

It was rough and calloused.

Like the hand of a martial artist who had spent their whole life training.

His slender, elegant hand was gone—the one that had learned only the minimum martial arts required of a Family Head, and whose calluses had slowly faded away.

Ever since the dark cloud of Dark Heaven had spread across the world, he had waited for this day.

The day he could prove why he had spent so long away from home.

“Have you decided who will stay and who will leave?”

“Yes.”

“You know what your mission is.”

“As if I could forget. I’ve been waiting for this moment all along.”

“Everyone under heaven is ready.”

Mae Jonghak emphasized the final words, then pulled a rolled-up sheet of paper from his robes and held it out.

“This is…”

“Chief Song gave it to me before I left Henan.”

Mae Jonghak’s absence was currently being kept an absolute secret. At the mention of Song Ho, Chief of the Hidden Shadow Pavilion, Zhuge Feng’s gaze grew intent.

“What does it say?”

“The names of the enemy spies still embedded in our ranks, along with the people who’ll join you and a map showing where they’ll meet.”

As Zhuge Feng opened the letter and read it for himself, delight flashed in his eyes.

“Just as I thought…”

“We put the Beggars’ Sect and Lower District Sect to work alongside the Hidden Shadow Pavilion. Chief Song personally selected everyone involved, so there’s no risk of the secret getting out.”

“I thought as much. I’ll carry it out without the slightest mistake.”

“Everyone’s worked hard to cultivate this field. We can’t let birds or insects peck it apart.”

“Don’t worry. Getting here was painful and hard, but I’ll finish the harvest in one swift stroke without a single mistake.”

“I trust you.”

Mae Jonghak took the letter back from Zhuge Feng and filled his hand with internal energy.

Whoosh.

The paper was swallowed by the flames of Samadhi True Fire, scattering into ash.

Having burned the letter as a precaution, Mae Jonghak watched as Zhuge Feng clasped both hands and bowed with utmost respect.

Zhuge Feng already knew the time had come for the greatest swordsman in the world to leave.

“Travel safely, Alliance Leader.”

He bowed, his respect sincere.

And when he raised his head again, all that remained were hundreds of mulberry trees trembling in the cold wind.

“What a hurry. He didn’t even say goodbye before leaving.”

Zhuge Feng let out a quiet snort and reached out to touch a drooping mulberry branch.

These trees were said to have been planted by the Zhuge Clan’s ancient ancestor, Zhuge Wuhou, and were one of the clan’s symbols. But the story the common folk liked to repeat was nothing more than a rumor.

*Wuhou followed Emperor Zhaolie of Han to settle in Bashu. There’s no way the mulberry trees he planted himself could be thousands of li away, in Hubei.*

These mulberry trees had been planted by Zhuge Wuhou’s descendants, who laid the foundation for the Zhuge Clan as it stood today.

They had planted them to carry on the Zhuge family line—and to remember their great ancestor.

No one knew what had become of the hundreds of mulberry trees left behind in Shu Han, which had ultimately fallen after Zhuge Wuhou’s death.

But their roots had taken hold in a new land.

As long as a single seed remained, the line would not end.

“What matters is the people, not the land.”

Murmuring softly, Zhuge Feng brushed the frost from the branches.

“When I come back, I hope you’ll be bearing fruit.”

With one last faint smile, Zhuge Feng turned and walked away without hesitation.

A few moments later, he addressed the people who were tearing through the Inner Hall, worried their Family Head might have been assassinated in the privy.

“All right, start packing.”

“What? Packing what now?”

“Wait, you haven’t finished packing yet?”

The bewildered group couldn’t make sense of his unexpected words. Then he struck them with another thunderbolt.

“I said pack! The Zhuge Clan is leaving this place immediately!”

At that moment, a few of them thought that damn Family Head might have been better off getting assassinated in the privy.

Yet a smile they couldn’t understand tugged at Zhuge Feng’s lips as he dropped that bombshell.

*May fortune be with you, Alliance Leader. And…*

*Just a little longer. Please, hold on just a little longer.*

Zhuge Feng repeated his desperate wish in his heart.

Blazing Flame Divine Dragon Jin Taekyung.

His gaze was fixed far to the west.
```
