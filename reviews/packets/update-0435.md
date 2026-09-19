<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0435.txt",
      "sha256": "e25996c6d6232fc65f06582db7b7ab1650d0bbe0dd55b464485614aa77ad33df",
      "bytes": 13553
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "cd2040d6bf3bcfa3188cf4e959493d55cdf06ae53f94a055130cb11c2cf01e1d",
      "bytes": 2637
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "af8f09cfbf3dc86f8427aae7c1b7c58f798a979c253ce2219c30f39c5770f400",
      "bytes": 142655
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c1881e2891c8968dfe4831da5ea35f1ec968319eb62faab73253c600a522534a",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8c01e2d215ddcc858a4d87a6631e13e6583f29ab7d98be94bc1f558a4af01b56",
      "bytes": 533
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "0a1865f30af1d8b2252bd5a830385767249c08bb3af35e39be399bb545c94f77",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d127e6b445d59f0ff62eefef16cbe9d6f0173feee860a4be3b7c769be5b722f2",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ded3273d9fbf1a254f181a29ff9c2215d44d599fc0e26739793b7029e57453d1",
      "bytes": 1416
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3d10fdad123fa7ada207e826ede2feff977bf5a9f6aa055787e81af9776481d6",
      "bytes": 622
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "f53a2caecc54397c42f31b5e6045a7ecc8a06d192495aedf534e3128109ab2bf",
      "bytes": 792
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "8f171a48c1e9cdcaedd79570728722d35648e56e7e20047e52b59367ea631059",
      "bytes": 666
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e33e6a918562c60e3a36d8b6f1a05d941619317d40e8006c2d3c8f02fdcd682b",
      "bytes": 135962
    }
  ],
  "estimated_tokens": 12455
}
-->

# Durable State Update — Chapter 435

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 435. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 435. Profile updates may replace only one
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
  "chapter": 435,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 435,
    "continuity_sources": [435],
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
    "The Arch Lich's magic-circle fragments match the patterns and symbols of the Moving Formation Jin saw in Murim, and can be assembled into one enormous circle.",
    "The circle appears to have absorbed human life force to accumulate mana, but this remains the Skeleton King's inference rather than a confirmed decipherment.",
    "Jin suspects that the Murim formation, the modern world's magic circle, the battle phenomena involving the Blood Lord and Western Heaven Demon Lord, and his junk capsule are connected.",
    "Magic Johnson knows Jin killed Lee Jungryong and Wu Heixing, accepts Jin as a friend, and has agreed to help protect Jin's people and support his growth.",
    "The Skeleton King remains hidden in Jin's Inventory or an extradimensional pocket when necessary and continues pursuing a human-world identity as Stone-King.",
    "Chairman Shao Yang has begun a political purge against Wu Xueming and leading Crown Prince Party figures, accompanied by a sweeping military reorganization.",
    "Jin's mother and Hayeon have left China with him aboard the chartered aircraft.",
    "Jin is using Ares Guild's leadership vacuum and Peace Guild's expected growth to encourage defections without openly declaring war.",
    "Chairman Shao Yang is Xiao Shen's grandfather and has promised Jin's fifty-trillion bounty after Jin saved Xiao Shen.",
    "Jin has logged in aboard the departing aircraft and begun returning toward the other world."
  ],
  "continuity_sources": [
    434,
    433
  ],
  "open_questions": [
    "What do the shared patterns and symbols represent, and why did the Arch Lich possess a circle matching the Moving Formation?",
    "What connection links the two worlds, the battle phenomena, and the junk capsule?",
    "How will Magic Johnson respond to what he now knows about Jin and the magic circle?",
    "How will Ares Guild's leadership vacuum affect its Hunters and influence?"
  ],
  "safe_through": 434,
  "temporary_decisions": [
    "Render 매직 존슨 as “Magic Johnson,” 스켈레톤 킹 as “Skeleton King,” 스톤-킹 as “Stone-King,” and 골골 as “Golgoli.”",
    "Render the suspected function of the circle as “life-force absorption” while preserving the uncertainty of the inference.",
    "Use “mental-manipulation magic” or “memory-manipulation magic” for 정신 조작 마법 and preserve its status as a serious felony.",
    "Preserve Jin's dry, profane voice and the Skeleton King's grandiose, Internet-influenced insults.",
    "Render 아공간 포켓 as “extradimensional pocket.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 평화 | **Peace Guild** | Guild name. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 명문혈 | **Mingmen acupoint** | Acupoint into which Jeok Cheongang sends internal energy while treating Hong Dao. |
| 부동심 | **Unshakable Mind** | Mental discipline Hongcheon is accused of abandoning when he loses composure. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 귀식대법 | **Turtle Breath Technique** | Cheongpung’s joking description of breath-holding and suspended bodily functions. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |

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
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 377
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 434
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 431
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 399
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 434
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, and can perceive the texture of qi well enough to sever layered magic.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 434
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 376
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** He has carried Jin Taekyung's party and Mungyeong from Guang'an to Chengdu and agreed to send subordinates to help them return.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 377
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the Divine Physician and former Slaughter Saint, and he has sworn never to kill again.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃435화



석양마저 집어삼킨 깊은 밤. 뱃머리에 앉아 검게 물든 강물을 응시하던 한 소년이 불쑥 입을 열었다.

“어인 일이십니까?”

“장강(長江)을 바라보며 술이나 기울일까 하고 왔지. 선객이 있는 줄은 몰랐지만.”

소년의 등 뒤, 기척도 없이 유령처럼 나타난 오척단구의 노인이 호리병을 흔들며 씩 웃었다.

“어때, 생각 있느냐?”

“과한 음주는 몸에 해롭습니다. 멀리하시지요.”

“그러지 말고 한잔하지 그러느냐? 운치도 좋은데.”

“혼자 남게 된다면 더 좋을 것 같군요.”

“거, 어린놈이 말하는 본새가 아주 샛노랗구나. 아까부터 어르신이 말씀하시는데 쳐다보지도 않고.”

그 순간, 소년이 눈살을 찌푸렸다. 푸른 하늘이 떠오를 만한 헌앙한 얼굴 위로 먹구름이 끼고 낙뢰가 내리쳤다.

이어 맑은 목소리 대신 깊게 가라앉은 음성이 소년의 입술 사이로 흘러나왔다.

“적당히 하지.”

푸르스름한 안광이 어둠 속에서 빛을 발한다.

그런 소년에게서는 늘 밝고 쾌활하던 어린 의생, 문경의 모습은 더 이상 찾아볼 수 없었다.

빈자리를 차지한 것은 살성(殺星)이라는 별호를 지닌 희대의 무인이며, 예리한 발톱을 드러낸 맹수다.

하지만 그것은 비단 그 한 사람에게만 해당되는 것이 아니었다.

“어이구, 무서워라.”

어지간한 절정 고수도 석상처럼 굳어 버릴 가공할 기세 앞에서 천연덕스럽게 입꼬리를 말아 올린 노인. 화왕(火王) 적천강이 호리병을 던졌다.

“어울리지도 않는 어린놈 흉내는 관두고 목이나 축여.”

느릿느릿하게 다가온 호리병을 받아 든 문경이 건조한 목소리로 대답했다.

“생각 없다.”

“왜, 아직 술 마실 나이가 아니라서?”

“끊었지. 오래전에.”

“의생 노릇 할 때부터겠군.”

“……안 자나?”

“늙으면 잠이 없어지거든. 누구처럼.”

문경은 작게 고개를 저었다. 일평생 과묵하고 감정 표현이 적은 그에게 있어 적천강은 대화를 나누기 힘든 상대다. 상대하기 싫다면 피하는 것이 맞다.

“가려고?”

“자네가 알 바 아니지.”

“술은?”

문경은 손에 든 호리병을 강물에 던졌다. 넘실거리는 장강의 물결이 호리병을 순식간에 집어삼켰다.

“다 마셨다.”

“……마시기 싫으면 돌려주기나 하던가. 고약한 늙은이로고.”

적천강을 스쳐 지나가던 문경의 눈빛이 날카로워졌다.

살성은 이미 존재하지 않는 사람. 지금의 그는 어디서나 흔히 볼 수 있는 어린 의생일 뿐이다.

“혀가 가볍군.”

“듣는 귀도 없는데 뭐가 어때서. 애초에 여기까지 따라온 마당에 굳이 정체를 감추는 이유가 뭔가?”

문경은 대답하지 않았다. 아니, 대답하지 못했다.

도대체 어째서였을까. 단지 한순간의 충동이었을까.

그건 수많은 살행(殺行)에서도 흔들리지 않던 냉철한 이성으로도 설명할 수 없는 일이었다.

“그렇군. 아직 스스로도 답을 찾지 못한 거야.”

적천강의 말에 잠시 침묵하던 문경이 입을 열었다.

“단순한 동행일 뿐이다.”

“이해해. 처음에는 노부도 그랬거든. 하지만 웬 괴이한 놈 하나를 만나서 말년이 꼬여 버렸지.”

문경은 ‘괴이한 놈’이 누구인지 알 것 같았고, 동시에 가장 어울리는 표현이 아닐까 생각했다.

풍진 강호에서 온갖 인간 군상과 사건을 겪은 그의 시선으로도 그놈은 난생처음 보는 생소한 부류였으니까.

“진태경.”

“역시 아는군. 하긴, 모를 수가 있나.”

“희한한 놈이더군. 나이에 비해 대단한 경지에 도달했어.”

적천강의 입꼬리가 씰룩거렸다.

“큼. 대단하긴 무슨. 그냥 운 좋은 놈이야. 순수한 무재(武才)로는 검성의 제자를 못 따라가. 아직 본인도 눈치채지 못한 것 같지만 이미 중단전(中丹田)을 열 준비를 끝마쳤더군.”

문경은 오는 내내 뱀으로 묘기를 부리던 청년을 떠올렸다.

이제 겨우 약관이 갓 넘은 나이로 휘황한 검강을 흩뿌리던, 사천당가에서의 모습도.

“그 아이도 대단, 아니 대단히 미친놈 같긴 했지. 확실히 재능으로만 따지면 진태경보다 한 수 위다.”

“뭣이!”

“……?”

“아.”

물끄러미 적천강을 바라보던 문경이 혀를 찼다.

“제자 사랑이 극진하군.”

“제자?”

잠깐 멈칫하던 적천강이 헛기침을 내뱉었다.

“크흠. 뭐. 제자일 수도 있고 아닐 수도 있는…….”

“그게 무슨 헛소리지?”

“아니, 그. 약간 복잡한 사정이 있긴 한데. 이게 어떻게 된 거냐면.”

문경은 문득 머리가 아파 왔다.

암천(暗天)이라는 듣도 보도 못한 놈들이 사천을 피로 물들인 것이 불과 며칠 전의 일이다.

가뜩이나 머릿속이 복잡한데, 이 괴이한 스승과 제자에 얽힌 이야기까지 듣고 있자니 없던 뱃멀미까지 생길 것 같았다.

“용건 없으면 이만 가 보겠다. 두 번 다시 오늘 같은 일이 없었으면 좋겠군.”

한마디를 툭 던진 문경이 선실로 걸음을 옮기던 그때였다.

“고맙네. 녀석을 구해 줘서.”

“…….”

“진심이야.”

문경은 대답하지 않고 선실의 문을 열었다. 까칠한 늙은이라며 투덜거리는 적천강의 목소리가 들려왔지만, 깨끗이 무시하고 딱딱한 목제 침상에 앉았다.

몇 발자국 떨어진 옆 침상에는 한참 전에 자리를 차지한 선객이 깊은 잠에 빠져 있었다.

문경은 미동도 하지 않는 진태경을 바라보며 생각했다.

‘정말 괴이한 놈이야.’

그래서인지 잠도 괴이하게 잔다. 처음에는 호흡이 거의 느껴지지 않아 귀식대법(龜息大法)을 펼친 것이 아닌가 의심이 될 정도였다.

그뿐인가. 수백 년에 한 명이 나올까 말까 한 천무지체의 소유자이기도 하다.

앞서 적천강에게선 점점 더 몸이 완벽해지고 있다는, 믿을 수 없는 말까지 들었다.

‘말도 안 되는 소리.’

천무지체가 왜 천무지체인가. 무공을 익히기에 가장 완벽한 몸이기에 하늘이 내린 무골이라고 불리는 것이다.

완벽이라는 두 글자는 조금도 더하거나 뺄 것이 없기에 성립되는 단어. 팔불출 스승의 눈에 콩깍지가 씐 탓에 잘못 판단한 것이 틀림없었다.

‘그래도 대단한 놈인 건 변함없지. 아니, 놈들인가?’

진태경의 바로 옆 침상에는 청풍이 침을 질질 흘리며 잠들어 있었다.

뭔가를 먹는 것처럼 입을 우물거리길래 자세히 보니 늘 옆에 끼고 있던 뱀의 대가리를 쪽쪽 빨며 잠꼬대 중이다.

“만두, 오리 구이, 월병도 주세요…….”

“…….”

“많이, 많이 주세요…….”

도대체 자신이 자리를 비운 동안 무슨 일이 있었던 것인가.

문경은 떨떠름한 표정으로 진태경과 청풍을 번갈아 바라보았다.

‘이런 녀석들이 향후 천하 무림을 밝힐 등불이라니.’

문경이 보기에도 두 사람은 이미 후기지수의 수준을 아득하게 뛰어넘었다.

약관을 갓 넘긴 새파란 나이에 초절정의 벽을 깨트린 희대의 천재들.

만약 둘 중 하나라도 이립 전에 중단전(中丹田)을 연다면 그때는…….

‘이건.’

순간, 진태경과 청풍을 유심히 바라보고 있던 문경의 눈가가 파르르 떨렸다.

‘도대체 언제? 아니, 어떻게?’

번개처럼 자리에서 일어난 문경은 황급히 곤히 잠든 진태경의 맥을 짚었다.

명문혈을 통해 공력을 흘려보내자, 도무지 믿을 수 없는 현실이 눈앞에 펼쳐졌다. 사고가 정지한 뇌리에 한 가지 사실만이 계속해서 맴돌았다.

‘중단전이…… 열렸다?’

오랜 세월 단련한 부동심(不動心)도 소용없었다. 그리고 문경이 넋 나간 눈빛으로 허공을 바라보던 바로 그 순간.

“뭐 하세요?”

시선을 내린 문경은 볼 수 있었다. 자신을 올려다보는 한 쌍의 눈동자를.

등허리의 명문혈과 중단전이 있는 가슴에 올려져 있는 문경의 두 손을 차례대로 바라본 진태경이 입을 열었다.

“뭐여, 시벌.”

문경은 진심을 담아 입을 열었다.

“오해다.”

“오예겠지.”

“잠시 진정하고 내 말을 들어 보…….”

그리고 진태경은 그의 진심에 응답했다.

쾌조선의 모두가 깨어날 만큼 커다란 외침으로.

“노야!”

콰앙!

선실의 문이 잿가루가 되며 흩어지며 화왕 적천강이 모습을 드러냈다.

모두가 잠든 깊은 밤, 고요하던 장강의 평화가 깨져 나가는 순간이었다.



* * *



장강수로맹주 해상왕의 제자이자, 사천의 강을 호령하는 수룡채의 채주, 선화아(船火兒) 무송은 하늘이 무너지는 듯한 얼굴로 부르짖었다.

“안 돼! 내 쾌조선이!”

나는 슬그머니 시선을 피했고 살성, 아니 문경은 갑자기 약초를 만들어야 한다며 자리를 떴다.

그리고 쾌조선 한 척을 불살라 버린 적천강은 무송의 어깨를 두드렸다.

“괜찮네. 배야 다시 만들면 되는 것인데 뭘.”

“안 돼! 안 돼애!”

“어허, 괜찮대도. 사람과 금만 있다면 뚝딱뚝딱 만들어지는 것이 배 아닌가.”

“그게 그렇게 쉬운 일이 아니란 말입니다! 그냥 배가 아니고 저희 장강수로맹에서만 만들 수 있는 특수한 쾌조선입니다! 다시 만들려면 총단에 요청해서 장인들을 데려오고, 천금을 쏟아부어야……!”

격하게 소리치던 무송의 목소리가 서서히 줄어들었다. 적천강이 심상치 않은 미소를 띤 채 그를 바라보고 있던 탓이었다.

어느새 주먹에는 열양지기가 이글거리는 중이다.

“천금을 쏟아부어야, 그다음에 뭐?”

무송이 입을 다물었다.

천금을 쏟아부어서 쾌조선을 다시 만들지, 장강에 자신의 피를 쏟아부을지 고민하는 것이 분명했다.

결국 돈이냐, 목숨이냐다. 선택은 그리 어렵지 않았다.

“……천금을 쏟아부어도 돈이 남는다, 그런 말씀을 드리려고 했습니다. 적 대협.”

“그렇지? 여기 장사 잘되잖아?”

무송이 흉악한 얼굴을 일그러트렸다. 양민들이 보면 오장육부까지 지릴 장면이지만 저래 보여도 저게 웃는 거다. 성골 수적답게 인상이 더러워서 그렇지.

그는 덩치에 안 맞게 양 손바닥을 싹싹 비볐다.

“어후, 이를 말씀이십니까. 없어서 못 뺏죠.”

“그래, 그래. 잘됐군. 기왕 생각난 김에 하는 말인데, 적당히 뺏으라고. 내 알 바는 아니지만 그 사람들도 먹고살아야지.”

“예, 예.”

“내 이 일에 대해서는 다시 한번 사과함세. 수련 도중에 잠깐 실수를 했지 뭔가.”

“그럼요. 당연히 그러실 수 있습니다. 혹시 다치신 곳은?”

“없네. 그런데 요즘 기가 허해. 뭐 씹을 거라도 있으면 좋겠는데…….”

“근래에 괜찮은 하수오가 몇 개 들어왔는데, 드디어 주인을 찾은 모양입니다.”

“주인은 자네지. 노부는 손님이고. 허허. 그래도 준다니까 고맙게 받겠네.”

무송의 어깨를 툭툭 두드리고 돌아선 적천강이 내게 인상을 썼다.

“빌어먹을. 그러게 왜 야밤에 그 난리를 쳤느냐.”

나는 침착하게 대답했다.

“자다가 깼는데 어떤 사내놈이 노야 가슴이랑 등허리를 만지고 있다고 생각해보세요.”

“뼛가루까지 태워 버려야지.”

“네, 그렇게 된 겁니다. 그 상황에서 무슨 판단을 해요. 그리고 갑자기 말릴 새도 없이 죄다 때려 부숴 놓고선.”

결과는 화끈했다.

문경은 살성이라는 별호답게 유령 같은 움직임으로 적천강의 공격을 피했고, 초고온의 열기가 담긴 화염신장은 쾌조선을 화끈하게 불태워 버렸으니까.

적천강이 인상을 찡그리며 중얼거렸다.

“저놈이 옛날 버릇 못 버린 줄 알았지.”

“하긴, 세 살 버릇 여든까지 가긴 하죠.”

“여든은 오래전에 넘겼을걸?”

“그럼 세 살 버릇 백 세까지 가는 걸로.”

물에 빠졌던 사람들을 살핀다며 바쁘게 돌아다니던 문경이 스쳐 지나가듯 속삭였다.

“죽고 싶지 않으면 입 다물어라.”

나는 입을 꾹 다무는 대신, 사람들이 모두 들을 수 있을 만큼 크게 외쳤다.

“문경아, 뭐라고?”

“예, 예?”

“아니. 방금 나한테 뭐라고 하지 않았어?”

“그럴…… 리가요. 잘못 들으신 것 같습니다.”

“그렇지?”

“네, 네.”

“그럼 계속 일 봐. 고생 많다.”

“감사……합니다.”

이게 바로 컨셉충의 최후다.

그나저나 아주 돌아오자마자 스펙타클 하구만.

‘이게 무림이지.’

나는 끝없이 펼쳐진 장강을 바라보며 고개를 내저었다.
```

## Final English reading copy

```markdown
# Chapter 435

Deep night had swallowed even the sunset. A boy sitting at the bow and staring at the blackened river suddenly opened his mouth.

“What brings you here?”

“I came to gaze at the Yangtze while having a drink. I didn’t realize there was already a passenger here.”

Behind the boy, an old man barely five feet tall appeared like a ghost without making a sound. He shook a gourd and grinned.

“Well? Care to join me?”

“Excessive drinking is harmful to the body. You should avoid it.”

“Don’t be like that. Have a drink with me. The atmosphere is nice.”

“I think it would be better if I were left alone.”

“Listen to the way this little brat talks. You haven’t even looked at me while this old man has been speaking to you.”

At that moment, the boy frowned. Dark clouds gathered over his handsome face, bright enough to call blue skies to mind, and lightning flashed.

Then, instead of his usual clear voice, a low, sunken voice slipped between his lips.

“That’s enough.”

A pale-blue gleam shone from his eyes in the darkness.

There was no trace left of Mungyeong, the bright and cheerful young medical apprentice.

What had taken his place was a peerless martial artist known by the sobriquet Slaughter Saint—a beast baring its sharp claws.

But that wasn’t true of only one person.

“Oh, how frightening.”

The old man curled up the corners of his mouth without a care in the world, standing before an aura powerful enough to freeze even an ordinary Peak master stiff as a statue. Then Fire King Jeok Cheongang tossed him the gourd.

“Drop the little-brat act—it doesn’t suit you—and wet your throat.”

Mungyeong caught the slowly approaching gourd and answered in a dry voice.

“Not interested.”

“What, are you not old enough to drink yet?”

“I quit. A long time ago.”

“Since you started playing medical apprentice?”

“…Don’t you sleep?”

“You get less sleep when you’re old. Like someone I know.”

Mungyeong gave a small shake of his head. For someone who had been taciturn and poor at expressing emotion his entire life, Jeok Cheongang was a difficult person to converse with. If he didn’t want to deal with him, avoiding him was the obvious choice.

“You leaving?”

“That’s none of your business.”

“What about the liquor?”

Mungyeong threw the gourd in his hand into the river. The rolling waves of the Yangtze swallowed it in an instant.

“I finished it.”

“…If you didn’t want to drink it, you could at least have given it back. What a nasty old man.”

As Mungyeong passed Jeok Cheongang, his gaze sharpened.

The Slaughter Saint was already a nonexistent person. The man standing here now was nothing more than an ordinary young medical apprentice one could find anywhere.

“Your tongue is too loose.”

“There aren’t any ears listening, so what does it matter? Besides, after coming all this way, why bother hiding your identity?”

Mungyeong did not answer.

No—he couldn’t answer.

Why had he done it?

Had it been nothing more than a momentary impulse?

It was something even the cold reason that had never wavered through countless killings could not explain.

“So you still haven’t found the answer yourself.”

After falling silent for a moment at Jeok Cheongang’s words, Mungyeong opened his mouth.

“It’s nothing more than traveling together.”

“I understand. This old man was the same at first. But then I met one bizarre bastard, and he completely ruined my later years.”

Mungyeong thought he knew who the “bizarre bastard” was. At the same time, he thought it was probably the most fitting description.

Even from the perspective of someone who had experienced every kind of person and incident in the turbulent martial world, that bastard was a completely unfamiliar type—the first of his kind Mungyeong had ever seen.

“Jin Taekyung.”

“So you do know him. Well, how could you not?”

“He’s a strange one. He’s reached an impressive realm for his age.”

The corner of Jeok Cheongang’s mouth twitched.

“Ahem. Impressive, my ass. He’s just lucky. In terms of pure martial talent, he can’t compare to the Sword Saint’s Disciple. He doesn’t seem to have noticed it yet, but he’s already finished preparing to open his Middle Dantian.”

Mungyeong recalled the young man who had performed tricks with a snake throughout the journey.

He also remembered the sight of that same young man at the Sichuan Tang Clan, scattering dazzling Sword Force despite being barely past the age of twenty.

“That kid was impressive too. No—he did seem impressively insane. In terms of talent alone, he’s definitely one step above Jin Taekyung.”

“What!”

“…?”

“Ah.”

Mungyeong stared at Jeok Cheongang and clicked his tongue.

“You dote on your Disciple.”

“Disciple?”

Jeok Cheongang hesitated briefly before letting out a hollow cough.

“Ahem. Well. He might be my Disciple, or he might not be…”

“What kind of nonsense is that?”

“No, well… There are some complicated circumstances. To explain how this happened…”

Mungyeong suddenly felt a headache coming on.

It had only been a few days since a group of people called Dark Heaven—people no one had ever heard of—had dyed Sichuan red with blood.

His thoughts were already tangled enough. Listening to a story involving this bizarre master and disciple made him feel as though he might develop seasickness despite having none before.

“If you have no business with me, I’ll be leaving. I hope nothing like what happened tonight ever happens again.”

Mungyeong tossed out the words and began walking toward the cabin.

“Thank you. For saving the kid.”

“…”

“I mean it.”

Mungyeong did not answer. He opened the cabin door. He could hear Jeok Cheongang grumbling about what a prickly old man he was, but he ignored him completely and sat down on a hard wooden berth.

On the berth beside his, a passenger who had claimed the spot long ago was deep asleep.

Mungyeong stared at the motionless Jin Taekyung and thought,

*He really is a bizarre one.*

Perhaps that was why he slept so strangely, too. At first, Mungyeong could barely detect his breathing and even wondered if Jin Taekyung had used the Turtle Breath Technique.

And that wasn’t all. He also possessed a Heavenly Martial Physique, a constitution that appeared only once every few hundred years.

Jeok Cheongang had even told him something unbelievable: that Jin Taekyung’s body was becoming more and more perfect.

*That’s impossible.*

Why was a Heavenly Martial Physique called a Heavenly Martial Physique?

Because it was the most perfect body for learning martial arts. That was why it was called a heaven-given martial constitution.

The word “perfect” only applied when there was nothing to add or subtract. Jeok Cheongang had surely judged the matter incorrectly because his foolishly doting eyes were clouded by his affection for his Disciple.

*Still, there’s no denying he’s an impressive bastard. No—are they both impressive bastards?*

On the berth immediately beside Jin Taekyung, Cheongpung was sleeping with drool dribbling from his mouth.

His lips were moving as though he were eating something. When Mungyeong looked more closely, he saw Cheongpung sucking on the head of the snake he always kept tucked beside him, mumbling in his sleep.

“Dumplings, roast duck, and mooncakes too, please…”

“…”

“Lots and lots, please…”

What on earth had happened while he was away?

Mungyeong looked back and forth between Jin Taekyung and Cheongpung with an awkward expression.

*These are the ones who are supposed to illuminate the future of Murim?*

Even to Mungyeong, the two had already gone far beyond the level of rising martial artists.

They were peerless geniuses who had broken through the wall into Supreme Peak despite being barely past twenty.

If either of them opened their Middle Dantian before turning thirty, then…

*This is…*

Mungyeong’s eyes twitched as he studied Jin Taekyung and Cheongpung.

*When? No, how?*

He sprang to his feet like lightning and hurriedly took Jin Taekyung’s pulse.

When he sent internal energy through the Mingmen acupoint, an utterly unbelievable reality unfolded before his eyes. One fact continued to circle through his frozen mind.

*His Middle Dantian… has opened?*

Even the Unshakable Mind he had cultivated over many years was useless.

And just as Mungyeong was staring blankly into the air, someone spoke.

“What are you doing?”

Mungyeong lowered his gaze and saw a pair of eyes looking up at him.

Jin Taekyung glanced in turn at Mungyeong’s two hands, one pressed against the Mingmen acupoint at his lower back and the other against his chest, where his Middle Dantian was located.

Then he opened his mouth.

“What the fuck?”

Mungyeong spoke sincerely.

“It was a misunderstanding.”

“More like, ‘Oh yeah.’”

“Please calm down and listen to me…”

Jin Taekyung answered his sincerity with an equally sincere response.

A shout loud enough to wake everyone aboard the fast ship.

“Old Master!”

*Boom!*

The cabin door exploded into ash and scattered as Fire King Jeok Cheongang appeared.

In the dead of night, the peaceful silence of the Yangtze was shattered.

* * *

Mu Song, known as Ship-Fire Boy, was the Disciple of the Seafaring King—the Alliance Leader of the Yangtze River Channel League—and the Stronghold Lord of Water Dragon Stronghold, which ruled the rivers of Sichuan. He cried out with a face as though the sky had fallen.

“No! My fast ship!”

I quietly looked away, while Mungyeong suddenly announced that he needed to prepare some medicinal herbs and left.

Jeok Cheongang, who had burned one of Mu Song’s fast ships to ashes, patted him on the shoulder.

“It’s fine. You can just build another ship.”

“No! Noooo!”

“Come now, I said it’s fine. Aren’t ships made in a snap as long as you have people and gold?”

“It isn’t that simple! This isn’t an ordinary ship. It’s a special fast ship that only our Yangtze River Channel League can build! To make another one, we’d have to request it from headquarters, bring in craftsmen, and pour a thousand gold pieces into it…”

Mu Song’s furious voice gradually grew quieter.

That was because Jeok Cheongang was looking at him with a sinister smile.

Scorching Yang Qi was already blazing around his fist.

“A thousand gold pieces, and then what?”

Mu Song shut his mouth.

He was clearly weighing whether to pour a thousand gold pieces into rebuilding the fast ship or pour his own blood into the Yangtze.

In the end, it came down to money or his life. The choice wasn’t difficult.

“…I was about to say that even after pouring a thousand gold pieces into it, we’d still have money left over. Great Hero Jeok.”

“Right? Business is good around here, isn’t it?”

Mu Song’s ferocious face twisted. It was a scene that would make ordinary people soil themselves right down to their organs, but despite how he looked, that was his smile. He was a true-blooded river bandit, so his features were simply atrocious.

Despite his size, he rubbed his palms together eagerly.

“Oh, don’t even ask. We’d take more if there were anything left to take.”

“Yes, yes. Good to hear. Since it came to mind, let me say this: don’t rob people too much. It’s none of my business, but they need to make a living too.”

“Yes, yes.”

“I apologize once again for what happened. I made a small mistake while training.”

“Of course. Anyone could make such a mistake. Did you get hurt anywhere?”

“No. But my qi has felt weak lately. It would be nice to have something to chew on…”

“A few good pieces of He Shou Wu came in recently. It looks like they’ve finally found their rightful owner.”

“The owner is you. This old man is merely a customer. Ha ha. Still, if you’re giving it to me, I’ll accept it gratefully.”

After patting Mu Song’s shoulder a few times, Jeok Cheongang turned around and glared at me.

“Damn it. Why did you make such a commotion in the middle of the night?”

I answered calmly.

“Imagine waking up from a nap and finding some man touching your chest and back.”

“I’d burn him down to bone ash.”

“Yes. That’s what happened. How was I supposed to make a judgment in that situation? And then you smashed everything to pieces before I had a chance to stop you.”

The result had been scorching.

Mungyeong had evaded Jeok Cheongang’s attacks with ghostlike movements, true to his sobriquet as the Slaughter Saint, while the Flame Divine Palm packed with superheated force had set the fast ship ablaze.

Jeok Cheongang frowned and muttered,

“I thought that bastard hadn’t kicked his old habits.”

“Well, they say a habit formed at three lasts until eighty.”

“He passed eighty a long time ago, didn’t he?”

“Then let’s say a habit formed at three lasts until a hundred.”

Mungyeong, who had been busily moving around and checking on the people who had fallen into the water, whispered as he passed us.

“If you don’t want to die, shut your mouth.”

Instead of keeping quiet, I shouted loudly enough for everyone to hear.

“Mungyeong, what did you say?”

“Yes, yes?”

“No. Didn’t you just say something to me?”

“That couldn’t… possibly be. You must have misheard me.”

“Right?”

“Yes, yes.”

“Then keep doing your work. Thanks for your hard work.”

“Thank… you.”

This was the fate of someone too committed to his persona.

Anyway, it sure was a spectacle immediately after coming back.

*This is Murim.*

I shook my head as I gazed at the Yangtze stretching endlessly into the distance.
```
