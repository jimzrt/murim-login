<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0796.txt",
      "sha256": "51eba766901edc691cd26e4f084159b0f48ce7bc75ffedea4206d609363cd986",
      "bytes": 13654
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "85d861bbba755fd306578754f0275f2ae5255954e8862509e73e85ab67b7f95d",
      "bytes": 2095
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4cc1c43df04a27376c78096a8513b1b8a19e0bca0db85016f56c056d7a15960f",
      "bytes": 224088
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "118bcefaebb8d83567691d53694758155a3f2de1f7e5941d8a80d4d0f6dc405e",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "387fe1fadacf5d674b97e36826846c0cfbe369de7698f37f91338e86ab3b99f2",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a651e605ffacb8896655a0b0feebad5ef8cca38951b9230a263c182d4e0cb457",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e035afbbc692332616b6b82f489775399f26b300a113fce33e31fb3b1b2fcb4a",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "e021fa26e239bc0f374f9e5bc39720e86167a552d30ff5063c075e6965a39458",
      "bytes": 666
    },
    {
      "path": "characters/Michael.md",
      "sha256": "4d439a8e6b3c7c5e88fb42bee4afe458eca13caf89be5714e1f691d4ab9d9745",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "321dcb2d4c2c9ddc6f4b31116954b6bf596d0c40922239c7143a1cfc7ca58661",
      "bytes": 704
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "c74da271293b0b18b1246800deca6f115aacf85b41a3f6b866fddea71ad6e938",
      "bytes": 405
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "50bf01a06a4c17b233b64742faa656a6aa6fc183edb6e81ea863a7c7120f45b2",
      "bytes": 246216
    }
  ],
  "estimated_tokens": 11492
}
-->

# Durable State Update — Chapter 796

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 796. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 796. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 796,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 796,
    "continuity_sources": [796],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and is pursuing the Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Supreme Peak Quest [An Unknown Death] is complete; it confirmed The Prophet killed Siegfried Wassmann, and Jin received the special Item Eyes of Truth.",
    "The Prophet is the fifth person to bear the identity Muninn. Huginn saw him once about three years ago and recalls a mostly concealed white man whose build seemed unsuited to close combat; that assessment is uncertain.",
    "The Muninn from about three years ago supplied Michael Silbert with information about Cheon Taemin, Leviathan, and Magic Gems, including the plan to lure Leviathan to Tokyo.",
    "Jin believes the Muninns secretly moved unrefined Magic Gems from the Middle East and Africa, eliminated rivals, and gathered intelligence. He has ordered the search teams recalled and the leadership team to the strategy room.",
    "Huginn remains captive and is unconscious in the torturers’ custody after Jin ordered further questioning.",
    "The Skeleton King and his undead army remain with Xiao Shen after defeating the desert Monster Wave without casualties.",
    "Twenty people were found dead in the desert in the same desiccated condition as Siegfried Wassmann; the cause remains unknown."
  ],
  "continuity_sources": [
    794,
    795
  ],
  "open_questions": [
    "Who is the current Prophet, and where is he?",
    "How did the Muninns discover Leviathan’s presence in the deep sea?",
    "What caused the deaths of Siegfried Wassmann and the twenty people in the desert?",
    "What disappeared from the desert without leaving a trace, as described by the Skeleton King?",
    "Can Jin find and eliminate The Prophet before the Main Quest’s time limit expires?"
  ],
  "safe_through": 795,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Do not identify the current Prophet or infer the uncertain thought Jin suppresses."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 철수     | **Cheol Soo**      |
| 천태민    | **Cheon Taemin**  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무인     | **martial artist**                               | Default term                                          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 대통령 | **President** | Title for Korea's head of state. |
| 고이즈미 | **Koizumi** | Japanese prime minister quoted in the news. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 조셉 | **Joseph** | Hunter named in the recorded Monster Wave footage. |
| 바이든 | **Biden** | Surname of former U.S. President Joseph Biden. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 도쿄 | **Tokyo** | City visible behind Huginn's departing ship. |
| 도쿄만 | **Tokyo Bay** | Port area where Sugihara Gyoiku works. |
| 스사노오 | **Susanoo** | Japanese nickname for the sea-and-storm monster. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 베이징 | **Beijing** | Chinese city targeted by the earlier terrorist attack. |
| 방위대신 | **Defense Minister** | Japanese Defense Minister who controlled the operation's field deployment. |
| 한국 | **Korea** | Destination of the international Hunters and Guild Masters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 방위대신 | 진태경 | Japanese Defense Minister to foreign Hunter | Jin Taekyung | insulting-shouting | The Minister calls for Jin using a deliberately mangled and contemptuous pronunciation of his name. |
| 진태경 | 방위대신 | foreign Hunter confronting the Japanese Defense Minister | old man | insulting-casual | Jin repeatedly blames the Defense Minister for withholding forces and sarcastically challenges him. |
| 고이즈미 | 진태경 | Japanese Prime Minister to allied foreign Hunter | Jinsang | formal and cordial | Koizumi addresses Jin with the retained Korean pun and later uses Mr. Jin Taekyung. |
| 진태경 | 고이즈미 | foreign Hunter to Japanese Prime Minister | Prime Minister | casual, familiar, and coercively playful | Jin asks Koizumi to lend Japan's S-rank Magic Gems and promises to return them. |
| 진태경 | 레비아탄 | enemy and hunted monster | Leviathan; you | insulting-casual | Jin orders Leviathan to leave and dismisses its attempt to kill the Skeleton King. |
| 레비아탄 | 진태경 | attacking enemy | you bastard | enraged-insulting | Leviathan directly curses Jin while resisting his attacks. |
| 기자 | 진태경 | Japanese reporter to celebrated foreign Hunter | Jin-sama | formal and reverent | Japanese reporters repeatedly address Jin with the honorific 사마. |
| 진태경 | 기자 | Hunter to Japanese reporter | reporter; you | blunt and insulting | Jin rebukes a reporter for talking back after criticizing Yamamoto's delayed arrival. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 795
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 793
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 793
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 793
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 795
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 795
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 795
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 767
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter whose delayed arrival during the Leviathan incident became a subject of post-raid media discussion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Not established.

## Korean source

```text
＃796화



그날 밤. 바쁜 걸음을 멈추고 창밖을 바라보던 누군가가 오늘따라 달이 붉다고 느꼈던 것은 결코 착각이 아니었다.

블러드 문(Blood Moon).

이는 개기월식이나 대기 상태가 불안정할 때 종종 보이는 현상이었고, 나날이 치솟는 마력 분포도는 대기 상태는 물론 기후마저 변화시키고 있었다.

쏴아아아.

점점이 떨어지던 빗방울이 거세진다.

연 강수량이 250mm도 되지 않는 척박한 땅과는 어울리지 않는 장대비는 금세 사방을 뒤덮으며 쏟아져 내렸다.

끝없이 펼쳐진 모래와 그 속에 드문드문 서 있는 나무.

그리고, 육안으로는 확인할 수 없는 어느 존재의 머리 위로도.

툭. 투두두둑.

몸 어디에도 닿지 못하고 튕겨 나가는 빗줄기.

보이지 않는 막을 두른 채 넓은 사막을 가로지르던 선지자는 불현듯 하늘을 올려다봤다.

어둡고 요란하다.

며칠 전부터 심상치 않던 먹구름이 험악한 기세로 비와 천둥을 쏟아내고 있었다.

마치 이 땅에서 벌어진 일에 대해 한껏 분노한 것처럼.

하지만 선지자는 아랑곳하지 않고 하늘을 살폈다. 아니, 정확히는 감각을 활짝 열고 사방에서 들려오는 모든 소리에 귀를 기울였다.

구궁, 쿠르르릉.

머리 위로 끊임없이 울려 퍼지는 천둥소리. 잠시 걸음을 멈춘 채 주위의 소리에 집중하던 선지자가 문득 뇌까렸다.

“사라졌다.”

말 그대로였다.

저 멀리에서 메아리처럼 들려오던 독수리들의 날카로운 울음소리가 들리지 않는다.

어느 추격자가 풀어놓았을 끈질긴 날짐승들이 끝끝내 포기하고 돌아간 것이다.

‘성가신 놈들이었는데, 잘됐군.’

위성 감시나 무인 정찰기를 피하는 것 정도는 쉽다.

대기에 뒤섞인 마력은 그 자체로 추적을 차단하는 방패였고, 온갖 은폐 마법은 스튜나 끓여 먹으라고 있는 것이 아니니까.

하지만 그 독수리들은 달랐다. 소수의 정신계 마법사들이 하수인으로 부리는 패밀리어(Familiar)도 그것에 비하면 발톱에 낀 때나 다름없다.

느려지는 기색 하나 없이 무려 수백 킬로미터를 쫓아 왔으니까.

게다가 마력으로 형형하게 빛나는 놈들의 눈동자는, 어쩌면 그의 마법마저 꿰뚫어 볼 것만 같았다.

‘패밀리어 따위는 아닐 테고…… 분명 그놈이겠지.’

스켈레톤 킹. 혹은 스톤 킹.

한낱 몬스터 주제에 인간의 편에 선 존재를 떠올린 선지자는 자신도 모르게 눈살을 찌푸렸다.

여전히 사막은 광활하다. 그러나 놈이 부리는 언데드 군단은 수색 범위를 확장하고, 소요 시간을 획기적으로 단축할 것이다.

‘이건 예상 밖인데.’

사실 예상을 벗어난 건 이미 한둘이 아니다.

미카엘 실베르트가 그렇게 쉽게 쓰러질지도 몰랐고, 세계 헌터 연맹이 이토록 빠르게 혼란스러운 내부를 수습하고 턱밑까지 치고 들어올 줄도 몰랐다.

다만 한 가지. 이 모든 이변이 한 사람으로 비롯되었음은 선지자 역시 알고 있었다.

‘진태경.’

지금껏 환히 빛나는 이들은 많았지만, 그들은 모두 유성(流星)에 불과했다. 아주 잠깐 빛을 발했다가 눈 깜짝할 사이에 사라지는.

그러나 진태경은 다르다. 놈은 혜성(彗星)이다.

처음 등장하던 그 순간부터 세계라는 천체의 일부였고, 이제는 중심이 되어 버렸다.

그 성장 속도가 너무나도 빨라서 누구도 한계를 예측할 수 없을 만큼. 지금까지 해 왔던 모든 준비가 무색하게 느껴질 만큼.

차륵.

무의식적으로 더듬은 손끝을 따라 희미한 금속음이 울려 퍼진다.

마음속에서 치밀어오르는 조급함을 애써 억누른 선지자는 작게 뇌까렸다.

“조금만. 조금만 더 하면 완성할 수 있어.”

문제는 시간이다.

한 치의 오차도 없어야 하는 이 계획을 완벽하게 해 줄 준비물은 아직 전부 모이지 않았고, 적들의 포위망은 빠르게 좁혀 오고 있었다.

그리고 이러한 상황 속에서 선지자에게 남은 방법은 하나밖에 없었다.

‘사냥.’

하지만 시간이 촉박하다. 계획을 성공적으로 완성하기 위해서는 지금보다 더 규모를 키우고, 과감해져야 한다.

이를테면…….

부우우웅.

높은 모래 언덕 위, 자욱한 먼지구름을 일으키며 움직이는 후송 차량들을 확인한 선지자는 눈을 빛냈다.



* * *



“칙쇼.”

일본의 S급 헌터, 야마모토 겐지의 나직한 욕설에 슬쩍 자리를 옮긴 자위대 소속 헌터들은 시선을 교환했다.

헌터 강국이라 불리기에는 상당한 거리가 있는 일본이지만, 중동에 파견된 이들은 모두 베테랑 중의 베테랑. 더군다나 오랫동안 봐 온 얼굴들이니 이제는 눈빛만 봐도 대충 뜻이 통한다.

‘왜 저래?’

‘뻔하지 뭐. 누구 때문이겠어.’

‘에에? 진 사마?’

‘그래, 아까 본대에서 온 통신 때문에 야마모토 상이 잔뜩 화가 났어.’

사건의 전모는 간단했다. 지금으로부터 약 삼십여 분 전, 본대에서 긴급 철수 명령이 떨어졌고 야마모토 겐지는 거부 의사를 표시했다.

그리고 곧장 답신이 왔다.

통신원의 딱딱한 목소리 대신, 한 청년의 생생한 목소리로.



‘레비아탄이 도쿄만 박살 낼 때는 오라고 해도 안 오더니 개새끼가. 뭐? 안 와? 당장 거기 좌표 불러. 네가 안 오면 내가 간다.’



진태경이 누군가.

의식불명이 된 천태민의 빈자리를 채울 수 있는 유일한 인물이자, 전 인류의 지지를 한 몸에 받는 세계 헌터 연맹의 맹주다.

하지만 그 전에 잊지 말아야 할 것은 가끔, 아니 꽤 자주 보여 주는 앞뒤 가리지 않는 성질머리와 그 무시무시한 실력.

예고 살인이나 다름없는 최고 존엄의 답신에 오금이 저린 자위대 헌터들은 필사적으로 만류했고, 야마모토 겐지는 후송 차량에 탑승한 뒤에도 줄곧 분을 삭이지 못하고 있었다.

“코노야로. 감히 조센징 따위가……!”

자위대 헌터들은 못 들은 척했다. 이 순간만큼은 모두가 장님이고 귀머거리여야 한다.

솔직히 그들도 야마모토 겐지의 태도가 썩 마음에 들지는 않았지만, 이런 태도가 상부에 알려지면 자신들뿐만 아니라 일본까지 싸잡혀서 욕을 먹는다.

‘여기서 더?’

‘안 돼. 절대 안 돼.’

이미 레비아탄 사태 당시 카미카제 작전까지 준비하며 활약했던 방위대신은 미카엘 실베르트와의 커넥션이 발각되어 연방 감옥에 갇힌 상태고, 착하지만 멍청한 총리는 그 며칠 새를 못 참고 또 입으로 똥을 싸질러 놨다.



[日 고이즈미 총리, “야마토 민족이여, 우리를 위해 스사노오를 쓰러트린 위대한 쇼군, 진 사마를 위해 싸워라!”]

[日 고이즈미 총리, 곧 중동에 파견될 자위대 전략을 묻는 기자의 질문에 “전투는 fun하고 cool하고 sexy해야 한다.”]

[美 전 대통령 조셉 바이든, “일본 총리를 이해한다. 나 역시 치매 초기에 내가 무슨 말을 하는지 몰랐다.”]

[척 헤이글, “그냥 둘 다 미친 것 같다.”]



자위대 헌터들은 자신들이 처지가 서글펐다.

방위대신은 연방 감옥에서 노후를 보내게 되었고, 총리는 언론이라는 확성기에 대고 일본의 국가 지도자가 미친놈이라는 사실을 가감 없이 밝히고 있다.

오죽하면 좋지 않은 분위기를 읽고 발언을 자제하던 한국 네티즌들이 이렇게 말했겠나.



(Best댓글) 요새 분위기 별로라 굳이 이런 얘기까지 하고 싶진 않은데, 쟤들 뭐 반일 감정 있음?

└ 일본 총리랑 방위대신이 반일ㅋㅋㅋㅋㅋㅋㅋ 씹

└ 내가 볼 땐 둘 다 전생에 뭐 있었다.

└ 하나는 전생에 거북선이었고, 하나는 도시락 폭탄이었던 것 같음. ㄹㅇ저 정도로 똥 싸는 것도 쉽지 않은데.

└ 독립운동 하셨던 분들이 무타구치 렌야 볼 때 이런 마음이었을까……?

└ 어둠의 독립군 ㅇㅈ

└ 스시국 : 어어 점마들 머고.



이런 상황에서 그나마 열도의 자랑으로 불리던 야마모토 겐지마저 체면을 구겼다. 그가 레비아탄 사태에 이어, 발족식까지 2연속 불참했다는 사실이 알려졌기 때문이었다.

발족식에 불참한 이유?

자위대 헌터들도 몰랐다. 아마 그들이 진짜 이유를 알았다면, 열도의 자랑이고 뭐고 면전에서 침을 뱉었을 것이다.

야마모토 겐지는 그냥…… 쪽팔렸다.

‘제기랄. 그냥 참석할걸.’

처음에는 겁이 나서 레비아탄을 피했고, 진태경과 마주치는 게 싫어서 개인 사정을 핑계로 발족식에 빠졌다.

물론 그 덕분에 몸 성히 지금껏 살아 있을 수도 있지만, 모든 것이 마무리된 뒤 그를 기다리고 있던 것은 죽음보다 더한 모욕이었다.



그나저나 진짜 대단한 새끼들은 맞다. S급 헌터라는 놈은 이 와중에도 코빼기 하나 안 비추네 ㅋㅋㅋㅋㅋㅋ걔 이름 뭐였냐

└ 겐지.

└ 한조 아님?

└ 걘 겐지 형이고.

└ 미친놈들인가.

└ 언제적 망겜 얘기하세요 틀딱 형님들;

└ 진짠데? 안 믿기면 검색해 보셈.

└ ?

└ 진짜네; 위로 형 하나 있는데 이름 야마모토 한조임;

└ 이왜진;

└ 그럼 겐지 질풍참 쓸 줄 앎?

└ 질풍불참은 잘함

└ ㅅㅂㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ 아ㅋㅋㅋㅋㅋㅋㅈㄴ 자존심 상하네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

└ wwwwwww아아 화내려고 했는데 나도 모르게 웃어 버렸달까?

└ 너무 비웃지 말라구? 하지만 좀 웃겼어 wwww

└ 와사비도 웃고 가네 ㅋㅋㅋㅋㅋ

└ ㅋㅋㅋㅋ와사비도 왔는데 짜장은 안 오냐.

└ 현재 밝혀진 바에 의하면 진태경은 중국 산서성 출신이 확실해. 베이징 대학의 저명한 역사학자들이 옛 사료를 조사해 본 결과 태원진가라는 무가를 발견했는데 (더보기)

└ ;;;;이 새끼들 킬각 나오자마자 바로 진북공정 들어오네.

└ 쟤들 옛 사료는 홍위병이 처리한 거 아니었냐.

└ (블라인드 처리된 댓글입니다.)

└ 그래서 겐지인지 한조인지는 이번에 중동 가긴 했냐?

└ ㅇㅇ일단 S급 헌터라 받아 줬다고 들음.

└ 전투에는 불참하는 거 아님? 별로 도움도 안 될 것 같은데 걍 위문 공연이나 돌리라고 해라.

└ 캡틴 와사비;



‘감히, 감히 이 겐지에게 내게 그런 모욕을!’

인터넷 댓글들을 다시 한번 떠올린 야마모토 겐지는 몸을 부르르 떨었다.

질풍불참이라니. 캡틴 와사비라니.

폐부를 들쑤시는 송곳 같은 그 말들을 되새길수록, 울컥거리며 차오르는 분노에 치가 떨릴 지경이었다.

더군다나…….

‘그런 무례한 답신을 해? 그것도 자위대가 보는 앞에서?’

위협이나 다름없는 진태경의 경고는, 그리고 그런 무례에도 분노하긴커녕 황급히 만류하는 자위대 헌터들의 모습은 야마모토 겐지의 마지막 남은 자존심마저 탈탈 털어가 버렸다.

‘이대로 돌아가면, 그럼 난 뭐가 되는 거지?’

명실상부한 S급 헌터지만 소문을 아는 모두가 자신을 무시한다. 그 시선을 바꿔 놓기 위해 눈에 불을 켜고 사막을 뒤졌고, 곧 결실이 보일 것 같았다.

그런데 갑작스러운 철수 명령이라니.

쉴 새 없이 속삭이듯 욕설을 내뱉던 야마모토 겐지는 문득 의심이 들었다.

‘그 조센징 녀석이 설마…… 아니, 확실해. 틀림없어.’

그래, 이건 모두 그가 공을 세우는 것을 경계하는 진태경의 계략이다. 오래전부터 시작된 반일 감정이 여기까지 이어진 것이다.

망상이나 다름없는 결론을 내린 야마모토 겐지가 버럭 외쳤다.

“오이, 스토프!”

갑작스러운 정지 명령에 후송 차량이 우뚝 멈춰 섰다.

명령 불이행을 극렬하게 반대하던 출발 전과 달리, 고분고분하게 자신의 명령을 듣는 자위대 헌터들의 모습에 그의 얼굴이 밝아졌다.

‘그래, 나는 위대한 야마토 민족의 등불이다! 이들이 따르는 건 그 한코쿠진이 아니라 바로 나……!’

하지만 그 생각은 바로 다음 순간 뚝 끊겼다.

어리둥절한 자위대 헌터들의 표정. 그리고 동시에 섬광처럼 뇌리를 스치는 한 가지 사실 때문이었다.

“잠깐, 지금 운전석에 누가 있지?”

자위대 헌터 중 하나가 눈을 깜빡이며 대답했다.

“아무도 없는데요.”

“에에?”

“무인 차량이잖습니까.”

순간 내려앉은 침묵.

멍하니 서로를 바라보던 그들은 불현듯 깨달았다.

멀쩡히 가던 차량이 멈춘 이유. 어느덧 주위에 가득하던 빗소리조차 들리지 않는 이유를.

“습겨억!”

“습격이다!”

그리고 그와 동시에.

쾅!

거대한 굉음과 충격이 그들을 덮쳤다.
```

## Final English reading copy

```markdown
# Chapter 796

That night, someone paused their hurried steps and looked out the window. They thought the moon looked redder than usual.

They weren’t imagining it.

Blood Moon.

It was a phenomenon sometimes seen during a total lunar eclipse or when the atmosphere was unstable. The magical power levels, climbing day by day, were changing not only the state of the atmosphere but the climate itself.

*Whoosh.*

The scattered raindrops grew heavier.

A downpour that seemed out of place in this barren land, where the annual rainfall was less than 250 millimeters, soon blanketed the whole area.

Endless sand, with a few trees scattered across it.

And the head of a being invisible to the naked eye.

*Tap. Patter-patter.*

The rain bounced away without touching any part of his body.

The Prophet, crossing the vast desert behind an invisible barrier, abruptly looked up at the sky.

Dark and noisy.

The ominous storm clouds that had been gathering for days were unleashing rain and thunder with ferocious force.

As if furious at everything that had happened on this land.

But The Prophet paid them no mind. He studied the sky—or, more precisely, opened his senses wide and listened to every sound coming from all around him.

*Rumble. Rrrumble.*

Thunder boomed ceaselessly overhead. The Prophet paused to focus on the sounds around him, then muttered,

“They’re gone.”

He meant it literally.

The sharp cries of eagles, echoing from far away, could no longer be heard.

The persistent flying beasts some pursuer must have sent after him had finally given up and turned back.

*What a nuisance. Good riddance.*

Avoiding satellite surveillance and unmanned reconnaissance aircraft was easy enough.

The magical power mixed into the atmosphere served as a shield against tracking, and concealment spells weren’t made just to boil in a stew.

But those eagles were different. Even the Familiars commanded by the few mages who specialized in mental magic were no more than dirt under their claws by comparison.

They’d followed him for hundreds of kilometers without showing the slightest sign of slowing down.

And their eyes, shining with magical power, looked as if they might even see through his magic.

*They can’t be Familiars… It must be him.*

The Skeleton King. Or perhaps the Stone King.

Thinking of a mere monster that had sided with humanity, The Prophet frowned without realizing it.

The desert was still vast. But the undead army that creature commanded would expand the search area and drastically shorten the time it took to search it.

*This is unexpected.*

Though a lot of things had already gone against his expectations.

He hadn’t thought Michael Silbert would fall so easily, and he hadn’t expected the World Hunter Federation to get its internal chaos under control so quickly and close in right on his heels.

But there was one thing The Prophet knew: every one of these anomalies had started with one man.

*Jin Taekyung.*

Many had shone brightly before, but they’d all been meteors—flashing into view for a brief moment, then vanishing in the blink of an eye.

Jin Taekyung was different. He was a comet.

From the moment he first appeared, he’d been part of the celestial body called the world. Now, he’d become its center.

He was growing so fast that no one could predict where his limits lay. Fast enough to make all of The Prophet’s preparations so far seem pointless.

*Clink.*

A faint metallic sound rang out, following his fingertips as they unconsciously groped for something.

Forcing down the impatience welling up inside him, The Prophet murmured,

“Just a little longer. I can finish it with just a little more time.”

The problem was time.

The necessary components to bring this plan—one that couldn’t afford the slightest error—to perfection had not yet all been gathered, and the enemy’s encirclement was closing in fast.

In these circumstances, The Prophet had only one option left.

*Hunt.*

But time was short. To complete his plan successfully, he had to make it bigger and bolder than before.

For example…

*Vroom.*

The Prophet’s eyes lit up as he spotted transport vehicles moving along a high sand dune, kicking up a thick cloud of dust.

* * *

“Chikushō.”

At the low curse from Yamamoto Genji, Japan’s S-rank Hunter, the Self-Defense Forces Hunters shifted away from him and exchanged glances.

Japan was a long way from being called a Hunter powerhouse, but everyone dispatched to the Middle East was a veteran among veterans. They’d also known each other for a long time, so by now a glance was enough to get the general idea.

*What’s his problem?*

*Isn’t it obvious? Who else could it be?*

*Eeh? Jin-sama?*

*Right. Yamamoto-san got really mad at that transmission from headquarters earlier.*

The whole story was simple. About thirty minutes ago, headquarters had issued an emergency withdrawal order, and Yamamoto Genji had refused.

Then a reply came right back.

Not in the communication officer’s stiff voice, but in the vivid voice of a young man.

> “When Leviathan was wrecking Tokyo Bay, you didn’t come even when we called. You son of a bitch. What? You’re not coming? Give me your coordinates right now. If you won’t come to me, I’ll come to you.”

Who was Jin Taekyung?

The only person who could fill the void left by the unconscious Cheon Taemin, and the Alliance Leader of the World Hunter Federation, who had the support of all humanity.

But before that, no one should forget his temper—the kind that ignored all caution, sometimes, or rather, quite often—and his terrifying skill.

The Self-Defense Forces Hunters, their knees weak at the Supreme One’s reply—practically a murder threat—had desperately tried to talk Yamamoto down. Even after climbing into an evacuation vehicle, Yamamoto Genji still couldn’t contain his anger.

“You bastard! How dare one of those damn Koreans…”

The Self-Defense Forces Hunters pretended not to hear him. Right now, they all had to be deaf and blind.

Honestly, they didn’t much like Yamamoto Genji’s attitude, either. But if word of it reached their superiors, not only would they be cursed out, Japan would get dragged into it, too.

*More of this?*

*No. Absolutely not.*

The Defense Minister, who had played a major role in the Leviathan incident—including preparing a kamikaze operation—was now in a federal prison after his connection to Michael Silbert had come to light. And the kind but stupid Prime Minister couldn’t even go a few days without spewing more shit.

> [Japanese Prime Minister Koizumi: “Yamato people, fight for Jin-sama, the great shogun who defeated Susanoo for us!”]
>
> [Japanese Prime Minister Koizumi, asked by a reporter about the Self-Defense Forces’ strategy for their upcoming deployment to the Middle East: “Combat should be fun, cool, and sexy.”]
>
> [Former U.S. President Joseph Biden: “I understand the Japanese Prime Minister. When my dementia was in its early stages, I didn’t know what I was saying, either.”]
>
> [Chuck Hagel: “I think they’re both just crazy.”]

The Self-Defense Forces Hunters felt sorry for themselves.

The Defense Minister would spend his twilight years in a federal prison, and the Prime Minister was using the media as a loudspeaker to announce, without a hint of restraint, that Japan’s leader was a lunatic.

The mood was so bad that even Korean netizens, who’d been holding back on their comments after picking up on the tension, had said things like this:

> **Top comment:** I don’t really want to bring this up when things are already tense, but… do those guys have something against Japan?
>
> └ The Japanese Prime Minister and Defense Minister are anti-Japan, lmao. Fuck.
>
> └ If you ask me, they must’ve had something going on in a past life.
>
> └ One of them was a turtle ship in a past life, and the other was a lunchbox bomb. Seriously, it’s not easy to spew that much shit.
>
> └ I wonder if this is how the independence fighters felt when they saw Mutaguchi Renya…
>
> └ Shadow independence army. Agreed.
>
> └ Sushi country: “Uh, what are those guys doing?”

In the middle of all this, even Yamamoto Genji, once called the pride of the island nation, had lost face. People had found out that he’d failed to show up twice in a row: first during the Leviathan incident, then at the launch ceremony.

Why had he skipped the launch ceremony?

Even the Self-Defense Forces Hunters didn’t know. If they’d known the real reason, they probably would’ve spat in his face, pride of the island nation or not.

Yamamoto Genji had simply been… embarrassed.

*Damn it. I should’ve just gone.*

At first, he’d been afraid and avoided Leviathan. Then, because he didn’t want to face Jin Taekyung, he’d made up a personal excuse to skip the launch ceremony.

Of course, that might have been why he’d survived this long in one piece. But once everything was over, what awaited him was an insult worse than death.

> Those guys really are something. That S-rank Hunter hasn’t shown his face once, even now, lmao. What was his name again?
>
> └ Genji.
>
> └ Isn’t it Hanzo?
>
> └ That’s Genji’s older brother.
>
> └ Are you guys insane?
>
> └ Why are you talking about a dead game from ages ago, you fossils?
>
> └ It’s true, though? Look it up if you don’t believe me.
>
> └ ?
>
> └ It’s real; he actually has an older brother named Yamamoto Hanzo.
>
> └ How is this real?
>
> └ So can Genji use Swift Strike?
>
> └ He’s great at Swift No-Show.
>
> └ LMAO
>
> └ Goddamn, that really hurts my pride.
>
> └ wwwwwww I was about to get mad, but I laughed without even realizing it?
>
> └ “Don’t laugh at him too much, okay? I thought it was kind of funny, though.” wwwww
>
> └ Even wasabi’s laughing, lmao.
>
> └ Lmao, wasabi showed up, but where’s the black bean sauce?
>
> └ It’s now confirmed that Jin Taekyung is from Shanxi Province, China. After examining old historical records, renowned historians at Peking University discovered the Jin Family of Taiyuan (see more)
>
> └ ;;;; The second they see an opening, these bastards launch straight into their Jin-is-Chinese campaign.
>
> └ Didn’t the Red Guards destroy their old records?
>
> └ (This comment has been hidden.)
>
> └ So did Genji—or was it Hanzo—actually go to the Middle East this time?
>
> └ Yeah. I heard they accepted him since he’s an S-rank Hunter, at least.
>
> └ Isn’t he just going to sit out the fighting? Doesn’t seem like he’d be much help anyway. They should just send him around to entertain the troops.
>
> └ Captain Wasabi.

*How dare they. How dare they insult me like that!*

Remembering the online comments once more, Yamamoto Genji shuddered.

Swift Retreat. Captain Wasabi.

The more he thought about those words, like awls digging into his lungs, the more his anger surged, making his teeth grind.

And on top of that…

*He sent such a rude reply? In front of the Self-Defense Forces, too?*

Jin Taekyung’s warning, which was practically a threat—and the way the Self-Defense Forces Hunters had hurried to hold Yamamoto back instead of getting angry at such rudeness—had stripped away every last bit of Yamamoto Genji’s pride.

*If I go back now, what does that make me?*

By all accounts, he was an S-rank Hunter. But everyone who’d heard the rumors looked down on him. He’d scoured the desert with everything he had, determined to change how they saw him, and it had looked as if he was about to get results.

And now, an emergency withdrawal order.

Yamamoto Genji had been muttering curses under his breath nonstop when suspicion suddenly crept into his mind.

*That Korean bastard… Could it be—no, it has to be. There’s no doubt.*

That was it. All of this was Jin Taekyung’s scheme to stop him from earning credit. The anti-Japanese sentiment that had started long ago had followed him all the way here.

Reaching a conclusion that was practically a delusion, Yamamoto Genji barked,

“Oi, sutoppu!”

At his sudden order to stop, the evacuation vehicle ground to a halt.

Unlike before they’d set out, when they’d strongly objected to disobeying the withdrawal order, the Self-Defense Forces Hunters now meekly followed his command. Yamamoto’s face brightened.

*That’s right. I’m the beacon of the great Yamato people! The one they follow isn’t that Korean—it’s me…!*

But the thought cut off the very next moment.

The Self-Defense Forces Hunters looked confused. And at the same time, one fact flashed through Yamamoto’s mind like a streak of light.

“Wait. Who’s in the driver’s seat right now?”

One of the Self-Defense Forces Hunters blinked and answered,

“No one.”

“Eeh?”

“It’s an unmanned vehicle.”

Silence fell.

They stared blankly at one another, then suddenly realized.

Why the vehicle, which had been moving along just fine, had stopped. Why even the sound of the rain, which had been all around them, had vanished.

“Ambush!”

“We’re under attack!”

And at the same time—

*BOOM!*

A tremendous roar and impact crashed down on them.
```
