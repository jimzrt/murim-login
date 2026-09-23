<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0802.txt",
      "sha256": "1ccb53be999d212f3e817bbcb652fd66a6f8049d5c7dae3031b3e940b3204c6f",
      "bytes": 13175
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a2078e977691e5135c4bfb302822f31d9c47abd5cd03b60212f958930a747121",
      "bytes": 2424
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8c9dc8070fa756b845bf81e2219201805fa9702c6b54e02735af9a47785da09b",
      "bytes": 224512
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "cde28d7b630c4a0944415c79a6af3c9cf9f170ac7cc786859f6d98e53996a1dd",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a5fc0e4c77f39ef14c0925aa145cb4b2cf119cd1424817fa47cb870f32435dc3",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e499d8d660ad6237064954bab5c3b91d74547607bf21121840bc355cc9239273",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b34b480d9dbb787e5d20e6f0077bdb9434645cd1d44448084758d1233f039d3b",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "2e7d9a0e0d95955d3c180585aa7ab7b1970015bfa5cf52734064aacd8e793ea3",
      "bytes": 820
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "b39cb41d9117581663c425b2e237cf14f24623a4da7e90c8f50bf45fa1abecd6",
      "bytes": 787
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "e17d653b0467dcc9ed069a09990f32905841c7c73dc492904cd651061600ce57",
      "bytes": 707
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8f35dc58e43912ac49e8f00d38d106f1430d346d27f8a4c09f50a87eb53641ab",
      "bytes": 247115
    }
  ],
  "estimated_tokens": 10451
}
-->

# Durable State Update — Chapter 802

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 802. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 802. Profile updates may replace only one
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
  "chapter": 802,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 802,
    "continuity_sources": [802],
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
    "The Prophet’s message directs Jin to the Rub’ al Khali, the land where the black jewel sleeps; Team Leader Choi considers the oil fields there the likeliest location.",
    "Jin’s thousand-Hunter force is advancing through the Rub’ al Khali; the magical-power concentration has exceeded their measuring equipment’s capacity.",
    "A substantial force including Chuck Hagel, Faye Chen, Prince Felix, and other S-rank Hunters guards the encirclement behind Jin’s group.",
    "The vehicles carrying Jin’s force have stopped, and an enemy is approaching; Magic Johnson has ordered the force to prepare for battle.",
    "Yamamoto Genji is J1’s sole survivor and has accompanied Jin’s force into the desert.",
    "The J1 victims’ bodies were severely desiccated despite having been dead for less than two hours; the pale mist absorbed from the dead remains unexplained.",
    "The Prophet stopped all ten J1 transport vehicles and absorbed blood and a pale mist from the dead; the nature and limits of this power remain unknown.",
    "The Skeleton King’s memories from before he regained consciousness in a Gate are limited to a dark, ominous place; he does not know The Prophet.",
    "Magic Johnson has never encountered The Prophet’s kind of ability and considers it possible The Prophet is an unidentified top-level Named monster.",
    "Amir and Hamid lead a group concealed by an unseen veil near a convoy of more than five hundred people; Amir ordered them to await The Prophet and the coming holy war."
  ],
  "continuity_sources": [
    800,
    801
  ],
  "open_questions": [
    "What are The Prophet’s identity, abilities, and limits, and what was the pale mist absorbed from the J1 victims?",
    "Why did The Prophet spare Yamamoto, and what happened when Yamamoto tried to flee?",
    "Who is approaching Jin’s force in the Rub’ al Khali, and what will happen when the forces meet?",
    "Where is Amir’s concealed group now, and what is its intended target?"
  ],
  "safe_through": 801,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Render 조센징 as “Chōsenjin,” identifying it as an ethnic slur."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 무인     | **martial artist**                               | Default term                                          |
| 습득               | **Acquired**                   |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 대통령 | **President** | Title for Korea's head of state. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 796
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 801
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 799
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 799
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 800
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 780
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 801
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃802화



스륵.

언덕 위의 모래가 천천히 미끄러진다. 바람도 불지 않는 무더운 날씨. 이글거리는 태양 아래로 날짐승의 그림자가 모두의 머리 위로 드리워졌다.

끼아아악!

비명과도 같은 울음소리를 토해 낸 십여 마리의 독수리가 하늘을 유영한다.

수 미터에 이르는 거대한 날개는 새하얀 뼈만 남아 있었고, 아득한 저 아래를 응시하는 것은 살과 피로 이루어진 눈동자가 아닌 시퍼런 안광(眼光)이었다.

죽음 언저리에서 돌아온 무언가가 지닐 수 있는 안광.

삶과 죽음 어딘가에서 맴도는 존재.

“언데드(Undead)……!”

누군가의 입술 사이로 탄식과 같은 목소리가 흘러나왔다.

그러나 머리 위를 가로질러 하늘 저 너머로 뻗어가는 독수리들을 바라보는 수많은 시선에는 어떤 두려움도 담겨 있지 않았다.

그들도 이미 알고 있기 때문이다.

저 언데드 몬스터들이 자신들의 적이 아니라는 것을.

아니, 정확히는 저것들의 주인이 확실한 아군이라는 것을.

그리고 그들 중 누군가는, 그를 단순한 아군이 아닌 친구로 생각하고 있었다.

“야.”

“왜. 말 걸지 마. 집중하는 중이다.”

“어느 정도냐.”

“말 걸지 말라니까. 시야 공유 중이라고.”

“아직도? 더럽게 느리네.”

“시발. 나 안 해.”

“미안.”

“그럼 입 좀 다물어라, 미친놈아. 이게 너 같은 인간들이 쓰는 저급한 패밀리어(Familiar) 따위와 같은 줄 아느냐.”

퉁명스러운 목소리. 마치 십년지기처럼 말을 주고받은 한 인간과 몬스터는 사막 위로 이글거리는 아지랑이를 노려보았다.

모래 언덕을 조금씩 허물어트리는 진동을 느끼며.

“아직이야?”

“아니, 사실 조금 전에 끝났다.”

“뭐야. 왜 말 안 했는데.”

“긴장감 조성.”

“또라이네, 이거.”

“농담이다. 사실 이걸 어떻게 말해야 할지 몰라서 입 다물고 있었다.”

“……그렇게 많냐?”

“그래.”

“얼마나?”

“최소 일만 이상. 그 뒤로는 너무 많아서 포기했다.”

스켈레톤 킹의 대답에, 진태경은 입을 다물었다.

일만.

실로 어마어마한 대군이다.

심지어 당장 확인된 것만 그 정도니, 어쩌면 정확한 머릿수를 헤아려 본다면 예상치를 훌쩍 뛰어넘을지도 모른다.

“시벌, 아주 작정했네.”

“여기까지 끌어들인 데에는 그만한 이유가 있었던 거지.”

“놈은?”

진태경이 말하는 ‘놈’의 의미를 알고 있는 스켈레톤 킹이 고개를 내저었다.

“아직 모르겠다. 위에서 보기에도 심상치 않은 놈들이 세 마리 정도 있긴 한데, 그게 선지자인지는…… 음.”

불현듯 신음을 토해 낸 스켈레톤 킹이 굳은 얼굴로 말을 이었다.

“공중에도 한 마리 있었군.”

“모두 S급?”

“아마도. 이 몸의 권속들이 손도 써 보지 못하고 당할 정도니.”

지상에 셋. 공중에 하나.

자그마치 네 마리의 S급 몬스터가 수만이 넘는 몬스터 대군을 이끌고 지척에 이르렀다는 소식에, 일천에 달하는 헌터들은 동요를 숨기지 못했다.

그들이 아무리 선별된 정예고, 전투에 숙달된 베테랑이라 한들 죽음에 대한 공포마저 없을 수는 없었으니까.

득. 드드득.

점점 더 거세지는 진동. 발아래에서 들썩이는 모래를 바라보는 시선들이 파르르 떨렸다.

곧 파도처럼 들이닥칠 수많은 몬스터의 모습이 벌써부터 눈앞을 스치는 듯했다.

놈들이 내지르는 괴성과 치열한 전투 속에서 피를 흩뿌리며 죽어 갈 동료, 혹은 자신의 모습도 함께.

그리고 바로 그 순간이었다.

한 사람의 담담한 목소리가 모두의 귓가에 닿은 것은.

“왜, 지금이라도 후퇴할까?”

시선을 떨구고 있던 사람들이 하나둘씩 고개를 들었다. 언덕 위에 선 진태경이 깊게 가라앉은 눈빛으로 그들을 응시하고 있었다.

“아니지. 이건 후퇴가 아니라 도망이라고 해야지. 안 그래?”

“……!”

“사실 전략적 후퇴든 도망이든, 내가 당신들을 비난할 수는 없지. 누구나 살아남고 싶으니까. 꽁지가 빠지게 도망쳐서라도 살아남아야 할 이유가 있으니까.”

이 세상 누구나 마찬가지다.

피를 나눈 가족이 있고, 피를 나누지 않아도 가족 같은 친구들이 있다. 설령 그런 가족과 친구가 없다 해도 계속해서 살아야 할 이유가 있다.

하지만…….

“어디서 나왔는지는 모르겠는데, 그런 말이 있더라고. 도망쳐서 도착한 곳에 낙원은 없다.”

이상한 일이었다.

머리 위로 쏟아지는 햇빛은 타오를 것처럼 뜨거운데, 진태경의 목소리를 듣는 순간 찬물을 뒤집어쓴 것처럼 서늘해졌다.

맞다.

도망쳐 도착한 곳에 낙원은 없다. 그들은 그런 시대에 살고 있었다.

“도망치고, 도망치고, 또 도망치고…… 그렇게 필사적으로 살아남은 어느 날 주위를 둘러보면, 그때까지도 당신들이 지켜야 할 게 남아 있을까.”

무려 삼십여 년 전이다.

인류는 대격변이 할퀴고 간 폐허 위에 더욱 크고 화려한 도시를 재건했고, 재앙이 남긴 흔적은 이제 기록으로만, 흉터로만 남아 있다.

그렇기에 전쟁에서 살아남거나, 평화가 찾아온 뒤에야 태어난 이들은 전쟁을 모른다.

하지만 진태경은 달랐다.

“한번 뒷걸음질 치기 시작하면, 그걸로 끝인 거야.”

전투와 전쟁. 게이트와 현실은 다르다.

저들이 지금껏 경험한 게이트에서는 전투를 피해 물러나면 그만이었지만, 지금 이 순간 모두가 서 있는 이곳은 그들이 나고 자란 세상이다.

지켜야 할 무언가가 있는.

그래서 반드시 지켜 내야 하는 세상.

진태경은 그 사실을 알고 있었다. 친형 같던 누군가를 남겨 두고 홀로 살아남았던 그 날부터, 또 다른 세상을 알게 된 지금까지.

“지키고 싶은 것이 있다면 목숨 걸고 싸워. 그걸 위해 당신들이 지금 이 자리에 있는 거잖아.”

누구나 궁금해하지만, 누구도 모른다.

저주받은 괴물들이 왜 이 세상으로 쳐들어왔는지, 그리고 어떻게 인간이 이토록 놀라운 힘을 갖게 되었는지.

하지만 모두가 어렴풋이 짐작은 하고 있었다.

어느 날 자신들에게 행운처럼 내려온 이 힘은, 괴물들로부터 이 세상을 지키기 위해 주어진 것이라는 사실을.

“그리고 바로 그 한 가지 이유 때문에.”

솨아아.

진태경을 중심으로 모래가 휘몰아친다. 어디선가 불어온 열풍(熱風)이 사람들을 감쌌다.

무더운 햇빛 아래에서도 얼음처럼 굳어 있던 그들의 손발을 녹이고, 저 멀리 거대한 모래 폭풍과 함께 모습을 드러낸 괴물들과는 다른 혈관 속 붉은 핏물을 들끓게 만들었다.

“사람들이, 이 세상이 우리를 헌터(Hunter)라고 부르는 거다.”

화아아악!

아득하리만치 거대한 기파(氣波)가 모두의 정신을 일깨운다. 천천히 돌아서는 진태경의 신형을 따라 아지랑이가 피어올랐다.

공간이 일그러졌다고 느껴질 만큼 끔찍한 열기.

햇빛을 받아 눈부시게 빛나는 창날은 마치 청백색의 태양처럼 이글거리고 있었다.

“포메이션, 갖춰.”

차차차창!

약속이라도 한 것처럼 동시에 뽑혀 나오는 무수한 병장기들.

매직 존슨이 스태프를 치켜들자 각각 수 톤에 달하는 수십여 대의 수송 차량이 전방을 가로막았다.

그 뒤로는 일백에 달하는 탱커가 제 몸뚱어리보다 큰 타워 실드를 모래 깊숙이 박아넣었다.

쿵, 쿠쿠쿵!

묵직한 소음과 함께 완성된 강철의 벽.

그리고…….

구구구궁.

거대한 모래먼지를 일으키며, 망망대해처럼 펼쳐진 사막을 맹렬히 가로지르는 괴물들의 파도.

하지만 그 광경을 바라본 진태경의 한 마디는, 모두를 놀라게 할 만큼 침착하고 담담했다.

“씨발. 다들 힘내자. 저 새끼들 다 죽이려면 진짜 좆 빠지겠다.”

그 순간 누군가가 웃음을 터트렸다. 옆자리의 전우를 미친놈처럼 바라보던 헌터도 피식 실소를 흘리고, 이내 모두가 어깨를 들썩였다.

다 죽여? 저 많은 몬스터들을?

평소였다면 말도 안 되는 헛소리라고 생각했을 거다.

만약 다른 사람이었다면, 그 어떤 대단한 헌터가 왔어도 내심 쌍욕을 퍼부었을 것이다.

그러나 저 새파랗게 젊은 동양인 청년의 이름은 진태경이었고, 세계 헌터 연맹의 새로운 맹주였다.

스스로를 증명한 영웅.

천태민에 이어 또 하나의 전설을 써 내려가고 있는 유일한 인물.

그렇기에 모두가 그를 믿지 않을 수 없었다.

진태경은 언제나 가장 앞에서, 누구보다 치열하게 싸워 왔으니까.

싸워야 할 이유는 그것만으로도 충분했다.

쿠궁. 드드드득!

크워어어어!

어느덧 고막이 먹먹할 만큼 거대해진 굉음과 포효를 들으면서도, 사람들은 웃음을 참지 못했다.

그리고 모래 언덕 위, 마치 태산처럼 우뚝 서 있던 진태경이 창날을 휘두르는 광경을 지켜보았다.

콰드드드득!

분수처럼 솟구치는 핏물이 땅에 닿기도 전에 증발하고, 갈기갈기 찢어진 몸뚱어리와 내장이 사방으로 흩날린다.

훗날 사막의 폭풍(Desert Storm)이라 불리게 될, 대전투의 서막이 열린 순간이었다.



* * *



척 헤이글은 손에 든 시가를 말없이 바라보고 있었다.

얼마 전 프랑스 대통령에게서 빼앗은, 아니 습득한 시가는 지금 이 순간에도 천천히 타들어 가는 중이었다.

나중에 듣기로는 미카엘 실베르트에게 직접 선물 받은 물건이라던데, 출처가 출처인 만큼 당연히 값어치도 엄청났다.

대격변 이전에 만들어진 쿠바산 시가는 이제 돈이 있어도 구하지 못하는 물건이 됐다.

이유?

간단하다. 쿠바가 멸망해 버렸으니까.

쿠바의 수도 중심가에서 시작된 몬스터 웨이브는 걷잡을 수 없이 커졌고, 케이맨 제도(諸島)에 속한 섬나라 세 개를 바닷속 깊숙이 가라앉힌 후에야 끝났다.

아마도 그때부터였을 것이다.

담배는 입에도 대지 않던 어느 중년인이, 습관처럼 시가를 피워 대기 시작했던 것은.

쿠바에는 그의 어머니가 있었다.

치직.

오랫동안 타들어 간 잿가루가 툭, 하고 떨어진다.

그 광경을 한참 동안 말없이 바라보던 척 헤이글이 불쑥 입을 열었다.

“지원 요청은?”

자욱하게 깔린 시가 연기를 휘휘 저어 흘려보낸 참모가 대답했다.

“아직입니다.”

“빌어먹을.”

“너무 걱정하실 필요 없습니다, 보스.”

“걱정? 내가 그 애송이를?”

애송이라고 하기에는 너무 강한데요. 심지어 상관이잖습니까.

자신도 모르게 튀어나오려는 그 말을 겨우 삼켜 낸 참모가 입맛을 다셨다.

“만반의 준비를 끝마치고 대기 중입니다. 룹 알 할리(Rub' al Khali) 사막의 후방은 저희가 책임지고 있어요.”

“제기랄. 그래 봤자 저 염병할 위성 감시는 통하지도 않잖나. 무인 정찰기는 왜 먹통인데? 혹시 방산 업체에서 뒷돈이라도 처먹였나?”

“세상에, 보스도 이미 아시지 않습니까. 마력 분포도가 너무 높아요.”

“난 그딴 거 몰라. 만약 혼자 멋대로 뛰쳐나간 그 애송이와 함께 있는 다른 녀석들에게 무슨 문제라도 생긴다면…… 저 Fucking 종이비행기를 만든 놈들이 내 손에 뒈질 거라는 건 알지.”

“…….”

참모는 지금 이 순간 방산 업체 관련자가 이곳에 없다는 것에 마음 깊이 감사했다.

자신의 성질 더러운 상관이 아직 본대를 지키고 있다는 사실도 함께.

하지만 안타깝게도, 그가 느낀 안도는 그리 오래가지 못했다.

삑. 삐빅.

“……어?”

난데없이 울려 퍼지는 긴급 신호음과 함께 켜진 붉은 경고등. 동시에 지휘 통제실 곳곳에서 다급한 외침이 터져 나왔다.

“발신자 및 좌표 파악해!”

“젠장! 빨리!”

그리고 잠시 후, 척 헤이글은 보고 내용을 확인한 참모의 얼굴이 딱딱하게 굳어 가는 것을 볼 수 있었다.

“뭐야?”

“……습격입니다. 외부에 나가 있는 수색대 일부가 당했어요.”

“뭐?”

“그리고.”

잠시 숨을 고른 참모가, 참았던 숨을 토해 냈다.

“적은, 몬스터가 아닙니다.”
```

## Final English reading copy

```markdown
# Chapter 802

*Slide.*

The sand on the hill slowly slipped downward. It was a sweltering day without a breath of wind. Beneath the blazing sun, the shadows of flying beasts fell over everyone.

*Kreeeaaak!*

A dozen or so vultures glided through the sky, letting out cries like screams.

Their enormous wings, spanning several meters, were nothing but bare white bones. And the eyes gazing down from far above weren’t made of flesh and blood—they glowed a vivid blue.

The kind of light that might shine in the eyes of something returned from the edge of death.

A being that hovered somewhere between life and death.

“Undead…”

A voice like a sigh slipped from someone’s lips.

But not one of the many people watching the vultures fly over their heads and on toward the horizon looked afraid.

They already knew.

Those undead monsters weren’t their enemies.

No—more precisely, their master was most definitely an ally.

And at least one of them thought of him as more than an ally. He was a friend.

“Hey.”

“What? Don’t talk to me. I’m concentrating.”

“How’s it going?”

“I said don’t talk to me. I’m sharing my vision.”

“Still? You’re damn slow.”

“Fuck. I’m not doing this anymore.”

“Sorry.”

“Then shut your mouth, you lunatic. You think this is some cheap Familiar like the ones humans like you use?”

The human and monster traded words as casually as old friends, then fixed their gazes on the heat haze shimmering over the desert.

They could feel the vibrations slowly crumbling the sand dunes.

“Anything yet?”

“No, actually, I finished a little while ago.”

“What? Why didn’t you say so?”

“To build the suspense.”

“You’re a nutcase.”

“I’m kidding. I didn’t say anything because I wasn’t sure how to tell you.”

“…There are that many?”

“Yeah.”

“How many?”

“At least ten thousand. After that, there were too many, so I gave up counting.”

At the Skeleton King’s answer, Jin Taekyung fell silent.

Ten thousand.

That was an enormous army.

And that was only what they’d confirmed so far. If they somehow counted the exact number, it might be far beyond their estimate.

“Fuck, they’re really going all in.”

“They must have had a good reason for drawing us all the way out here.”

“What about him?”

The Skeleton King knew who Jin meant by *him*, and shook his head.

“I still don’t know. From above, there are about three that look like serious threats, but whether one of them is The Prophet… Hmm.”

The Skeleton King let out a low groan. His expression stiffened as he continued.

“There was one in the air, too.”

“Are they all S-rank?”

“Probably. My servants couldn’t even fight back before they were defeated.”

Three on the ground. One in the air.

The news that four S-rank monsters had led an army of tens of thousands right to their doorstep shook the nearly one thousand Hunters. No matter how carefully selected and battle-hardened they were, they couldn’t simply cast aside their fear of death.

*Thud. Rumble, rumble.*

The vibrations grew more and more violent. As the sand shifted beneath their feet, the Hunters’ eyes trembled.

They could already picture the countless monsters about to surge in like a wave.

They could picture their comrades—or themselves—spattered with blood and dying amid the monsters’ roars and the fierce battle.

And it was right then that a calm voice reached everyone’s ears.

“So, want to retreat now?”

One by one, the people who’d been looking down raised their heads. Jin Taekyung stood on the hill, gazing at them with eyes sunk deep and steady.

“No, I suppose we should call it running away, not retreating. Right?”

“……!”

“Honestly, whether you call it a strategic retreat or running away, I can’t blame you. Everyone wants to survive. We all have reasons to keep living, even if we have to run like hell to do it.”

That was true of everyone in the world.

They had family bound to them by blood, and friends who felt like family even without the blood. And even if they had neither, they still had reasons to keep living.

But…

“I don’t know where it came from, but there’s a saying: There’s no paradise at the end of the road when you run away.”

It was strange.

The sunlight pouring down overhead was hot enough to set them on fire, yet the moment they heard Jin Taekyung’s voice, they felt as if someone had doused them in cold water.

He was right.

There was no paradise at the end of the road when you ran away. They lived in a time like that.

“Run away, and run away, and run away again… Then one day, after fighting tooth and nail to survive, you look around. Will there still be anything left for you to protect?”

It had been more than thirty years.

Humanity had rebuilt cities even larger and more splendid on the ruins left behind by the Great Cataclysm. The traces of that disaster remained only in records and scars.

Those who survived the war, or were born after peace arrived, didn’t know what war was like.

But Jin Taekyung was different.

“Once you start backing down, it’s over.”

Combat and war were different. So were Gates and reality.

In the Gates they’d experienced until now, they could simply retreat to avoid a fight. But the place they were standing in at that very moment was the world where they’d been born and raised.

A world with something they had to protect.

A world they had to protect, no matter what.

Jin Taekyung knew that. From the day he survived alone, leaving behind someone who’d been like an older brother, to now, when he’d come to know another world.

“If there’s something you want to protect, fight for it with your life on the line. That’s why you’re all here, isn’t it?”

Everyone wondered, but no one knew.

Why the cursed monsters had invaded this world, or how humans had come to possess such incredible power.

But everyone had some vague idea.

This power that had come to them one day like a stroke of luck had been given to them so they could protect this world from monsters.

“And for that one reason…”

*Whoosh.*

Sand whipped around Jin Taekyung. A hot wind blew in from somewhere and swept over the people.

It thawed their hands and feet, frozen like ice even beneath the sweltering sun, and made the red blood in their veins boil—unlike the monsters now appearing in the distance beside a gigantic sandstorm.

“That’s why people—why this world—calls us Hunters.”

*Fwoosh!*

An immensely powerful wave of energy jolted everyone’s senses awake. As Jin Taekyung slowly turned around, heat haze rose around him.

The heat was so intense that it made the space around him seem to warp.

The spearhead gleaming in the sunlight blazed like a blue-white sun.

“Get into formation.”

*Clang, clang, clang!*

Countless weapons were drawn at once, as if on cue.

When Magic Johnson raised his staff, dozens of transport vehicles, each weighing several tons, blocked the way ahead.

Behind them, nearly a hundred tanks drove tower shields larger than their own bodies deep into the sand.

*Boom. Rumble!*

A steel wall took shape with a series of heavy thuds.

And then…

*Rumble…*

Raising a vast cloud of sand, a wave of monsters rushed fiercely across the boundless desert.

But Jin Taekyung’s words as he watched them were so calm and matter-of-fact, they surprised everyone.

“Fuck. Hang in there, everyone. We’re going to bust our fucking asses killing all those bastards.”

Someone burst out laughing.

A Hunter who’d been staring at the comrade beside him as if he’d gone insane let out a snort, and soon everyone’s shoulders were shaking.

Kill them all? All those monsters?

Normally, they’d have thought it was absurd nonsense.

If anyone else had said it, no matter how great a Hunter they were, they’d have cursed them under their breath.

But that startlingly young Asian man was Jin Taekyung, the new Alliance Leader of the World Hunter Federation.

A hero who had proven himself.

The only one writing another legend after Cheon Taemin.

They couldn’t help believing in him.

Jin Taekyung had always fought at the very front, harder than anyone else.

That alone was reason enough to fight.

*Boom. Rumble, rumble!*

*Graaaar!*

Even as the thunderous rumbling and roars grew loud enough to make their eardrums throb, the Hunters couldn’t keep from laughing.

They watched Jin Taekyung stand tall on the sand dune like a mountain, then swing his spear.

*Crunch!*

Blood erupted like a fountain and evaporated before it could touch the ground. Torn bodies and entrails scattered in every direction.

The opening moment of the great battle that would later be called the Desert Storm.

* * *

Chuck Hagel stared silently at the cigar in his hand.

The cigar he’d taken—or, rather, acquired—from the French President not long ago was still slowly burning.

He’d heard later that it had been a direct gift from Michael Silbert. Given its provenance, it was obviously worth a fortune.

Cuban cigars made before the Great Cataclysm were impossible to find now, no matter how much money you had.

Why?

Simple. Cuba had been destroyed.

The monster wave that began in the center of Cuba’s capital had grown beyond control. It ended only after sinking three island nations in the Cayman Islands deep beneath the sea.

Perhaps that was when it started.

When a certain middle-aged man, who’d never even touched tobacco, began smoking cigars out of habit.

His mother had been in Cuba.

*Crackle.*

Ash that had been burning for a long time dropped with a soft *tap*.

After watching it in silence for a long while, Chuck Hagel abruptly spoke.

“Any request for backup?”

An aide, who’d just waved the thick cigar smoke away, answered.

“Not yet.”

“Goddamn it.”

“You don’t need to worry so much, boss.”

“Worry? About that punk?”

*He’s too strong to call a punk. And he’s your superior, too.*

The aide barely swallowed the words that had almost slipped out and clicked his tongue.

“We’re fully prepared and standing by. We’re responsible for the rear of the Rub’ al Khali Desert.”

“Damn it. That’s all well and good, but that goddamn satellite surveillance still doesn’t work. Why are the drones down? Did some defense contractor take a kickback?”

“Come on, boss. You know why. The concentration of magical power is too high.”

“I don’t know about any of that. If anything happens to the others with that punk who ran off on his own… you know the bastards who made those fucking paper airplanes will die by my hand.”

“……”

The aide was profoundly grateful that there was no one from a defense contractor around at that moment.

He was also grateful that his short-tempered superior was still guarding the main force.

Unfortunately, the relief he felt didn’t last long.

*Beep. Beep-beep.*

“…Huh?”

A sudden emergency alarm rang out, and red warning lights flashed on. Urgent shouts erupted around the command center.

“Identify the sender and the coordinates!”

“Damn it! Hurry!”

A moment later, Chuck Hagel saw the aide’s face stiffen as he read the report.

“What is it?”

“…We’re under attack. Part of the search party outside has been hit.”

“What?”

“And…”

The aide paused for breath, then let it out.

“The enemy isn’t a monster.”
```
