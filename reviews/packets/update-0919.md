<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0919.txt",
      "sha256": "6d01825e2a62287893a9bea180b4ba9c3598ebb49d108db505657fde7ffbe251",
      "bytes": 13170
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "70291b68f90e94bdf6c9b17e14cab15de56f7fdb78723f1d61b29e2ef7fa53c4",
      "bytes": 1176
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a63b515f2e07963dba92df6716e73fd64a70a72b09948dfecf483064a6fd7b86",
      "bytes": 231549
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d103bbdd534997f704886d32c0b87c6040124a72075f5bf8efb97a57a3e0fbe4",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "cf1dd9942ee0f6e177d2f8a02349d68faddf4457f48a241bdee01b21e8eb9827",
      "bytes": 731
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "de673914284fa91eb52da98e5497607c97a0a351f7cdde34ca8c990cd9a19d9b",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2a896d410b3e6fd015e9fda54132382da2e2dcbb178332fa2899cac10c0a76d8",
      "bytes": 1429
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "43e45d1b9deb63397fb18d1e1c37cce7e436d708808be6d5fdb5f6cae88c923b",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "1d77b7a015cbf74544ebc162c7623a76175bdd809bd715e7d51d07d07a9e168a",
      "bytes": 850
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "6f5f9e568559d72228e31512802ab4ff5a9b18eb9b7001b16369887756c24bda",
      "bytes": 1252
    },
    {
      "path": "characters/So Gyo.md",
      "sha256": "9b36e90382332729be0049867cce532311aba956a59e8d171adb70a53f8712c8",
      "bytes": 900
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d27f2d3bda307350d4f79e0cce236e615acfc0d09ba53ee365e2e9ed8f509f9e",
      "bytes": 265000
    }
  ],
  "estimated_tokens": 11542
}
-->

# Durable State Update — Chapter 919

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
1 and safe_through 919. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 919. Profile updates may replace only one
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
  "chapter": 919,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 919,
    "continuity_sources": [919],
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
    "Jin Taekyung has returned from a seemingly unrecoverable injury with his body and internal energy restored; the cause is unknown.",
    "Jeok Cheongang and Jin Taekyung reunite and face the threat together; Jeok is exhausted.",
    "Heaven's Slaughter serves Dark Heaven under coercion and attacks Jeok again to preserve his chance of revenge.",
    "Heaven's Slaughter's latest strike reaches Jin Taekyung's chest after Taekyung sees through his concealment; the outcome is unknown.",
    "The Eastern Heaven Demon Lord is sprawled and apparently dazed; his fate is unconfirmed."
  ],
  "continuity_sources": [
    918
  ],
  "open_questions": [
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?",
    "What is the outcome of Heaven's Slaughter's strike on Jin Taekyung?",
    "Will Jeok Cheongang and Jin Taekyung defeat Heaven's Slaughter?",
    "Did the Eastern Heaven Demon Lord survive the spear's impact?",
    "What is So Gyo's identity and allegiance?"
  ],
  "safe_through": 918,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 살기     | **killing intent**                               |                                                       |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 소교 | **So Gyo** | The palace attendant leading the group assigned to serve Prince Shangshan. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 검남춘 | **Jiannan Chun** | Sichuan liquor offered to the Heavenly Power Demon. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 살천문 | **Salcheonmun** | Vanished assassin sect once associated with Mungyeong. |
| 은영술 | **concealment techniques** | Stealth arts associated with ninjas. |
| 칠공 | **seven apertures** | The seven bodily openings through which Taekyung's overflowing heat escapes. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |
| 금우궁 | **Golden Ox Palace** | Palace title held by the Imperial Guard commander. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 소교 | 진태경 | palace attendant addressing a martial artist and guest under escort | Young Master Jin | formal and respectful, but firm | Addresses him as 진 공자 while escorting him and warning him not to investigate. |
| 진태경 | 소교 | palace attendant and martial artist under imperial scrutiny | you | formal-polite, controlled and challenging | Taekyung addresses So Gyo as 당신 while questioning her presence and demanding an explanation. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |
| 동천마군 | 소교 | enemies | you; you woman | hostile and demanding | He demands that So Gyo reveal her identity. |
| 소교 | 동천마군 | enemies | you | casual, taunting, and threatening | She warns him to stop and taunts him about whether suicide would still kill him. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 금우궁 | master to commanded undead subordinate | Fire King | commanding | The Eastern Heaven Demon Lord’s bell-imprinted order directs Golden Ox Palace to kill the Fire King. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 918
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 918
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a being no longer human, a former Maoshan Sect disciple who commands the dead with a bell.
- **Personality:** His hatred of rulers is rooted in the loss of his family to the violence of the age of chaos and the destruction of the Maoshan Sect, where he had found happiness.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 918
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 918
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao, whom Taekyung killed, has been raised among the Eastern Heaven Demon Lord’s undead, while Jeong Hogun and the Embroidered Uniform Guard have declared themselves allies of the Emperor, and So Gyo’s allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 918
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 916
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan as a disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 654
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung is accompanying him while learning his martial arts through observation, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### So Gyo.md

# So Gyo (소교)

- **Safe through:** Chapter 916
- **Aliases:** None
- **Role:** A palace attendant assigned to Prince Shangshan who is a Supreme Peak master and has a mission to keep Jin Taekyung alive; her identity and allegiance remain unconfirmed.
- **Personality:** Calm, calculating, and self-possessed; she conceals her strength and identity and can be openly taunting.
- **Voice:** Measured and composed, shifting from deferential formality to casual, pointed taunts and threats.
- **Relationships:** She poses as the leader of the palace attendants assigned to Prince Shangshan and is Jin Taekyung’s opponent, yet believes he may be the person she seeks and the person foretold by “that person”; she says only she and the Emperor know a secret she withheld from Baek Yeon, while her true allegiance remains unknown.

## Korean source

```text
＃919화



맹수가 먹잇감을 사냥하는 방법은 크게 두 가지로 나뉜다.

자신이 직접 몸을 움직여 쫓든지. 혹은 먹잇감이 제 발로 다가오게 만들든지.

전자는 간단하지만, 후자는 어렵다.

그러나 훨씬 어려운 만큼 사냥이 성공할 확률도 높다.

먹잇감을 지척까지 끌어들였다는 건, 그만큼 상대를 방심시켰다는 의미니까.

혹은…….

‘먹잇감이 스스로를 맹수로 착각하게 만들었거나.’

한 가지는 확실하다.

지금 이 순간, 섬광처럼 뻗어 나간 창날과 맞닿은 몸뚱어리의 주인은 명백한 후자라는 것.

푸욱!

사냥이 성공했음을 알리는 섬뜩한 파육음과 동시에 허공이 일렁인다.

잿가루와 흙먼지만이 흩날리던 그곳에는, 언제 나타났는지 모를 한 노인이 작살에 꽂힌 생선처럼 파르르 떨고 있었다.

“어, 어떻…… 쿨럭.”

투두둑.

끝맺지 못한 말과 함께 입가를 적시며 쏟아져 내리는 핏물.

나는 고통으로 악귀처럼 일그러진 노인의 얼굴을 바라보며 침착한 어조로 입을 열었다.

“보였거든. 그것도 아주 선명하게.”

“그럴 리가, 그럴 리가 없다.”

노인이 숨을 헐떡였다. 이제는 불과 십여 명밖에 남지 않은 살수들이 위기에 처한 우두머리를 구하기 위해 사방에서 달려들었다.

마치, 타들어 갈 것을 알면서도 불꽃 속으로 몸을 내던지는 부나방처럼.

하지만 이 짧은 이야기의 결말은 이미 정해져 있었다.

내가 맑은 종소리와 함께 눈을 떴을 때부터.

그리고 적천강이 언제 도망칠지 모르는 먹잇감을 유인하기 위해 약한 모습을 보였을 때부터.

퍼엉!

화염신장(火焰神掌)의 열기가 공간을 일그러트린다.

화왕이라 불리는 맹수가 화염이 깃든 발톱을 휘두르자, 부나방들은 단말마조차 내지르지 못한 채 쓰러졌다.

스륵, 쿵.

상반신이 까맣게 그을린 마지막 살수가 무릎을 꿇는다.

볼 것도 없는 절명.

눈앞에서 완전히 사그라진 마지막 희망에, 노인의 목소리는 도리어 담담하게 가라앉았다.

“허점을 보여 목표를 유인한다라. 보기보다 살수의 기질이 있군.”

나는 짐짓 눈살을 찌푸렸다.

“칭찬 같긴 한데, 어째 욕처럼 들리네. 내가 아는 살수는 한 명 빼고 죄다 쓰레기라서.”

“그래, 그렇겠지.”

경련하듯 작게 고개를 끄덕인 노인이 말을 이었다.

“문경. 그놈은 아직 여전한가?”

“뭐?”

나도 모르게 미간이 좁혀졌다.

문경은 살성(殺星)의 본명이다.

그리고 그 사실을 아는 이들의 숫자는 천하를 통틀어 불과 다섯도 되지 않는다.

아니, 그보다 적을 수도 있다.

나를 포함한다 하더라도.

“어떻게…….”

“그 이름을 어떻게 알고 있느냐고?”

쿨럭. 다시 한번 피를 토해 낸 노인이 덧붙였다.

“모를 수가 없지. 놈이 직접 말해 주었으니까.”

그 순간, 나는 문득 노인의 정체를 알 것 같았다.

몇 달 전 사천에 머무를 당시 살성이 지나가듯 언급했던, 모든 것이 베일에 싸여 있는 그의 과거에서 유일하게 드러난 몇 안 되는 정보였으니까.

“살천문(殺天門).”

한때 모두가 두려워했던 천하제일의 살수 문파.

그러나 자신들이 벼린 살성이라는 비수에 멸망한, 이제는 사람들의 기억 속에서 사라진 과거의 흔적.

내 입술 사이로 흘러나온 그 세 글자에, 고개를 끄덕인 노인이 흐릿하게 웃었다.

“문경. 그놈에게 똑똑히 전해라.”

죽어 가는 이의 것이라고는 믿을 수 없는 강렬한 안광이 번뜩인다. 끊임없이 피가 쏟아지는 노인의 입술 사이로 살기 어린 음성이 새어 나왔다.

“우리가, 살천문이 찾아갈 것이라고. 어떠한 희생이 뒤따르더라도, 얼마나 긴 세월이 흐르더라도 반드시.”

음…….

보아하니 살천문 12기 동문회, 뭐 그런 목적이 아닌 건 확실하다.

만나서 검남춘 몇 병 싹 비우고 대리 기사 불러서 마차 끌고 귀가하는, 그런 상식적이면서도 아름다운 결말은 살수 세계에서 통용되지 않을 테니까.

살성이 자신의 손으로 직접 살천문을 멸망에 이르게 했다면 더더욱.

‘모산파에 이어, 이제는 살천문이라.’

어쩐지, 처음 봤을 때부터 뭔가 이상하다 싶었다.

파도 파도 끝없이 이어지는 은원(恩怨)의 고리에, 나는 작게 한숨을 내쉬었다.

“이 정도로 친절하게 공지까지 띄워 주니까 내가 다 고맙네. 걱정하지 마. 지금 들은 말은 토씨 한 글자 안 빼놓고 그대로 전해 줄 테니까.”

그리고 노인을 똑바로 응시하며 덧붙였다.

“살천문의 계야부가, 그렇게 말했다고.”

“……!”

금방이라도 감길 것 같던 노인의 눈동자가 부릅떠졌다.

코앞까지 다가온 죽음을 담담하게 받아들이던 모습은 이제 어디에서도 찾아볼 수 없다. 핏물과 함께 터져 나온 목소리는 숨길 수 없는 경악으로 가득했다.

“그걸, 그걸 어떻게?”

“말했었잖아. 보인다고.”

“……뭐?”

나는 대답 대신 그의 머리 위를 턱짓했다.

아무것도 없어야 할 허공 위에는, 이 세상에서 오직 나만이 볼 수 있는 반투명한 명부(名簿)가 적혀 있었다.



[Lv.140 계야부]



간단한 차이다.

노인. 아니, 계야부는 신기(神技)에 가까운 은영술의 소유자였고, 나는 신기 그 자체라 부를 수 있는 시스템을 갖고 있었다.

그리고 그 차이가, 계야부를 먹잇감으로 만들었다.

“잘 가라.”

이 짧은 만남의 종지부를 알리는 인사와 함께, 나는 손아귀에 쥔 창 자루를 비틀었다.

퍼걱.

마침내 되찾은 애병, 백염(白炎)은 뼈와 살을 두부처럼 가르며 심장에 닿았다.

투명한 창날에 깃든 화염이 그 안으로 스며들었다.

퍼엉.

작은 폭발음과 함께 비틀거리는 신형.

칠공(七空)에서 검붉은 핏물을 쏟아내는 계야부의 모습은, 태풍을 만난 촛불을 닮아 있었다.

푹, 푸확!

창날을 뽑으며 돌아섰다. 허물어지는 신형을 뒤로하고 걸어가는 내 귓가로 기다리던 종소리가 울려 퍼졌다.

띠링.



- [Lv.140 계야부]를 처치하셨습니다!

- 대량의 명성을 획득하셨습니다!

- 대량의 경험치를 획득하셨습니다!

- 이 사실이 알려질 시, 당신은 [살천문]의 추적을 받게 됩니다.

- [살천문]은 [계야부]의 죽음을 잊지 않을 것입니다.



시스템 알림을 통해 두 가지 사실을 알았다.

첫째. 계야부가 죽기 전 했던 말들이 결코 거짓이 아니었다는 것.

둘째. 무려 140레벨의 적을 죽여도 레벨이 오르지 않을 정도로, 그리고 살천문의 표적이 될 것이라는 경고를 듣고도 아무렇지 않을 만큼 내가 강해졌다는 것.

‘좀 쎄하긴 한데.’

어차피 오는 놈 죽이고, 가는 놈도 죽이면 그만이다.

살천문의 살수들이 얼마나 숙련된 인간 백정들인지는 몰라도, 나는 이미 천주의 관심을 한 몸에 받고 있던 몸.

할라피뇨에 청양고추 추가해 봤자 얼마나 더 매워지겠나.

그전에 시원한 우유나 한 잔 마시면 되겠지.

칼슘 대신 경험치가 듬뿍 들어 있는, 이 지긋지긋한 싸움을 끝낼 살아 있는 우유를.

“생각보다 좀 늦었다. 기다리느라 심심했지?”

저벅.

사지 중 유일하게 멀쩡한 한쪽 다리를 버둥거리며 기어가던 누군가의 앞길을 가로막는 발걸음.

내 얼굴을 확인한 동천마군이 일그러진 얼굴로 웃었다.

“오냐, 이 괴물아.”



* * *



실패한 이들은 절망한다.

눈물을 흘리며 깊이 좌절한다.

그러나 동천마군은 아니었다.

그는 절망하지도, 눈물을 흘리거나 좌절하지도 않았다.

자신의 복수는 아직 끝나지 않았으니까. 희망은 여전히 남아 있으니까.

대계(大計)는 실패했으나 그는 아직 살아 있었다.

‘가지가 부러져도 나무는 죽지 않는다.’

뿌리가 있는 한, 나무는 쓰러지지 않는다. 언제고 다시 굵은 가지와 싱그러운 잎사귀를 틔워 낼 수 있을 것이다.

과거 태조에 의해 사라진 모산파의 모든 것이 자신에게 이어져 내려온 것처럼.

그렇기에 발버둥 쳤다.

고작 하나뿐인 다리로, 죽지 않는 몸뚱어리를 버둥거리며 이곳을 빠져나가고자 했다.

‘아직, 아직 끝나지 않았다.’

이미 금우궁이 죽었다. 마삼보는 생사도 알지 못한 채 사라졌다.

뿐인가.

강시들을 조종할 수 있는 요령을 잃었고, 계야부를 비롯한 살천문의 살수들이 죽었다.

하지만 오늘을 위해 준비해 두었던 것이 단지 그뿐이었다면, 동천마군은 이 대계를 시작하지도 않았을 것이다.

‘시간이 필요하다. 시간이.’

환관이라는 신분으로 황실에 스며든 지 어언 반세기.

동천마군이 대국에 드리운 암천의 그늘은 상상 이상으로 짙고 거대했다.

수만 명의 대군을 이끄는 도독부터, 함대를 통솔하는 제독.

짧은 말 몇 마디, 휘갈겨 쓴 글귀 몇 줄로 막강한 영향력을 행사할 수 있는 정계의 거물들까지.

동천마군은 그들의 탐욕을 넘치도록 채워 주었고, 충성을 맹세한 그들은 기꺼이 한배에 올랐다.

순수한 무력, 영향력, 권한 등.

그들이 지닌 모든 것들을 짊어진 채.

대국을 뒤엎을 이 거대한 역모(逆謀)는, 비단 대연회장에만 국한된 것이 아니었다.

그리고 그것이야말로, 동천마군이 지금 이 순간에도 웃을 수 있는 이유였다.

자신보다 더한 괴물을 보면서도 웃을 수 있는 이유.

“생각보다 좀 늦었다. 기다리느라 심심했지?”

저벅.

오랜만에 만난 친구에게 건네는 듯한 가벼운 목소리. 그러나 앞을 가로막는 발걸음은 무겁고 굳건하다.

‘진태경.’

머릿속을 스쳐 지나가는 한 사람의 얼굴이, 이내 동천마군의 망막에 비쳤다.

“오냐, 이 괴물아.”

그리고 그 순간.

콰직.

섬뜩한 파육음과 함께 하나밖에 없던 다리마저 박살 났다.

마침내 모든 사지를 잃은 동천마군은, 느껴지지 않는 고통 속에서 또 다른 상대를 향해 담담하게 입을 열었다.

“세인들이 알면 놀라겠군. 그 거칠기로 이름난 화왕이, 이토록 지극하게 제자를 생각할…….”

콰드득!

이어지려던 목소리가 굉음에 파묻혔다.

곧이어 지면 깊숙이 틀어박힌 동천마군의 귓가에, 맹수가 으르렁거리는 듯한 음성이 닿았다.

“주둥이 닥쳐라. 혀를 뽑아 버리기 전에.”

“혀? 내 혀를 뽑겠다고?”

동천마군이 피식 웃었다.

“그거 괜찮은 생각이군. 나로서도 나쁘지 않은 경험이 되겠어.”

“놈!”

“귀가 울리는군. 시끄럽게 소리치지만 말고 어디 한번 해 보게. 지금 당장.”

“……!”

“뭣 하고 있나. 어서 혀를 뽑아 보라니까.”

그러나 연이은 재촉에도 들려오지 않는 대답에, 동천마군의 미소가 더더욱 짙어졌다.

“그래, 못 하겠지. 할 수 없겠지. 지금 이 자리에서 내 혀를 뽑는다면, 너희가 원하는 대답을 영영 들을 수 없게 될 테니까.”

동천마군은 이미 알고 있었다.

각자의 생사를 건 혈투가 벌어지는 상황이라면 모를까, 이미 승기가 기운 현재로서는 자신을 죽일 수 없을 거라는 사실을.

그는 암천과 천주에 관련된 수많은 정보를 알고 있는 사람이다. 어쩌면 동천마군의 말 한마디가, 향후 천하의 향방을 판가름할 거대한 전쟁을 뒤바꿀 수도 있다.

수십만, 혹은 수백 만의 목숨이 걸려 있는 대전쟁을.

그리고 그것이, 동천마군이 움켜쥔 마지막 희망이었다.

“이보게, 화왕.”

드득. 드드득.

지면을 통해 전해지는 미약한, 동시에 빠르게 거세지는 진동을 느끼며 동천마군은 너털웃음을 터트렸다.

“아직, 하늘이 나를 버리지 않은 모양일세.”

그 순간.

콰드드득!

지축을 떨어 울리는 굉음과 함께 산산이 허물어진 외벽을 넘어 들이닥치는 수천의 군세에, 동천마군은 크게 소리 내어 웃었다.

아니, 웃으려 했다.

고오오오옹.

어디선가 쏘아진 거대한 빛줄기가, 그들을 휘감으며 터져 나가기 전까지는.

콰아아아앙!

그 믿을 수 없는 위력 앞에서, 동천마군은 눈을 부릅떴다.

동시에 한 사람의 이름을 부르짖었다.

“소교……!”
```

## Final English reading copy

```markdown
# Chapter 919

There are two main ways a predator hunts its prey.

It can chase it down itself—or make the prey come to it.

The first is simple. The second is hard.

But the harder the hunt, the greater the chance of success.

Luring prey right up to you means you’ve made it lower its guard.

Or…

*You’ve made the prey mistake itself for the predator.*

One thing was certain.

At that very moment, the body touched by the spearhead flashing through the air belonged unmistakably to the latter.

*Puhk!*

A gruesome sound of flesh being pierced announced the hunt’s success, and the air rippled.

Where only ash and dust had been swirling, an old man—no one knew when he had appeared—quivered like a fish skewered on a harpoon.

“Wha—how…? Cough!”

Blood spilled from his mouth, running down his chin before he could finish speaking.

I looked at the old man’s face, twisted into a Fiendish mask of pain, and spoke in a calm voice.

“I saw you. Clear as day.”

“That’s impossible. It can’t be.”

The old man gasped for breath. The assassins—now barely a dozen—came rushing from every direction to save their leader in his moment of danger.

Like moths throwing themselves into a flame, even though they knew they would burn.

But the ending to this short story had already been decided.

From the moment I opened my eyes to the sound of a clear bell.

And from the moment Jeok Cheongang showed weakness to lure in prey that might flee at any moment.

*Boom!*

The heat of the Flame Divine Palm warped the air.

When the predator known as the Fire King swung his flame-cloaked claws, the moths fell without even a dying cry.

*Rustle. Thud.*

The last assassin, his upper body charred black, dropped to his knees.

There was no need to check. He was dead.

With his last hope extinguished right before his eyes, the old man’s voice sank into an oddly calm murmur.

“So you showed an opening to lure in your target. You have more of an assassin’s nature than I expected.”

I furrowed my brow, pretending to take offense.

“That sounds like a compliment, but somehow it feels like an insult. Every assassin I’ve ever met has been trash, except for one.”

“Of course.”

The old man gave a tiny, spasmodic nod and continued.

“Mungyeong. Is that bastard still the same?”

“What?”

My brow furrowed before I could stop it.

Mungyeong was the Slaughter Saint’s real name.

And fewer than five people in all the world knew that.

Maybe even fewer than that.

Even if you counted me.

“How do you…”

“You’re asking how I know that name?”

The old man coughed up blood again, then added, “I couldn’t not know. He told me himself.”

In that moment, I thought I realized who the old man was.

A few months ago, while I was in Sichuan, the Slaughter Saint had mentioned Salcheonmun in passing. It was one of the few things he’d revealed about his otherwise shrouded past.

“Salcheonmun.”

The greatest assassin sect in the world, once feared by all.

But it had been destroyed by the dagger it had forged—the Slaughter Saint—and was now just a remnant of the past, forgotten by most.

At those three words, which had slipped from my lips, the old man nodded and smiled faintly.

“Mungyeong. Make sure you tell him this.”

A fierce light flashed in the dying man’s eyes. His lips were still pouring blood, but a voice full of killing intent slipped out between them.

“Tell him we—the Salcheonmun—will come for him. No matter the sacrifice, no matter how many years pass, we will come.”

Hmm…

Judging by that, it definitely wasn’t a reunion for Salcheonmun’s twelfth class.

The kind of reasonable, beautiful ending where they meet up, polish off a few bottles of Jiannan Chun, call a designated driver, and ride home in a carriage wasn’t something the assassin world did.

Especially if the Slaughter Saint himself had brought about Salcheonmun’s destruction.

*First the Maoshan Sect, and now the Salcheonmun.*

I’d thought something was off from the moment I first saw him.

The chain of gratitude and grudges went on and on, no matter how far I dug. I let out a small sigh.

“I’m touched you went out of your way to give me such a thorough heads-up. Don’t worry. I’ll pass on every word exactly as I heard it.”

I looked the old man straight in the eye and added, “That’s what Gye Yabu of the Salcheonmun said.”

“……!”

The old man’s eyes, which had seemed ready to close at any moment, flew open.

The calm acceptance of his approaching death had vanished. His voice burst out along with a spray of blood, filled with undisguised shock.

“How—how do you know that?”

“I told you. I can see you.”

“……What?”

Instead of answering, I jerked my chin toward the space above his head.

Floating in the empty air was a translucent roster that no one but me in this world could see.



[Lv. 140 Gye Yabu]



It was a simple difference.

The old man—no, Gye Yabu—possessed concealment techniques bordering on the miraculous. I had a System that could be called a miracle itself.

And that difference had turned Gye Yabu into prey.

“Goodbye.”

With that farewell to mark the end of our brief encounter, I twisted the spear shaft in my grip.

*Crunch.*

My long-lost weapon, White Flame, at last, cut through bone and flesh like tofu and reached his heart.

The flames clinging to its transparent blade seeped inside him.

*Boom.*

His body staggered with a small explosion.

Gye Yabu poured dark-red blood from his seven apertures. He looked like a candle caught in a typhoon.

*Puhk! Splurt!*

I pulled out the spear and turned away. As I walked off, leaving his crumpling body behind, the long-awaited bell rang in my ears.

*Ding.*



> **System**
>
> You have defeated Lv. 140 Gye Yabu!
>
> You have gained a large amount of Fame!
>
> You have gained a large amount of EXP!
>
> If this becomes known, you will be pursued by the Salcheonmun.
>
> The Salcheonmun will not forget Gye Yabu’s death.



The System notification told me two things.

First, that Gye Yabu hadn’t been lying when he spoke before he died.

Second, that I’d grown strong enough not to level up even after killing a Level 140 enemy—and not to care even when warned I’d become a target of the Salcheonmun.

*It’s a little unsettling, though.*

Either way, I could just kill whoever came after me—and whoever left.

I didn’t know how many hardened human butchers the Salcheonmun had, but I already had the Lord of Heaven’s undivided attention.

How much hotter could a jalapeño really get if you added a Cheongyang chili?

I’d just have to drink a nice, cold glass of milk beforehand.

Living milk packed with EXP instead of calcium—the kind that could put an end to this damnable fighting.

“Sorry I’m a little late. Get bored waiting?”

*Step.*

My foot came to a stop in front of someone crawling away, scrabbling with the only leg he had left intact.

The Eastern Heaven Demon Lord confirmed it was me, then smiled through his twisted face.

“Yeah, you monster.”



* * *



Those who failed despaired.

They wept and sank into deep despair.

But the Eastern Heaven Demon Lord did not.

He neither despaired nor wept. He did not give in.

His revenge wasn’t over yet. There was still hope.

The grand plan had failed, but he was still alive.

*Even if a branch breaks, the tree doesn’t die.*

As long as the roots remained, the tree wouldn’t fall. Someday, it could grow new, sturdy branches and fresh leaves.

Just as everything from the Maoshan Sect, destroyed by Taizu long ago, had passed down to him.

That was why he struggled.

With just one leg, his undying body squirmed as he tried to escape.

*Not yet. It’s not over yet.*

Golden Ox Palace was dead. Ma Sanbao had disappeared, and he didn’t even know whether he was alive or dead.

And there was more.

He had lost the means to control the jiangshi, and the Salcheonmun assassins—including Gye Yabu—were dead.

But if that was all he had prepared for today, the Eastern Heaven Demon Lord would never have begun this grand plan.

*I need time. Time.*

It had been half a century since he had infiltrated the imperial court under the identity of a eunuch.

The shadow of darkness the Eastern Heaven Demon Lord had cast over the Great Nation was deeper and larger than anyone could imagine.

From commanders leading armies of tens of thousands to admirals commanding fleets.

And even the political heavyweights who could wield enormous influence with a few quiet words or a handful of hastily written lines.

The Eastern Heaven Demon Lord had more than satisfied their greed, and those who swore loyalty had willingly climbed aboard the same ship.

They had staked everything they possessed—their strength, their influence, their authority.

This great rebellion, meant to overturn the Great Nation, was not confined to the grand banquet hall.

And that was precisely why the Eastern Heaven Demon Lord could still smile at this very moment.

Why he could smile even as he faced a monster greater than himself.

“Sorry I’m a little late. Get bored waiting?”

*Step.*

The voice was light, as if greeting an old friend. But the footstep blocking his way was heavy and firm.

*Jin Taekyung.*

The face of one man crossed his mind, then appeared in the Eastern Heaven Demon Lord’s vision.

“Yeah, you monster.”

And at that very moment—

*Crack!*

With a gruesome sound of flesh being crushed, the only leg he had left was smashed to pieces.

Now missing all four limbs, the Eastern Heaven Demon Lord calmly spoke to another opponent through pain he could no longer feel.

“The world would be astonished to learn that the Fire King, famed for his rough ways, cares so deeply for his Disciple…”

*Crack!*

A booming crash drowned out the rest of his words.

Then, as the Eastern Heaven Demon Lord was driven deep into the ground, a voice reached his ears, growling like a beast.

“Shut your mouth. Before I rip out your tongue.”

“My tongue? You’d rip out my tongue?”

The Eastern Heaven Demon Lord gave a short laugh.

“That’s not a bad idea. It would be a new experience for me, too.”

“You bastard!”

“My ears are ringing. Stop shouting and try it. Right now.”

“……!”

“What are you waiting for? I said, rip out my tongue.”

But even after he urged him again and again, no answer came. The Eastern Heaven Demon Lord’s smile deepened.

“Right. You can’t. You won’t. If you rip out my tongue here and now, you’ll never get the answers you want.”

The Eastern Heaven Demon Lord already knew.

Unless they were in a desperate fight for their lives, they couldn’t kill him now, when the advantage was already theirs.

He knew a great deal about Dark Heaven and the Lord of Heaven. One word from the Eastern Heaven Demon Lord could change the course of a great war that would decide the future of the world.

A war that would put hundreds of thousands, perhaps millions, of lives at stake.

That was the last hope he clung to.

“Listen, Fire King.”

*Rumble. Rumble.*

Feeling the faint vibrations travel through the ground, growing stronger by the moment, the Eastern Heaven Demon Lord burst into hearty laughter.

“It seems Heaven hasn’t abandoned me after all.”

At that moment—

*CRAAASH!*

With a roar that shook the earth, thousands of soldiers poured through the outer wall, which had crumbled to pieces.

The Eastern Heaven Demon Lord laughed aloud.

No—he was about to laugh.

*Gooooooom.*

Until an enormous beam of light shot from somewhere, wrapped around them, and burst.

*KABOOM!*

Faced with that unbelievable power, the Eastern Heaven Demon Lord’s eyes flew wide.

At the same time, he screamed one person’s name.

“So Gyo…!”
```
