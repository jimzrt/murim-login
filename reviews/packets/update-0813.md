<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0813.txt",
      "sha256": "7cdedcfb2d3e7da8eac36f0a47ecab75b84ab2c72cc02de991b4ac4d0ae50630",
      "bytes": 13223
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3b76038f4888ccff0f205a5591bb4d2f33be537f6d7dd5a52cf7a6103b415bd9",
      "bytes": 1179
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1e8b8a33ae952423b359fb7c39a8c3a83fe8a43b894e38ef519681dd66dd55a7",
      "bytes": 225527
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6ba4f34ec419fd1a4e666e0cecbf40e1f612e37e5a25764d8ebf723cc33bcdcc",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b4eae17529b1f0efb5f75685b88c0c65f5097c9890fad5ce6828d9ecdd9aeef4",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b7071f9fb7f7206d5c61d1fb5c08df89b6c15a917413984dfff1a60b28d2c834",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "6b338c662c752d63368294c23f7a836625236191984dae8b56ec340f03a93e6a",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "cd05b299008fa9248a1483bbffcc2846751f227b238820491efa530b264dcc9f",
      "bytes": 709
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "32e9b06ee285eff02faa6817a43b5bd580f54e77e6576d3b4687dd351bf9c251",
      "bytes": 588
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "00e6d7d0bd6884c780f65f7d2a6a060a0e493a989f7f38fc51b7ef2e9500d415",
      "bytes": 248856
    }
  ],
  "estimated_tokens": 10157
}
-->

# Durable State Update — Chapter 813

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 813. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 813. Profile updates may replace only one
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
  "chapter": 813,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 813,
    "continuity_sources": [813],
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
    "The Prophet is revealed to be Yamamoto Genji; Jin concludes that the same individual has been Muninn for more than thirty years and taught Michael Silbert to use magical power.",
    "Jin has attacked The Prophet in the canyon, where the Skeleton King and hundreds of monsters are present.",
    "Jin sent the other forces east so they would not be caught up in the confrontation.",
    "Jin remains uncertain whether Magic Johnson is human; Johnson says he helped Jin because they are friends."
  ],
  "continuity_sources": [
    812
  ],
  "open_questions": [
    "What will happen in the confrontation between Jin and The Prophet?",
    "What unresolved pieces of evidence are needed to complete Jin’s understanding of the conspiracy?",
    "Is Magic Johnson human?"
  ],
  "safe_through": 812,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep the Demon Realm language distinct from other languages."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 살기     | **killing intent**                               |                                                       |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 무닌 | **Muninn** | One of the two ravens associated with Odin in Norse mythology. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 조이 | **Joey** | U.S. military or political official introduced by first name only. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 진태경 | 야마모토 | Alliance Leader to Japanese S-rank Hunter he sent on the mission | Yamamoto | blunt and familiar | Jin quietly says Yamamoto’s name while treating him. |
| 야마모토 | 진태경 | Japanese Hunter to the Alliance Leader who rescued him | Chōsenjin | insulting | Yamamoto uses the ethnic slur as he regains the ability to speak. |
| 진태경 | 선지자 | enemy commander addressed by Jin | The Prophet | blunt and informal | Jin asks where The Prophet is while confronting the Manticore Lord. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 812
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 812
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 812
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 812
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 812
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster revealed as Yamamoto Genji, who Jin concludes has been the same Muninn for more than thirty years and taught Michael Silbert to use magical power.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 812
- **Aliases:** None
- **Role:** Yamamoto Genji is revealed to be The Prophet, the monster who has posed as Muninn.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃813화



스아아.

모든 것이 선명하고 느려진다.

비틀거리며 물러나는 발걸음을 따라 튀어 오르는 흙과 모래, 부릅떠진 눈동자, 가슴에서 솟구치는 핏물까지.

그리고…….

“너, 뭐 하는 새끼냐?”

입술 밖으로 토해 낸 한마디와 함께 느려졌던 시간이 돌아온다.

입꼬리를 끌어올리며 히죽 웃는 야마모토 겐지의, 아니 놈의 얼굴이 똑똑히 보였다.

‘선지자.’

조금 전만 해도 고통으로 부릅떠져 있던 두 눈동자는, 어느덧 이해할 수 없는 기쁨과 놀라움으로 번뜩이고 있었다.

‘기쁘다고? 이 상황이?’

도대체 왜, 라는 의문을 뒤로한 채 손에 쥔 단검을 재차 휘둘렀다.

핏물이 솟구치는 가슴을 움켜잡으며 비틀거리던 선지자가 허리춤의 검자루를 잡은 순간. 단검의 날을 타고 뛰쳐나간 참격(斬格)이 그보다 한발 앞서 섬광처럼 어둠을 가로질렀다.

서걱.

서늘한 절삭음과 함께 선지자의 손목 위로 희미한 실선이 그어진다.

검신을 반쯤 뽑아 올리고 있던 놈의 오른손이 힘을 잃고 몸뚱어리에서 떨어져 나왔다.

툭. 푸화악!

뿜어져 나온 핏물이 바닥을 적셨다. 여느 인간과 다를 것 없는 붉은 선혈이었고, 그렇기에 더욱 믿기지 않았다.

놈을 향해 달려들고 있는 지금 이 순간조차.

후웅, 콰직!

천근(千斤)의 힘을 발끝에 실어 내리찍듯 짓밟는다. 종아리의 살이 터지고 뼈마디가 으스러진다.

완전히 몸의 균형을 잃어버린 채 한쪽 무릎을 꿇은 선지자가 하나밖에 남지 않은 손을 뻗었으나 이번에는 내가 나설 필요조차 없었다.

“멈춰.”

깊게 가라앉은 목소리와 함께 바람이 멎는다. 공기가 떨렸다.

보이지는 않지만 분명히 느껴진다.

주위를 휘감은 대마도사의 강대한 마나(Mana)가. 내게 닿으려던 선지자의 손목을 움켜쥔 그 힘이.

으드득.

허공에서 우뚝 멈춘 손. 뼈 어긋나는 소리와 함께 놈의 미간이 일그러진다.

마치 보이지 않는 거인의 손이 몸뚱어리를 잡고 들어 올리는 것처럼, 선지자의 신형이 허공으로 천천히 떠오른 그때였다.

쐐액, 푸푸푹!

새하얀 무언가가 빛살처럼 날아와 선지자의 사지(四肢)를 꿰뚫었다.

길고 날카로운 뼛조각은 살과 뼈를 두부처럼 가르고, 허공에 떠올라 있던 놈의 몸뚱어리를 절벽 깊숙이 박아넣었다.

콰드득!

수백, 어쩌면 수천 년간 제자리를 지키고 있었을 단단한 암석은 훌륭한 지지대였다.

예상치 못한 내 기습을 시작으로 한순간에 제압당한 선지자는 왈칵 핏물을 토해 냈다.

“쿨럭. 크흐흐.”

고통은 그 누구에게나 평등하다.

하지만 놈은 마치 고통을 느끼지 못하는 것처럼, 피에 젖은 입꼬리를 말아 올리며 웃었다.

“좋아, 먼저 칭찬해 주지. 아주 잘했어.”

뻑!

안면을 직격당한 선지자의 머리가 뒤로 젖혀졌다. 굉음과 함께 절벽에 뒤통수를 처박은 놈이 고개를 흔들었다.

“오랜만에 골이 울리는군. 재미 보는 것도 좋지만 적당히 하자고.”

“……!”

나는 새어 나오려는 신음을 억눌렀다.

이미 손목을 자르고 무릎을 부쉈다. 그뿐인가. 가장 처음의 일격은 심장 어림을 정확히 파고들었다.

마지막 순간 놈이 몸을 빼긴 했지만, 단검에 실린 엄청난 열양지기가 신체 내부를 엉망으로 만들기에는 충분했다.

‘평범한 인간이라면 이미 숨이 끊어지고도 남았다.’

하지만 놈은, 선지자는 아니었다.

저 불가사의할 정도로 강인한 생명력은 인간의 것이 아니었다.

게다가 반인반마(半人半魔)와 다름없던 미카엘 실베르트가 괴물의 모습으로, 괴물의 피를 흘리며 죽었던 것과는 달리 지금도 붉은 선혈을 흘리고 있었다.

“……진.”

“저놈은, 저놈은 도대체 뭐지?”

귓가를 파고드는 두 줄기의 음성.

파르르 떨리는 시선으로 불가해(不可解)의 존재를 바라보는 매직 존슨과 스켈레톤 킹의 모습에, 선지자는 피 끓는 소리를 내며 웃었다.

“그 누구도 답하지 못할 것이다. 나는 그런 존재니까.”

아니다. 놈의 말은 틀렸다.

나는 어느새 가빠진 호흡을 가라앉혔다. 은은한 빛을 토해 내는 두 눈동자는 타오르는 것처럼 뜨거웠다.

이것은 인간이 아닌 초월적인 힘을 일시적으로나마 받아들인 대가다.

동시에 시스템이 어느 멍청한 인간에게 건네준 선물이자, 이 거대한 퍼즐을 맞출 수 있는 유일한 열쇠이기도 했다.

‘진실의 눈.’

지크프리트 바스만의 죽음으로 시작된 퀘스트, [알 수 없는 죽음]을 완료한 보상으로 받았던 특수 아이템.

내가 스쳐 지나가듯 확인했던 [진실의 눈]의 정보를 다시금 떠올렸던 것은, 실마리를 잡은 직후였다.



아이템창



[진실의 눈]

종류 : 일회용 아이템

등급 : 특수

제한 : 진태경

설명 : 아득히 먼 옛날, 신화가 되어 버린 과거의 신이 지혜의 샘물을 마시기 위해 바친 눈동자. 그는 한쪽 눈동자를 바친 대가로 무한한 지혜를 얻었고, 샘 밑바닥에 가라앉은 눈은 다른 세상의 진실마저 꿰뚫는 힘을 얻었다.

효과 : 단 하나의 대상에 한하여 [진실의 눈]을 적용할 수 있다.





‘돌이켜 생각해 보면, 시스템은 언제나 길을 알려 줬었지.’

처음에는 몰랐다. 시스템이 [진실의 눈]이라 이름 붙인 소모성 아이템이 무엇을 위한 것인지. 오직 내게만 보이는 저 홀로그램이 내게 무엇을 말하고자 하는지.

하지만 지금은 아니다.

나는 몇 시간 전 유일한 실마리를 얻었고, 시스템은 그보다 한발 앞서 실마리를 풀 수 있는 열쇠를 쥐여 주었다.

단 하나의 대상에게만 사용할 수 있는, 그래서 더욱 신중하게 사용해야 하는 열쇠를.

그리고 지금 이 순간, 나는 모든 진실을 꿰뚫는 힘을 얻었다.

화아아악.

뜨겁다. 눈앞이 새하얗게 물든다.

하지만 그 안에 깃들어 있는 신의 이능(異能)은 고통을 딛고 뻗어 나갔다.

야마모토 겐지를 향해. 이 사막에 신전을 세운 광신도들의 교황을 향해.

지난 삼십여 년간 무닌이라는 이름으로 이 땅에 재앙의 씨앗을 심고, 이제 스스로 꽃피우려 하는 알 수 없는 존재를 향해.

그것은 [기감]조차 뚫지 못한 두터운 장막이었으나, 오딘이라 불린 옛 신의 눈동자는 그 모든 것을 직시했다.

관통하고, 밝혀 냈다.

파앗.

아득한 섬광이 시야를 물들인 그 순간. 무수한 종소리가 뇌리에서 몸부림쳤다.

지금껏 들은 적도, 본 적도 없는 시스템 알림과 홀로그램 창이 사방을 땅끝을 내달리고 구름 위로 치솟았다.

띠링. 띠링. 띠링. 띠리리링!

소리가 소리를 집어삼킨다. 반투명한 홀로그램 창이 하나에서 다섯으로, 다섯에서 수십으로, 또 일백으로 증식한다.

그건 파도였고, 산이었다.

“아……!”

나도 모르게 외마디 탄식이 터져 나왔다. 눈 앞에 펼쳐진 광경에 서늘한 한기가 등골을 타고 흘렀다.

수백, 어쩌면 수천.

헤아릴 수도 없을 만큼 무수한 홀로그램 창이 폭죽처럼 터져 나오고 있었다. 이 모든 것의 시작이자 중심인, 한 존재로부터.

‘선지자.’

숨이 막혔다. 지금 내가 보고 있는 것은 단순한 정보가 아니다. 지금껏 놈이 집어삼킨 수많은 생명이며, 그들이 남긴 묘비였다.

레벨과 이름뿐인 묘비.

그리고 내게 깃든 [진실의 눈]은, 망자들의 이름이 가득한 이 거대한 묘지를 쌓아 올린 묘지기의 정체를 간파해 냈다.

놈이 뒤집어쓴 두꺼운 장막을 걷어내고 진실을 밝혔다.

띠링.

귓가를 울리는 마지막 종소리. 그와 함께 머릿속에서 맞춰지는 퍼즐의 마지막 한 조각.

‘이건.’

비로소 깨달았다.

선지자의 진정한 본질이 무엇인지. 이 저주받은 괴물이 어떻게 삼십여 년간 자신의 정체를 숨기며 모든 일을 해낼 수 있었는지.

‘그래, 이제야 알겠다.’

나는 여전히 웃고 있는 선지자를 응시했다. 그리고 참았던 숨과 함께 한 마디를 토해 냈다.

“도플갱어(Doppelganger).”

그 순간, 똑똑히 보였다.

“……!”

반달처럼 휘어져 있던 입꼬리가 경직되는 모습이. 놈의 정수리 위에 떠 있는 홀로그램 창이 유독 음울하게 빛나는 광경이.



[Lv.170 “최후의 심연” 도플갱어]



* * *



도플갱어.

악운(惡運)의 전조이자, 미신처럼 전해져 내려오는 존재.

그러나 전설로만 전해지던 무수한 괴물들이 낡은 신화의 한 페이지를 찢고 현실로 뛰쳐나오는 와중에도 도플갱어라는 존재는 단 한 번도 모습을 드러내지 않았고, 인류는 생각했다.

자신들이 지금껏 쓰러트린, 혹은 앞으로 쓰러트려야 할 적 중 도플갱어는 없다고.

저 끔찍한 마계에서조차 존재하지 않는, 그저 사람들의 두려움이 불러온 허상이며 단순한 미신에 불과했다고.

하지만 틀렸다.

도플갱어는 처음부터 존재했다. 단지 단 한 번도 드러난 적이 없었기에 모두가 착각했을 뿐이었다.

적어도 진태경만큼은 그 사실을 누구보다 잘 알고 있었다.

무수한 생명을 집어삼킨 저 불가해(不可解)의 존재가, 도대체 언제부터 이 세상에 스며들었는지도.

“미카엘 실베르트. 파리 대전투.”

불쑥 흘러나온 청년의 목소리는 앞뒤를 둘러싼 절벽의 암반처럼 딱딱했고, 잠시 경직되어 있던 괴물의 입꼬리는 부드럽게 풀어졌다.

“그래, 맞다. 너희 인간들이 크리스마스라고 부르는 바로 그 날. 나는 그를 만나 이 세상의 일원이 되었다.”

2020년 12월 25일.

역사의 한 페이지를 장식하는 동시에 미카엘 실베르트라는 이름을 인류에게 각인시킨 대전투.

그날의 진실이 한 꺼풀 몸을 벗자 진태경은 숨을 삼켰다. 스켈레톤 킹은 이를 악물었고, 매직 존슨은 믿을 수 없다는 눈빛으로 선지자를, 아니 도플갱어를 바라보았다.

“말도 안 돼. 당시 파리를 습격했던 건 분명히…….”

“드래곤이었지. 정확히는 태어난 지 삼백 년도 되지 않은 헤츨링(Hatchling)이었어. 태어나길 용이라 천성이 오만했고, 어린놈답게 방심했다. 물론 그렇다 해도 인간에게 죽은 건 의외이긴 했지만.”

매직 존슨의 말을 잘라 낸 도플갱어가 말을 이었다.

“결국 운이 없었던 거야. 그 어린 드래곤도, 그리고 용을 상대로 기적적으로 살아남았던 인간들도.”

대격변이라는 파도를 온몸으로 헤쳐나온 대마도사는 참지 못하고 신음을 흘렸다.

“……거짓말이었군. 그 모든 게 미카엘 실베르트가 꾸며 낸 거짓말이었어.”

“글쎄. 완전히 꾸며 냈다고는 할 수 없지. 드래곤이 파리를 습격한 것도, 홀로 살아남은 것도 사실이긴 했으니까.”

도플갱어는 히죽 웃었다.

“처음 미카엘을 보자마자 느낌이 왔지. 다른 인간들과는 달리 녀석은 계산이 빨랐어. 절반을 죽이기도 전에 내게 무릎을 꿇더군. 살고 싶다고. 무엇이든 할 테니 제발 살려만 달라고.”

“……!”

“흥미로운 제안이었다. 나는 그 제안을 받아들였고, 녀석은 남은 인간들은 제 손으로 죽였지.”

진태경은 문득 떠올렸다. 미카엘 실베르트가 최후를 맞이하기 전, 마지막으로 주고받았던 대화에서 들었던 한 마디를.



‘나 역시, 살기 위해 몸부림쳤을 뿐이다!’



피를 토하는 듯했던 외침.

그 말이 맞았다. 미카엘 실베르트는 살기 위해 몸부림쳤다. 그에게는 누구보다 커다란 생존 욕구가 있었고, 아직 이루지 못한 야망이 있었다.

그렇게 인간과 몬스터는 손을 잡았다.

그러나 그것은 족쇄가 아닌 계약이었다. 겉모습은 다르나 본질은 같은 두 괴물이, 각자의 목적을 이루기 위한 계약.

하지만…….

“뭘 위해서였지?”

“뭐?”

“뭘 위해서였냐고 물었다. 이 세상에서, 사람들 사이에 섞여 살고자 했던 진짜 목적이.”

씹어뱉듯이 흘러나온 진태경의 목소리에, 잠시 침묵하던 도플갱어가 입꼬리를 끌어올렸다.

“글쎄. 지금은 내 대답을 기다릴 때가 아닌 것 같은데.”

그리고 그 순간.

드드드득.

저 멀리에서부터 전해진 진동이, 협곡을 휩쓸었다.
```

## Final English reading copy

```markdown
# Chapter 813

*Fwoosh.*

Everything sharpened and slowed.

The dirt and sand kicked up by his staggering retreat. His eyes, wide open. Even the blood surging from his chest.

And then…

“What the fuck are you?”

With those words spat from my lips, time returned to normal.

I could clearly see Yamamoto Genji—or rather, the bastard—grinning as he curled up the corners of his mouth.

*The Prophet.*

His eyes, which had been wide with pain just moments ago, now glinted with incomprehensible joy and surprise.

*He’s happy? In this situation?*

I shoved aside the question of why and swung the dagger in my hand again.

The Prophet was staggering, clutching his blood-spurting chest. The moment he reached for the sword at his waist, a slash burst from the dagger’s blade and streaked through the darkness like a flash of light, a step ahead of him.

*Shhk.*

A faint line appeared across The Prophet’s wrist with a chilling cut.

His right hand, which had half-drawn the sword, lost its strength and fell away from his body.

*Thud. Splatter!*

Blood sprayed across the ground. It was the same red blood as any ordinary human’s, which made it all the harder to believe.

Even as I charged at him.

*Whoosh. Crack!*

I drove my heel down with the force of a thousand pounds. The flesh of his calf burst, and the joints in his bones shattered.

The Prophet had completely lost his balance and dropped to one knee. He reached out with his only remaining hand, but this time, I didn’t even need to step in.

“Stop.”

The wind died at the sound of a deep, low voice. The air trembled.

I couldn’t see it, but I could feel it.

The Grand Mage’s mighty mana wrapped around us. That power had seized The Prophet’s wrist before his hand could reach me.

*Crack.*

His hand stopped dead in midair. The sound of bones grinding out of place twisted his brow.

Just then, The Prophet’s body began to rise slowly into the air, as though an invisible giant had grabbed him and lifted him up.

*Whistle—thud, thud, thud!*

Something pure white shot toward him like a beam of light and pierced his limbs.

The long, sharp bone shards sliced through flesh and bone like tofu, pinning his body—which had been floating in the air—deep into the cliff.

*Crunch!*

The solid rock, which might have stood in that spot for hundreds or even thousands of years, made an excellent support.

Taken down in an instant, starting with my unexpected ambush, The Prophet abruptly spat out blood.

“Cough. Heh heh.”

Pain was the same for everyone.

But The Prophet laughed, curling his bloodstained lips as if he couldn’t feel a thing.

“Good. I’ll give you this much first: you did very well.”

*Wham!*

The Prophet’s head snapped back from a direct hit to the face. His skull slammed into the cliff with a boom, and he shook his head.

“It’s been a while since I felt my head ring. Having fun is nice, but let’s not overdo it.”

“……!”

I stifled the groan trying to escape my lips.

I’d already severed his wrist and shattered his knee. And that wasn’t all. My very first strike had pierced the area around his heart.

He’d pulled away at the last moment, but the tremendous Scorching Yang Qi infused into my dagger had still been enough to wreak havoc inside his body.

*An ordinary human would already be dead.*

But he wasn’t. The Prophet wasn’t.

That life force, strong to the point of being incomprehensible, didn’t belong to a human.

And unlike Michael Silbert, who had been practically half-human and half-demon, then died in the form of a monster while bleeding monster’s blood, The Prophet was still shedding red human blood.

“……Jin.”

“What… what the hell is that thing?”

Two voices pierced my ears.

Magic Johnson and the Skeleton King stared at the incomprehensible being, their gazes trembling. The Prophet laughed, his voice thick with blood.

“No one will ever be able to answer that. That’s what I am.”

No. He was wrong.

I steadied my breath, which had grown ragged without me noticing. The two eyes giving off a faint glow were as hot as flames.

This was the price of temporarily accepting a power beyond humanity.

At the same time, it was a gift the System had given to one foolish human—and the only key that could put this enormous puzzle together.

*The Truthful Eye.*

A special item I’d received as a Reward for completing the Quest **Unknown Death**, which began with Siegfried Bassman’s death.

I’d only glanced at the details of the Truthful Eye before. I recalled them again the moment I found a clue.

> **System**
>
> **Item Window**
>
> **Truthful Eye**
>
> **Type:** Single-Use Item  
> **Grade:** Special  
> **Restriction:** Jin Taekyung  
> **Description:** In the distant past, a god who would become part of myth offered up an eye to drink from the spring of wisdom. In exchange for one eye, he gained infinite wisdom, while the eye that sank to the bottom of the spring gained the power to pierce even the truths of other worlds.
>
> **Effect:** Can be applied to a single target only.

*Looking back, the System had always shown me the way.*

At first, I hadn’t known what the consumable item the System called the Truthful Eye was for. I hadn’t known what that hologram only I could see was trying to tell me.

But not anymore.

A few hours ago, I’d found the only clue. And the System had handed me the key to unravel it one step ahead of me.

A key that could be used on only one target—and therefore had to be used with even greater care.

And now, in this very moment, I’d gained the power to pierce every truth.

*Fwoooosh.*

It was hot. My vision turned white.

But the divine power dwelling within it pushed through the pain and reached out.

Toward Yamamoto Genji. Toward the Pope of the fanatics who had built a temple in this desert.

Toward the incomprehensible being who, under the name Muninn, had spent the past thirty-odd years sowing the seeds of catastrophe in this land, and was now about to make them bloom himself.

It was a thick veil that even **Qi Sense** couldn’t penetrate. But the eye of the old god called Odin saw through it all.

Pierced it. Revealed it.

*Flash!*

The instant a distant, blinding light flooded my vision, countless bells thrashed inside my mind.

System notifications and holographic windows I’d never heard or seen before raced to the ends of the earth and soared above the clouds.

*Ding. Ding. Ding. Diiiiing!*

One sound swallowed another. The translucent holographic windows multiplied from one to five, from five to dozens, then to a hundred.

They were a wave. A mountain.

“Ah…!”

A gasp escaped me before I knew it. A chill ran down my spine at the sight unfolding before my eyes.

Hundreds, perhaps thousands.

More holographic windows than I could count burst forth like fireworks. They all came from one being—the beginning and center of everything.

*The Prophet.*

I could hardly breathe. What I was looking at wasn’t mere information. They were the countless lives he had devoured, and the gravestones they had left behind.

Gravestones that held nothing but names and levels.

And the Truthful Eye within me had seen through the identity of the gravedigger who had built this enormous cemetery, filled with the names of the dead.

It stripped away the thick veil he’d wrapped around himself and revealed the truth.

*Ding.*

The final bell rang in my ears. With it, the last piece of the puzzle fell into place in my mind.

*This is…*

At last, I understood.

The Prophet’s true nature. How this cursed monster had hidden his identity and carried out everything for more than thirty years.

*Right. Now I understand.*

I stared at The Prophet, still smiling. Then, with the breath I’d been holding, I spat out a single word.

“Doppelganger.”

In that instant, I saw it clearly.

“……!”

The corners of his mouth, which had been curved like a half-moon, stiffened. The holographic window hovering above his head shone with a particularly gloomy light.

> **System**
>
> **Level 170 “The Final Abyss” Doppelganger**

* * *

Doppelganger.

A harbinger of ill fortune, a being passed down like a superstition.

Yet even as countless monsters from old myths tore through the pages of legend and leaped into reality, the doppelganger had never once shown itself. Humanity believed there were no doppelgangers among the enemies they had defeated—or those they still had to defeat.

They believed that not even in that horrifying Demon Realm did such a being exist. That it was merely an illusion born of people’s fear, nothing more than a superstition.

But they were wrong.

Doppelgangers had existed from the very beginning. Everyone had simply been mistaken because one had never once revealed itself.

At least, Jin Taekyung knew that better than anyone.

He even knew just how long this incomprehensible being, which had devoured countless lives, had been seeping into the world.

“Michael Silbert. The Great Battle of Paris.”

The young man’s voice emerged abruptly, hard as the cliff rock surrounding them. The monster’s mouth, which had stiffened for a moment, relaxed into a smooth grin.

“That’s right. On the very day you humans call Christmas, I met him and became part of this world.”

December 25, 2020.

The great battle that made a page in history—and made the name Michael Silbert known to all humanity.

As one layer of that day’s truth peeled away, Jin Taekyung swallowed hard. The Skeleton King clenched his teeth, while Magic Johnson stared at The Prophet—or rather, the doppelganger—in disbelief.

“That can’t be. The one that attacked Paris at the time was definitely…”

“A dragon. More precisely, a hatchling less than three hundred years old. It was born a dragon, so arrogance was in its nature. And it let its guard down, as young ones do. Of course, it was unexpected that a human would kill it, even so.”

The doppelganger cut Magic Johnson off, then continued.

“In the end, it was just bad luck. For that young dragon, and for the humans who miraculously survived facing it.”

The Grand Mage, who had lived through the Great Cataclysm firsthand, couldn’t hold back a groan.

“……It was a lie, then. Michael Silbert made all of it up.”

“Well, I wouldn’t say he made it all up. It was true that a dragon attacked Paris, and that he was the only one to survive.”

The doppelganger grinned.

“I knew the moment I first saw Michael. Unlike the other humans, he was quick to size up the situation. Before I’d even killed half of them, he was already on his knees before me. He begged me to let him live. Said he’d do anything.”

“……!”

“It was an interesting offer. I accepted, and he killed the rest of the humans with his own hands.”

Jin Taekyung suddenly remembered a line from the conversation he’d had with Michael Silbert just before the man met his end.

*I was struggling to survive, too!*

The cry had sounded as if he were spitting blood.

He’d been right. Michael Silbert had struggled to survive. He’d had a greater will to survive than anyone, and ambitions he hadn’t yet fulfilled.

And so, a human and a monster joined hands.

But it wasn’t a shackle. It was a contract. Two monsters who differed in appearance but shared the same nature had made a deal to achieve their own goals.

But…

“What for?”

“What?”

“I asked what it was for. What was your real reason for wanting to live among people in this world?”

At Jin Taekyung’s words, spat out as if he were grinding his teeth, the doppelganger fell silent for a moment, then curled up the corners of his mouth.

“Well, I don’t think now’s the time to wait for my answer.”

And at that moment—

*Rumble.*

A tremor coming from far away swept through the canyon.
```
