<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0707.txt",
      "sha256": "91ddd674c0598c3a1cf71f60ffb9e4c4f657e1e3a752261284691d15f5c5508f",
      "bytes": 13044
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b81cc2391c3c2fbc38cae15743e9c389d65489291d08f1b2bd34ba9aaaf9f16d",
      "bytes": 1863
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c1986676bc48fdff4fd48cf0f0b57f97ebad0bdfdd8467f01fb8d3155af76b6e",
      "bytes": 207119
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "593eab5dbe9d7b1b895afda02cea3c9e58b655c009d7f1ed7750141f4466255c",
      "bytes": 930
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "03543d8337fb5d6136f562cb5a8b2bcfbb75445b16b58c49a5c30e7237290db4",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "23316accaff5f6110b3e100b5abe7501e6b24066dfb141e789966aaace7078cc",
      "bytes": 1907
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3a6af89f16094224f8edeba1c96f851f13ae62580ac5bd626400c32f0cc462a7",
      "bytes": 622
    },
    {
      "path": "characters/Masked Man.md",
      "sha256": "0491b8acd5d7d08b837bd734c450520743261ccb348a4ad5cb607a33028629bc",
      "bytes": 686
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "bc68b0b0be6e73e21727a712db5f806ad4bb2d46292f6374417ebfb26c8048a5",
      "bytes": 847
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "3798d20af993a37c7c3db81a6b40be69b924a83e97ff702929397d037e445285",
      "bytes": 603
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "79f60d1354e1a6bfab21c3e3e993a361ba027b77741dd85d68564def6d4372fa",
      "bytes": 217101
    }
  ],
  "estimated_tokens": 10929
}
-->

# Durable State Update — Chapter 707

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 707. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 707. Profile updates may replace only one
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
  "chapter": 707,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 707,
    "continuity_sources": [707],
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
    "The Beast Miao King is fighting the Southern Heaven Demon Empress and currently has the advantage.",
    "The Southern Heaven Demon Empress is exhausted and bleeding after fighting the Beast Miao King.",
    "The Baekcheon Unit has lost more than half its members in the battle against the mutants.",
    "The mutants are enlarged and strengthened by mutation and demonic qi while retaining their former human martial arts.",
    "Jin Taekyung is severely depleted after using One Annihilation but continues fighting with White Flame from the guardian spirit's back.",
    "The guardian spirit and Jin Taekyung lead the surviving forces after the Beast Miao King separates to duel the Southern Heaven Demon Empress.",
    "The guardian spirit tells Jin Taekyung that the mutants do not resent him and urges him to stop blaming himself.",
    "Jin Taekyung and the guardian spirit advance toward the Southern Heaven Demon Empress because the Inner Palace disaster is not yet over."
  ],
  "continuity_sources": [
    706
  ],
  "open_questions": [
    "Can the Beast Miao King defeat the exhausted Southern Heaven Demon Empress?",
    "Can Jin Taekyung and the guardian spirit reach and defeat the Southern Heaven Demon Empress?",
    "What will happen to the remaining mutants and surviving Baekcheon Unit warriors after the battle?"
  ],
  "safe_through": 706,
  "temporary_decisions": [
    "Retain One Annihilation, White Flame, Fist Force, Force, Sword Energy, Internal Injury, demonic qi, and Baekcheon Unit.",
    "Render 초일류 as Supreme First Rate and 백천대주 as Commander of the Baekcheon Unit.",
    "Render 신수 as divine beast and 신병이기 as divine weapon.",
    "Preserve Jin Taekyung's conversational profanity and the guardian spirit's terse, teasing, and compassionate voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 십왕     | **Ten Kings**       |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 일격     | **One Strike**                         |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 복면인 | **Masked Man** | The Southern Heaven Demon Empress's trained hunting dog; identity remains unknown. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 권강 | **Fist Force** | Qi force projected through the Western Heaven Demon Lord's fist. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 외공 | **external arts** | Martial arts focused on extreme bodily training. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 진태경 | 복면인 | hostile combatant to unknown hostile combatant | you | blunt, hostile, and incredulous | Jin directly questions the masked man about his identity and his relationship with the Great Snow Fiend. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 706
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people, leading roughly thirteen thousand allied warriors against the Southern Heaven Demon Empress while the Baekcheon Unit battles the mutants.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang is his sworn younger brother and childhood companion, Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple whom he now fights beside against the Southern Heaven Demon Empress.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 706
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 705
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license; he is recovering from severe injuries sustained when One Annihilation failed to kill the Southern Heaven Demon Empress.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 705
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Masked Man.md

# Masked Man (복면인)

- **Safe through:** Chapter 704
- **Aliases:** None
- **Role:** The Masked Man is the Southern Heaven Demon Empress's trained hunting dog; the guardian spirit has killed him four times, but he repeatedly rises again, recovering faster and growing stronger under the rift's demonic qi.
- **Personality:** The Masked Man is emotionless, silent, and indifferent to extreme bodily damage.
- **Voice:** No spoken voice has been established.
- **Relationships:** He serves the Southern Heaven Demon Empress as her hunting dog; his identity and relationship with the Great Snow Fiend remain unknown.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 706
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, creator of the rift behind the Inner Palace; after her five hundred elites were annihilated, she is exhausted and bleeding from fighting the Beast Miao King while Jin Taekyung and the guardian spirit advance toward her.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 706
- **Aliases:** Whitey
- **Role:** The White Tiger is the guardian spirit of the sacred stone and leads the Sacred Land beasts, but both the stone's power and the White Tiger's strength are weakening under the rift's demonic qi.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger carries Jin Taekyung and Yohi, guards the sacred stone, and advances with Jin's forces.

## Korean source

```text
＃707화



남천마후는 이해할 수 없었다.

도대체 어째서. 완벽하리라 의심치 않았던 대계(大計)가 이토록 흐트러졌는지. 그리고 왜 자신이 고작 십왕(十王) 따위와 동수를 이루는 수모를 겪게 된 것인지.

그러나 의문은 이어질 수 없었다.

후웅!

맹렬한 파공성이 바람을 뭉갠다.

공간을 지우며 쇄도하는 거대한 신형. 야수묘왕의 주먹 끝에서 터져 나온 녹색 권강(拳罡)이 세상을 환하게 물들인다.

콰아아아!

그렇게 먼 이야기도 아니다.

과거의, 아니 적어도 두 시진 전의 남천마후였다면 코웃음을 치며 저 권강을 튕겨 냈을 것이다.

야수묘왕이 제아무리 십왕의 한 사람이라 해도, 남만인이기에 비교적 과소평가를 받았다 해도 그녀보다는 명백하게 한 수 아래였으니까.

분명 그랬다.

누군가의 일격에 한쪽 팔이 사라지고, 옆구리가 뜯겨 나가기 전까지는.

‘진태경.’

그저 떠올리는 것만으로도 울분이 차오르는 한 사람의 이름.

으득, 이를 악문 남천마후가 발을 뻗었다. 그녀의 신형이 사라졌다. 공격이 무위로 돌아갔음을 깨달은 야수묘왕은 즉각적으로 반응했다.

쉭!

팔 척이 넘는 장대한 체구. 그러나 야수묘왕의 움직임은 바람처럼 빨랐고, 화염이 줄기줄기 쏟아지는 호목(虎目)은 어느덧 그의 옆구리를 향해 쇄도하는 남천마후를 향하고 있었다.

슈화악!

호랑이의 앞발처럼 커다란 손이 공간을 할퀴었다.

서걱!

칼날처럼 일어난 바람이 궁장의 옷자락을 잘라 낸 순간, 야수묘왕의 품을 향해 뛰어든 남천마후가 전력을 다해 일장(一掌)을 뻗었다.

후웅!

본래대로면 살을 짓이기고, 뼈와 내장을 터트려야 했을 일격이다.

그러나 피에 흠뻑 젖은 남천마후의 자그마한 손을 기다리고 있던 것은, 그보다 몇 배나 커다란 야수묘왕의 손바닥이었다.

콰앙!

세상이 뒤흔들렸다. 동시에 마치 극독을 머금은 듯한 혼탁한 내력이 맞닿은 점을 향해 흘러 들어가 한 사람의 내부를 진탕시킨다.

하지만 야수묘왕은 울컥 솟구치는 핏물을 삼키며 웃어 보였다.

“그래, 겨우 이 정도였느냐?”

“……!”

남천마후는 눈을 부릅떴다.

믿을 수 없었다. 감히 야수묘왕 따위가 이런 상황에서도 웃음을 보일 수 있다는 것이.

그리고 전력을 다한 자신의 일장이, 이토록 약해 빠졌다는 것이.

으득.

악문 잇새 사이로 핏줄기가 흘러내린 그때, 남천마후의 신형이 흐릿해졌다.

쉬쉬쉭, 퍼엉!

파공성과 함께 압축된 공기가 터져 나간다.

찰나의 순간, 섬전처럼 전신 곳곳을 후려친 남천마후의 손발에 야수묘왕의 신형이 들썩였다.

하지만 그뿐이었다.

긴 세월 동안 익혀 왔던 외공(外功)은 야수묘왕의 신체를 강철만큼이나 단단하게 만들었고, 진즉 피를 토하며 무릎을 꿇고도 남았을 남천마후의 공격은 전처럼 무겁지 않았다.

아니, 오히려 서서히 위력이 줄어들고 있었다.

‘균열’에서 흘러나온 마기의 기운을 받고 있으나, 앞서 진태경에게 입은 막대한 부상과 그로 인해 흐트러진 심력(心力)마저 어찌할 수는 없었다.

그리고 이 사실을 누구보다 먼저 깨달은 것은, 다름 아닌 남천마후 본인이었다.

‘……지쳤다고? 내가?’

모든 것에는 한계가 있다. 하지만 남천마후는 어느 날부터 자신의 한계를 잊었다. 잊을 수밖에 없었다.

오랜 세월 동안 한계를 느꼈던 적이 없었으니까. 그 누구도 자신을 한계까지 밀어붙이지 못했으니까.

바로 지금처럼.

쉭, 콰득!

무언가에 쫓기듯 쉴 새 없이 울려 퍼지던 파공성이 멎은 순간 남천마후는 손아귀로부터 전해지는 격통을 느꼈다.

우득.

가슴을 후려치고 심장을 터트려야 했을 작은 주먹에서 뼈가 어긋나는 소리가 새어 나온다.

커다란 손바닥으로 남천마후의 주먹을 움켜쥔 야수묘왕이 피에 젖은 이빨을 드러냈다.

“말했었지. 네년의 사지를 찢어 죽이겠다고.”

“……!”

귓가를 파고드는 서늘한 목소리에 실핏줄이 터져 나간 눈동자가 부릅떠진다.

남천마후는 본능적으로 다른 한 손을 뻗어 야수묘왕의 목줄기를 붙잡으려 했지만, 곧이어 눈앞을 가득 채운 녹색 권강을 바라보며 깨달았다.

‘아.’

자신의 한쪽 팔은, 이미 다른 이가 가져갔다는 것을.

퍼어어엉!

세상이 뒤집혔다. 포탄처럼 튕겨 나간 남천마후의 시야가 아득해졌다.

느려진 세상 속, 눈앞에 드리워진 빛과 어둠이 끊임없이 명멸하고 하늘과 땅이 위치를 바꾸며 뒤섞인다.

그리고 그 끝에, 전신을 가루로 만들어 버릴 듯한 충격이 그녀를 기다리고 있었다.

콰아아아앙!

작은 산처럼 쌓여있던 내궁의 잔해. 그 중심을 관통하며 깊숙이 처박힌 남천마후가 왈칵 핏물을 토해 냈다.

“쿠에에엑!”

촤아악.

어둡고, 붉다.

내장 조각이 뒤섞인 검붉은 핏물이, 사방에 가득한 크고 작은 잔해 위에 흩뿌려졌다.

끔찍한 격통과 함께 덜덜 떨리는 몸뚱어리가 느껴졌다.

‘이, 이럴 수는. 이럴 수는 없어.’

현실을 부정하는 한 줄기 생각만이 머릿속을 가득 채운 그때. 남천마후의 흐릿한 시야에 무엇인가 들어왔다

투둑. 툭.

조금씩 들썩이는 잔해와 그 속에서 비틀비틀 일어나는 누군가의 신형.

쉴 새 없이 흔들리던 남천마후의 눈동자에 희미한 빛이 떠올랐다.

희망. 그건 바로 희망이었다.

“나, 나를. 어서 나를…….”

금방이라도 꺼질 듯한 목소리로, 남천마후는 파르르 떨리는 손을 뻗었다.

기이하게 꺾여 나간 두 다리로 천천히 일어나는 신형을 향해.

이미 무언가에 의해 뜯겨 나간 목줄기를 축 늘어트린 채. 괴력난신(怪力亂神)이라는 단어로도 부족할 회복을 기다리는 자신의 충실한 수하를 향해.

“어서, 어서 날 데리고 이곳에서 최대한 멀리…….”

지금 이 순간. 남천마후는 세상 그 누구보다 간절했다.

그녀가 준비했던 대계(大計)는 절반의 성공에 그쳤고, 단 한 번도 생각해 본 적 없던 죽음이 눈앞에 드리워지고 있다.

어떻게든 이 자리에서 도망쳐야 한다.

그렇게라도 살아남고 싶었다. 살아남기만 한다면 후일을 도모할 수 있으니까.

다시 돌아와 또 다른 곳에서 대계를, 복수를 이어나갈 수 있을 테니까.

그러나 남천마후의 마지막 희망은, 다음 순간 복면인의 머리 위에 드리운 그림자와 함께 사그라들었다.

후웅. 콰직!

그림자의 정체는 야수묘왕도, 진태경도. 그리고 또 다른 누군가도 아닌, 그저 거대한 하나의 바위였다.

아마도 충격의 여파였을 것이다.

산처럼 쌓여 있던 잔해 어딘가, 어쩌면 남만야수궁의 주춧돌이었을지도 모르는 천근거석(千斤巨石)은 남천마후의 마지막 희망을 덮쳤다.

이미 오래전 이지(已知)를 상실한 채 그저 주인의 명령만을 따르던 복면인은 바위에 깔려 사지를 움찔거렸다.

그리고 그 광경을 멍하니 바라보던 남천마후의 귓가에, 천둥과도 같은 발걸음 소리가 닿았다.

저벅. 저벅.

핏물을 머금은 땅을. 모래와 잔해를 밟으며 다가오는 발걸음. 아니, 발걸음들.

유난히도 크게 울려 퍼지는 그 걸음들 사이에는 어떠한 괴성도, 날붙이가 부딪치는 소리도 섞여 있지 않았다.

‘아.’

고개를 든 남천마후는 비로소 깨달았다.

이 땅의, 남만의 명운(命運)을 건 치열한 전투는 이미 끝났다는 것을.

그와 더불어 긴 세월 동안 이어진 자신의 명운 또한 마지막을 향해 달려가고 있다는 것을.

그들의 선두에는, 이 모든 상황을 만들어 낸 한 사람이 있었다.

투둑.

핏물로 흠뻑 젖은 맹수의 앞발이 잔해를 밟으며 다가온다.

불과 삼 장의 거리를 두고 멈춰 선 거대한 백호의 등 위에, 꿈에서라도 보기 싫은 얼굴이 그녀를 응시하고 있었다.

“잠깐 못 본 것 같은데…… 많이 예뻐졌네.”

쉭! 푸푹!

본능처럼 쏘아 보낸 지풍(指風)이 진태경의 어깨를 스쳐 지나가 잔해 어딘가를 관통한다.

베어 나간 살갗에서 흐르는 피를 슥 문지른 그가 핏물이 흥건한 손바닥을 핥았다.

“고맙다. 안 그래도 목말랐는데. 이게 할머니의 마음인가 하는 그거냐?”

“……!”

울컥.

악문 잇새 사이로 핏물이 흘러나온다.

온 힘을 쥐어짜 몸을 일으키려는 남천마후의 모습에, 진태경의 머리 위로 십여 자루의 돌격창이 날아왔다.

쐐애애액, 쾅!

단 한 번의 손짓으로 백천대가 쏘아 보낸 돌격창을 튕겨 낸 남천마후가 실핏줄이 터져 나간 눈을 부릅떴다.

“감히!”

화아아악!

공력이 실린 목소리가 사방을 뒤흔들었다. 한쪽 팔을 잃은 데다 막대한 내상까지 입은 남천마후였지만, 균열로부터 흘러나온 마기(魔氣)가 주는 힘은 여전했다.

하지만…….

‘부족해.’

그럼에도 불구하고, 현재의 상황을 뒤집을 수는 없다.

남천마후는 누구보다 그 사실을, 자신에게 닥친 절망적인 현실을 잘 알고 있었다.

그리고 다음 순간 진태경의 양옆에 나란히 선 야수묘왕의 모습을 보며 확신했다.

‘죽는다.’

이렇게 만신창이가 된 몸으로는 아무것도 할 수 없다.

설령 기적적으로 살아남아 이 자리를 빠져나간다 해도, 저 밖에는 수천 명이 넘는 남만의 전사들이 자신을 기다리고 있었다.

필사(必死).

그 두 글자가 상상도 못 한 무게로 전신을 옭아맨다. 머릿속의 모든 생각을 지우고, 어지럽던 마음을 텅 비우게 했다.

그리고 남천마후의 모든 사고가 정지한 그 순간, 나지막한 파공성이 적막을 깨트렸다.

쐐액!

야수묘왕과 수호령. 그리고 진태경.

마치 처음부터 약속이라도 한 것처럼, 그들은 한 줄기의 바람이 되어 쇄도했다.

더 이상 찰나의 틈도, 유언을 남길 시간도 주지 않겠다는 듯이. 남천마후라는 악귀(惡鬼)의 숨통을 끊어 놓겠다는 일념 하나만으로.

콰아아아아!

강대한 녹색 권강이 공기를 짓누른다. 피에 젖은 이빨이 바람을 가른다. 마지막 한 줌의 공력이 실린 투명한 창날이 청백색의 겁화를 머금는다.

그리고 그 모든 광경이, 한 사람의 눈동자에 고스란히 담겼다.

동시에 세상 그 누구보다 아름다웠던 모습을 잃어버린 채, 시시각각 들이닥치는 죽음을 지켜보던 노파의 공허한 눈빛에 희미한 빛이 스며들었다.

‘천주(天主)시여.’

세상 그 누구보다 존귀하며 존엄한 자.

아득한 과거, 남천마후는 천주를 처음 본 순간부터 사랑을 느꼈고 그의 발아래에 엎드려 충성을 맹세했다.

이 하찮은 목숨을 당신을 위해 바치겠노라고.

언젠가 나의 젊음과 아름다움이 사그라지더라도, 먼발치에서나마 영원히 당신의 곁을 지키겠다고.

그때는 몰랐다.

목숨을 바칠 그 날이, 이토록 빨리 찾아오리라고는.

경애해 마지않는 천주의 곁을 지키지 못할 날이 올 것이라고는.

하지만…….

‘부디 기억해 주소서. 이 천녀(賤女)가 당신 곁에 있었음을.’

천주께서 자신을 기억한다면, 누구보다 당신을 사랑했던 종복으로나마 기억된다면 그것으로 충분하다.

그럴 수만 있다면…… 기꺼이 웃으며 남은 생명을 불태울 수 있다.

바로 지금 이 순간처럼.

콰득.

느려진 세상 속, 남천마후는 오직 그녀만이 느낄 수 있는 ‘균열’의 소리를 들었다.

선천지기(先天地氣).

탄생과 함께 품었던 가장 순수하면서도 강력한 힘이 깨어난다.

거대한 미증유의 기운이 전신을 타고 솟구쳐 올라 그녀의 손에 깃들었다.

고오오오옹.

마치 보이지 않는 손이 잡아 찢는것처럼 일그러지는 공간. 경악이 떠오른 세 존재의 얼굴을 보며, 남천마후는 웃었다.

아니, 웃으려 했다.

푹!

남천마후의 등 뒤에 놓인 잔해더미 사이. 그 깊고 어두운 틈새 사이로 튀어나온 한 자루의 검이 그녀의 등에 틀어박히기 전까지는.
```

## Final English reading copy

```markdown
# Chapter 707

The Southern Heaven Demon Empress could not understand.

Why had the grand plan she had never doubted would be perfect fallen into such disarray? And why had she been reduced to the humiliation of matching a mere member of the Ten Kings?

But she had no time to continue wondering.

Whoosh!

A fierce sound of splitting air crushed the wind.

A massive figure surged forward, erasing the space around it. Green Fist Force erupted from the Beast Miao King’s fist, illuminating the world.

Kraaaaaaash!

It had not been that long ago.

If this had been the Southern Heaven Demon Empress of the past—or even the Southern Heaven Demon Empress from just two shichen ago—she would have snorted and deflected that Fist Force.

Even though the Beast Miao King was one of the Ten Kings, and even if he had been relatively underestimated because he was from Nanman, he was clearly a level below her.

That was how it had been.

Until someone’s attack took one of her arms and tore open her side.

*Jin Taekyung.*

A single name that filled her with rage merely by bringing it to mind.

Gritting her teeth, the Southern Heaven Demon Empress thrust out a foot. Her figure vanished.

The Beast Miao King realized that his attack had failed to connect and reacted instantly.

Whoosh!

His towering body stood over eight feet tall. Yet the Beast Miao King moved like the wind, and his tiger eyes, from which flames poured in streams, were already fixed on the Southern Heaven Demon Empress as she rushed toward his side.

Shwaaak!

His enormous hand, as large as a tiger’s forepaw, raked across the air.

Slice!

The wind that rose like a blade cut through the hem of her robe. At that instant, the Southern Heaven Demon Empress leaped into the Beast Miao King’s reach and thrust out a palm with all her strength.

Whoosh!

Under normal circumstances, that strike should have crushed flesh and burst bone and internal organs.

But waiting for the Southern Heaven Demon Empress’s small hand, drenched in blood, was the Beast Miao King’s palm—several times larger than hers.

Boom!

The world shook.

At the same time, murky internal energy, as though laced with deadly poison, flowed toward the point where their palms met and churned one person’s insides.

But the Beast Miao King swallowed the blood surging up his throat and grinned.

“So this is all you’ve got?”

“……!”

The Southern Heaven Demon Empress’s eyes widened.

It was unbelievable. That the Beast Miao King could smile even in a situation like this.

And that her full-strength palm strike had become so pathetically weak.

Crack.

At that moment, blood trickled through the gaps between her clenched teeth, and the Southern Heaven Demon Empress’s figure blurred.

Whoosh-whoosh-whoosh—boom!

Compressed air burst outward with a series of sharp reports.

In the span of an instant, her hands and feet struck every part of the Beast Miao King’s body like flashes of lightning, making his massive frame jolt.

But that was all.

The external arts he had trained for countless years had hardened the Beast Miao King’s body until it was as tough as steel. And the Southern Heaven Demon Empress’s attacks—which should long ago have left the Beast Miao King vomiting blood and collapsing to his knees—were no longer as heavy as before.

No. Their power was gradually diminishing.

The demonic qi flowing from the rift was strengthening her, but it could not undo the massive injuries Jin Taekyung had inflicted on her earlier, nor could it repair the mental strength that had been thrown into disorder as a result.

And the first person to realize this was none other than the Southern Heaven Demon Empress herself.

*…Tired? Me?*

Everything had a limit. But at some point, the Southern Heaven Demon Empress had forgotten her own.

She had no choice but to forget it.

She had not felt her limits in a very long time. No one had been able to push her that far.

Until now.

Whoosh—crack!

The relentless sounds of splitting air, ringing as if something were chasing her, abruptly stopped.

At that moment, the Southern Heaven Demon Empress felt a sharp pain travel through her hand.

Crack.

The bones shifted out of place in the small fist that should have smashed into his chest and burst his heart.

The Beast Miao King seized her fist in his enormous palm and bared his bloodstained teeth.

“I told you. I’d tear off all four of your limbs and kill you.”

“……!”

At the cold voice boring into her ear, the blood vessels in the Southern Heaven Demon Empress’s eyes burst as she stared wide-eyed.

She instinctively reached out with her other hand to seize the Beast Miao King by the throat. But then she saw the green Fist Force filling her vision and realized—

*Ah.*

Someone else had already taken one of her arms.

Boom!

The world turned upside down.

The Southern Heaven Demon Empress’s vision faded as she flew away like a cannonball.

In the slowed-down world, light and darkness flashed endlessly before her eyes. The sky and the earth traded places, twisting together.

And at the end of it all, an impact awaited her—one that seemed capable of grinding her entire body into powder.

Kraaaaaaang!

The ruins of the Inner Palace had been piled up like a small mountain. The Southern Heaven Demon Empress crashed deep into their center, piercing through the mound, and violently vomited blood.

“Kweh-heeeeeck!”

Splash!

It was dark. Red.

Dark-red blood mixed with pieces of internal organs sprayed across the countless large and small fragments scattered in every direction.

She felt her body trembling along with the horrible pain.

*This… This can’t be happening. This can’t be happening.*

At that moment, when a single thought denying reality filled her mind, something entered the Southern Heaven Demon Empress’s blurred field of vision.

Thud. Thud.

The ruins shifted little by little. From within them, someone’s figure staggered upright.

A faint light appeared in the Southern Heaven Demon Empress’s eyes, which had been shaking without pause.

Hope.

That was what it was.

“M-Me. Hurry, take me…”

With a voice that seemed ready to go out at any moment, the Southern Heaven Demon Empress extended her trembling hand.

Toward the figure slowly rising on two legs twisted at unnatural angles.

Toward her loyal subordinate, whose neck hung limply, already torn open by something, and who was awaiting a recovery that surpassed even supernatural powers.

“Hurry. Hurry and take me as far away from here as possible…”

At this moment, the Southern Heaven Demon Empress was more desperate than anyone else in the world.

The grand plan she had prepared had achieved only half of its intended success, and death—something she had never once considered—now loomed before her eyes.

She had to escape this place somehow.

She wanted to survive, even if that was all she could do. If she survived, she could plan for the future.

She could return again and continue her grand plan and her revenge somewhere else.

But the Southern Heaven Demon Empress’s final hope faded the next moment, along with the shadow that fell over the masked man’s head.

Whoosh. Crack!

The thing casting that shadow was not the Beast Miao King, Jin Taekyung, or anyone else.

It was simply a massive boulder.

It had probably been dislodged by the force of the impact.

Somewhere in the ruins piled up like a mountain—perhaps even the foundation stone of the Nanman Beast Palace—a massive stone weighing a thousand geun crashed down over the Southern Heaven Demon Empress’s final hope.

The masked man, who had lost his reason long ago and now did nothing but obey his master’s commands, was crushed beneath the boulder. His limbs twitched.

And as the Southern Heaven Demon Empress stared blankly at the sight, the sound of footsteps like thunder reached her ears.

Thud. Thud.

A footfall approached over blood-soaked ground, treading on sand and rubble.

No—footfalls.

No strange cries or clashing weapons accompanied those unusually loud steps.

*Ah.*

The Southern Heaven Demon Empress raised her head and finally understood.

The fierce battle that had wagered the fate of this land—the fate of Nanman—was already over.

And along with it, the fate she had carried forward for so many years was also nearing its end.

At the head of the approaching group was the person who had created this entire situation.

Thud.

The blood-soaked forepaw of a wild beast stepped over the ruins as it came closer.

A massive White Tiger stopped only three jang away. On its back, a face she never wanted to see again—not even in a dream—stared down at her.

“Feels like it’s been a while since I last saw you… You’ve gotten a lot prettier.”

Whoosh! Thud!

The Finger Qi she fired on instinct grazed Jin Taekyung’s shoulder and pierced through some part of the ruins behind him.

He casually rubbed the blood flowing from the cut, then licked his palm, wet with blood.

“Thanks. I was thirsty anyway. Is this what they mean by a grandmother’s affection?”

“……!”

A surge of blood welled up and leaked through her clenched teeth.

As she forced every last bit of strength into her body and tried to rise, a dozen or so spears flew over Jin Taekyung’s head.

Whiiiiiiish—boom!

With a single wave of her hand, the Southern Heaven Demon Empress knocked away the assault spears fired by the Baekcheon Unit. The blood vessels in her eyes burst as she glared at Jin Taekyung.

“How dare you!”

Fwoooooosh!

Her voice, carrying internal energy, shook the surroundings.

The Southern Heaven Demon Empress had lost one arm and suffered massive Internal Injury, but the power granted by the demonic qi flowing from the rift remained.

But…

*It’s not enough.*

Even so, she could not overturn the current situation.

The Southern Heaven Demon Empress understood that better than anyone. She knew the desperate reality that had befallen her.

And when she saw the Beast Miao King standing beside Jin Taekyung, she became certain.

*I’m going to die.*

In a body reduced to this state, she could do nothing.

Even if she miraculously survived and escaped this place, thousands of Nanman warriors were waiting for her outside.

Certain death.

Those two words bound her entire body with an unimaginable weight. They erased every thought from her mind and emptied her confused heart.

Then, at the moment all of the Southern Heaven Demon Empress’s thoughts stopped, a low sound of splitting air broke the silence.

Whoosh!

The Beast Miao King, the guardian spirit, and Jin Taekyung.

As though they had agreed from the start, they became a single streak of wind and surged forward—as if to deny her even the briefest opening, let alone time for final words.

They had only one resolve: to cut off the breath of the Fiend known as the Southern Heaven Demon Empress.

Kraaaaaaaash!

Powerful green Fist Force pressed down on the air.

Bloodstained teeth tore through the wind.

A transparent spearhead carrying the last handful of internal energy held blue-white hellfire within it.

And every one of those sights was reflected in a single person’s eyes.

At the same time, a faint light entered the empty gaze of the old woman watching death approach from every direction, second by second, after losing the beauty she had once possessed above all others.

*Lord of Heaven.*

The most noble and dignified being in the world.

In the distant past, the Southern Heaven Demon Empress had felt love from the moment she first saw the Lord of Heaven, and she had prostrated herself at his feet and sworn her loyalty.

She had vowed to offer that insignificant life for him.

Even if her youth and beauty faded someday, she had promised to remain by his side forever, even if only from a distance.

She had not known then.

She had not known that the day she would offer her life would come so soon.

She had not known that a day would come when she could no longer remain at the side of the Lord of Heaven she revered above all else.

But…

*Please remember me. Remember that this lowly woman once stood at your side.*

If the Lord of Heaven remembered her—if he remembered her as a servant who had loved him more than anyone else—that would be enough.

If only that could happen…

She could gladly burn through the life she had left with a smile.

Just as she was doing at this very moment.

Crack.

In the slowed-down world, the Southern Heaven Demon Empress heard the sound of the *rift*—a sound only she could perceive.

Innate qi.

The purest and most powerful force she had carried since birth awakened.

A vast, unprecedented energy surged through her entire body and gathered in her hand.

Gooooooooong.

Space twisted, as though invisible hands were tearing it apart.

Looking at the astonished faces of the three beings before her, the Southern Heaven Demon Empress smiled.

No—she tried to smile.

Thud!

Until a sword thrust out from the heap of ruins behind her and buried itself in her back, emerging from the deep, dark gap between the fallen stones.
```
