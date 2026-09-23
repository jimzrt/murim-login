<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0827.txt",
      "sha256": "fc7270406bffbd212e3262b5cea20c4b8d2e9ce491b53baeffbbc850595a79be",
      "bytes": 13114
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1e8957c9f2c6fcff2795cb6e598c61526a4ed879eac7d488add663bce11c9ee0",
      "bytes": 2043
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3c3b9627e7353c69a66f8e10657ef055c79a30700111295e071d564e07f7e0ae",
      "bytes": 226707
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "eddd6d651ab878af2a7c0f4bc960a05c44eb0bb002735400332136421470c0b5",
      "bytes": 776
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c0fdd042ca4b984203c0bb9df6fe84969363bbbc5dcd834b7c189c653f46f025",
      "bytes": 723
    },
    {
      "path": "characters/Doppelganger.md",
      "sha256": "65bfa12becdcb9588b178f577c941ded972dec58b781dfcd683c83ed81a3366f",
      "bytes": 855
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f166e9cd2790f9014c23208458aedbed7f5d76165074eb03a5c6e0325129266a",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bca93f58fcaee58f2b1cc877f2e6c3aa232daa090fc31a52e1965ec76d2bebce",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "13360456b7acca4787981cf8c388f1a6ad6264a016814bc22236e3f92567d25a",
      "bytes": 820
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "67c773e1faecc341a7cfdee91a1ed0aa8d8bc470d8ce806fc6749e013e6e32b8",
      "bytes": 250673
    }
  ],
  "estimated_tokens": 10204
}
-->

# Durable State Update — Chapter 827

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
1 and safe_through 827. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 827. Profile updates may replace only one
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
  "chapter": 827,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 827,
    "continuity_sources": [827],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a Level 170 Doppelganger titled “The Final Abyss,” the last surviving member of its species, which spent decades manipulating events in the human world.",
    "The Doppelganger can resurrect by consuming absorbed lives and reproduce absorbed people’s appearances, abilities, and memories; it has taken Siegfried Bassman’s face and Grand Mage abilities.",
    "The Doppelganger has regained its composure and grown a new arm; its dwindling absorbed lives were replenished by killing twenty followers and absorbing their vitality and souls.",
    "The Doppelganger brought Jin and the Skeleton King to a vast temple concealed beneath the ruins, where it says it heard its unnamed master’s command.",
    "Jin and the Skeleton King are in the temple, preparing a coordinated attack; Jin is exhausted but secretly gathering energy, while the Skeleton King absorbs magical power and awaits Jin’s signal.",
    "Jin believes the Demon King Asmodeus is dead, but the Doppelganger challenges that belief."
  ],
  "continuity_sources": [
    825,
    826
  ],
  "open_questions": [
    "Who is the Doppelganger’s master, and what is the plan behind the command it heard at the temple?",
    "What does the Chosen One designation mean?",
    "Is the Demon King Asmodeus truly dead?",
    "What is the temple’s purpose, and what preparations did the Doppelganger complete there?"
  ],
  "safe_through": 826,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword.”",
    "Render 에어 슬래시 as “Air Slash” and 실드 마법 as “Shield magic.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 도플갱어 | **Doppelganger** | The Prophet’s revealed species. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 골렘 | **Golem** | Magical rock-based monster classification. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 진태경 | 도플갱어 | enemy | you; the Doppelganger | blunt and informal | Jin directly challenges the Doppelganger and demands to know what it wants. |
| 도플갱어 | 진태경 | enemy | you | measured and informal | Replies to Jin’s taunt without using a name or title. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 817
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Ares Guild Master and humanity's greatest Hunter, the Slayer who defeated the Demon King and created the first Mana Cultivation Method during the Great Cataclysm; after more than twenty years in seclusion, he remains unconscious in a secret area within Area A.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 826
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Doppelganger.md

# Doppelganger (도플갱어)

- **Safe through:** Chapter 826
- **Aliases:** The Final Abyss
- **Role:** The last surviving member of its species, the Doppelganger is a powerful being from the Demon Realm that spent decades manipulating events in the human world.
- **Personality:** Arrogant and manipulative, it treats others as tools and is willing to sacrifice its followers to escape, but becomes desperate when its own survival is threatened.
- **Voice:** It speaks with theatrical, grandiose confidence, taunting opponents in polished, self-important phrasing.
- **Relationships:** It serves an unnamed master whose command it heard at the temple, regarded Michael Silbert as a subordinate and disposable tool, and selected Yahya Muhammad Ahmad Bedouin to teach him magical power.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 825
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 825
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 826
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃827화



순간, 마치 세상이 멈춘 듯했다.

나는 소리 없이 웃고 있는 도플갱어를 멍하니 바라보았다.

사고가 정지된 머릿속에서는 조금 전 들었던 목소리가 끊임없이 반복 재생 되고 있었다.



‘정말 그렇게 생각하나?’



숨이 막혔다.

저 물음에 담긴 뜻이 무엇인지, 이미 깨달아 버렸기 때문이다.

그러나 가슴 깊숙한 곳에서 울컥, 하고 솟구친 본능적인 거부감은 나도 모르게 입술을 움직이고 있었다.

“개소리 지껄이지 마.”

그럴 리 없다.

나도 알고, 이 세상 모두가 안다.

마왕은, 아스모데우스는 이미 죽었다.

훗날 ‘승리의 날’이라 불리는 대격변의 끝자락에서 인류의 영웅은 마왕과 맞서 싸웠고, 전 세계를 불구덩이로 몰아간 재앙을 마침내 쓰러트렸다.

그리고 몇 시간 뒤 삼면이 바다로 둘러싸인 반도의 어느 나라에서 작은 생명이 태어났다.

바로 지금, 이 자리에 서 있다.

“마왕은 죽었어. 내가 태어났던 그 날에. 승리의 날에.”

입술 밖으로 흘러나오는 갈라진 목소리가 마치 남의 것처럼 낯설었다.

나는 스스로에게 다짐하듯 힘주어 말을 이었다.

“놈은 소멸했고, 우리는 승리했다. 그게 전부야. 진실이고.”

단지 서 있는 것뿐인데. 입술을 움직여 말하는 것뿐인데도 호흡이 가쁘다. 내뱉는 숨결은 독이라도 실려 있는 것처럼 쓰게 느껴졌다.

마치 지금 이 순간, 내 귓가를 파고드는 목소리처럼.

“그래, 그 말 또한 맞다. 진태경. 선택받은 자여.”

도플갱어.

심연을 닮은 괴물이 나를 바라보며 입꼬리를 말아 올린다.

훔쳐 온 대마도사의 얼굴로 그려 낸 미소는 독사의 그것처럼 간교하고 사악했다.

“그것이 너희가 알고 있는 전부고, 진실이겠지.”

저벅.

천천히 내디딘 걸음이 나를 향한다.

거대하고도 기괴한 신전을 울리는 발걸음 소리가 이어지는 목소리와 뒤섞인다.

“그러나 나를 보아라.”

깊게 가라앉은 눈빛. 심연처럼 소용돌이치는 그 눈동자가 나를 응시했다.

“인간이 수없이 죽어 나가던 그때에도, 승리에 기뻐 눈물 흘릴 때도 그저 지켜만 보았던 나를. 위대하신 왕의 명령을 받들어 너희와 함께하고 있던 나를.”

“……!”

“아직도 모르겠느냐? 내 존재가 곧 증거다. 너희가 믿는 진실은 거짓이며, 너희가 모르는 진실이 존재한다는 증거.”

순간 눈앞이 뿌옇게 흐려졌다.

이 신전을 지탱하는 거대한 기둥도, 기괴한 석상들과 뭐라 입술을 달싹이고 있는 스켈레톤 킹의 모습도 사라졌다.

오직 한 존재.

도플갱어만이 시야를 가득 채웠다. 두 눈동자에 선명하게 틀어박혔다.

‘파리 대전투.’

머릿속이 어지러웠다.

그 속에서 자그마한 퍼즐 조각들이 떠올라 하나둘씩 빈자리를 채웠다.

‘마왕 아스모데우스가 쓰러지기 한참 전부터, 도플갱어는 이미 이 세상에 스며들어 있었다.’

처음부터 미카엘 실베르트가 도플갱어를 선택한 것이 아니다.

도플갱어가 그를 선택했다.

이계(異界)의 괴물은 현계(顯界)의 괴물을 알아보았고, 살과 뼈로 이루어진 인간의 몸속에 웅크린 거대한 야망을 읽었다.

‘도플갱어는 왜 하필 미카엘 실베르트를 선택했을까.’

마음속으로 던진 질문에 대한 답을, 이미 나는 알고 있다.

‘놈이 원했던 건, 단지 이 세상에 존재하는 것만이 아니었으니까.’

도플갱어는 유일무이(唯一無二)라 부를 만한 능력을 지녔다.

외관과 능력뿐만 아니라 기억조차도 흡수하여 자신의 것으로 만들 수 있으니, 그저 한 사람의 인간으로 살아가는 일은 그 무엇보다 쉬웠을 것이다.

그러나 이제는 안다.

도플갱어가 인류 속으로 스며들었던 것은, 단순한 배신이나 전향(轉向) 따위가 아니었음을.

놈은 명령을 받았다.

자신이 목숨을 다해 충성하는 주인, 마왕 아스모데우스의 명령을.

그 후의 이야기는 내가 아는 그대로일 것이다.

도플갱어는 미카엘 실베르트를 내세워 세상을 움직였다.

파리 대전투에서 이름을 알린 허수아비는 천태민이라는 하늘을 피해 조용히 몸집을 불렸고, 허수아비를 조종하는 그림자는 보이지 않는 곳에서 누군가의 영혼으로 배를 불렸다.

그리고 자그마치 삼십 년이 넘는 세월 동안 자신이 받은 명령을 되새기며 계단을 올랐다.

끝없이 위로 이어진 이 계단이 끊길 때까지.

마침내 기다리던 때가 도래하고, 굳게 닫혀 있는 문이 나타날 때까지.

“표정을 보아하니 이제야 감이 좀 잡히는 모양이군.”

소리 내어 웃은 도플갱어가 손을 들어 올린 그때.

슈욱.

햇빛 한 줄기 들어오지 않는 어둠 속에서 홀로 유영하던 빛의 구가 거대한 신전의 끝자락에 다다라 멈추었다.

드넓은 공간을 밝히는 흐릿한 빛무리.

그리고 그 아래에 놓인 단 하나의 왕좌(王座).

‘저건.’

텅 빈 왕좌를 본 순간, 나는 본능적으로 깨달았다.

이 신전이, 저 자리가 누구를 위해 만들어진 것인지.

또한 저 기괴하면서도 흉측한 일흔두 개의 거석상(巨石像)이 무엇을 의미하는지.

“마계 72군단장…….”

스켈레톤 킹이 신음하듯 뇌까렸다. 도플갱어가 환희에 가득 찬 얼굴로 왕좌를 향해 두 팔을 펼쳤다.

“위대한 왕께서는 반드시 돌아오실 것이다. 머지않은 그날, 당신을 따르는 무수한 군세(軍勢)와 함께.”

“……!”

전신의 털이 바짝 곤두선다. 서늘한 기운이 뱀처럼 등골을 타고 기어올랐다.

나는 도플갱어를 믿지 않는다. 놈은 거짓 그 자체로 이루어진 존재니까.

지금껏 들은 말이 진실인지, 혹은 날 흔들기 위한 거짓말인지도 당장은 확신할 수 없다.

하지만…….

‘저 말들이 모두 사실이라면.’

그렇다면, 내가 해야 할 일은 이미 정해져 있었다.

심지가 끊어진 다이너마이트는 폭발하지 않는다. 열쇠가 없으면 굳게 잠긴 문은 열리지 않는다.

그리고 그런 의미에서 도플갱어는 심지이자 열쇠였다.

곧 일어날 거대한 재앙의 신호탄.

인류에게 있어 악몽과도 같은 어느 존재의 재림(再臨)을 막을 기회는 바로 지금뿐이다.

‘놈을 죽인다.’

먹구름으로 가득하던 머릿속이 맑아진다.

사명과도 같은 하나의 생각과 함께 전신의 기운이 들끓었다.

솨아아아.

눈앞이 아득해진다. 무리한 텔레포트 마법의 여파를 고스란히 감당해야 했던 몸뚱어리가 고통을 호소한다.

그러나 나는 한 치의 망설임도 없이, 하단전에서 끌어올린 열양지기를 사지백해로 쏟아 보냈다. 통증을 둔화시키고, 파열된 근육에 억지로 생기를 불어넣으며, 마침내 폭발시켰다.

꽈앙!

염화일로(炎火一路).

발끝을 따라 터져 나온 청백색의 화염이 어둠을 살라 먹는다.

찰나를 쪼개고 쪼갠 시간 속, 공간을 지우며 쇄도한 나는 창을 뻗었다.

수천, 수만 번도 넘게 반복한 그 동작으로.

단 한 존재를 향해.

쐐애애액!

백염(白炎)이라는 그 이름대로 어둠을 가르며 나아가는 창날은 새하얀 불꽃처럼 눈부셨고, 강렬하게 타올랐다.

그 어떤 것도 막아설 수 없을 것처럼.

모든 것을 잿더미로 만들어 버릴 것처럼.

적어도 다음 순간, 도플갱어의 손짓과 함께 보이지 않는 무언가가 앞을 가로막기 전까지는 그렇게 보였다.

꽈앙!

귓가를 먹먹하게 물들이는 굉음.

그리고 거대한 반발력.

‘흡.’

나는 찌르르 울리는 창대를 억세게 움켜쥐었다.

불과 열 걸음 앞.

여전히 웃고 있는 도플갱어의 얼굴이 보이지 않는 투명한 막(膜)에 휩싸여 일렁이고 있었다.

“이제야 알겠나? 내가 굳이 이곳까지 온 이유를?”

방어 마법?

아니, 이건 단순한 방어 마법이 아니다.

지금의 도플갱어가 제아무리 대마도사라 해도, 내 일격을 이토록 손쉽게 막을 만큼 견고한 마법의 방패를 순간적으로 만들어 내는 것은 불가능에 가깝다.

단 하나의 경우를 제외한다면.

‘마법진.’

지크프리트 바스만.

전 세계에서 단 세 명뿐인 대마도사 중에서도 최고로 손꼽히는 마법진의 대가.

그리고 그런 이의 영혼을 흡수한 도플갱어에게 주어진 삼 년이라는 시간.

“너, 이 새끼…….”

“너희 인간들은 보험이라는 걸 들더군. 비슷하다고 생각하면 이해가 될까.”

말아 올린 입꼬리에서 여유가 묻어나온다.

나로 인해 무수한 죽음을 겪으며 도주할 때만 해도 볼 수 없었던 미소였다.

“괜한 헛수고하지 마라. 이곳의 주인은 바로 나니까.”

우우웅.

미증유의 기운이 사방에서 공명한다.

휘황한 빛무리를 머금은 마법진이 사방에서 떠오르고, 마계 72군단장을 형상화한 거대한 석상들이 부르르 몸을 떨었다.

“위대한 왕의 대리인으로 명하니, 잠에서 깨어날지어다.”

파스슥.

힘이 실린 도플갱어의 목소리와 함께 사방에서 떨어져 내리는 돌 부스러기.

그와 동시에 영원히 움직이지 않을 것 같던 거석상들이 움직였다.

아니, 눈을 떴다.

팟.

작게는 수 미터, 크게는 수십 미터에 달하는 거대한 괴물들이 붉은 안광(眼光)으로 아득한 지상을 굽어본다.

앞서 공격을 시도했던 나와 별다를 것 없이, 반투명한 막에 가로막혀 있던 스켈레톤 킹이 그 광경을 멍하니 바라보았다.

그리고 이내 벼락처럼 외쳤다.

“피해!”

그 순간.

후우우웅!

암석으로 이루어진 괴물들의 팔과 다리가, 그리고 발톱이 시야를 가득 메우며 떨어져 내린다.

동시에 세상이 느려지고 호흡이 길게 흩어졌다.

‘아니야, 피할 수 없다.’

그만큼 저 석상들의 공격이 강맹하고 빨라서가 아니다.

저것들을 피하기 위해 물러나면 물러날수록, 도플갱어와는 멀어지기 때문이다.

‘지금은 가야 할 때다.’

도플갱어가 조종하는 저 석상들은 분명 강력한 존재다.

그러나 나는 안다.

놈이 흉내 낸 것은 마계 72군단장들의 형상일 뿐, 각각의 힘은 S급 몬스터에도 미치지 못한다는 것을.

그렇다면.

‘벤다.’

생각과 동시에 몸이 움직였다.

아니, 그 순간 내가 움직인 것은 비단 피륙으로 이루어진 몸뚱어리뿐만이 아니었다.

우우우우웅.

강한 공명음과 함께 닫혀 있던 중단전(中丹田)이 열린다.

그와 동시에 이 거대한 신전에 비하면 턱없이 비좁은, 그러나 목표한 바를 이루기에는 충분한 공간이 내 지배하에 떨어졌다.

‘흡.’

순간 시야가 아득해질 정도의 두통.

하지만 참는다. 참아야 한다.

입술이 너덜너덜해질 정도로 이를 악문 나는 손아귀에 쥔 백염의 창대를 놓았다.

화륵.

뜨겁다. 눈부시다.

하단전으로부터 비롯된 열양지기를 머금은 한 자루의 창은 청백색으로 타오르고 있었고, 중단전의 의지가 그것을 움직였다.

아니, 휘몰아쳤다.

쏴아아아악!

굉음은 들리지 않았다.

오직 파공성으로 가득 찬 그 세상 속에서, 한 줄기의 광염(光焰)이 주위의 모든 것을 베었다.

슈확!

공간을 가르고.

서걱!

영혼 없이 움직이는 골렘(Golem)들을 스치듯 가로질렀다.

몇 번이나. 혹은 수십 번이나.

그리고 마침내 사방을 찢어발기고 주인을 찾아 돌아온 그것을 내 손아귀로 붙잡은 순간.

콰아아아아!

모든 것이 허물어져 내렸다.

거대하기 그지없는 일흔두 개의 석상도. 세계수처럼 두꺼운 기둥도.

그리고.

신전 곳곳에 가득하던 수많은 마법진들도.

콰창!

한계를 넘어 끝자락까지 도달한 몸 상태 때문일까.

눈앞이 새하얗다. 아무것도 보이지 않는다.

그러나 들을 수 있다. 느낄 수 있다.

산산이 흩어지는 마나와 마력을. 그 너머에서 경악하고 있는 한 존재도.

“다시 지껄여 봐.”

나는 끊어질 것 같은 목소리로 뇌까렸다.

남아 있는 마지막 힘을 끌어내어 걸음을 내디뎠다.

저벅.

“도대체 누가, 이곳의 주인이라고?”

그 순간, 대답 대신 눈부신 광휘가 신전을 가득 메웠다.
```

## Final English reading copy

```markdown
# Chapter 827

For a moment, it was as if the world had stopped.

I stared blankly at the Doppelganger, smiling without a sound.

In my frozen mind, the voice I’d heard moments ago kept playing over and over.

*“Do you really think so?”*

I couldn’t breathe.

I’d already realized what that question meant.

But a deep, instinctive rejection surged up from my chest, and before I knew it, my lips were moving.

“Don’t spout that bullshit.”

There was no way.

I knew it, and so did everyone in this world.

The Demon King—Asmodeus—was already dead.

Near the end of the Great Cataclysm, on what would later be called Victory Day, humanity’s hero fought the Demon King and finally brought down the calamity that had turned the whole world into a blazing inferno.

And hours later, a small life was born in a country on a peninsula surrounded by the sea on three sides.

That life stood here now.

“The Demon King died the day I was born. On Victory Day.”

The hoarse voice escaping my lips sounded like someone else’s.

I continued, putting force into my words as if making a vow to myself.

“He was erased, and we won. That’s all there is to it. That’s the truth.”

I was only standing there. Only moving my lips to speak. Yet I was short of breath. Every exhalation tasted bitter, as if it carried poison.

Like the voice now burrowing into my ears.

“Yes. That, too, is true, Jin Taekyung. Chosen One.”

The Doppelganger.

The abyss-like monster looked at me and curled its lips.

The smile it drew with the Grand Mage’s stolen face was as sly and wicked as a serpent’s.

“That is all you know. And it is the truth, as far as you know it.”

*Step.*

It took a slow step toward me.

The sound echoed through the vast, grotesque temple, mingling with its voice.

“But look at me.”

Its gaze was dark and deep. Its eyes, swirling like the abyss, fixed on me.

“Look at me, who merely watched while countless humans died, and watched as you wept for joy at your victory. Look at me, who was with you, carrying out the command of the Great King.”

“……!”

“Do you still not understand? My very existence is proof. Proof that the truth you believe is a lie, and that there is a truth you don’t know.”

My vision blurred in an instant.

The massive pillars supporting the temple vanished, along with the grotesque statues and the Skeleton King, whose lips were moving as if to say something.

There was only one presence.

The Doppelganger filled my vision. Its image was etched clearly into both my eyes.

*The Great Battle of Paris.*

My mind reeled.

Small puzzle pieces surfaced within it, one by one, filling the empty spaces.

*Long before the Demon King Asmodeus fell, the Doppelganger had already infiltrated this world.*

Michael Silbert hadn’t chosen the Doppelganger from the start.

The Doppelganger had chosen him.

The monster from another world had recognized a monster in this one. It had read the immense ambition curled up inside a human body of flesh and bone.

*Why had the Doppelganger chosen Michael Silbert, of all people?*

I already knew the answer to the question I’d asked myself.

*Because all it wanted wasn’t simply to exist in this world.*

The Doppelganger possessed an ability that could only be called one of a kind.

It could absorb not only someone’s appearance and abilities, but even their memories, making them its own. Living as a single human would have been easier than anything.

But now I understood.

The Doppelganger’s infiltration of humanity hadn’t been a simple act of betrayal or defection.

It had received an order.

An order from the master it served with its very life—the Demon King Asmodeus.

Everything that came after must have happened just as I knew it.

The Doppelganger used Michael Silbert to move the world.

The puppet that had made a name for itself at the Great Battle of Paris quietly grew in the shadow of Cheon Taemin, the sky above it. And the shadow controlling the puppet fed on someone’s soul, out of sight.

For more than thirty years, it climbed the stairs, reflecting on the order it had received.

Until this endless staircase came to an end.

Until the long-awaited moment arrived, and a tightly shut door appeared.

“Judging by your face, it looks like you’re finally starting to understand.”

The Doppelganger laughed aloud and raised a hand.

*Whoosh.*

A solitary sphere of light, drifting through the darkness where not a single ray of sunlight could reach, stopped at the far end of the vast temple.

A hazy glow illuminated the enormous space.

And beneath it stood a single throne.

*That’s…*

The moment I saw the empty throne, I knew instinctively.

I knew who this temple—and that seat—had been built for.

And I knew what the seventy-two bizarre, hideous stone colossi meant.

“The seventy-two commanders of the Demon Realm…”

The Skeleton King muttered as if groaning. The Doppelganger spread both arms toward the throne, its face alight with rapture.

“The Great King will surely return. On that day, which is not far off, He will come with the countless armies that follow Him.”

“……!”

Every hair on my body stood on end. A chill crawled up my spine like a snake.

I didn’t believe the Doppelganger. It was made of lies, through and through.

For now, I couldn’t be sure whether what I’d heard was true or a lie meant to shake me.

But…

*If every word it said was true.*

Then I already knew what I had to do.

Dynamite with a severed fuse doesn’t explode. A locked door won’t open without a key.

And in that sense, the Doppelganger was both the fuse and the key.

The opening signal for a massive calamity about to unfold.

This was the only chance to stop the return of a being who would be a nightmare for humanity.

*I’ll kill it.*

The clouds filling my mind cleared.

Along with the single thought that felt like a mission, energy boiled throughout my body.

*Fwoooosh.*

My vision went hazy. My body, still bearing the full brunt of the strain from the reckless Teleport spell, cried out in pain.

But without a moment’s hesitation, I sent the Scorching Yang Qi I’d drawn up from my Lower Dantian rushing through every limb and acupoint. I dulled the pain, forced life into my torn muscles, and finally unleashed it.

*BOOM!*

Flamefire Path.

Blue-white flames burst from my heels, devouring the darkness.

In a moment split into ever smaller pieces, I erased the space between us and thrust my spear.

With a motion I’d repeated tens of thousands of times.

Toward a single being.

*SHWAAA!*

Just as its name, White Flame, promised, the spearhead cut through the darkness, bright as a white flame, burning fiercely.

As if nothing could stop it.

As if it would turn everything to ash.

At least, that was how it looked—until the next moment, when something invisible blocked the way at the Doppelganger’s gesture.

*BOOM!*

A deafening roar filled my ears.

Then came a tremendous force of repulsion.

*Hngh.*

I gripped the spear shaft tightly as it vibrated in my hands.

Ten paces away.

The Doppelganger’s still-smiling face wavered inside a transparent barrier I couldn’t see.

“Do you understand now why I came all the way here?”

Shield magic?

No. This wasn’t simple Shield magic.

Even if the Doppelganger was now a Grand Mage, it was nearly impossible for it to conjure a barrier sturdy enough to stop my strike so effortlessly.

Unless there was one explanation.

*A magic circle.*

Siegfried Bassman.

One of only three Grand Mages in the entire world, and considered the greatest master of magic circles among them.

And the three years granted to the Doppelganger after it absorbed his soul.

“You son of a…”

“You humans take out insurance. Can you understand if I say it’s similar?”

There was confidence in the Doppelganger’s curled lips.

It hadn’t been smiling like this when it was fleeing after suffering one death after another at my hands.

“Don’t waste your effort. I am the master here.”

*Vwoom.*

An unprecedented force resonated from every direction.

Magic circles, holding dazzling halos of light, rose up all around us, and the enormous statues depicting the seventy-two commanders of the Demon Realm began to tremble.

“As the Great King’s representative, I command you: awaken from your slumber.”

*Crackle.*

At the Doppelganger’s commanding voice, fragments of stone fell from all around us.

And at the same time, the colossi that seemed destined to remain still forever began to move.

No—they opened their eyes.

*Flash.*

Monsters, ranging from a few meters to dozens of meters tall, gazed down at the distant ground with glowing red eyes.

The Skeleton King, whose earlier attempt to attack had been blocked by a translucent barrier just like mine, stared blankly at the sight.

Then he shouted like a bolt of lightning.

“Move!”

At that moment—

*WHOOOOM!*

Arms, legs, and claws made of stone filled my vision as they came crashing down.

At the same time, the world slowed, and my breath scattered.

*No. I can’t dodge.*

Not because the statues’ attacks were too powerful or too fast.

The farther I retreated to avoid them, the farther I’d get from the Doppelganger.

*Now’s the time to go.*

The statues controlled by the Doppelganger were undoubtedly powerful.

But I knew that, though it had copied the forms of the seventy-two commanders of the Demon Realm, their individual strength didn’t even measure up to an S-rank monster.

Then…

*I’ll cut them down.*

My body moved as soon as I thought it.

No—in that instant, it wasn’t only my body of flesh that moved.

*Vwoooooom.*

With a powerful hum, my closed Middle Dantian opened.

At the same time, a space woefully small compared to the enormous temple—but sufficient to accomplish my goal—fell under my control.

*Hngh.*

A headache so sharp it nearly blacked out my vision.

But I endured. I had to.

Clenching my teeth until my lips were ragged, I let go of the shaft of White Flame in my hand.

*Fwoosh.*

Hot. Blinding.

The spear, holding the Scorching Yang Qi that sprang from my Lower Dantian, blazed blue-white, and the will of my Middle Dantian moved it.

No—it sent it hurtling.

*SHWAAAA!*

There was no roar.

In a world filled only with the sound of air splitting, a streak of light-flames cut through everything around it.

*SHWAK!*

It cleaved through space.

*SHHK!*

It sliced through the soulless Golems as if barely grazing them.

Again and again. Maybe dozens of times.

And at last, when I caught it in my hand as it tore through everything around us and returned to its master—

*KWA-AAAA!*

Everything crumbled.

The seventy-two colossal statues. The pillars as thick as the World Tree.

And—

The countless magic circles that had filled every corner of the temple.

*KWA-CRASH!*

Maybe it was because my body had reached its absolute limit.

My vision turned white. I couldn’t see a thing.

But I could hear. I could feel.

The mana and magical power scattering into fragments. And beyond them, a presence stricken with shock.

“Say that again.”

My voice came out broken as I muttered.

I gathered up the last of my strength and stepped forward.

*Step.*

“Who exactly is the master here?”

At that moment, instead of an answer, a dazzling radiance filled the temple.
```
