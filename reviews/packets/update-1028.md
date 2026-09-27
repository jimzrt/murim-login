<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1028.txt",
      "sha256": "8126bcfbe31af04e7c20be57fdfa7443b294da1c1dd79695470b978304467255",
      "bytes": 13153
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4e55d29f02a06e7aedf26543db97211ce836a6214e78b41792e4c4f726150390",
      "bytes": 1003
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a66501f684135b54b6631e5c2962356b020be649c6bbbe0bb070c85ef55335cd",
      "bytes": 239693
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "0627da13bbd6638fa400618a1f5251d66329207444af7edd88e82a6c92c36edc",
      "bytes": 875
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e01112f1b42ecca913edf99fdfb877c815b705d2492516906c73641f994c89be",
      "bytes": 760
    },
    {
      "path": "characters/Heavenly Power Demon.md",
      "sha256": "ea17c02e86a30350e578b84487505084d7d8e9a334cd1d84eba73be2cf30a032",
      "bytes": 993
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "004b8ba149e46bafd70b911a7f577176566fe818810bf86a868d0a52711d5ff1",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "85d866deea9c4f98a6872a852c15a244337688f9752222efa3d8d0bf971446bf",
      "bytes": 1682
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5f676e680f074937a40a65fc4ffdea52cf60cddc5146a161a35941c3ac643e4b",
      "bytes": 623
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "a0c94e0bcc035531d9f5ebde9a16aedbeee53e5e3fb0f0a4eff311a648fb1dd8",
      "bytes": 1069
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1f7b20e9c53a1c233e8cffd7b382e80a304ee5ab7e6e3cb0a76a0d4682abc802",
      "bytes": 278820
    }
  ],
  "estimated_tokens": 11621
}
-->

# Durable State Update — Chapter 1028

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
1 and safe_through 1028. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1028. Profile updates may replace only one
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
  "chapter": 1028,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1028,
    "continuity_sources": [1028],
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
    "The Blood-Sword Demon Lord has appeared before Jin Taekyung, Jeok Cheongang, and Sama Pyo; he killed Goyangcheon, the last survivor of the Goyang Family and the former Spear King.",
    "The Blood-Sword Demon Lord once served the Heavenly Demon as a favored guard dog and now serves the Lord of Heaven.",
    "The Blood-Sword Demon Lord says he fears Jin Taekyung might defeat the Lord of Heaven and signals a strike as Taekyung, Jeok Cheongang, and Sama Pyo charge; roughly a thousand heads fall."
  ],
  "continuity_sources": [
    1026,
    1027
  ],
  "open_questions": [
    "When did Dark Heaven and the Lord of Heaven emerge, and did Dark Heaven cause the Great Faction War?",
    "Who or what was the target of the Blood-Sword Demon Lord’s commanded strike, and what happened to the meeting party and the thousand prisoners?",
    "What is the Lord of Heaven’s identity and purpose?"
  ],
  "safe_through": 1027,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 하북팽가   | **Hebei Peng Family**            |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 천력마 | **Heavenly Power Demon** | Formerly imprisoned Tang Clan criminal; distinct from 천력부, Heavenly Axe. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 삼노 | **Three Old Men** | Mocking designation used by the Western Heaven Demon Lord for the aged Qilian Three Fiends. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 구천 | **Nine Springs** | Euphemism for the realm of the dead. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 천산삼노 | **Three Elders of Tianshan** | The three former Demonic Cult fiends serving the Blood-Sword Demon Lord. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 진태경 | 천력마 | prisoner_feeder_to_prisoner | you | casual and mocking | Taekyung questions the Heavenly Power Demon and mocks him as the Kunlun Sect's public-pissing criminal. |
| 천력마 | 진태경 | prisoner_to_prisoner_feeder | you | gruff and self-possessed | The Heavenly Power Demon speaks of himself as 노부 while questioning Taekyung. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 혈검마군 | 삼노 | former Demonic Cult fiend to subordinate | Elder Three | familiar and contemptuous | Addresses the wounded elder as 삼노 while asking how he compares to the Fire King. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |

## Listed compact profiles

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1027
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Contemptuous of his former master and certain of his new cause, he treats the weak with ruthless disdain yet takes sincere delight in being recognized and openly admires formidable opponents.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He once served the Heavenly Demon and now serves the Lord of Heaven; he has been ordered not to kill Jin Taekyung and wants to meet him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1027
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Heavenly Power Demon.md

# Heavenly Power Demon (천력마)

- **Safe through:** Chapter 996
- **Aliases:** None
- **Role:** The Heavenly Power Demon was a former Elder of the Great Heavenly Demon Divine Cult who led the subjugation of Qinghai and opened the first front of its holy war before dying after passing his remaining internal energy to Jin Taekyung.
- **Personality:** Quiet and self-possessed despite his severe imprisonment, he is reflective about the moral ambiguity of the Great Faction War and disillusioned with the Divine Cult's corruption.
- **Voice:** Gruff and dry, with formal self-reference as 노부.
- **Relationships:** He was once an Elder and commander under the Great Heavenly Demon Divine Cult's Cult Leader, has spent more than forty years imprisoned by the Sichuan Tang Clan, and identifies the Western Heaven Demon Lord as one of the Divine Cult's four Protectors who served closest to and led astray the Cult Leader.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1027
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1027
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1027
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1027
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and calculating, he is protective of Taishan and pragmatic in combat; he recognizes that his father's ruthless, survival-driven worldview shaped him, even as its influence weighs on him.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan and is Sima Gong's son and heir; his father's ruthless treatment of family shaped his rise and remains a source of inner constraint. He joined the Fire Dragon Pavilion intending to use Jin Taekyung, and Sima Gong has now ordered him to spy on Taekyung's group. He was Ju Hwaran's former fiancé in a political engagement and is openly hostile toward fellow member Song Ilseom.

## Korean source

```text
＃1028화



그 순간, 혈검마군은 웃고 있었다.

초승달처럼 휘어진 그 눈매에 담긴 것은 순수한 즐거움과 흥분이었고, 세로로 길게 찢어진 동공의 떨림은 앞으로 벌어질 일에 대한 기대감으로 인한 것이었다.

정확히는, 한 청년에 대한 기대감.

‘그래, 그것이다. 바로 그 모습이다.’

경악과 분노로 눈을 부릅뜬 진태경을 바라보며, 혈검마군은 가슴이 뛰는 것을 느꼈다.

손짓 한 번으로 일천의 생명을 지워 버렸음에도, 그는 아랑곳하지 않고 진태경에게 모든 감각을 기울였다.

죽은 이들에 대한 일말의 죄책감도, 약속을 어긴 것에 대한 미안함도 없었다.

마교에서 태어나 마교에서 자란 그다.

어미의 배 속에서부터 타고난 잔인한 성정은 걸음마를 시작할 무렵부터 익힌 마공(魔功)을 만나 꽃을 피웠고, 이는 천마가 거느린 이십사 인의 거마(巨魔) 중에서도 따라올 자가 없었다.

이제 그의 관심사는 오직 진태경뿐이었다.

자신의 주인이 예의주시하는 중원 무림의 신룡이자 기린아(麒麟兒).

혈검마군은 저 어린놈의 모든 것을 보고 싶었다.

손끝에서 펼쳐지는 무위를, 토해 내는 감정을, 그 안에 숨겨진 특별함을 온전히 느끼고 싶었다.

‘내게 보여다오. 어서!’

그리고 혈검마군이 마음속으로 애타게 부르짖은 그때.

화아아악!

거대한 미증유의 기운이, 한 사람을 중심으로 솟아올랐다.

“누구부터 죽여 줄까.”

진태경.

차가운 불길이 쏟아지는 청년의 눈빛에, 순간 혈검마군의 입가에 맺힌 미소가 진해졌다.



* * *



천산삼노(天山三老)가 가장 먼저 떠올린 감정은 의심이었다.

분명 조금 전까지는 보이지 않았던 한 자루의 창이 진태경의 손에 들려 있었으니까.

‘어떻게?’

비록 이제는 물거품이 되어 버린 약속이지만, 만남의 조건 중 하나는 무장 해제였고 진태경 측은 그 조건을 충실하게 이행했다.

하여 그들 모두는 빈손으로 이곳에 왔고, 그 점은 천산삼노에게 있어 상당한 위안이 되었다.

화왕이라는 무시무시한 노괴(老怪)만 감당할 수 있다면, 무기도 없는 핏덩이 두 놈쯤이야 어려울 것이 없을 테니까.

비록 그중 하나가 그 대단하다는 열화신룡 진태경이라 할지라도, 그들 세 사람은 천산을 넘어 중원에까지 악명을 떨친 전대의 대마두.

그렇기에 천산삼노의 입장에서는 충분히 승산 있는 싸움이었다.

최소한 진태경의 손에 창이 들리기 전까지는.

그리고 만년한철로 이루어져 있음이 분명한 저 신병이기(神兵利器)에, 예상을 아득히 뛰어넘는 거대한 힘이 덧씌워지기 전까지는.

우우웅.

눈이 부시도록 새하얀 창날이 흔들린다.

아니, 주변의 공기가 잘게 몸을 떨었다.

그와 동시에 고작 수년 전 약관을 넘긴 청년의 몸에 담기기에는 너무나도 크고, 정순한 기운이 창날을 휘감으며 솟아올랐다.

츠츠츠츠.

호사가들이 강기(罡氣)라 부르는 그것은 더 이상 눈부신 청백색이 아니었다.

‘이건.’

세 늙은이는 순간 자신들도 모르게 숨을 삼켰다.

이 힘을, 이것을 도대체 뭐라 정의해야 할까.

창날에 깃든 강기는 마치 깊은 바닷속 심해처럼 거무스름했고, 한편으로는 극에 달한 불꽃처럼 푸르게 타올랐으며, 또한 벽력(霹靂)과도 같은 번뜩임이 있었다.

‘다르다.’

천산삼노는 본능적으로 느낄 수 있었다.

저 기운은 자신들이 일평생 쌓아 온 기운과는 종류가, 궤가 다르다는 것을.

하지만 천산삼노로서는 그 정확한 실체를 알 도리가 없었다.

지금 이 순간 그들에게 전해지는 왠지 모를 익숙함이 진태경이 천력마(天力魔)로부터 넘겨받은 공력 때문이라는 것도.

마공으로부터 비롯된 저 불길한 힘이, 열화문의 겁화(劫火)와 하북팽가의 벽력으로 마침내 하나가 되었다는 것도.

그리고 저 검푸른 빛줄기에 담긴 힘이, 얼마나 거대하면서도 예리한지도.

이 모든 것을 누구보다 잘 알고 이해하는 유일한 사람은, 지금 진태경의 곁에 있었다.

‘허.’

화왕 적천강은 침잠하게 가라앉은 눈빛으로 진태경을 응시했다.

짐작은 했다. 다만 직접 확인하지 못했을 뿐이다.

등봉조극(登峰造極).

하늘과 맞닿은 가장 높은 봉우리에 오른 청년은, 이제 나이와 관록 따위로 판단할 수 없는 존재가 되었다.

다른 누군가가 거쳐 갔던 것이 아닌, 오직 그만의 길을 개척해 낸 위대한 무인.

적천강은 진심으로 묻고 싶었다.

네 녀석이 이룬 경지가 얼마나 대단한 것인지 아느냐고.

또한 말해 주고 싶었다.

중원 무림을 통틀어 이와 같은 경지에 오른 그들을, 사람들은 모든 경의를 담아 이렇게 부른다고.

십왕(十王).

광활하기 그지없는 하늘과 세 개의 별.

그 아래에 우뚝 서 있던 열 명의 거인.

그리고 바로 오늘, 이 자리에서 진태경은 스스로를 증명하고 있었다.

자신이 바로 열한 번째 거인임을.

하지만 세월을 이기지 못해 쓰러지고, 적들이 휘두르는 시퍼런 날붙이에 피를 뿌리며 허물어진 과거의 그들과는 다른 새로운 시대의 영웅임을.

일천 명의 생명이 사그라진 이 전장에서, 거대한 화염이 타오르고 있었다.

‘실로, 눈부시구나.’

적천강은 등골을 찌르르 울리는 전율을 느꼈다.

동시에 넋 나간 얼굴로 진태경을 바라보는 천산삼노의 모습에서, 서서히 그들에게 드리워지는 죽음의 그림자를 보았다.

“노야.”

나직한 음성.

무수한 죽음을 막지 못한 것에 대한 괴로움과 그로 인한 분노가 들끓는 부름에 적천강은 불현듯 입을 열었다.

“결심한 대로 행하거라.”

천산삼노는 알지 못했다.

이 뜻 모를 한 마디가 위험을 무릅쓰고자 하는 제자에게 건네는 스승의 신뢰와 격려임을.

그리고 그 짧은 대화가, 그들의 운명을 결정지었음을.

슈확!

그 순간, 한 줄기의 예리한 바람이 불었다.

화염인지, 파도인지, 벽력인지 알 수 없는 검푸른 섬광이 공간을 일그러트리며 들이닥쳤다.

믿을 수 없을 만큼 쾌속하고, 거대한 힘을 실은 채.

서걱!

일노(一老)의 전신에 소름이 돋았다. 오직 본능에 의지하여 비틀어 낸 몸뚱어리를 따라, 붉은 핏물과 끔찍한 고통이 퍼져나갔다.

“커흑!”

섬광이 번뜩였고, 그것이 전부였다.

마지막 순간 흐릿한 무언가를 보지 못했다면 이미 구천을 떠도는 고혼(孤魂)이 되었을 터.

‘도대체, 도대체 어찌 이런……!’

이를 악물어 고통과 충격을 가까스로 참아낸 일노는, 혼비백산한 얼굴로 길게 베여 나간 가슴팍을 움켜쥐고 뒷걸음질 쳤다.

예상을 아득히 뛰어넘는 속도와 힘 앞에서 물러난다면 남은 것은 죽음뿐이지만, 다행히도 그에게는 든든한 두 의형제가 있었다.

“대형!”

“안 돼!”

이노(二老)와 삼노(三老)가 비명처럼 부르짖으며 달려들었다. 제각각 한 자루의 도와 검을 쥔 그들의 손이 흐릿해지며 한 방향을 향해 휘둘려졌다.

마치 살수처럼 유령 같은 움직임으로 들이닥친, 진태경을 향해.

콰아아앙!

하나의 창과 두 개의 도검.

수 갑자의 기운이 실린 세 자루의 병장기가 맞닿으며 무시무시한 굉음이 사방을 떨어 울렸다.

뒤집히는 땅거죽과 터져 나가는 공기.

동시에 지금껏 느껴 본 적 없을 만큼 극렬하게 들끓는 힘의 파도 속에서, 두 노인은 똑똑히 볼 수 있었다.

차가운 불길이 쏟아지는 진태경의 눈동자와, 두 명의 초절정 고수를 상대로도 조금의 흔들림도 없이 창대를 굳게 움켜쥔 손을.

그리고 그 손은, 하나뿐이었다.

“조……!”

퍼엉!

조심이라는 두 글자를 내뱉을 틈도, 그럴 시간도 주지 않은 진태경의 일장(一掌)이 삼노의 가슴을 후려쳤다.

‘아.’

순간 아득해진 시야 속, 삼노는 뼈와 살을 부수고 몸속 깊은 곳으로 침투하는 끔찍한 열기를 느꼈다.

우드득.

뒤늦게 들려온 섬뜩한 파열음이 메아리처럼 멀게 느껴진다. 울컥, 솟구치는 핏물을 느끼며 허물어지는 삼노의 귓가에 익숙한 외침이 울려 퍼졌다.

“노옴!”

“셋째야!”

틀림없다. 형님들이다.

세상 사람들이 마두며 개새끼라고 온갖 손가락질을 했어도, 마치 한배에서 나온 친형제처럼 자신을 아껴 주었던 그들이었다.

까득.

삼노는 혀를 깨물며 허물어지려는 신형을 바로잡았다.

이대로 쓰러질 수는 없다. 고작 이따위 허망한 최후를 맞이하기 위해 지금까지 살아온 것이 아니었다.

게다가.

‘우리에게는 마군이, 그 힘이 있다.’

삼노는 확신했다.

지금쯤이면 틀림없이 혈검마군이 나섰을 것이라고.

비록 정신이 혼미한 탓에 잘 보이지는 않지만, 그의 명령 한 마디면 이 극심한 내상과 고통에서도 벗어날 수 있을 거라고.

그런데.

그런데 어째서.

‘왜, 아무것도 느껴지지가 않지?’

시야가 흐릿해진 지금에도 초절정 고수로서의 감각은 여전하다. 하지만 비틀비틀 신형을 바로잡는 삼노의 기감에는 모든 것이 그대로였다.

그의 두 의형이 온 힘을 다해 진태경과 격돌하는 이 순간에도, 혈검마군의 기척은 여전히 십여 장이나 떨어진 그곳에 남아 있었다.

“마군, 마군이시여!”

콰드득, 쾅!

창날 끝에서 터져 나온 굉음이 삼노의 애탄 부르짖음을 집어삼켰음에도, 그 부름을 듣지 못할 혈검마군이 아니었음에도 달라지는 것은 아무것도 없었다.

아니, 정확히는 달라지는 것이 있었다.

사방에서 요동치는 거대한 기운들에 비하면 아주 미세한, 그렇기에 더욱 은밀히 다가온 무언가가.

쐐애액, 푹!

“……!”

순간 덜컥 굳는 신형.

등줄기를 관통한 서늘한 날붙이와, 그 끝에 실린 도기(刀氣)의 존재를 깨달은 삼노는 빛살처럼 돌아서며 팔을 휘둘렀다.

후웅, 펑!

압축된 공기가 폭발했지만, 닿는 것은 아무것도 없다.

아무것도 없는 텅 빈 허공을 후려치고 멍하니 굳어 버린 삼노의 시야에, 서서히 선명해지는 누군가의 형체가 보였다.

칠흑처럼 새카만 흑의와 담담한 눈동자.

이제 겨우 이립이나 됐을까 싶은 젊은 놈의 목소리는, 어찌 저럴 수 있을까 싶을 만큼 낮고 침착했다.

“항상 등 뒤를 조심했어야지. 그런 빈틈을 보이면 나로서도 가만히 있을 수 없지 않겠소.”

“네놈……!”

으직.

삼노는 피가 흐를 만큼 강하게 입술을 깨물었다.

화왕 적천강도, 열화신룡 진태경도 아니었다.

처음부터 지금까지, 줄곧 신경도 쓰지 않았던 어린놈이 언제 숨겨 왔는지 모를 비수를 그의 등줄기에 박아넣었다.

그것도 한순간의 기습으로.

“이러고도, 이러고도 네놈이 정파인이라 할 수 있느냐!”

의미도 명분도 없는 삼노의 공허한 외침에, 사마표가 어깨를 으쓱하며 대답했다.

“괜찮소. 난 사파라.”

“……!”

“그리고 한 가지 더 알려 주자면.”

문득 말을 멈춘 사마표가 자연스럽게 손을 내저었다.

동시에 무복치고는 풍성한 소매 사이로, 또 하나의 섬광이 번뜩였다.

“비수는 넉넉하게 챙겨 왔소.”

쉭!

나지막하게 이어지는 뒷말을 지우며 울려 퍼진 예리한 파공성.

자신을 향해 일직선으로 쇄도하는 그 빛줄기를 바라보며, 삼노는 내심 비웃음을 감추지 못했다.

적어도 앞서 진태경에게 입은 극심한 내상과, 조금 전 등줄기에 틀어박힌 비수로 인해 몸이 움직이지 않는다는 사실을 깨닫기 전까지는.

‘이게 무슨……!’

뻐억!

정확히 미간을 관통한 비수와 함께, 삼노는 어두워지는 세상을 느꼈다.

이 모든 것을 그저 지켜만 보던 적천강의 한 마디를 마지막으로 들으며.

“이제 한 놈. 아니, 둘.”

이미 숨이 끊어진 삼노는 보지 못했다.

그가 최후의 숨결을 내뱉던 그때, 검푸른 강기가 깃든 백염의 창날이 이노의 목줄기를 갈랐다는 것을.

서걱!

솟구치는 피 분수 아래, 경악으로 눈을 부릅뜬 일노가 신형을 파르르 떨었다.
```

## Final English reading copy

```markdown
# Chapter 1028

At that moment, the Blood-Sword Demon Lord was smiling.

The crescent curve of his eyes held nothing but pure delight and excitement. His long, vertically slit pupils trembled with anticipation for what was about to happen.

More precisely, with anticipation for one young man.

*Yes. That’s it. That’s exactly the look.*

Watching Jin Taekyung’s eyes widen with shock and fury, the Blood-Sword Demon Lord felt his heart pound.

He’d erased a thousand lives with a single gesture, yet he paid them no mind. All his senses were fixed on Jin Taekyung.

He felt not the slightest guilt for the dead, nor the slightest regret for breaking his promise.

He had been born in the Demonic Cult and raised in the Demonic Cult.

The cruelty he’d possessed since before he was born blossomed when it met the demonic martial arts he’d learned around the time he began to walk. Among the twenty-four great fiends under the Heavenly Demon, no one could compare to him.

Now, Jin Taekyung was the only thing that interested him.

The Divine Dragon of the Central Plains Murim, a rising star whom his master was watching closely.

The Blood-Sword Demon Lord wanted to see everything about that young brat.

He wanted to fully feel the martial prowess unleashed at his fingertips, the emotions pouring out of him, the special quality hidden within.

*Show me. Hurry!*

And just as the Blood-Sword Demon Lord cried out in his heart—

Whooosh!

An immense, unprecedented force surged up around one man.

“Who should I kill first?”

Jin Taekyung.

At the sight of the cold flames pouring from the young man’s eyes, the Blood-Sword Demon Lord’s smile deepened.

* * *

The first emotion the Three Elders of Tianshan felt was suspicion.

A spear was in Jin Taekyung’s hand—a spear that hadn’t been there moments ago.

*How?*

The promise had turned to dust, but one of the terms of their meeting had been to come unarmed. Jin Taekyung’s side had faithfully honored that condition.

So they had all come here empty-handed, which had been a considerable comfort to the Three Elders of Tianshan.

If they could handle the terrifying old monster called the Fire King, two young brats without weapons shouldn’t be much trouble.

Even if one of them was the renowned Blazing Flame Divine Dragon, Jin Taekyung, the three of them were fiends of a bygone age whose infamy had spread from Tianshan to the Central Plains.

From their perspective, it had been a fight they could win.

At least, until Jin Taekyung had a spear in his hand.

And until an immense power, far beyond their expectations, had enveloped that divine weapon, clearly made of Ten-Thousand-Year Cold Iron.

Rumble.

The dazzling white spearhead trembled.

No—the air around it shuddered in tiny ripples.

At the same time, a pure, immense force surged up around the spearhead, far too vast to fit inside the body of a young man who’d only passed his twentieth year a few years ago.

Ssssss.

What martial arts enthusiasts called Force was no longer a dazzling blue-white.

*This is…*

The three old men drew in a breath before they knew it.

What could they call this power?

The Force gathered at the spearhead was dark, like the deepest depths of the sea. Yet it also burned blue, like flames at their most intense, and flashed with the brilliance of a thunderbolt.

*It’s different.*

The Three Elders of Tianshan could feel it instinctively.

That energy was of a different kind, a different order, from the energy they had cultivated all their lives.

But they had no way of knowing what it truly was.

They didn’t know that the strange familiarity they felt in that moment came from the internal energy Jin Taekyung had received from the Heavenly Power Demon.

They didn’t know that the ominous power born of demonic martial arts had finally become one with the Fire Gate Clan’s hellfire and the Hebei Peng Family’s thunder.

And they didn’t know how immense and keen the power in that dark-blue streak of light was.

The only person who knew and understood all of this better than anyone else was standing beside Jin Taekyung.

*Oh.*

The Fire King, Jeok Cheongang, watched Jin Taekyung with a gaze sunk deep in thought.

He’d suspected as much. He simply hadn’t been able to confirm it for himself.

Ascending to the summit of perfection.

The young man who had reached the highest peak, touching the heavens, was no longer someone who could be judged by age or experience.

He was a great martial artist who had forged a path that belonged to him alone, not one followed by someone else before him.

Jeok Cheongang truly wanted to ask him:

Did he know just how remarkable the realm he’d attained was?

And he wanted to tell him:

Those who reached such a realm in all the Central Plains Murim were called this, with the world’s deepest respect.

The Ten Kings.

An endless sky and three stars.

Beneath them stood ten giants.

And today, right here, Jin Taekyung was proving himself.

He was the eleventh giant.

But unlike the heroes of the past, who had fallen to time or collapsed spilling their blood on the cold-blue blades of their enemies, he was a hero of a new age.

On this battlefield, where a thousand lives had faded, an immense blaze was rising.

*Truly, you shine.*

A shiver ran down Jeok Cheongang’s spine.

At the same time, as he looked at the Three Elders of Tianshan staring at Jin Taekyung in a daze, he saw the shadow of death slowly falling over them.

“Old Master.”

A quiet voice.

The call was thick with the pain of failing to stop so many deaths, and the fury born from it. Jeok Cheongang suddenly spoke.

“Do as you’ve decided.”

The Three Elders of Tianshan didn’t know.

They didn’t know those few, cryptic words were the trust and encouragement of a master to his Disciple, who was willing to risk his life.

Nor did they know that the brief exchange had sealed their fate.

Whoosh!

A sharp gust of wind swept through.

A dark-blue flash—impossible to tell whether it was flame, wave, or thunderbolt—distorted space as it came crashing down on them.

It was impossibly fast, and carried tremendous force.

Slash!

The First Elder’s whole body broke out in goose bumps. He had twisted away on instinct, but red blood and horrible pain spread across him.

“Gah!”

The flash flickered, and that was all.

If he hadn’t caught sight of a faint something at the last moment, his ghost would already have been wandering the Nine Springs.

*How—how can this be…!*

The First Elder gritted his teeth, barely holding back the pain and shock. Panic on his face, he clutched his deeply slashed chest and staggered backward.

If he retreated in the face of such speed and power, all that awaited him was death. But fortunately, he had two dependable sworn brothers.

“Elder Brother!”

“No!”

The Second and Third Elders cried out and charged. Each held a saber or sword, and their hands blurred as they swung toward a single target.

Jin Taekyung, who had rushed at them with the ghostlike movement of an assassin.

KWAANG!

One spear against two blades.

The three weapons, carrying several jiazi of internal energy, collided with a terrible roar that shook the surroundings.

The earth flipped. The air burst apart.

Amid a storm of power more violently turbulent than anything they’d ever felt, the two old men saw it clearly.

Jin Taekyung’s eyes, cold flames pouring from them—and his hand, gripping the spear shaft firmly without the slightest tremor, even against two Supreme Peak masters.

And he was holding the spear with only one hand.

“Wa—!”

Before they had the chance—or the time—to get out the two words *watch out*, Jin Taekyung struck the Third Elder in the chest with a palm.

*Ah.*

As his vision blurred, the Third Elder felt a horrible heat smash through his flesh and bones and burrow deep inside him.

Crack.

The sharp sound of breaking came late, seeming to echo from far away. Blood welled up in his mouth. As he crumpled, a familiar shout rang in his ears.

“You bastard!”

“Little Brother!”

No mistake. His elder brothers.

No matter how much the world had called them fiends and bastards, they had cherished him like brothers born of the same mother.

His teeth clacked.

The Third Elder bit his tongue hard and forced his collapsing body upright.

He couldn’t fall here. He hadn’t lived all this time to meet such an empty end.

Besides…

*We have the Demon Lord. We have his power.*

The Third Elder was certain.

By now, the Blood-Sword Demon Lord must have stepped in.

His mind was hazy, and he couldn’t see clearly, but with a single command from the Demon Lord, he could escape this terrible internal injury and pain.

But—

But why?

*Why can’t I feel anything?*

Even with his vision blurred, his senses as a Supreme Peak master remained. Yet as the Third Elder staggered and steadied himself, his Qi Sense told him everything was just as it had been.

Even as his two sworn brothers fought Jin Taekyung with all their might, the Blood-Sword Demon Lord’s presence remained a dozen or so yards away.

“Demon Lord! Demon Lord!”

Crash! Boom!

The roar erupting from the spearhead swallowed the Third Elder’s anguished cry. But the Blood-Sword Demon Lord couldn’t have failed to hear him.

And still, nothing changed.

No—that wasn’t quite true. Something did change.

Compared with the immense energies surging all around them, it was tiny—so tiny it crept in all the more stealthily.

Whoosh—thunk!

“……!”

The Third Elder’s body suddenly locked up.

He realized there was a cold blade through his back, with Saber Force gathered at its tip. He spun around in a flash and swung his arm.

Whoom—boom!

Compressed air exploded, but struck nothing.

As the Third Elder stared dumbly at the empty air he’d struck, someone’s form slowly came into focus.

Black clothes as dark as night, and calm eyes.

The young man looked barely thirty, yet his voice was astonishingly low and composed.

“You should always have watched your back. When you leave an opening like that, I can hardly just stand by.”

“You…!”

Crack.

The Third Elder bit down so hard his lips bled.

It wasn’t the Fire King, Jeok Cheongang. It wasn’t the Blazing Flame Divine Dragon, Jin Taekyung.

From the beginning until now, the young brat he’d paid no attention to had driven a dagger into his back—one he’d somehow kept hidden.

And he’d done it in a single surprise attack.

“And you still call yourself a man of the orthodox faction!”

At the Third Elder’s hollow shout, Sama Pyo shrugged.

“It’s all right. I’m from the unorthodox faction.”

“……!”

“And there’s one more thing I should tell you.”

Sama Pyo paused, then casually flicked his hand.

At the same time, another flash gleamed from the ample sleeve of his martial robe.

“I brought plenty of daggers.”

Whoosh!

A sharp whistle rang out, drowning out the quiet words that followed.

Watching the streak of light shoot straight toward him, the Third Elder couldn’t help sneering inwardly.

At least, until he realized he couldn’t move because of the terrible internal injury Jin Taekyung had dealt him, and the dagger just driven into his back.

*What is this…!*

Thwack!

The dagger pierced the center of his forehead. The Third Elder felt the world grow dark.

As his final memory, he heard Jeok Cheongang’s words, spoken as he watched it all.

“That’s one. No, two.”

The Third Elder, whose breath had already stopped, didn’t see it.

At the very moment his final breath left his body, the spearhead of White Flame, cloaked in dark-blue Force, sliced through the Second Elder’s throat.

Slash!

Beneath the fountain of blood, the First Elder’s eyes widened in horror as his body trembled.
```
