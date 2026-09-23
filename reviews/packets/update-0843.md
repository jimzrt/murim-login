<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0843.txt",
      "sha256": "fe17f595b653339d1fa66a0b569b57b98cd0364847ae63f91f80a67ecf16680d",
      "bytes": 12675
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c4a4e47cf9ca83562e5dd8c3b562bbcdd7c2916968ad41db405a22013434bb1b",
      "bytes": 2743
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ac235886e36b4a9cfac67990c4e303d5cbbbaacdc20104970ce04b7ba9ca08c",
      "bytes": 227427
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8c0d3f1c0e205b436b7353f65362b079a2d2bf8ade0eb1b754d477457f3c40cb",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "6b3dd74017e0e5c0138695de2126c3e33f9b634d1aa73300eba1d7f438a416c2",
      "bytes": 866
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b7f91bc7e82da3d4350707974ac18c32d9338936bb18e687b6e237cf35ea5be0",
      "bytes": 1599
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c6dbecb8c7ce677d94440317ae059f6499e99d917009aff3b2b0a654ef759588",
      "bytes": 1888
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "91c9ca5a2f7de09d08fea0981126f15de116caee63978a27dc51567c4b7783ec",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "e81285be6b3e4f6dbc2013afe401d0e53862e9db73ae7f4da0ce444986e3d9f6",
      "bytes": 1384
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "2e1f52bc03269280bd1ab38596df7296dd1da99f129b41da0fd2f4ed9fb800ba",
      "bytes": 752
    },
    {
      "path": "characters/Michael.md",
      "sha256": "0179bc7a453d0773c5a13c26cd52ba9426dc9030eaf77af259cdbe6d300157ea",
      "bytes": 820
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fd4790bf594f3f982af466f12b95b581c707ae942c0105f2f4d7be2cafb615a6",
      "bytes": 252065
    }
  ],
  "estimated_tokens": 12054
}
-->

# Durable State Update — Chapter 843

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
1 and safe_through 843. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 843. Profile updates may replace only one
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
  "chapter": 843,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 843,
    "continuity_sources": [843],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision of a black-haired man killing Ahomed after the ritual; whether it was real is unknown, and Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jin is at the Sichuan Tang Clan after returning from another world; he and Jeok Cheongang have been talking for two days.",
    "The Divine Physician is preparing a pill for Jin’s recovery.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to treat patients and guard against another attack.",
    "Tang Sadok is Family Head of the Sichuan Tang Clan and considers Jin and Cheongpung benefactors.",
    "Ju Wongong remains temporarily appointed acting City Lord of Sichuan Province by imperial order while under exile.",
    "Jeok and Jin have never formalized their Master-Disciple bond; Jeok suggests they may do so when the time comes and everything is set right."
  ],
  "continuity_sources": [
    841,
    842
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What did Jeok mean by the time when everything returns to its proper place?"
  ],
  "safe_through": 842,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "Render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 이정룡    | **Lee Jungryong** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 법왕     | **Dharma King**               | Hong Dao       |
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무인     | **martial artist**                               | Default term                                          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 마교     | **Demonic Cult**                                 |                                                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 도산검림 | **a mountain of sabers and a forest of swords** | Idiom describing the lethal life of martial artists. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 적천강 | 법왕 | close deceased friend and peer | you | familiar and reflective | Jeok addresses the Dharma King in private thought while wishing he were present to clarify Jeok's confusion. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 842
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 833
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger was a Demon Realm being capable of regenerating in new bodies and was erased by Jin Taekyung.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It claims to have served Demon King Asmodeus as its master and acted on his order, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 842
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan, though they have never formalized their bond; Jeok hints they may do so when the time comes. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 842
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, Jin-ho is his older friend and trusted confidant, and he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 842
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 795
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 835
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 832
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃843화



적천강은 무림(武林)이라는 드넓은 모래밭에 자신만의 족적을 새긴 거인이다.

스스로는 인정하지 않을 수도 있지만, 무림에 한 걸음이라도 걸친 이들이라면 모두가 그렇게 생각했다.

그는 화왕(火王)이라 불리는 위대한 무인이었고, 장장 일백여 년이 넘는 아득한 세월 동안 숱한 전란과 위기 속에서 살아남은 생존자였으니까.

강자가 경외의 대상이라면, 노장(老將)은 존경의 대상이다.

그리고 화왕 적천강은 이 두 가지 조건을 충족할 수 있는 몇 안 되는 인물이었다.

이 광활한 천하에서 최소 열 손가락 안에 들어가는 무위. 거기에 더해 끝을 짐작할 수 없을 만큼 깊은 연륜과 견문.

하지만 그런 적천강조차 자신이 백 년도 넘게 살아온 이 세상에 대한 모든 것을 알지는 못했다.

하물며 ‘이 세상’이 아닌 다른 세상의 일이라면 더더욱.

“좆 됐군.”

제법 긴 침묵 끝에 토해 낸 한 마디와 함께, 적천강은 확신했다.

자신이 들은 이야기가 모두 사실이라면 이보다 더 적절한 표현은 없을 것이라고.

그리고 그런 적천강을 향해, 마주 앉은 청년은 고개를 끄덕여 주었다.

“예, 노야께서 하신 말씀이 정확해요.”

청년, 진태경은 쓰게 입맛을 다셨다.

좆 됐다. 그 말밖에는 딱히 다른 표현이 떠오르지 않을 만큼 현대의 상황은 심각했다.

쉴 새 없이 잇따라 터진 사건 사고들.

지금 돌이켜 생각해 보면 이정룡은 선녀다. 무려 삼십여 년에 걸친 미카엘 실베르트와 도플갱어의 합작으로 전 세계가 개판 오 분 전에 접어들었으니까.

아니, 이미 본격적인 개판이 시작되었다고 봐도 무방했다.

“그러니까 그, 뭐라고 했지?”

“몬스터요.”

“그래, 모수타. 그 마교 같은 놈들이 본격적으로 네 녀석이 사는 선계(仙界)로 쳐들어온다는 말이렷다.”

“예. 삼십여 년에 그랬던 것처럼요.”

적천강이 이런 이야기를 들은 것은 처음이 아니었다.

남만야수궁을 떠난 직후 한 번. 그리고 이틀 전부터 지금까지 또 한 번.

그러나 진태경이 처음보다 훨씬 더 상세한 설명을 곁들였음에도, 적천강은 자신이 들은 내용을 쉽사리 이해할 수 없었다.

설령 스무 번을 더 듣는다고 해도 마찬가지일 터였다.

‘어찌 그런 곳이 존재할 수 있단 말인가?’

수십, 수백 년을 걷고 또 걸어도 닿을 수 없는 머나먼 세상.

산을 넘고, 바다를 건너도 보지 못할 미지의 땅.

그뿐인가.

수만 리 밖에서도 서로의 얼굴을 마주한 채 대화할 수 있고, 강철로 된 거대한 새가 구름 위를 넘나든다 했다.

일평생 동안 도산검림(刀山劍林)만을 거닐었던 적천강의 입장에서는, 한 마디 한 마디를 들을 때마다 놀라움과 불신이 동시에 찾아오는 것은 당연했다.

만약 그 말을 한 것이 다른 누군가였다면, 진작 귀싸대기를 갈기고 화염신장으로 지져 버렸을 것이다.

설령 그것이 무신(武神)이나 천자(天子)라 해도.

하지만…….

‘저 녀석이 하는 말이니, 믿어야지.’

믿는다. 진태경을.

그것은 적천강에게 있어 너무나도 당연한 일이 되어 버렸다. 노인을 청년을, 청년은 노인을 믿는다.

어느 날부터인지는 모르겠지만, 그들은 그런 관계가 되어 있었다.

그 어떤 헛소리를 지껄여도 사실로 받아들일 수 있을 만큼.

“법왕(法王), 그 땡중이 살아서 이 자리에 있었다면 기절초풍했겠군. 허구한 날 하늘의 별이나 쳐다보던 놈이 이런 것까지 짐작이야 했겠느냐.”

적천강은 이미 먼 곳으로 떠난 벗을 생각하며 진태경을 바라보았다.

“들으면 들을수록 알 수 없는 세상이로구나. 그러나 한편으로는 이곳과 퍽 닮아 있어. 그렇게 생각하지 않느냐?”

진태경이 고개를 끄덕였다.

처음에는 주위를 둘러싼 모든 것이 마냥 낯설고 다르게 느껴졌지만, 이제는 아니다.

현대와 무림. 무림과 현대.

두 세계는 서로 놀랍도록 닮아 있었다. 문명의 격차가 아닌, 세상을 움직이는 변화의 흐름이.

“무림에 암천이 있다면, 제가 살아온 세상에는 몬스터가 있습니다. 그리고 두 곳 모두 좋지 않은 방향으로 흘러가고 있고요.”

“그리 멀지 않은 과거에, 각자의 세상에서 정마대전(正魔大戰)이 일어났다는 점도 같지.”

“맞습니다.”

“그렇다면 네 녀석은…….”

문득 말꼬리를 흐린 적천강이 무겁게 말을 이었다.

“이 모든 상황이, 단순한 우연이라고 생각하느냐?”

짧은 침묵이 내려앉은 그 순간.

어둠 속에서 흔들리는 호롱불을 바라보던 진태경의 눈동자가 불그스름하게 달아올랐다.



* * *



별들도 잠든 늦은 밤.

적천강을 뒤로하고 전각을 빠져나온 나는 홀로 내원(內院)을 거닐었다.

정해지지 않은 목적지 대신, 조금 전 들었던 물음을 마음에 품은 채.



‘이 모든 상황이, 단순한 우연이라고 생각하느냐?’



만약 적천강이 좀 더 자세하게 무언가를 물었다면, 나는 답하기를 주저했을 것이다.

나조차도 아직 모르는 것투성이니까. 두 세상에는 아직 무수히 많은 비밀이 감추어져 있으니까.

그러나 적어도 저 물음에서만큼은, 나도 확신할 수 있었다.



‘전혀요.’



우연이 아니다.

그것이 바로 내가 짧은 침묵 끝에 내놓은 대답이었고, 이를 확신하기까지는 아주 오랜 시간이 걸렸다.

처음 무림에서 눈을 뜬 순간부터 지금까지. 나는 줄곧 그것에 대해 생각해 왔으니까.

그리고 기나긴 고민 끝에 도달한 결론은 하나였다.

‘연관성이 있다. 확실한 연관성이.’

처음에는 나를 둘러싼 모든 것이 엄청난 불운처럼 느껴졌다.

빌어먹을 고물 캡슐에서 잠들었을 뿐인데, 게임인지 현실인지 분간도 되지 않는 세상에서 온갖 위험과 맞서 싸워야 했으니.

그러나 주위를 둘러싼 환경이 바뀌면서 생각도 변화했다.

나는 하루아침에 직장을 잃은 F급 헌터에서 유명인사가 되었고, 과거에는 상상할 수도 없던 힘과 부를 양손에 움켜쥐었다.

그것도 현대와 무림. 두 세상에서 동시에.

‘불운이 행운으로 변한 거지.’

재수가 없어도 이렇게 없을 수 있냐며 한탄하던 시절은 금세 스쳐 지나갔다.

불운이라고 생각했던 그것은 알고 보니 하늘에서 내려 준 행운이었고, 어쩌면 그 이상인 천운(天運)이라고도 볼 수 있었다.

어느 날부터 알 수 없는 기시감을 느끼기 전까지는.

‘산서성에서부터 하남. 사천을 넘어 호북까지.’

암천(暗天)이라는 먹구름 아래, 피를 머금은 불길이 솟구쳤다.

가슴 한구석에 복수심을 간직하고 있던 태원진가의 대장로가 긴 세월 동안 숨겨 두었던 검을 뽑았고, 놀라운 무위와 지혜로 존경받던 고승은 죽음을 맞이했으며, 소림사를 휩쓴 불길은 사천과 호북으로까지 번졌다.

‘그리고 마침내 저 머나먼 남만에 닿았다.’

그나마 다행이었던 점은, 사방으로 번진 불길이 모든 것을 잿더미로 만들지는 못했다는 것이다.

비록 수많은 이들이 희생당했으나 그보다 더 많은 이들이 불길을 피할 수 있었고, 나는 그 끔찍한 재앙이 휩쓸고 지나간 자리에 남아 있는 여러 흔적을 발견할 수 있었다.

이성을 상실하고 미쳐 버린 수신룡.

마치 몬스터처럼 괴이한 모습으로 변해 버린 어부와 물고기들.

단순한 사술이나 진법이라고 받아들이기에는 현대의 텔레포트 마법과 너무나도 닮아 있는 암천의 이동진(移動陳).

그리고 마지막으로…….

‘남만에서 발생한 균열.’

지금도 똑똑히 기억난다. 아니, 잊을 수조차 없다.

살아있는 생물처럼 꿈틀거리던 그 어둠을, 무림인들이 마기(魔氣)라 칭하는 그것에서 몇 번이고 느꼈던 익숙함을.

‘마력이었어, 분명히.’

처음에는 그 사실을 받아들이지 못했다.

있어서도 안 되고, 있을 수도 없는 일이니까.

하지만 시간이 흐르며 서서히 드러나기 시작한 선명한 윤곽은, 내게 현실을 받아들이라 종용하고 있었다.

‘단순히 명칭의 차이가 아니야.’

마나와 공력의 본질은 완벽하게 같다. 바로 기(氣)다.

어디에도 있으며 동시에 어디에도 없는 것.

푸른 바다와 산림에도, 매연 가득한 빌딩 숲에도 존재하지만 대부분의 이들이 느끼지 못하는 무형의 것.

그러나 마력은 다르다.

죽음을 품은 그 악한 기운은 또 다른 세상에서 흘러들어온 것이다.

마나와 공력이 본래에도 존재했던 원주민이라면, 마력은 몬스터와 함께 저 너머에서 건너온 낯선 이방인이자 침략자였다.

한데 바로 그 마력이 등장했다.

현대도 아닌 바로 이곳, 무림에서.

‘이걸 어떻게 받아들여야 하나.’

허.

이 말도 안 되는 상황에 헛웃음이 흘러나왔다.

어떻게 받아들이긴, 어차피 애써 부정하고 싶어도 더는 외면할 수 없는 현실이다. 나는 이미 답을 알고 있다.

‘암천(暗天).’

틀림없다.

현대와 무림을 잇는 진짜 연결고리는 암천뿐이다.

지금껏 놈들과 얽히기 시작하면서 직접 목격한 모든 것들이 증거였고, 검사인 동시에 판사였다.

‘하지만, 어떻게?’

도대체 어떻게 이 세상에, 무림에 발을 디뎠을까.

정마대전(正魔大戰)이라는 큰 사건이 있었다고는 하지만, 그 역시 결국 천하 무림의 패권을 둘러싼 하나의 전란에 불과했다.

만약 대격변과 같은 일이 벌어졌다면 내가, 아니 적어도 그 시절을 온몸으로 헤쳐 나왔던 적천강이나 다른 이들이 모를 리 없었다.

온갖 흉측한 괴물들이 천하를 휩쓸었다는 소문은 궁벽한 촌구석에까지 퍼질 테니까.

‘하지만 지금까지 알려진 건 암천이 마교의 후신(後身)이고, 기이한 사술을 쓴다는 것 정도밖에 없지.’

그리고 이 사실이 의미하는 바는 명백했다.

‘존재해서는 안 될 무언가가 무림에 나타났다. 정마대전이라는 혼란의 시기가 이어지던 도중. 혹은 그 직후에.’

그렇다면 시기가 정확히 맞물린다. 암천이 처음 대장로에게 접근했을 때가 바로 그 무렵이었으니.

하지만 아직 근본적인 원인이자, 해결되지 않은 가장 큰 의문이 남아 있었다.

‘천주(天主).’

암천의 주인.

아니, 그들이 모시는 신이라 해도 과언이 아닌 절대자.

놈이 어떻게 무림에 존재할 수 있는지는 그리 궁금하지 않다. 삼십여 년 전 일어난 대격변의 시작 역시 그러했으니까.

문제는…….

‘천주의 진짜 정체.’

저벅.

문득 걸음을 멈췄다.

세상을 둘러싼 어둠은 깊고 내원 곳곳에 세워진 횃불은 붉게 타오른다.

그 불꽃을 멍하니 바라보며 생각에 잠겨 있던 나는, 불현듯 정수리를 관통하는 듯한 충격을 느꼈다.

“설마……?”

나도 모르게 신음처럼 흘러나온 목소리가 어둠에 섞여 흩어진 그때.

스륵.

일렁이는 횃불이 만들어 낸 그림자가 내 발끝에 닿았다.

마치 더는 존재하지 않는 어느 저주받은 존재처럼. 영원한 소멸을 맞이하면서도 웃었던 누군가처럼.

그리고 그와 동시에, 수많은 기억 속에 잠겨 있던 대화가 환청처럼 귓가에 울려 퍼졌다.



‘위대한 왕께서는 신의 저주를 극복하신 분. 흔들리되 꺾이지 않으며, 스러져도 일어나실 것이다. 그리하여 마침내 이 세상 모든 흙과 물을 당신의 것으로 만들 것이다.’

‘뭐?’

‘그것만이 진실이다. 알면서도 막을 수 없는, 머지않은 미래에 현실이 될 진실.’



“……!”

나는 석상처럼 굳어 버렸다. 도플갱어와 마주했던 그때 그 순간으로 되돌아간 것처럼.
```

## Final English reading copy

```markdown
# Chapter 843

Jeok Cheongang was a giant who had left his own footprints in the vast sandpit that was Murim.

He might not admit it himself, but everyone who had ever set foot in Murim thought so.

He was a great martial artist known as the Fire King, and a survivor who had lived through countless wars and crises over the course of more than a hundred years.

If the strong were objects of awe, then the old masters were objects of respect.

And Jeok Cheongang, the Fire King, was one of the few people who met both conditions.

His martial prowess placed him among the top ten in all the vast world. On top of that, his experience and knowledge ran deeper than anyone could guess.

But even Jeok Cheongang didn’t know everything about the world he’d lived in for more than a hundred years.

Much less about a world that wasn’t *this* one.

“We’re fucked.”

After a fairly long silence, Jeok Cheongang spat out those words and became certain.

If everything he’d heard was true, there couldn’t be a more fitting way to put it.

The young man sitting across from him nodded.

“Yes. You’ve got it exactly right, Old Master.”

The young man, Jin Taekyung, clicked his tongue bitterly.

*We’re fucked.* There was no other way to describe how bad things were in the modern world.

One disaster after another had erupted without pause.

Looking back now, Lee Jungryong seemed like a fairy. Michael Silbert and the Doppelganger had spent more than thirty years working together to bring the whole world to the brink of chaos.

No—the chaos had already well and truly begun.

“So, what was it called?”

“Monsters.”

“Right. Mosu-tuh. Those Demonic Cult-like bastards are finally coming in force to the realm of immortals where you live, is that it?”

“Yes. Just like they did thirty years ago.”

This wasn’t the first time Jeok Cheongang had heard this story.

Once, right after they left the Nanman Beast Palace. And again, from two days ago until now.

But even though Jin Taekyung’s explanation was far more detailed this time, Jeok Cheongang still couldn’t easily understand what he’d heard.

He wouldn’t have understood even if he heard it another twenty times.

*How could such a place exist?*

A distant world no one could reach, no matter how many decades or centuries they walked.

An unknown land they’d never see, even after crossing mountains and seas.

And that wasn’t all.

They could speak face-to-face with one another from tens of thousands of li away, and enormous birds made of steel soared above the clouds.

For Jeok Cheongang, whose entire life had been spent walking through a mountain of sabers and a forest of swords, it was only natural that each sentence brought both amazement and disbelief.

If anyone else had told him all this, he’d have slapped them across the face and burned them to a crisp with Flame Divine Palm.

Even if it had been the Martial God or the Son of Heaven.

But…

*Since that brat’s the one telling me, I have to believe him.*

Believe him. Jin Taekyung.

For Jeok Cheongang, it had become only natural. The old man trusted the young man, and the young man trusted the old man.

He didn’t know when it had started, but that was what their relationship had become.

They trusted each other enough to take even the most unbelievable nonsense as fact.

“If Dharma King—that bald monk—were alive and here with us, he’d have fainted dead away. That fool spent all his time staring up at the stars. Do you think he could’ve ever imagined something like this?”

Jeok Cheongang looked at Jin Taekyung, thinking of the friend who had already gone far away.

“The more I hear, the less I understand this world. And yet, in a way, it’s a lot like this one. Don’t you think?”

Jin Taekyung nodded.

At first, everything around him had felt unfamiliar and different. But not anymore.

The modern world and Murim. Murim and the modern world.

The two worlds were astonishingly alike—not in their civilizations, but in the currents of change driving them.

“If Murim has Dark Heaven, then the world I lived in has monsters. And both are headed in a bad direction.”

“Not so long ago, the Great Faction War broke out in each of our worlds, too.”

“That’s right.”

“Then you…”

Jeok Cheongang trailed off, then continued in a grave voice.

“Do you think all of this is just coincidence?”

A short silence fell.

As Jin Taekyung gazed at the oil lamp flickering in the darkness, his eyes began to glow red.

* * *

Late at night, when even the stars had fallen asleep.

Leaving Jeok Cheongang behind, I stepped out of the pavilion and walked alone through the Inner Court.

Instead of heading for any particular destination, I carried the question I’d just heard in my mind.

*Do you think all of this is just coincidence?*

If Jeok Cheongang had asked me something more specific, I would’ve hesitated to answer.

There was so much even I still didn’t know. So many secrets remained hidden in both worlds.

But at least when it came to that question, I was certain.

*Not at all.*

It wasn’t a coincidence.

That was the answer I’d given after a short silence, and it had taken me a very long time to become certain of it.

From the moment I first opened my eyes in Murim until now, I’d kept thinking about it.

And after a long, long time spent wondering, I’d reached one conclusion.

*There’s a connection. A definite connection.*

At first, everything around me had felt like a tremendous run of bad luck.

All because I’d fallen asleep in a damn old capsule. I’d had to fight one danger after another in a world where I couldn’t even tell whether it was a game or reality.

But as my surroundings changed, so did my thoughts.

I’d gone from an F-rank Hunter who lost his job overnight to a celebrity, gripping power and wealth in both hands that I never could’ve imagined before.

And that, in both worlds—the modern one and Murim.

*My bad luck turned into good luck.*

The days when I’d lamented, *How can I be this unlucky?* quickly faded into the past.

What I’d thought was bad luck turned out to be good fortune sent down from the heavens. Maybe it was even more than that—a stroke of heavenly fortune.

That is, until I began to feel a strange sense of déjà vu.

*From Shanxi Province to Henan. Across Sichuan and all the way to Hubei.*

Beneath the dark clouds of Dark Heaven, flames soaked in blood had surged upward.

The Head Elder of the Jin Family of Taiyuan, who had harbored a grudge in a corner of his heart, drew the sword he’d hidden for so many years. A revered monk, praised for his astonishing martial prowess and wisdom, met his death. And the flames that swept across Shaolin Temple spread as far as Sichuan and Hubei.

*And finally, they reached distant Nanman.*

The one saving grace was that the flames spreading in every direction hadn’t turned everything to ash.

Though countless people had died, even more had escaped the fire. And I’d found many traces left behind where that terrible disaster had swept through.

The Water God Dragon, driven insane and stripped of reason.

The fishermen and fish, transformed into grotesque creatures that looked like monsters.

Dark Heaven’s Moving Formation, so much like modern Teleport Magic that it couldn’t simply be dismissed as dark arts or a formation.

And finally…

*The rift that opened in Nanman.*

I still remembered it vividly. No—I couldn’t forget it, even if I tried.

That darkness, writhing like a living creature. The familiarity I’d felt time and again in what the martial artists called demonic qi.

*It was magical power. It had to be.*

At first, I couldn’t accept it.

It shouldn’t exist. It couldn’t exist.

But as time passed, its clear outline began to emerge, urging me to accept reality.

*This isn’t just a difference in terminology.*

Mana and internal energy were identical in their essence. They were both qi.

Something that existed everywhere and nowhere at once.

In the blue sea and the forests, in the smog-filled canyons of skyscrapers—an intangible force that most people couldn’t sense.

But magical power was different.

That evil energy, steeped in death, had flowed in from another world.

If mana and internal energy belonged to the natives, things that had always existed, then magical power was a foreign invader that had crossed over from beyond, along with the monsters.

And that very magical power had appeared.

Not in the modern world, but right here—in Murim.

*How am I supposed to make sense of this?*

Heh.

A hollow laugh escaped me at the absurdity of it all.

How was I supposed to make sense of it? It was reality, and I could no longer turn away from it, even if I wanted to. I already knew the answer.

*Dark Heaven.*

There was no doubt.

Dark Heaven was the true link connecting the modern world and Murim.

Everything I’d personally witnessed since becoming entangled with them was evidence—and served as both prosecutor and judge.

*But how?*

How on earth had they set foot in this world—in Murim?

The Great Faction War had been a major event, but in the end, it was just another war over supremacy in Murim.

If something like the Great Cataclysm had happened, I—or at the very least, Jeok Cheongang and the others who’d lived through that time—would have known.

Rumors that all sorts of hideous monsters had swept across the land would’ve reached even the most remote villages.

*But so far, all anyone knows is that Dark Heaven is the successor to the Demonic Cult and uses strange dark arts.*

And the meaning of that was clear.

*Something that shouldn’t exist appeared in Murim. During the chaos of the Great Faction War, or shortly after it ended.*

If so, the timing lined up exactly. That was when Dark Heaven first approached the Head Elder.

But one fundamental cause remained unknown. The biggest question had yet to be answered.

*The Lord of Heaven.*

The master of Dark Heaven.

No, a being beyond compare, no less than the god they worshiped.

How he could exist in Murim wasn’t what puzzled me. The Great Cataclysm thirty-odd years ago had begun much the same way.

The problem was…

*The Lord of Heaven’s true identity.*

Step.

I suddenly stopped walking.

Darkness shrouded the world, while torches set throughout the Inner Court burned red.

As I stared blankly into their flames, lost in thought, I suddenly felt a shock as if something had pierced through the top of my head.

“Could it be…?”

My voice slipped out like a groan and scattered into the darkness.

Just then—

Swish.

The shadow cast by a wavering torch touched the tips of my feet.

Like someone who had once been a cursed being, someone who no longer existed.

Like someone who had smiled even as he met his eternal Erasure.

And at the same time, a conversation buried in the depths of my memories rang in my ears like an illusion.

*The great king is one who overcame a god’s curse. He may waver, but he will not break; even if he falls, he will rise again. And at last, he will claim all the earth and water in this world as his own.*

*What?*

*That alone is the truth. A truth that cannot be stopped, even when known—a truth that will become reality in the not-too-distant future.*

“……!”

I froze like a statue, as though I’d been transported back to that moment when I’d faced the Doppelganger.
```
