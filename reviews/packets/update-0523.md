<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0523.txt",
      "sha256": "415c4b416d66281891edce7fb376e45de5d91487867d59b5346a4fb69f9030c9",
      "bytes": 13006
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8c0c1f6a8ce81365b589fa6613fbf105726fe0fb2db9fe1219a15794f7fed881",
      "bytes": 4080
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "64cd8fb4c8747cb48df6679f201570de17fee035b6ae67fc3809e0150ce53748",
      "bytes": 166781
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "42f6821144ffb49fc3c4540c621d27741b53a2264582b155b263b105e4900320",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "f1541f2009361e697a98fe8aafe6bee12735dd8c149aa46355a143da18334db3",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "03f0074ad6074dc47aea39023c9707b8aadde646927358e164902628fe34ad7f",
      "bytes": 1630
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4bd81ddea8b1aa4a1c637e5b7e6f47b6f1ee98065eaf89c0e1fde38c2fa03226",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8083ca96c95ee9ce8810572e9f49d625961f04002d862c512c9a55ebd1e146a4",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "b23e69387ba8b9e01363c33e9f52e2c45b37f6e5789a843198d8f37ac0ab81ed",
      "bytes": 985
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5055fd089787aa6ed7851e0569df53546ad0b97272966a57ddd5f2bcd686b8b4",
      "bytes": 158189
    }
  ],
  "estimated_tokens": 11873
}
-->

# Durable State Update — Chapter 523

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 523. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 523. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 523,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 523,
    "continuity_sources": [523],
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
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he entered a new realm, achieved Returned to Youth, and began his long-promised duel with Nangong Cheon, the Azure Sky Sword King.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; he is training Taekyung to control the violent internal energy produced by the Fire Gate Divine Technique.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but its permanence and repeatability remain unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "Mae Jonghak remains the New Murim Alliance's administrator after Jeok Cheongang refused the Alliance Leader position because it was troublesome; Mae accepts the burden because someone must do it.",
    "Song Ho is the reinstated Chief of the Hidden Shadow Pavilion and commands a vetted intelligence network, including five concealed agents whom Taekyung detected inside the Alliance.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, and leveled up.",
    "Wudang's second report identifies the Killing Ghost as Jang Sam, a fisherman who disappeared near Mount Wudang; Taekyung suspects the Blood Fish caused or participated in his transformation.",
    "Taekyung assesses that no second Gate has erupted yet, that Dark Heaven cannot open Gates easily, and that the Murim Alliance and Hidden Shadow Pavilion are mobilizing against future outbreaks."
  ],
  "continuity_sources": [
    522,
    521
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "How will the New Murim Alliance proceed with Mae Jonghak still administering it, and will Jeok Cheongang accept the Alliance Leader position?",
    "Did the Blood Fish cause Jang Sam's transformation, and could similar Blood Fish or Gate-related transformations occur elsewhere?"
  ],
  "safe_through": 522,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 화약고 as powder keg; preserve the chapter's blunt profanity and monster-comparison humor."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 살성     | **Slaughter Saint**           | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 영약     | **elixir**                                       |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 주화입마   | **qi deviation**                                 |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 사형     | **Senior Brother**                           |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 매력               | **Charm**                      |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 오기조원 | **Five Qi Returning to Origin** | High martial realm displayed by Jeok Cheongang. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 삼화취정 | **Three Flowers Gather at the Crown** | Near-completed phenomenon associated with entering the Supreme Peak realm. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 기해혈 | **qi-sea acupoint** | Acupoint at the dantian whose destruction releases stored internal energy. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 기경팔맥 | **Eight Extraordinary Meridians** | The eight extraordinary meridians of wuxia physiology. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 화기 | **fire qi** | The fire nature imparted to internal energy by the Fire Gate Divine Technique. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 522
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 517
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 522
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, and Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 517
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 517
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 521
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung after testing his basics, and Mu Song plus five Water Dragon Stronghold subordinates now know he is an exceptionally powerful master but not that he is the Slaughter Saint.

## Korean source

```text
＃523화



스으으으.

뜨겁다. 단전으로부터 솟구친 열양지기가 사지백해로 뻗어 나가며 혈도를 내달린다. 모든 것이 고요하고 생생하게 느껴진다.

나는 기경팔맥(奇經八脈)을 따라 공력을 운용했다.

한 번, 두 번, 세 번…….

운기조식은 높은 언덕에서 눈덩이를 굴리는 것과 같다. 반복할 때마다 눈덩이는 커진다.

반면 흙이나 돌, 나뭇가지 등의 이물질이 섞여들 수도 있다.

이는 곧 공력의 정순함을 흐리는 탁기(濁氣)이며, 운기조식을 반복함으로써 그 탁기를 태우고 정순한 공력이 완성된다.

‘더, 더, 더.’

나는 마음속으로 홀린 듯 중얼거리며 운기를 지속해 나갔다.

자그마치 삼 갑자에 달하는 공력이 화룡의 모습으로 화하여 거침없이 몸 안을 헤엄쳤다.

내가 그려 낸 심상(心想) 속에서, 화룡의 덩치는 더욱 거대해지고 열기는 뜨겁게 타올랐다.

그리고 어느 순간 깨달았다.

‘지금.’

화륵.

내 의지에 따라 열양지기가 사방으로 솟구쳤다. 실로 압도적인 열기. 몸 안에서 작은 태양이 터져 나간 것만 같았다.

감고 있던 눈이 뜨거워지고 코에서는 숨 대신 화염이 흘러나오는 것만 같다.

아니, 그런 것 같은 것이 아니라 필시 그럴 것이다.

물이 많으면 넘치는 것처럼, 지금 내 몸 안을 가득 채운 공력은 바깥을 향해 흘러나오고 있었다.

눈, 코, 입 등. 이른바 칠공(七孔)이라 부르는 일곱 개의 구멍으로부터 흘러나온 열기가 외부를 뜨겁게 달구었다.

전신 곳곳의 수많은 모공(毛孔)에서도 같은 상황이 벌어지고 있었다.

스아아아아.

느껴졌다. 정수리 위로 모여드는 막대한 기의 흐름이. 동시에 나는 머릿속에 펼쳐진 깨끗한 도화지에 그림을 그려나갔다.

나는 나의 주인이다. 몸 안에 존재하는 혈도 하나, 밖으로 흘러나온 한 올의 기운도 마찬가지다. 전부 내 것이니 주인의 뜻을 거스를 수 없다.

비록 눈으로 볼 수는 없으나 느낄 수 있었다. 머리 위로 몰려든 열양지기가 주인이 원하는 형태를 취하는 것을.

하나, 둘, 셋.

마치 타오르는 것처럼 붉게 물든 세 개의 꽃잎.

‘삼화취정(三花聚顶).’

초절정이라는 경지에 깨달음이 더해져 낳은 결과다.

이것만으로도 천하의 무림인 중 누구나 꿈꾸는 경지지만, 이제 겨우 언덕 하나를 넘은 것에 불과하다.

후우.

입술 사이로 짧게 내뱉은 숨결에는 운기조식을 통해 걸러 낸 탁기의 잔재가 스며들어 있다.

마지막 한 줌의 탁기마저 배출해 냄으로써 공력과 머릿속을 깨끗이 비워 낸 나는, 다음 언덕을 향해 걸음을 내디뎠다.

‘오기조원(五氣朝元).’

중단전을 연 후에도 몇 번 시도해 봤지만 끝내 이룰 수 없었던 경지. 내 앞을 가로막은 또 다른 벽.

‘넘는다. 바로 지금.’

굳은 결심과 함께 가슴 한구석이 찌르르 울린다.

지금 잡고 있는 이 긴장의 끈을 놓아서는 안 된다. 괜히 앞뒤 가리지 않고 벽을 맨주먹으로 후려쳐 봤자 주먹만 상하는 법이니까.

최소한 벽에 실금이라도 가게 하려면 긴장 속에서 정확한 흐름을 읽어야 한다.

‘조금이라도 방심했다가는 공력이 역류할 가능성이 있어.’

이미 나 있는 길을 걷는 것은 쉽다.

그러나 이건 나만의 새로운 길을 개척하는 과정이다. 바위를 치우고, 풀숲을 쳐내야 한다. 절벽을 올라가다가 삐끗하는 경우 역시 있었다.

공력의 역류는 내상으로 이어지고, 내상을 입은 상태에서 계속 무작정 들이댔다가는 주화입마(走火入魔)에 빠지기 딱 좋았다.

적천강에게 들은 바에 의하면, 그런 식으로 죽거나 반병신이 된 무림인이 한둘이 아니라고 했다.

나 역시 암천이 무림에 거대한 똥을 싸대고 있는 지금 휠체어 신세를 질 생각은 없었다.

‘천천히. 신중하게.’

다행히 문경과의 수련은 큰 도움이 되었다.

열화문의 근간이 되는 내공 심법, 열화신공(熱火神功)으로 쌓은 열양지기는 다른 명문 대파의 심법 이상으로 강한 힘과 폭발력을 갖추었지만, 그만큼 움직임이 거친 것이 사실이다.

그러나 이번 수련을 통해 불완전함을 조금이나마 메울 수 있었다.

‘할 수 있다. 정신만 똑바로 차리면 충분히 가능해.’

따끈하다. 정수리 위로 삼화취정이 흔들린다. 하지만 걱정하지 마라. 공력은 손보다 빠르니까.

‘우선 첫 번째 고리.’

내가 신중하게 공력을 움직이기 시작한 바로 그때였다.

“공력을 갈무리해라. 어차피 지금 당장은 헛수고다.”

“……!”

파사삭!

갑작스럽게 들려온 누군가의 목소리에 집중력이 깨지자, 오기조원의 형태를 갖춰 가던 공력이 산산이 흩어진다.

동시에 찾아온 공력의 역류. 나는 몸속 깊은 곳에서 울컥 솟구치는 위액을 토해 냈다.

“오기이이잇!”

촤악.

소량의 피가 섞인 토사물이 바닥으로 쏟아졌다.

시벌, 사진으로 봤던 나이아가라 폭포가 여기 있었네.

순간 치밀어 오른 것을 쏟아 내고 숨을 헐떡이는데, 바닥에 오늘 아침에 먹은 반찬들이 나를 향해 손을 흔들고 있다.

“우웩, 웨에에엑!”

아, 이건 못 참지.

몇 번이고 반복해서 한바탕 쏟아낸 후에야 정신이 든 나는, 어느새 멀찌감치 떨어져 있는 가죽신의 주인을 노려보았다.

“뭐 하는 겁니까, 지금?”

신고 있던 가죽신을 신중히 살핀 문경이 대답했다.

“산 지 사흘 밖에 안 된 신발이다. 더러워지면 곤란하지.”

“그거 말고요. 왜 운기조식 중에 말 거십니까?”

“흔든 것도 아닌데 뭐가 문제냐? 그 정도 경지에 올랐는데도 고작 말 몇 마디로 평정심(平定心)이 깨지는 네놈이 부족한 거다.”

“깜짝 놀랐잖습니까!”

“나도 깜짝 놀랐다. 도대체 어제 오늘 뭘 처먹었길래 저렇게 많이…….”

문경이 눈살을 찌푸리며 바닥에 질펀한 토사물을 바라보았다.

“보면 볼수록 더럽군. 모양만 보면 얼추 오기조원의 형상 같긴 해.”

“어이, 문 씨!”

“뭔 씨?”

나는 문경의 서늘한 시선을 피하지 않고 마주 노려보았다.

일 초, 이 초, 삼 초.

음. 이 정도면 충분한 것 같아.

“말이 헛나왔네요. 제가 내상을 크게 입은 모양입니다.”

“……네놈을 보고 있자니 기해혈이 다 욱신거린다.”

짜게 식은 문경의 눈빛을 피한 나는 황급히 화제를 돌렸다.

“그런데 갑자기 무슨 일로, 아니. 그전에 여긴 어떻게 들어오셨습니까?”

“문이 왜 있다고 생각하는 거냐?”

“하지만 문은 무진이가 지키고 있을…….”

말꼬리를 흐린 바로 그 순간.

스르륵, 쿵!

반쯤 열려 있는 문틈 사이로 한 사람의 신형이 픽 하고 쓰러졌다.

못 알아볼 수가 없을 만큼 낯익은 뒤통수에 저절로 눈이 부릅떠졌다.

“무진아! 혁무진!”

비명을 지르는 내게, 문경이 스산한 목소리로 입을 열었다.

“놔두어라. 어차피 흔들어도 일어나지 못할 테니.”

흔들어도 일어나지 못한다고?

이 피에 미친 살귀가 드디어 일을 냈구나.

나는 분노를 담아 버럭 외쳤다.

“이 피도 눈물도 없는 살인마! 살성 같은 새끼!”

“문을 막고 자고 있길래 깨우려고 했더니 꿈쩍도 안 하던…… 지금 뭐라고 했지?”

“예?”

“뭐라고 했냐 물었다.”

“어?”

뭐여, 시벌.

때맞춰 혁무진의 시신, 아니 몸이 들썩였다. 힘찬 코골이 소리와 함께.

드르렁.

“…….”

“…….”

말없이 허공에서 부딪치는 시선. 나는 매력적인 미소와 함께 입을 열었다.

“아주 약간, 사소한 오해가 있었던 것 같습니다.”

문경이 메마른 표정으로 대꾸했다.

“오해가 아니었던 것 같은데. 사소하지도 않고.”

“좋은 게 좋은 거 아니겠습니까.”

“죽은 게 죽은 거라고?”

“오…… 그게 어떻게 그렇게 되나요?”

“안 될 것도 없지. 불만 있느냐?”

불만도 있고, 달팽이관에도 큰 문제가 있는 것 같았지만 내겐 그걸 지적할 만한 용기가 없었다.

“잘못했습니다.”

“사과하면 모두 끝나나?”

“진심이 담긴 대화는 모든 응어리를 풀 수 있다고 믿습니다.”

“잘됐군. 그럼 암천의 천주에게 가서 대화로 풀어 봐라. 주둥이 찢어 버리기 전에 그 재수 없는 웃음 싹 지우고.”

“선조들께서 그러셨지요. 웃는 얼굴에 침 못 뱉는다고.”

“퉤.”

철퍽.

음. 선조들의 말이 틀렸군.

하지만 이럴 때일수록 평정심을 되찾아야 한다. 나는 뺨에 묻은 침을 침착하게 닦아 냈다.

“발사 속도가 굉장히 빠르시군요. 암기인 줄 알았습니다.”

“공력을 실어 뱉으면 사람 눈알 정도는 터트릴 수 있지.”

“대단하시네요. 혹시 종족이 저그십니까?”

“저승사자다.”

“……다시 한번 말씀드리지만, 거듭 죄송합니다.”

이 자식을 몇 토막을 내야 잘 죽였다고 소문이 날까, 하는 눈빛으로 나를 바라보던 문경이 작게 혀를 찼다.

“됐다. 네놈과 이야기를 나눌 때마다 기가 빨리는군.”

“…….”

누가 할 말을. 이쪽은 시시각각 생명력이 빨리는 중이다.

방금 그 대화로 수명이 사흘 정도는 줄어들었다는 것에 혁무진의 좌심방을 걸겠다.

‘혁무진 저 새끼는 호법을 서라니까 그새를 못 참고 또 처자고 있네.’

문경도 문경이지만 저놈도 대단한 건 매한가지다.

“그런데 여긴 어쩐 일로……?”

“또 무슨 개 같은 짓거리를 하려고 찾아왔냐는 뜻으로 들리는군.”

“오.”

“오?”

“오……니요. 그게 오니라 그냥 궁금해서 여쭤본 겁니다.”

“못 본 사이 발음이 상당히 이상해졌다고 생각이 드는 건, 기분 탓이겠지.”

“그럼요. 기분 탓입니다.”

작게 한숨을 내쉰 문경이 손에 든 보퉁이를 던졌다.

툭, 반사적으로 받아 낸 내가 눈을 동그랗게 떴다.

“이게 뭡니까?”

“단환(丹丸)이다.”

“단환이요?”

봄철 산타클로스인가. 갑자기 웬 선물이래.

반신반의하며 보퉁이를 풀어헤치자 작고 단단해 보이는 목갑(木匣)이 하나 나왔다.

동시에 콧속 깊숙이 스며드는 기묘한 향기.

‘이건…….’

단환과 같은 영약은 직접 보기도 전에 그 효과를 안다고 했는데, 지금이 딱 그 경우다.

나는 목갑을 열기도 전에 이 안에 든 것이 상당한 효력을 지닌 단환이라는 걸 깨달았다.

달칵.

목갑을 열자 붉은빛을 띤 단환 하나가 모습을 드러냈다. 척 보기에도 범상치 않은 첫인상.

멍하니 단환을 응시하던 나는 고개를 들어 문경을 바라보았다.

“뭘 그리 보는 것이냐.”

“갑자기 이런 걸 왜 주시나 해서요.”

“적지 않은 화기(火氣)를 품고 있으니, 네놈에게 도움이 될 것이다.”

“예?”

“귀에 암기라도 박혔나. 두 번 말 하게 만들지 마라.”

“아니, 효력을 여쭤본 게 아닌데…….”

문경이 와락 얼굴을 구겼다. 평소 대부분을 늘 삭막한 표정을 짓고 있는 문경이라고는 믿기지 않을 만큼 풍부한 감정표현이다.

“오다 주웠다.”

“……?”

“정정하지. 지나가는 길에 보이길래 샀다. 되었느냐?”

되긴 뭐가 돼, 이 양반아.

나는 목갑 안에 들어 있는 붉은 단환을 건드렸다.

‘아이템 확인.’

띠링.



[문경이 특별 제작 한 진태경 맞춤 단환]

더 자세한 정보를 확인하시겠습니까?

Y  /  N



응. 아냐. 됐어. 이걸로 충분해.

간이 시스템창을 닫은 나는 뜨뜻미지근한 시선으로 문경을 응시했다.

“보이길래 샀다. 예, 그렇군요.”

“……뭐냐, 그 눈빛은.”

“아무것도 아닙니다. 아무튼 감사히 받을게요.”

지금 문경에게 드는 감정은 정확히 고마움 반, 두려움 반이다.

‘좋은 단환을 준 건 땡큐긴 한데, 도대체 다음 수련이 뭐길래…….’

갑자기 이러면 사형수한테 밥 잘 먹이는 것 같잖아.

내 떨리는 시선에 담긴 뜻을 알아차린 듯, 문경이 입을 열었다.
```

## Final English reading copy

```markdown
# Chapter 523

Ssssss.

It was hot. The Scorching Yang Qi surging from my dantian spread through my limbs and bones, racing along my acupoints. Everything felt quiet and vivid.

I circulated my internal energy along the Eight Extraordinary Meridians.

Once, twice, three times…

Circulating qi was like rolling a snowball down a high hill. With every repetition, the snowball grew larger.

But it could also pick up foreign matter along the way—dirt, stones, twigs, and the like.

That was turbid qi, which muddied the purity of one’s internal energy. Repeating the circulation burned away that turbid qi and refined the internal energy.

*More. More. More.*

I muttered the words in a daze as I continued circulating my energy.

Internal energy amounting to no less than three jiazi transformed into the shape of a fire dragon and swam fiercely through my body.

Within the mental image I had created, the fire dragon grew larger, its heat blazing hotter and hotter.

Then, at some point, I realized it.

*Now.*

Fwoosh.

At my command, the Scorching Yang Qi surged in every direction. It was truly overwhelming heat. It felt as if a small sun had exploded inside my body.

My closed eyes grew hot, and it felt as though flames were flowing from my nose instead of breath.

No. It wasn’t merely a feeling. That was certainly what was happening.

Just as too much water overflowed, the internal energy filling my body was flowing outward.

The heat flowing from the seven openings known as the seven apertures—my eyes, nose, mouth, and so on—scorched the air around me.

The same thing was happening in the countless pores covering my entire body.

Ssssss.

I could feel it—the enormous flow of qi gathering above my crown. At the same time, I began drawing a picture on the clean, blank canvas spread across my mind.

I was the master of myself. Every acupoint inside my body and every strand of energy that had flowed outside belonged to me as well. None of it could defy its master’s will.

I could not see it, but I could feel the Scorching Yang Qi gathered above my head taking the shape I wanted.

One, two, three.

Three petals, colored red as if they were burning.

*Three Flowers Gather at the Crown.*

It was the result of adding enlightenment to the Supreme Peak realm.

Any martial artist in the world would dream of reaching this realm, but I had merely crossed one hill.

Hoo.

The short breath escaping my lips carried the remnants of turbid qi filtered out through circulating my internal energy.

After expelling even the last handful of turbid qi and clearing my internal energy and mind, I took a step toward the next hill.

*Five Qi Returning to Origin.*

Even after opening my Middle Dantian, I had tried to reach this realm several times, but I had never succeeded. It was another wall blocking my path.

*I’ll cross it. Right now.*

Along with my firm resolve, a corner of my chest gave a sharp, tingling thrum.

I could not let go of the thread of tension I was holding. Even if I recklessly punched the wall without considering the consequences, all I would accomplish was injuring my fist.

To put even a hairline crack in the wall, I had to read the exact flow of energy while maintaining that tension.

*If I let my guard down even slightly, my internal energy could reverse its flow.*

Walking along an existing road was easy.

But this was the process of carving out a new path of my own. I had to move boulders and hack through the undergrowth. I could also slip while climbing a cliff.

A reversal of internal energy led to an Internal Injury, and if I continued recklessly forcing my way forward while injured, I would be practically asking for qi deviation.

According to Jeok Cheongang, more than a few martial artists had died or been left half-crippled that way.

I had no intention of ending up in a wheelchair while Dark Heaven was taking a gigantic dump all over the Murim.

*Slowly. Carefully.*

Fortunately, my training with Mungyeong had helped immensely.

The Scorching Yang Qi built through the Fire Gate Divine Technique, the cultivation technique at the foundation of the Fire Gate Clan, possessed power and explosiveness at least on par with the cultivation techniques of other prestigious sects.

But its movements were just as rough.

Through this training, I had managed to make up for some of that imperfection.

*I can do this. As long as I keep my head straight, it’s entirely possible.*

It was warm. The Three Flowers Gather at the Crown trembled above my head.

*But don’t worry. Internal energy is faster than hands.*

*First ring.*

That was when I began moving my internal energy carefully.

“Rein in your internal energy. It’s a waste of effort for now anyway.”

“……!”

Crack!

My concentration shattered at the sudden voice, and the internal energy that had been taking shape as Five Qi Returning to Origin scattered to pieces.

At the same time, my internal energy reversed its flow. Gastric juices surged up from deep inside my body, and I vomited.

“Oooooogh!”

Splash!

Vomited matter mixed with a small amount of blood spilled onto the floor.

*Fuck. So this is where the Niagara Falls I saw in pictures were hiding.*

After spewing out everything that had surged up and panting for breath, I saw the side dishes I had eaten that morning waving at me from the floor.

“Uweeegh! Bleeegh!”

Ah, I couldn’t hold that back.

Only after emptying my stomach several more times did my mind finally clear. I glared at the owner of the leather shoes who had already moved a considerable distance away.

“What are you doing right now?”

Mungyeong, who was carefully examining the leather shoes he was wearing, answered,

“I bought these shoes only three days ago. It would be troublesome if they got dirty.”

“That’s not what I meant. Why did you speak to me while I was circulating my qi?”

“I didn’t even touch you, so what’s the problem? You’ve reached that realm, yet your composure is shattered by a few words. That is your deficiency.”

“You startled me!”

“I was startled too. What the hell did you eat yesterday and today to produce that much…?”

Mungyeong frowned as he looked at the mess of vomit covering the floor.

“The more I look at it, the filthier it becomes. Judging by the shape, it does vaguely resemble Five Qi Returning to Origin.”

“Hey, Mr. Moon!”

“Did you just call me ‘Mr. Moon’?”

I met Mungyeong’s cold stare without flinching.

One second. Two seconds. Three seconds.

*Hmm. That should be enough.*

“I misspoke. I must have suffered a serious Internal Injury.”

“Looking at you is making my qi-sea acupoint throb.”

I avoided Mungyeong’s completely deflated stare and hurriedly changed the subject.

“But what brings you here all of a sudden? No, before that, how did you get in?”

“Why do you think there is a door?”

“But Mujin was guarding the door…”

That was when my voice trailed off.

Slide. Thump!

A figure collapsed with a faint flop through the half-open doorway.

The back of the head was so familiar that my eyes widened before I could stop them.

“Mujin! Hyuk Mujin!”

As I shouted, Mungyeong spoke in a grim voice.

“Leave him. He won’t wake up even if you shake him.”

He wouldn’t wake up even if I shook him?

This blood-crazed Killing Ghost had finally done something.

I roared furiously.

“You cold-blooded murderer! You’re just like that bastard the Slaughter Saint!”

“I tried to wake him because he was sleeping in front of the door, but he didn’t move at all… What did you just say?”

“Huh?”

“I asked what you said.”

“What?”

*What the fuck?*

Right on cue, Hyuk Mujin’s corpse—or rather, his body—twitched.

Along with a vigorous snore.

“Grrrrrr.”

“……”

“……”

Our gazes collided silently in midair. I opened my mouth with a charming smile.

“There seems to have been a very slight, insignificant misunderstanding.”

Mungyeong answered with a dry expression.

“It doesn’t seem to have been a misunderstanding. Nor does it seem insignificant.”

“Can’t we just agree that good is good?”

“You mean dead is dead?”

“Oh… How did you get that from what I said?”

“There’s no reason it couldn’t be. Do you have a problem with it?”

I did have a problem with it, and his cochlea also seemed to have a serious problem, but I lacked the courage to point that out.

“I was wrong.”

“Does apologizing make everything end?”

“I believe sincere conversation can untangle every knot.”

“Good. Then go talk things out with Dark Heaven’s Lord of Heaven. And wipe that irritating smile off your face before I tear your mouth apart.”

“Our ancestors used to say that you can’t spit in a smiling face.”

“Ptui.”

Smack.

Hmm. Our ancestors had been wrong.

But the more important the moment, the more important it was to regain my composure. I calmly wiped the spit from my cheek.

“You have an incredible launch speed. I thought it was a hidden weapon.”

“If I spit while infusing it with internal energy, I can burst out a person’s eyeballs.”

“That’s impressive. Are you a member of the Zerg by any chance?”

“I’m the Grim Reaper.”

“……As I said, I’m deeply sorry.”

Mungyeong looked at me as though he were wondering how many pieces he would have to cut me into for people to say I had died properly, then clicked his tongue.

“Enough. Every time I talk to you, I feel my energy being sucked away.”

“……”

*Who does he think he’s talking about? My life force is draining away by the second.*

I would bet Hyuk Mujin’s left atrium that the conversation just now had shaved at least three days off my life.

*That bastard Hyuk Mujin. I told him to stand guard, and he couldn’t even resist going back to sleep.*

Mungyeong was something else, but Hyuk Mujin was no less impressive.

“But what brings you here…?”

“You make it sound as though you’re asking why I came here to do some other dogshit thing.”

“Oh.”

“Oh?”

“Oh… no. I was just curious.”

“It must be my imagination, but I think your pronunciation has become rather strange since we last met.”

“Of course. It’s your imagination.”

Mungyeong let out a small sigh and threw the bundle in his hand.

Thump.

I caught it reflexively and stared at it with wide eyes.

“What is this?”

“A pill.”

“A pill?”

*Is this Santa Claus in spring? Why is he suddenly giving me a present?*

I undid the bundle with mixed feelings and found a small, solid-looking wooden case inside.

At the same time, a strange fragrance seeped deep into my nose.

*This is…*

They said that with elixirs like this, you could recognize their effects before even seeing them. This was exactly such a case.

Before opening the wooden case, I realized that the pill inside possessed considerable efficacy.

Click.

When I opened the case, a reddish pill came into view. Even at first glance, it was clearly no ordinary pill.

I stared blankly at it, then raised my head and looked at Mungyeong.

“What are you staring at?”

“I was wondering why you suddenly decided to give me something like this.”

“It contains a considerable amount of fire qi. It will help you.”

“What?”

“Do you have a hidden weapon stuck in your ear? Don’t make me say it twice.”

“No, I wasn’t asking about its efficacy…”

Mungyeong’s face crumpled. It was such an expressive display of emotion that I could hardly believe it was the same Mungyeong whose expression was usually bleak.

“I found it on the way here.”

“……?”

“Correction. I saw it while passing by and bought it. Satisfied?”

*What do you mean, satisfied, old man?*

I touched the red pill inside the wooden case.

*Item check.*

Ding.



> **System**
>
> **Mungyeong’s Specially Crafted, Custom-Made Pill for Jin Taekyung**
>
> Would you like to view more detailed information?
>
> **Y / N**

*Yeah. No. That’s enough.*

I closed the simple System window and stared at Mungyeong with a tepid gaze.

“‘I saw it while passing by and bought it.’ Yes, I see.”

“……What is that look?”

“Nothing. In any case, I’ll accept it gratefully.”

What I felt toward Mungyeong right now was exactly half gratitude and half fear.

*Thanks for the good pill, but what in the world is the next training session going to be…?*

When someone suddenly treated you this well, it felt like they were feeding a condemned man a proper meal.

As if he had sensed the meaning behind my trembling gaze, Mungyeong opened his mouth.
```
