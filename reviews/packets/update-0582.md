<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0582.txt",
      "sha256": "fde16aec70ec70170de36c1052f61337ff0bf63562f626874b7ee9998e54581b",
      "bytes": 14746
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c2a8d3e4bd60189506fa9dcf625f08af713629f0cd3b4044ac7f93e57d7f1bda",
      "bytes": 2596
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "872b44b3bc2143b0aa83b6931c9399ee529a7f8a4a234f65ffa2f3c90f0bd7f1",
      "bytes": 182629
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "f07c5c69df838780974ac3ef5a2d558fedf2ef531c3811ef08d6e1d35dd40945",
      "bytes": 730
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "1e3f25c6bd4c0b8fd65dfc0114a4084afe1693b0bb30c2508abf30a43b995918",
      "bytes": 590
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "5647539a62770c6aecdb5e7e189fdb3f6475a0d8bbeadb8bbebf8844a0d48ecc",
      "bytes": 562
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "2b3edae766337605fc350216dc3e40407044a47b90bf306516c4e71c68c3ab1b",
      "bytes": 538
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "98a0e7ff18d5826a6ebd88c881aa6ffee288743b065100a674edbcd8356bd4a6",
      "bytes": 1080
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "c776a094cb99fb1ce6185588424195bed017ebaec223e6efb18322d75b11714a",
      "bytes": 951
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6e2761f01fdbcea3667a47286683f8bd548b73d24c7372cfdee895dcf82ac342",
      "bytes": 180237
    }
  ],
  "estimated_tokens": 10777
}
-->

# Durable State Update — Chapter 582

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 582. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 582. Profile updates may replace only one
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
  "chapter": 582,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 582,
    "continuity_sources": [582],
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
    "Song Cheonwoo says Cheon Taemin suddenly collapsed more than twenty years ago and has remained unconscious, but no one knows why.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition, waited two years, conducted experiments, and purged aides who knew the truth.",
    "Hwa-jong was not told about Taemin's condition and remains loyal to Choi Minwoo.",
    "Song claims Taemin is still alive, but his location is unknown and Area A is only suspected.",
    "Choi Minwoo has confirmed Song's account enough to treat Taemin's status as genuine while continuing to investigate.",
    "Busan's Kraken has been eliminated, but more than one thousand Mermen remain across Haeundae and Gwangalli while the Peace Guild and other forces contain the disaster.",
    "Go Jun seized Song Cheonwoo's children as leverage and used the threat to force Song to attack Choi Minwoo.",
    "Go Jun used an S-grade Magic Gem to artificially cause the Busan Monster Wave and sent Kim Ho-jung to Busan.",
    "Go Jun intends to kill Choi Minwoo through Song Cheonwoo and may be relying on another unidentified being.",
    "Song Cheonwoo was killed after falling into an abyss and being attacked by an unidentified monster.",
    "The unused object in Song Cheonwoo's pocket released darkness that became light after his death.",
    "The B-grade Yeti's Winter Range Gate in Pyeongchang has opened a Monster Wave that connects the Gate to the modern world, with Choi Minwoo and Kim Hwajong at the scene."
  ],
  "continuity_sources": [
    581,
    580
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept unused in his pocket, and what did its release of darkness and light accomplish?",
    "How will Choi Minwoo and Kim Hwajong respond to the Monster Wave that has opened from the Yeti's Winter Range Gate?"
  ],
  "safe_through": 581,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Yeti's Necklace for 예티의 목걸이, Hyung for 형님, and S-grade Magic Gem for S급 마정석."
  ],
  "version": 1
}
```

## Exact glossary matches

| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 평화 | **Peace Guild** | Guild name. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 광안 | **Guang'an** | Sichuan location where the party boards Mu Song's ship. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 광안대교 | **Gwangan Bridge** | Busan suspension bridge central to Taekyung's childhood memory and the current disaster. |
| 머맨 | **Merman** | Sea monster species serving under the Kraken. |
| 평창 | **Pyeongchang** | Location in Gangwon Province where the Gate is situated. |
| 예티 | **yeti** | Monster species in the Gate's name and raid dialogue. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 송천우 | 화종 | former_allies | Hwa-jong | familiar and informal | Song uses Hwa-jong's personal name, prompting Hwa-jong to reject the familiarity. |
| 화종 | 송천우 | former_allies_now_hostile | you | formal and cold | Hwa-jong challenges Song's right to expect Choi's trust and rejects their former intimacy. |
| 송천우 | 최민우 | older_former_ally_to_younger_former_ally | Minwoo | familiar and informal | Song addresses Choi by his given name while discussing the meeting place and surveillance. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 최민우 | 화종 | Young Master to butler | Butler Kim | formal and respectful | Choi refers to Hwa-jong as 김 집사님 while discussing the concealed truth. |
| 최민우 | 송천우 | temporary ally to rival | Regional Director | formal and cutting | Choi uses 지사장님 while condemning Song's survival and concealment. |
| 송천우 | 천태민 | former subordinate to revered older brother by respect | Hyung | reverent and familiar; shocked | Song Cheonwoo recognizes Cheon Taemin's blood in Choi Minwoo and mutters 형님 while facing Choi. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 579
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he is believed to remain alive after more than twenty years of unconsciousness, with Area A only suspected as his location.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 581
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 581
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 581
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong is a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort.
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 581
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; after being forced to attack Choi Minwoo to protect his hostage family, he fell into an abyss and was killed by an unidentified monster.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, helped conceal Taemin's condition and purge aides who knew the truth, negotiated the European regional director position to save himself and his family, and had his children seized by Go Jun as leverage that forced him to attack Choi Minwoo.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 581
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and is mobilizing every available power to unseat Go Jun from Ares Guild leadership.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃582화



이것을 무엇이라 불러야 할까.

최민우, 김화종. 그리고 게이트 밖을 지키고 있던 평화 길드의 정예 헌터 스무 명.

모두가 같은 의문을 품었으나, 그 누구도 답하지 못했다. 아니, 답할 수 없었다.

단지 아연한 눈빛으로 현세에 도래한 ‘그것’을 바라볼 뿐이었다.

- 그아아아아아!

하늘을 떨어 울리는 천둥 같은 괴성.

그것은 하마였고, 코끼리인 동시에 소였으며, 코뿔소이기도 했다. 그러나 동시에 그 무엇도 아니었다.

그것은 짐승이라고 부르기에는 너무나도 거대하면서 강했으니까.

후우우웅. 콰직!

단 한 걸음. 그러나 그 여파는 엄청났다.

반경 십여 미터를 뒤덮은 그림자와 함께 거대한 앞발이 게이트 관리소를 짓이긴다.

지진이라도 난 것처럼 땅이 흔들리고, 산 밑으로 연결되는 케이블 선이 끊어지며 곤돌라가 추락했다.

그리고 다음 순간, 김화종은 까마득한 과거의 기억 속에서 어떤 괴물의 이름을 떠올렸다.

“……베히모스(Behemoth).”

베히모스. 혹은 베헤모스.

히브리어로 짐승을 뜻하는 것에서 유래된 괴물의 이름.

깊고 어두운 심연에서 일어난 신화 속 괴물의 흔적은 성경에서도 찾아볼 수 있었다.

베헤못을 보아라. 내가 너를 만든 것처럼, 그것도 내가 만들었다.

그것이 소처럼 풀을 뜯지만.

그러나 성경에 적힌 기록은 틀렸다.

어떤 존재가 저 괴물을 만들었는지는 몰라도, 베히모스는 풀을 뜯고 연못에서 물을 마시는 평화로운 생명체와는 거리가 멀었다.

콰직! 콰드드득!

- 쿠워, 쿠워어어!

게이트가 열리며 세상 밖으로 나온 것은 베히모스뿐만이 아니었다.

비명과도 같은 울음소리를 내지르며 도망치는 이백여 마리의 예티들. 베히모스의 첫 목표는 바로 놈들이었다.

이 거대한 생명체는 동족인 동시에 부하인 놈들을 가차 없이 짓밟고, 씹어 삼켰다.

촤악, 투두두둑!

푸른 핏물이 비가 되어 떨어져 내린다.

신전의 기둥과도 같은 네 개의 다리가 땅을 짓밟고, 코끼리의 상아를 닮은 엄니가 지면을 스칠 때마다 잘려나간 괴물의 사지와 핏물이 뿜어져 나왔다.

누군가의 입술 사이로 덜덜 떨리는 음성이 흘러나왔다.

“이, 이건…….”

보는 것만으로도 절망을 불러일으키는 광경.

그리고 모두가 얼어붙은 채, 넋 나간 시선으로 처참하게 죽음을 맞이하는 예티 무리의 모습을 지켜보던 그때였다.

화아아악!

어느새 주위에 내려앉은 검은 안개 너머로, 눈부신 광휘가 솟구쳤다.

따뜻한 온기가 서린 빛은 안개를 밀어 내며 조금씩, 조금씩 그 범위를 넓혀 갔다.

그제야 참았던 숨을 토해 낸 사람들이 광휘의 근원지를 찾았다.

이십여 쌍의 눈동자. 그들의 시선이 닿은 곳에, 휘황한 빛을 토해 내는 검을 든 한 청년이 있었다.

어느 때보다 빛나는 눈동자를 한 그가 입을 열었다.

“모두, 내 뒤로.”

“……!”

침착한 목소리가 귓가를 파고든 순간, 평화 길드의 헌터들은 비로소 자신들이 베히모스가 뿜어내는 피어(Fear)의 영향에서 벗어났음을 깨달았고, 이 광경을 지켜보던 한 사람은 전율로 몸을 떨었다.

‘이건.’

더없이 익숙하고, 아련한 기분.

과거의 기억 속에서, 이제는 흐릿해진 누군가의 얼굴을 떠올린 김화종이 중얼거렸다.

“여기 계셨군요.”

과거와 현재가 겹쳐진다. 지금 김화종의 눈동자에 비친 것은 천태민인 동시에 최민우였고, 최민우인 동시에 천태민이었다.

그와 같은 것을 본 송천우는 절망을 느꼈지만, 노집사는 이 위태로운 상황 속에서도 가슴 깊숙이 차오르는 기쁨을 느꼈다.

그는 홀로 빛나는 청년의 옆에 섰다.

화르르르륵!

길고 맹렬한 불의 채찍이 양손에 잡힌다. 김화종과 시선이 마주친 최민우가 침착한 얼굴로 입을 열었다.

“놈을 막아야 합니다. 무슨 수를 써서라도.”

목소리에서 결코 물러서지 않겠다는 의지가 묻어나온다. 이미 산 아래에서는 이변을 알아차린 이들의 비명이 울려 퍼지고 있었다.

“꺄아아아악!”

“으아, 으아아!”

- 그아아아아아!

이백여 마리의 예티를 도륙 중인 베히모스의 포효에, 산에 쌓여 있던 눈이 파도처럼 쓸려 내려간다.

새된 비명과 함께 언뜻 보기에도 천 명이 훌쩍 넘어가는 사람들이 이리저리 흩어지고 있었다.

만약 그들이 천운으로 눈앞의 괴수를 피해 도망친다면, 베히모스의 다음 표적은 저들이 될 것이다.

최민우와 김화종. 그리고 이 자리에 모인 평화 길드의 헌터들은 그 사실을 잘 알고 있었다.

자신들만으로는 저 괴물을 상대할 수 없다는 사실 역시도.

“티, 팀장님.”

모두가 상위 헌터의 실력을 지니고 있지만, 상대는 신화 속에서나 등장하는 괴수다. 누군가의 두려움 섞인 목소리에 최민우가 대답했다.

“강요하지 않겠습니다. 도망치고 싶다면, 도망치세요.”

술렁임이 시작되기도 전에, 나직한 목소리가 이어졌다.

“하지만 잊지 마십시오. 자신이 이 자리에서 어떤 선택을 했는지. 스스로를 헌터라고 부를 수 있는지.”

“……!”

흔들리던 눈동자의 떨림이 멎었다. 최민우의 손에 들린 검에서는 그 어느 때보다 환한 광휘가 흘러나오고 있었다.

[영웅의 혼]. 자격을 갖춘 자에게 한하여 영웅에 걸맞은 힘을 부여하는 에고 소드.

우웅. 화아아악.

검신이 거세게 몸을 떨었다. 섬광처럼 터져 나온 빛이 어둠을 밀어내고 빛에 담긴 온기가 모두를 감싼다.

어느덧 황금빛으로 물든 최민우의 눈동자에, 마침내 동족을 모조리 먹어치운 베히모스의 모습이 비쳤다.

“우리가 받은 힘은…… 이런 날을 위해 주어진 것이 아닙니까.”

단 한 사람의 예외도 없다. 이 자리에 있는 이들은 어느 날 알 수 없는 누군가에게 선택을 받았고, 평범함을 벗어난 힘을 얻게 되었다.

그리고 그 힘에는 의무와 사명감이 따른다.

헌터(Hunter).

인류를 지키는 검이고, 위협에서 보호하는 방패이며, 몬스터와의 전투에서 늘 선두에 서야 하는 수호자.

그들이 얻게 된 부와 명예로 퇴색되었을지언정, 그 순수한 본질만은 남아 있다.

“공격 대형. 갖춰.”

저벅.

최민우는 걸음을 내디뎠다. 그의 발걸음을 따라 빛이 움직이고, 그 뒤를 김화종과 스무 명의 헌터가 따랐다.

그리고 화살과도 같은 공격 대형을 갖춘 채 나아가는 그들의 모습이, 새로운 세상에서의 첫 번째 식사를 끝마친 괴물의 거대한 눈동자에 비쳤다.

- 그. 아. 아. 아. 아.

괴물, 베히모스는 비웃음과도 같은 울음소리를 흘렸다. 수백의 예티를 먹어치웠음에도 그것은 여전히 굶주렸다.

불쾌한 빛을 뿜어내며 자신을 향해 다가오는 인간들을 짓밟고, 씹어 삼킬 준비가 되어 있었다.

- 오. 너. 라. 인. 간. 들. 이. 여.

이 자리에 베히모스의 마계어(魔界語)를 알아들을 수 있는 사람은 없다.

그러나 그 의미만큼은 모두에게 고스란히 전해졌다.

스르릉. 화륵.

무기가 뽑힌다. 발현된 마법이 스태프와 손을 타고 솟구친다.

짙은 어둠 속에서 광휘를 받아 밝게 빛나는 스물두 명의 헌터들.

그리고 팽팽한 활시위처럼 당겨진 그들을 쏘아 보낸 것은, 선두에 선 최민우의 외침이었다.

“돌격-!”

귀가 먹먹해질 만큼 거대한 함성과 함께, 그들은 하나의 화살이 되어 쏘아졌다

쐐애애애액!

어둠을 가르는 한 줄기의 빛. 그 끝에 선 괴수가 심연에서 끌어올린 듯한 괴성을 내질렀다.

- 콰우우우우!

다음 순간.

꽈앙! 콰드드득!

함성과 괴성이, 빛과 어둠이 뒤섞였다.



* * *



- 키잇!

“아가리 닥쳐. 이 개새꺄.”

뻑!

둔중한 타격음과 함께 머맨의 머리통이 사라졌다.

하지만 나는 굳이 놈의 죽음을 확인하지 않았다. 사체가 쓰러지기도 전에 신형을 튕겨 도망치는 머맨들을 가로막았다.

“똥이란 똥은 죄다 싸질러 놓고, 이제 와서 도망치는 건 어느 나라 상도덕이냐. 안 그래?”

- 키, 키이잇.

살고자 하는 간절함이 가득한 울음소리. 하지만 이미 늦었다. 놈들은 몬스터고, 난 인간이다.

더군다나 부산에까지 기어들어 와서 똥을 싸질렀으면, 그에 대한 변상은 반드시 치러야 한다.

이에는 이. 목숨에는 목숨으로.

나는 망설임 없이 손에 쥔 백염을 휘둘렀다.

후웅!

창날을 타고 솟구친 불길이 횡으로 뻗어 나간다.

화룡일미(火龍一尾). 막강한 열기가 담긴 화룡의 꼬리가 단숨에 오십여 마리의 머맨을 후려치자, 살이 타들어 가는 끔찍한 악취와 함께 괴성이 울려 퍼졌다.

- 끼이이이잇!

애처로운 단말마. 나는 가장 가까운 머맨을 빠르게 스쳐 지나갔다.

서걱. 희미한 절삭음과 함께 놈의 머리가 붕 떠오르는 것이 바짝 곤두선 감각을 타고 느껴졌다.

하지만 아직이다.

한데 모여 퇴로(退路)를 물색하던 놈들의 숫자는 자그마치 오백여 마리에 달했고, 그것은 곧 내가 이 자리에서 죽여야 할 몬스터의 숫자와 같다는 뜻이었다.

서걱. 서걱. 쉬쉬쉬쉬쉭!

핏물과 함께 몬스터의 사지가 솟구쳤다. 창이 그린 궤적에 걸려든 모든 것이 잘려 나가고, 펼쳐진 손바닥에서부터 터져 나온 화염신장(火焰神掌)의 장력이 이십여 마리의 머맨을 불태웠다.

화륵, 콰아아아!

뜨거웠다.

초고온의 열기에 녹아내린 아스팔트가 그러했고, 버스의 옆구리를 박은 채 공회전하는 자동차의 타이어가 그랬으며, 엑셀을 밟은 채 죽어 있는 운전자를 바라보는 내 마음이 그랬다.

툭. 투둑.

깨진 유리창을 적신 핏물이 보닛을 타고 흘러내린다.

최첨단 에어백도 운전석 앞 유리창을 뚫고 가슴에 박힌 삼지창을 막아내진 못한 모양이다.

이미 빛이 빠져나간 중년인의 눈동자는 공허했고, 백미러에 부적처럼 매달아 놓은 가족사진은 피에 젖어 있었다.

중년의 부모. 초등학생쯤으로 보이는 남자아이와 그보다도 어려 보이는 여자아이.

더욱 좆 같은 사실은…… 사진 속의 가족이 모두 차 안에 있다는 점이다. 하나같이 웃음을 잃은 채로. 전신에 피를 뒤집어쓴 채로.

“이…… 개씨발 새끼들아!”

화륵. 콰아아아!

더욱 맹렬해진 불길이 몬스터를 집어삼켰다.

나는 불길이 만든 길을 따라 가로지르며 창을 휘둘렀다. 쉬지 않고 베고, 가르고, 찢고, 부수었다.

뜨거운 열기와 증발하는 핏물 사이에서 문득 그런 생각이 들었다.

‘어쩌면.’

어쩌면 이들도 여행을 온 것은 아니었을까. 몇 년 만에 부산으로 떠난 가족 여행에서, 즐겁게 웃고 떠들다가 몬스터를 만난 것은 아닐까.

얼마 떨어지지 않은 광안대교를 보며, 이 부자(父子)는 지킬 수 없는 약속을 한 것이 아닐까.

퍼걱!

내뻗은 주먹이 단단한 비늘을 뚫고 뼈와 살을 부수었다.

나는 킷, 하고 짧은 신음을 토하는 머맨을 말없이 바라보다가, 손아귀에 닿은 뭉클한 무언가를 그대로 잡아 뜯었다.

푸화아악! 털썩!

손을 빼내기가 무섭게, 녹색 핏물이 얼굴에 튀었다. 끔찍한 악취가 풍겼지만 이미 전신에 핏물을 뒤집어쓴 후라 상관없었다.

나는 눈을 부릅뜬 채 쓰러진 머맨의 사체 위로 막 뽑아낸 심장을 떨어트렸다.

툭.

그리고 믿을 수 없다는 놈의 눈빛이, 원통해하는 듯한 표정이 마음에 들지 않아서 발로 짓밟았다.

콰득. 펑.

그제야 비로소 깨달을 수 있었다. 더 이상 주위에서 덤벼드는 몬스터가 없다는 사실을. 도망치는 놈도, 살아 있는 놈도 없다는 사실을.

내가 녹색 피 웅덩이에서 뜨거운 숨을 뱉어 낸 그때였다.

“……간악한 인간이여. 너.”

“왜.”

고개를 돌리며 묻는 나와 눈빛이 마주친 스켈레톤 킹이 한숨을 내쉬었다.

“아니, 아니다.”

지금 녀석의 눈동자에 비친 나는 어떤 모습을 하고 있을까. 문득 그런 생각이 들었으나 묻지는 않았다.

스켈레톤 킹의 등 뒤에 선 백여 명의 헌터들의 눈빛만 봐도 대충 알 것 같았기 때문이었다.

“여긴 끝났습니다.”

나 스스로도 남의 것처럼 낯선, 건조한 목소리에 상급자로 보이는 헌터가 화들짝 놀라며 대답했다.

“예? 아, 예. 예.”

“다른 곳은 어떻게 되어 가고 있습니까?”

“저, 저놈들이 마지막이었습니다. 병력을 모아 한번에 치려고 했는데…….”

꿀꺽.

마른침을 삼킨 그가 말을 이었다.

“잘 정리된 것 같군요.”

“그럼 다행이고요. 너도 고생했다.”

나는 스켈레톤 킹의 어깨를 툭 친 다음, 다시 걷기 시작했다. 어디 가냐는 물음에 짧게 대답했다.

“사람들 구해야지. 지금도 죽어 가는 사람들. 아직까지 살아남은 사람들.”

피곤하다. 육체보다는 정신적인 피로가 더 컸다. 하지만 지금은 쉴 수 없었다.

아직도 어딘가에서 죽음의 공포에 맞선 채 구조를 기다리는 이들이 있을 테니까. 한 사람이라도 구해야 했다.

그리고…….

철벅.

녹색 핏물로 이루어진 발자국이 도심의 아스팔트를 밟은 그 순간이었다.

치직. 치지직.

거슬리는 기계음과 함께, 고층 빌딩의 전광판이 깜빡인다. 노이즈 낀 화면 속에서 익숙한 얼굴이 모습을 드러냈다.

재수 없을 만큼 잘생긴 외모. 바로 최 팀장이다. 동시에 작은 자료 화면과 함께 자막이 떴다.



[평화 길드 최민우 헌터. 평창에서 발생한 몬스터 웨이브에 휘말려…….]



이런 씨발.
```

## Final English reading copy

```markdown
# Chapter 582

What should this be called?

Choi Minwoo, Kim Hwajong, and the twenty elite Hunters from the Peace Guild guarding the Gate from outside.

They all shared the same question, but no one could answer it. No—they couldn’t answer it.

All they could do was stare at *it*, which had arrived in the modern world, with bewildered expressions.

—GRAAAAAAAH!

A thunderous roar shook the sky.

It was a hippopotamus, an elephant, an ox, and a rhinoceros all at once. And yet it was none of those things.

It was simply too enormous and powerful to be called a beast.

*Whoooosh. CRUNCH!*

One step.

But the impact was tremendous.

A huge foreleg crushed the Gate control station beneath a shadow that covered more than ten meters around it.

The ground shook as if an earthquake had struck. The cable lines running down toward the foot of the mountain snapped, and a gondola came crashing down.

And in the next moment, Kim Hwajong recalled the name of a monster from a distant memory.

“…Behemoth.”

Behemoth. Or Behemos.

The name of a monster derived from the Hebrew word for “beast.”

Traces of the mythical monster that had risen from a deep, dark abyss could even be found in the Bible.

> Look at Behemoth. Just as I made you, I made it too.
>
> It grazes grass like an ox.

But the record written in the Bible was wrong.

Kim Hwajong did not know what kind of being had created that monster, but Behemoth was far removed from a peaceful creature that grazed on grass and drank water from ponds.

*CRUNCH! CRRRUNCH!*

—Kwooh! Kwoooooh!

Behemoth was not the only thing to emerge from the Gate and enter the world.

More than two hundred yetis fled, their cries sounding like screams.

Behemoth’s first target was them.

The enormous creature mercilessly trampled and devoured the creatures that were both its kind and its subordinates.

*SHAAK! Thud-thud-thud!*

Blue blood fell like rain.

Four legs like the pillars of a temple stamped across the earth. Every time tusks resembling an elephant’s ivory scraped across the ground, severed limbs and blood burst from the monsters beneath them.

A trembling voice escaped between someone’s lips.

“T-This is…”

The sight alone was enough to inspire despair.

Everyone stood frozen, watching the yeti horde meet a gruesome death with vacant eyes.

Then—

*FWOOOOSH!*

Beyond the black mist that had settled around them, dazzling radiance surged upward.

The light, infused with warm energy, pushed back the mist and gradually expanded its range.

Only then did the people who had been holding their breath finally exhale and search for the source of the radiance.

Twenty-odd pairs of eyes.

Where their gazes fell, a young man stood holding a sword that spewed forth brilliant light.

His eyes shone brighter than ever as he opened his mouth.

“Everyone, behind me.”

“...!”

The moment his calm voice reached their ears, the Peace Guild Hunters finally realized that they had escaped the influence of the Fear emanating from Behemoth.

And one person watching the scene trembled with emotion.

*This is…*

A feeling both deeply familiar and achingly distant.

Kim Hwajong recalled the face of someone whose features had faded in his memories of the past and murmured,

“So you were here.”

The past and present overlapped.

What Kim Hwajong saw reflected in his eyes was Cheon Taemin and Choi Minwoo at the same time—and Choi Minwoo and Cheon Taemin at the same time.

Song Cheonwoo, who saw the same thing, felt despair.

But the old butler felt joy welling up from deep within his chest, even in this precarious situation.

He stepped to the side of the young man shining alone.

*FWOOSH!*

Long, fierce whips of flame appeared in both his hands.

Choi Minwoo met Kim Hwajong’s gaze and spoke with a composed expression.

“We have to stop it. No matter what it takes.”

His voice carried an unshakable determination not to retreat.

Down below the mountain, the screams of people who had noticed the anomaly were already echoing through the air.

“Aaaah!”

“A-Aaaah!”

—GRAAAAAAAH!

Behemoth’s roar as it slaughtered the two hundred yetis sent the snow piled up on the mountain sliding down like a wave.

More than a thousand people scattered in every direction, screaming in shrill voices.

If the Hunters escaped the monster before them through sheer luck, those people would become Behemoth’s next targets.

Choi Minwoo, Kim Hwajong, and the Peace Guild Hunters gathered there all knew that.

They also knew that they could not face that monster on their own.

“L-Team Leader.”

They all possessed the strength of high-level Hunters, but their opponent was a monster that appeared only in mythology.

At the sound of the fear-stricken voice, Choi Minwoo answered.

“I won’t force you. If you want to run, run.”

Before the murmuring could even begin, he continued in a quiet voice.

“But don’t forget what choice you made here today. Whether you can still call yourself a Hunter.”

“...!”

The trembling in their wavering eyes stopped.

The sword in Choi Minwoo’s hand was radiating a brighter light than ever.

[Hero’s Soul].

An ego sword that granted the strength befitting a hero only to those who possessed the necessary qualifications.

*Hummm. Fwoooosh.*

The blade trembled violently.

Light burst forth like a flash, pushing back the darkness. The warmth contained within it wrapped around everyone.

By then, Choi Minwoo’s eyes had turned golden, and Behemoth’s form was reflected in them as it finished devouring every last one of its kind.

“Wasn’t the power we received given to us for a day like this?”

There was not a single exception.

Everyone gathered here had been chosen one day by someone unknown and had gained power beyond the ordinary.

And that power came with duty and a sense of responsibility.

Hunters.

The sword that protected humanity, the shield that defended it from threats, and the guardians who had to stand at the forefront of every battle against monsters.

Their wealth and fame might have dulled that ideal, but its pure essence remained.

“Attack formation. Take your positions.”

*Step.*

Choi Minwoo moved forward.

The light moved with his footsteps, followed by Kim Hwajong and the twenty Hunters.

They advanced in an arrowhead formation, and their figures were reflected in the enormous eyes of the monster that had just finished its first meal in this new world.

—G. R. A. A. A. A. H.

The monster, Behemoth, let out a cry that sounded almost like a sneer.

Even after devouring hundreds of yetis, it was still hungry.

It was ready to trample, chew, and swallow the humans approaching it while radiating that irritating light.

—Come. Hu. Mans.

No one there could understand Behemoth’s Demon Realm language.

But everyone understood its meaning perfectly.

*Shing. Fwoosh.*

Weapons were drawn.

Manifested magic surged through staffs and hands.

Twenty-two Hunters shone brightly in the deep darkness, bathed in the radiance.

And the shout of Choi Minwoo at the front launched them forward, taut as bowstrings.

“Charge!”

With a roar enormous enough to leave their ears ringing, they shot forward as one arrow.

*SHWAAAAAAK!*

A single ray of light cut through the darkness.

At its tip, the monster raised a roar that seemed to have been dragged up from the depths of an abyss.

—KWOAAAAAAH!

The next moment—

*BOOOOM! CRRRUNCH!*

Shouts and roars, light and darkness, all blended together.

* * *

—Kik!

“Shut your mouth, you fucking bastard.”

*Wham!*

With a heavy impact, the Merman’s head disappeared.

But I didn’t bother confirming its death.

Before the corpse had even fallen, I launched myself forward and blocked the Mermen trying to flee.

“You shit everywhere you go, then run away when it’s time to pay up. What kind of business ethics is that? Huh?”

—K-Kiiik.

Their cries were filled with a desperate desire to live.

But it was too late.

They were monsters, and I was human.

Besides, if they had crawled all the way to Busan and shit everywhere, they had to pay compensation for it.

An eye for an eye.

A life for a life.

Without hesitation, I swung White Flame in my hand.

*Whoosh!*

Flames surged along the spearhead and swept horizontally.

Fire Dragon’s Single Tail.

The fire dragon’s tail, packed with immense heat, lashed fifty Mermen in a single strike.

Their screams rang out alongside the horrific stench of flesh burning away.

—KIEEEEEEK!

A pitiful death cry.

I swiftly passed the nearest Merman.

*Slice.*

I felt its head rise into the air through my heightened senses, accompanied by the faint sound of something being cut.

But it wasn’t over yet.

There had been more than five hundred of them gathered together while searching for an escape route.

That meant there were just as many monsters I had to kill here.

*Slice. Slice. Shhhhhk!*

Monster limbs flew through the air with sprays of blood.

Everything caught in the path of my spear was sliced apart, while the force of Flame Divine Palm bursting from my outstretched palm burned more than twenty Mermen.

*Fwoosh! KRAAAASH!*

It was hot.

The asphalt melting beneath the ultra-high heat was hot.

So were the tires of the car spinning uselessly after slamming into the side of a bus.

And so was my heart as I looked at the driver who had died with his foot still on the accelerator.

*Drip. Drip.*

Blood ran over the hood after soaking the shattered windshield.

Apparently, even the most advanced airbag couldn’t stop the trident that had pierced through the windshield and embedded itself in the driver’s chest.

The eyes of the middle-aged man had already lost their light and were hollow.

The family photograph hanging from the rearview mirror like a talisman was soaked in blood.

Middle-aged parents.

A boy who looked like he was in elementary school, and a girl who looked even younger.

The worst fucking part was that the entire family in the photograph was inside the car.

Every one of them had lost their smiles.

Every one of them was covered in blood from head to toe.

“You fucking bastards!”

*Fwoosh! KRAAAASH!*

The flames grew even more ferocious and swallowed the monsters.

I cut across the path created by the fire, swinging my spear.

I kept cutting, slicing, tearing, and smashing without pause.

Between the scorching heat and the evaporating blood, a thought suddenly crossed my mind.

*Maybe.*

Maybe they had been traveling too.

Maybe they had gone on a family trip to Busan for the first time in years, laughing and chatting happily before they encountered the monsters.

Looking at Gwangan Bridge not far away, maybe this father and son had made a promise they could never keep.

*Crack!*

My fist punched through hard scales and crushed bone and flesh.

I silently looked at the Merman that let out a short groan.

Then I grabbed the warm, pulpy thing my hand had touched and tore it out.

*SPURT! Thud!*

The moment I pulled my hand free, green blood splashed across my face.

The stench was horrific, but I didn’t care. I was already covered in blood from head to toe.

With my eyes wide open, I dropped the heart I had just ripped out onto the corpse of the fallen Merman.

*Plop.*

Then I stomped on it because I disliked the disbelief in its eyes and the expression that seemed to accuse the world of wronging it.

*CRUNCH. Pop.*

Only then did I realize it.

There were no more monsters attacking me from all around.

There were no monsters fleeing.

There were no monsters still alive.

I was breathing heavily in the pool of green blood when—

“…Wicked human. You.”

“Why?”

The Skeleton King met my gaze as I turned my head and asked, then let out a sigh.

“No. Never mind.”

I briefly wondered what kind of figure I appeared to be in its eyes, but I didn’t ask.

I could probably guess from the expressions of the hundred or so Hunters standing behind the Skeleton King.

“We’re done here.”

At the dry voice that sounded strangely unfamiliar even to me, a Hunter who appeared to be a superior jolted and answered,

“Pardon? Ah, yes. Yes.”

“How are things in the other areas?”

“T-Those were the last ones. We were gathering our forces to strike them all at once, but…”

*Gulp.*

After swallowing nervously, he continued,

“It looks like everything has been taken care of.”

“Then that’s good. You worked hard too.”

I patted the Skeleton King on the shoulder and began walking again.

When someone asked where I was going, I answered briefly.

“We have to save people. The people still dying right now. The people who have survived this long.”

I was tired.

The mental fatigue was greater than the physical exhaustion.

But I couldn’t rest yet.

There had to be people somewhere still facing the terror of death and waiting for rescue.

I had to save even one person.

And then—

*Splash.*

The moment a footprint made of green blood stepped onto the asphalt in the middle of the city—

*Bzzzt. Bzzzt.*

Alongside an irritating electronic buzz, the electronic billboard on a high-rise building flickered.

A familiar face appeared on the screen through the static.

A face so handsome it was almost irritating.

It was Team Leader Choi.

At the same time, a small inset image appeared alongside a caption.

> **Peace Guild Hunter Choi Minwoo. Caught up in the Monster Wave that occurred in Pyeongchang…**

God fucking damn it.
```
