<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0755.txt",
      "sha256": "624b2092910dfd1aac96047a6672572d44c85491012782303c1239670592062f",
      "bytes": 15293
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8da19a45a52b245edeb4f4b81f8b61ef0d4b44aead5b84d76042efd8a07d8be0",
      "bytes": 1029
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1c194b7ea34a08f4c9fccdfb93409df0ce999feea07887b709b1a47dc5bc35b1",
      "bytes": 218344
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d1bcedca37e55509fbe1e846e218fca312e5df6b625e0cb51641be2e29aa4258",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ccfc855f55312ec12467adaa4cf44ec3ef31256e5d5fdb0c586d556332ff0c70",
      "bytes": 2168
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "832c79600e4f2d026972e0f7aea18cd118bfaca4c0dbbabd6676bf07a1f59334",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "1ba1321af788ea90a2e4eda8e249349f4cd247897ba5041e39c6c7703ba9d7cd",
      "bytes": 741
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9cb3f55b4a97e46513878b680d6969a2f5f5f3ef63f6bde22a80ed2ef1186f33",
      "bytes": 232802
    }
  ],
  "estimated_tokens": 10625
}
-->

# Durable State Update — Chapter 755

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 755. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 755. Profile updates may replace only one
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
  "chapter": 755,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 755,
    "continuity_sources": [755],
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
    "Jin Taekyung is fighting Leviathan while weakened by the Broken Body debuff.",
    "Jin Taekyung has pierced Leviathan's brow with his flaming spear and is attacking from its body.",
    "The Skeleton King's skeletal body can draw and survive Leviathan's lightning.",
    "Leviathan believes Jin may be the human who defeated Asmodeus and is fleeing in fear toward the deep sea.",
    "Jin intends to fight Leviathan together with the Skeleton King.",
    "An unknown mass of bones blocks Leviathan's path in the deep sea."
  ],
  "continuity_sources": [
    754
  ],
  "open_questions": [
    "What is the source or identity of the bones blocking Leviathan?",
    "Can Jin Taekyung and the Skeleton King stop Leviathan in the deep sea?",
    "Will Leviathan survive the injuries to its brow and body?"
  ],
  "safe_through": 754,
  "temporary_decisions": [
    "Render 망가진 신체 as Broken Body.",
    "Retain Skeleton King as the English title for 스켈레톤 킹."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 생도     | **cadet**                                    |
| 일격     | **One Strike**                         |
| 칭호               | **Title**                      |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 상어 | **shark** | Ordinary Korean term for shark used in the protagonist's clarification. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 베히모스 | **Behemoth** | Mythical monster emerging from the Pyeongchang Gate. |
| 바인딩 | **Binding** | A restraining spell used by the mage unit. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 레비아탄 | enemy and hunted monster | Leviathan; you | insulting-casual | Jin orders Leviathan to leave and dismisses its attempt to kill the Skeleton King. |
| 레비아탄 | 진태경 | attacking enemy | you bastard | enraged-insulting | Leviathan directly curses Jin while resisting his attacks. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 754
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 754
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, the creator of the beginner-accessible Smiling Mana Cultivation Method, and a practitioner of the Turtle Breath Technique learned from the Slaughter Saint who is currently fighting Leviathan while weakened by the Broken Body debuff.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 754
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 754
- **Aliases:** None
- **Role:** Leviathan is an ancient S-rank sea monster and ruler of the sea that has been severely wounded by Jin Taekyung, is fleeing toward the deep sea in fear after mistaking him for the human who defeated Asmodeus, and is now blocked by an unknown mass of bones.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

## Korean source

```text
＃755화



스켈레톤 킹의 존재는 마검(魔劍)과 같다.

어떤 것도 베어 낼 수 있을 만큼 예리한 날과 뛰어난 살상력을 지녔지만, 검집에 넣어 놓을 수밖에 없는.

사람들의 이목이 없는 곳에서, 반드시 꼭 필요할 때만 뽑아 휘둘러야 하는 마검.

그런 의미에서, 온 사방이 어둠에 잠식된 깊은 바닷속은 실로 최적의 장소였다.

솨아아악!

물살을 가르며 휘몰아치는 뼈의 파도.

수백, 어쩌면 수천 년 동안 축적되었을 해양 생물들의 사체가 한 존재의 부름을 받고 깨어난다.

눈을 뜸과 동시에 혼백(魂魄)을 사슬처럼 옭아맨 명령을 따라, 헤아릴 수조차 없이 무수히 많은 뼈가 서로를 향해 달려들었다.

우득, 촤르르륵!

잇고, 뭉치고, 비로소 완성해 낸다.

심해의 입구를 틀어막은 거대한 뼈의 관문을. 일체의 숨결도 허락하지 않는 견고한 망령의 방패를.

그리고 이 경이로운 현상의 중심에, 해저 깊숙이 잠들어 있던 망령들을 일으켜 세운 왕이 있었다.

- 멈춰라.

화아아악.

거대한 기운이 부풀어 올랐다.

눈부신 금발이 물결을 따라 흔들린다. 훤히 드러난 이마 위로 희미한 은빛 광휘가 떠올라 하나의 형태를 갖추었다.

왕관.

그것은 스스로 왕좌에 오른 존재에게 허락된 징표였고, 마력이라고 부르기에는 너무나도 찬란히 빛나는 힘이었다.

- 어명(御名)이다.

위엄 어린 음성과 오만한 눈빛.

빛나는 금안(金眼)으로 자신을 응시하는 그의 모습에, 레비아탄은 감히 동족을 배신한 변절자의 진정한 정체를 깨달았다.

‘스켈레톤 킹(Skeleton King)……!’

망령들의 왕.

마왕 아스모데우스에게 충성을 맹세한 72군단의 주인 중 하나이자, 끊임없이 되살아나는 불사(不死)의 군단을 이끌며 인간들과 맞서 싸우다 소멸을 맞이한 존재.

그러나 놈은, 어느새 눈부신 왕관을 쓴 채 앞길을 막아선 저 변절자는 레비아탄의 기억 속에 남아 있는 스켈레톤 킹이 아니었다.

‘도대체 어떻게!’

소멸이 있으면 탄생도 있는 법.

공석이 되어 버린 왕좌에 또 다른 누군가가 앉는 것은 당연한 이치였으나, 새롭게 즉위한 망령들의 왕은 달라도 너무나 달랐다.

- 어찌 그만한 마력을 지니고도 인간 따위의 편에 선단 말이냐!

당혹감과 분노가 뒤섞인 괴성.

직경만 수백 미터에 이르는 레비아탄의 거체(巨體)가 빛살처럼 쏘아졌다.

콰아아아아!

사방에서 회오리치는 거센 와류.

새하얀 뼈의 장벽을 향해 나아가는 레비아탄의 움직임에는 한 치의 망설임도 없었다.

아니, 그 외에는 남은 선택지가 없었다.

반드시 뚫어야 한다. 앞을 가로막은 저 벽을 넘고, 더 깊은 곳으로 들어간다면 반드시 살아남을 수 있다.

자신은 심해에서 처음 눈을 뜬 존재. 누구도 침범하지 못하는 그 칠흑 같은 공간에서라면 충분히 승리를 장담할 수 있었다.

적어도 레비아탄은 그렇게 믿고 있었다.

나직한 목소리와 함께 찾아온 격통을 느끼기 전까지는.

“어딜 그렇게 바쁘게 가시나. 아직 정산도 안 끝났는데.”

퍼걱!

- 크아아아아!

순간, 빛살처럼 쏘아지던 레비아탄의 거체가 용틀임했다.

한 손으로 괴물의 미간 깊숙이 박아 넣은 창대를 단단히 틀어쥔 채, 다른 한 손으로는 언제 꺼내 들었는지 모를 검을 거대한 눈동자에 쑤셔 박은 진태경이 속삭이듯 중얼거렸다.

“한 명당 한 방으로 치면 3박 4일은 걸릴 테니까, 깔끔하게 천 명으로 계산하자.”

채 하루도 지나지 않은 현재 시점에서 밝혀진 사상자만 무려 10만 이상.

비록 얼굴도 이름도 모르는 낯선 이들이었지만, 고통에 몸부림치는 레비아탄을 응시하는 진태경의 눈동자는 차가운 분노로 달구어져 있었다.

“핏값은 돌려받아야지, 안 그래?”

몬스터와 인간. 인간과 몬스터.

이것은 삼십여 년 전, 마왕 아스모데우스가 이 땅에 처음 발을 디딘 그 순간부터 정해진 운명이었다.

한때 소년이었던 청년은 어느 날 영영 돌아오지 못하게 된 자신의 아버지를 똑똑히 기억하고 있었다.

이번 재앙으로 인해 자신과 같은 상황에 처한 이들의 아픔도 함께.

‘인벤토리 오픈. 소환.’

창, 검, 도끼.

뭐든 상관없다.

틈날 때마다 인벤토리 깊숙이 처박아 두었던 수많은 무기들이 스치듯 손아귀에 잡혔고, 찰나의 순간 표적을 향해 내리꽂혔다.

푸푸푸푹! 퍼걱!

비늘이 박살 나고, 뼈와 살점이 으스러진다.

평소와 같은 세밀한 공력의 운용은 찾아볼 수 없었지만, 그것만으로도 충분했다.

일평생 바다의 재앙으로 군림해 왔던 신화 속 괴물은 지금껏 겪어 본 적 없는 끔찍한 격통에 몸부림쳤다.

- 끄아아아아아!

구구구궁!

레비아탄을 중심으로 발산된 마력이 바다를 뒤흔들었다.

파도에 휩쓸려 떠밀려 온 해양 생물들이 막강한 피어를 이기지 못하고 눈을 허옇게 까뒤집었고, 뒤이어 한 존재의 나직한 음성이 죽은 육신에 새로운 혼백을 불어넣었다.

- 일어나라.

서서히 가라앉던 대왕고래의 지느러미가 꿈틀거린다. 불과 몇 시간 전 괴물의 한 끼 식사로 몸뚱어리가 토막 났던 수십 마리의 철갑상어가 톱날 같은 이빨을 드러냈다.

- 구우우웅.

- 그그그극.

죽었으나, 죽지 않은 존재들.

비로소 하나의 군단으로 거듭난 무수한 해양 생물들은 한몸처럼 움직였다. 그리고 그 선두에, 이들을 깨운 망령들의 왕이 있었다.

- 군단이여!

콰드드득!

스켈레톤 킹의 부르짖음과 함께 뼈의 장벽이 허물어졌다.

아니, 뼈로 이루어진 거대한 괴물로 화하여 레비아탄을 향해 돌격했다.

콰아아아아!

온통 녹색 핏빛으로 물든 시야 너머, 자신을 향해 한몸이 되어 달려드는 스켈레톤 군단을 본 레비아탄이 울부짖었다.

- 감히! 이 잡스러운 것들 따위가!

고오오옹. 퍼엉!

깊은 수심 속, 압축된 바닷물이 포탄처럼 쏘아졌다. 수백에 이르는 파동이 무수한 뼈를 부수고 깨트렸다.

그러나 바다의 재앙으로 군림하는 레비아탄이라 할지라도 모든 것을 통제할 수는 없었다.

이 드넓은 대양은 오롯이 그의 것이되, 파도에 뒤섞여 흐르고 있는 무수한 죽음과 망령들은 오직 왕관의 주인을 따랐으니까.

- 눈을 떠라.

스켈레톤 킹을 중심으로 거대한 마력이 꿈틀거렸다.

휘몰아치는 와류 사이로 소멸해 가던 망령들이 고개를 들었다.

- 레이즈 스켈레톤(Raise Skeleton).

촤르르르륵!

레비아탄은 진태경에 의해 반쯤 뭉개진 눈을 크게 떴다.

- ……!

파동에 휩쓸려 사라졌던 뼈들이 다시금 모여든다.

부서진 뼈마디를 재조립하고, 또 다른 형태로 변모한 그것들이 레비아탄의 거체에 달라붙었다.

균열이 간 힘의 틈새로 스며들어 아직도 바닥을 드러내지 않은 괴물의 마력을 거머리처럼 빨아들였다.

스아아아악!

‘이런 미친……!’

레비아탄은 경악했다. 과거의 스켈레톤 킹조차 이토록 쉽고 빠르게 군단을 재구성하지는 못했다.

그런데 저 풍부한 마력은, 명백한 상위 몬스터인 자신을 공격하게끔 만드는 이 말도 안 되는 지배력은 뭐란 말인가.

게다가…….

‘내 마력에 의한 영향을 전혀 받지 않는다.’

몬스터 간의 관계는 오직 철저한 힘의 논리로 이루어진다.

하지만 스켈레톤 킹은, 새롭게 망령들의 왕좌에 오른 저 변절자는 달랐다.

비록 두려움은 품었을지언정 레비아탄의 마력에 지배당하지 않았고, 수심이 깊은 곳으로 들어오자 오히려 마음껏 날뛰고 있었다.

‘도대체 어떻게?’

만약 레비아탄이 과거의 힘을 온전히 회복했거나, 혹은 최대한 평정심을 유지했더라면 알 수 있었을 것이다.

스켈레톤 킹이 지닌 힘이 일반적인 마력과 전혀 다른 성질을 띠고 있다는 것을.

그리고 S급 몬스터 중에서도 네임드로 꼽히던 아크 리치와 베히모스를 쓰러트리며 상당한 마력을 흡수한 스켈레톤 킹의 격은, 자신에 비해 그리 떨어지지 않는다는 것을.

하지만 지금의 레비아탄은 달랐다.

오랜 잠에서 깨어난 지 불과 며칠 만에 큰 상처를 입고 지쳐 있던 신화 속 괴물에게는, 이 모든 상황이 믿을 수 없이 혼란스럽게만 느껴졌다.

아주 잠깐이나마 자신에게 들이닥친 현실을 잊을 만큼.

그리고 레비아탄의 흐릿한 정신을 일깨운 것은, 뒤이어 찾아온 끔찍한 작열통(灼熱痛)이었다.

화륵. 치지지직!

레비아탄은 이미 절반이나 빠져 버린 이빨을 악물었다.

대격변 당시에도 헌터라 불리는 수많은 인간들과 전투를 치렀지만 이런 고통은 느껴 본 적 없었다.

오러가 서린 날붙이에 베여도 그저 미약한 통증에 그쳤고, 가장 큰 부상이라 해 봤자 다른 몬스터의 마력을 흡수하고 쉬면 금세 나았으니까.

그러나 지금 이 순간에도 자신의 거대한 머리를 들쑤시며 살점과 뼈를 재로 만들고 있는 화염은, 저 자그마한 인간은 달랐다.

“오십. 오십일. 오십이. 오십삼…….”

푸푸푸푹!

지금껏 상대했던 인간들과는 질이 다르다. 아니, 격이 다르다.

쉴 새 없이 중얼거리며 어디서 나왔는지 모를 무기를 곳곳에 박아 넣고 들쑤신다. 중얼거리는 말에서는 몬스터조차 범접할 수 없는 광기마저 느껴질 정도였다.

“벌써 절반 왔다. 우리 조금만 더 힘내자.”

“회원님, 한 세트만 더.”

“움직이지 말고 딱 대라. 뼈 나간다.”

“물론 안 움직여도 나간다. 지금보다 더 아프게 죽고 싶으면 지랄해 봐, 어디.”

그아아아아아!

레비아탄은 괴성을 내질렀다.

아니, 그것은 괴성이 아닌 비명이었다.

한때 다섯 개의 대양을 넘어 대륙의 해안까지 떨게 했던 피어(Fear)는, 말 그대로 공포가 되어 레비아탄 스스로를 옭아매고 있었다.

그것도 그에 비해 한없이 작은 한 인간에 의해서.

‘죽어? 죽는다고? 내가?’

일평생 포식자로 살아오며 잊고 있던 생존 본능이 깨어난다.

이미 주위를 제대로 식별할 수 없을 만큼 뭉개진 눈동자와 시시각각 죽음에 가까워지고 있는 몸뚱어리.

그만큼 점점 무뎌지는 고통 속에서 레비아탄은 빠르게 자신이 처한 현실을 판단했다.

‘단 한 번. 단 한 번의 기회를 노려 놈들을 떼어 내고 최대한 멀리 도망친다.’

다행히 아직 희망은 남아 있었다.

끈질긴 생명력과 아직 절반밖에 소모하지 않은 마력. 게다가 적들 역시 처음 만났을 때와는 달랐다.

특히 하루 전, 엄청난 위력의 일격으로 자신에게 극심한 타격을 안겼던 저 인간은 더더욱.

‘그때와 같은 힘을 보일 수 있다면 나는 이미 죽고도 남았겠지. 놈에게도 문제가 생긴 것이 틀림없다.’

레비아탄은 높은 지능을 지닌 고등 몬스터였다. 교활할 만큼 그 판단은 정확했고, 목숨을 건 결단은 신속했다.

- 콰우우우우!

직경만 수백여 미터에 이르는 거체가 온 힘을 다해 몸부림치며 마력을 발산한다. 거대한 기운이 부풀어 오르듯 뻗어 나가며 주위의 모든 것을 밀어 냈다.

콰아아아!

엄청난 수압(水壓)과 함께 생겨난 수십여 개의 회오리.

거머리처럼 달라붙어 마력을 흡수하던 스켈레톤들을 단번에 떨쳐 낸 레비아탄은 한 방향을 향해 돌진했다.

후우우우웅!

거대한 몸뚱어리를 타고 흐른 물살이 거센 와류가 되어 휘몰아친다.

간발의 차로 레비아탄을 놓친 스켈레톤 킹이 비명처럼 외쳤다.

- 인간! 피해라!

이미 늦었다.

그 말을 속으로 삼킨 레비아탄은 온 힘을 다해 쏘아져 갔다.

이미 수천 년 전부터 해저 깊숙이 뿌리내린 절벽을 향해.

이 지긋지긋한 인간을 떼어 내기 위해.

그리고 다음 순간.

구구구구궁!

엄청난 파동이 충돌과 함께 바다를 뒤흔들었다.



* * *



피하려고 했다. 충분히 피할 수 있었다.

다만, 전투의 열기에 휩쓸려 한 가지 중요한 사실을 잊고 있었을 뿐이다.

내가 가진 어떤 종류의 힘에는, 유통 기한이 있다는 것을.

삐빅.



- [수상 구조대원]의 칭호 유지 시간이 종료되었습니다!

- [수상 구조대원]의 칭호 효과가 사라집니다!

- [수상 구조대원의 물갈퀴]가 사라집니다!

- [수상 구조대원의 아가미]가 사라집니다!

- [6일 23시간 59초] 후 재발동이 가능합니다!



빌어먹을.

그 외마디 욕설을 내뱉기도 전에, 녹색 이끼와 해조류에 뒤덮인 거대한 바위가 내 등 뒤에 성큼 다가와 있었다.

콰드득!

“커헉!”

강렬한 충격. 그리고 통증이 전신을 쥐어짠다.

순간 새하얗게 물든 시야 속, 충돌의 여파를 완전히 흡수하지 못했음에도 비틀거리며 수면 위로 도망치는 레비아탄의 뒷모습이 보였다.

반쯤 토막 난 상어를 타고 그 뒤를 쫓는 스켈레톤 킹의 모습도 함께.

촤르르륵!

본 바인딩(Bone Binding).

물살을 가로지르며 뻗어 나간 뼈의 그물이 거대한 동체를 가로막았지만, 필사(必死)의 의지를 담아 몸부림치는 괴물을 묶어 둘 수는 없었다.

콰직!

산산조각 나며 흩어지는 뼛조각들.

그러나 아직 끝난 것이 아니다.

나는 전신을 짓누르는 수압을 이겨 내며 창대를 쥔 손아귀에 힘을 더했다.

까드드득.

어둡고 차가운 바닷물이 입과 코를 향해 스며들었지만, 괜찮다.

날카롭게 벼려진 오감(五感)은 아직 표적을 향하고 있으니까.

지금 이 순간, 투명한 창날에 서린 청백색의 겁화도. 올올히 피어 오른 근육도 저 멀리 도망치는 거대한 괴물의 몸뚱어리를 향하고 있었으니까.

스으으윽.

전신의 감각이 곤두선다.

하루 전과 같은 상황, 그러나 이번에는 다를 것이라는 확신이 몸과 마음을 지배하고 있었다.

‘두 번은 없다.’

스스로에 대한 믿음.

그리고 필살(必殺)의 의지를 실어, 나는 온 힘을 다해 창을 쏘아 보냈다.

슈확!

바다를 가로지르는 한 줄기의 불꽃. 그 끝에, 기다리던 비명이 있었다.

- 그아아아아아!

사냥의 끝이었다.
```

## Final English reading copy

```markdown
# Chapter 755

The Skeleton King’s existence was like a demonic sword.

It possessed a blade sharp enough to cut through anything and tremendous killing power, yet it was something that could only be kept sheathed.

A demonic sword that had to be drawn and wielded only when absolutely necessary, and only where no one was watching.

In that sense, the deep sea, where darkness had swallowed every direction, was truly the perfect place.

*Shwoooooosh!*

A wave of bones surged and churned through the water.

The corpses of marine creatures, accumulated over hundreds—perhaps thousands—of years, awoke at the call of a single being.

The moment they opened their eyes, countless bones raced toward one another, obeying commands that bound their souls like chains.

*Crack. Clatter-clatter!*

They connected.

They merged.

And at last, they were complete.

A massive bone gateway that blocked the entrance to the deep sea.

A sturdy shield of wraiths that permitted not even a single breath to pass through.

And at the center of this wondrous phenomenon stood the king who had awakened the wraiths sleeping deep beneath the seabed.

—Stop.

*Fwoooooosh.*

A massive force swelled.

Brilliant blond hair swayed with the current. A faint silver radiance appeared above his fully exposed forehead and took shape.

A crown.

It was a mark granted to one who had ascended the throne by his own power, and the force it represented shone far too brilliantly to be called mere magical power.

—This is a royal command.

A voice filled with dignity and eyes filled with arrogance.

When Leviathan saw him staring back with shining golden eyes, it finally realized the true identity of the traitor who had dared to betray his own kind.

*The Skeleton King…!*

The king of wraiths.

One of the lords of the seventy-two legions who had sworn loyalty to the Demon King Asmodeus, and a being who had met its end after leading an endlessly resurrecting immortal legion against humanity.

But that traitor blocking Leviathan’s path with a dazzling crown was no longer the Skeleton King preserved in its memories.

*How?*

Where there was erasure, there was birth.

It was only natural that someone else would sit upon a throne left vacant. Yet the newly enthroned king of the wraiths was different—far too different.

—How can you stand on the side of mere humans while possessing such tremendous magical power?!

A shriek filled with equal parts bewilderment and rage.

Leviathan’s massive body, hundreds of meters in diameter, shot forward like a ray of light.

*Kwaaaaaa!*

Violent whirlpools spun in every direction.

Leviathan did not hesitate for even an instant as it advanced toward the wall of pure-white bones.

No. It had no other choice.

It had to break through. If it overcame the wall blocking its path and entered the deeper waters, it could survive.

Leviathan was a being that had first opened its eyes in the deep sea. Within that pitch-black space that no one could invade, it was confident that victory would be within reach.

At least, that was what Leviathan believed.

Until it felt the agony that arrived with a low voice.

“Where are you off to in such a hurry? We haven’t even settled the bill yet.”

*Crunch!*

—GRAAAAAAAH!

Leviathan’s massive body, which had been shooting forward like a ray of light, writhed violently.

Jin Taekyung had one hand tightly wrapped around the spear shaft driven deep into the monster’s brow. With his other hand, he had rammed a sword—no one knew when he had drawn it—into the monster’s enormous eye.

He muttered in a whisper.

“If we count one hit per person, it’ll take three days and four nights. Let’s make it a clean thousand.”

The number of casualties confirmed in less than a day already exceeded one hundred thousand.

They were strangers whose faces and names Jin did not know, but as he stared into the writhing Leviathan’s eyes, his own gaze burned with cold fury.

“We’ll have to get paid back for all that blood, won’t we?”

Monster and human.

Human and monster.

This was a fate decided from the moment the Demon King Asmodeus first set foot on this land more than thirty years ago.

The young man who had once been a boy remembered his father clearly—the father who had one day left and never returned.

He also remembered the pain of all those who had been placed in the same situation by this disaster.

*Inventory open. Summon.*

Spear, sword, axe.

It did not matter.

Countless weapons he had shoved deep into his Inventory whenever he had the chance flashed into his hands one after another, then plunged toward their targets in the blink of an eye.

*Thrust-thrust-thrust! Crunch!*

Scales shattered.

Bone and flesh were crushed.

The precise circulation of internal energy he usually employed was nowhere to be seen, but even that was enough.

The mythical monster that had reigned as the calamity of the sea for its entire life writhed in horrible agony unlike anything it had ever experienced.

—GRAAAAAAAH!

*Ruuuuumble!*

Magical power erupted from Leviathan and shook the sea.

Marine creatures swept along by the waves were unable to resist the overwhelming Fear. Their eyes rolled back until only white showed, and then a low voice breathed new souls into their dead bodies.

—Rise.

The fin of a blue whale that had been slowly sinking twitched.

Dozens of sturgeon whose bodies had been torn apart only hours earlier to serve as a monster’s meal bared their sawlike teeth.

—Grrrrrrr.

—Grk. Grk.

They were dead, yet not dead.

The countless marine creatures that had finally become a single legion moved as one body. And at their head stood the king of wraiths who had awakened them.

—My legion!

*Craaaaaack!*

At the Skeleton King’s cry, the wall of bones collapsed.

No—it transformed into a massive monster made of bones and charged toward Leviathan.

*Kwaaaaaa!*

Beyond a field of vision dyed entirely green with blood, Leviathan saw the Skeleton Legion charging toward it as one body and let out a roar.

—How dare you! You filthy little things!

*Gooooong. Boom!*

Deep beneath the water, compressed seawater shot out like cannonballs. Hundreds of waves shattered and broke countless bones.

But even Leviathan, who reigned as the calamity of the sea, could not control everything.

This vast ocean belonged entirely to it, but the countless deaths and wraiths flowing within the waves followed only the owner of the crown.

—Open your eyes.

Massive magical power writhed around the Skeleton King.

Through the raging whirlpools, wraiths that had been fading away raised their heads.

—Raise Skeleton.

*Clatter-clatter-clatter!*

Leviathan opened wide the eye that Jin Taekyung had half-crushed.

—…!

The bones that had been swept away by the waves gathered once more.

They reassembled their shattered joints, transformed into different shapes, and clung to Leviathan’s massive body.

They seeped through the cracks in its strength and clung to the monster’s magical power, which still had not run dry, draining it like leeches.

*Shhhhhhh!*

*What the hell…?*

Leviathan was stunned. Even the Skeleton King of the past had never been able to rebuild his legion so easily or so quickly.

Then what was that abundant magical power?

What was that absurd power of domination that made them attack Leviathan, a monster clearly superior to them?

And besides…

*It isn’t affected by my magical power at all.*

The relationship between monsters was governed solely by the ruthless logic of strength.

But the Skeleton King—the traitor who had newly ascended the throne of the wraiths—was different.

Even if he felt fear, he was not controlled by Leviathan’s magical power. And once they entered deeper waters, he was instead rampaging to his heart’s content.

*How?*

If Leviathan had fully recovered its former strength, or if it had maintained its composure as much as possible, it would have realized.

It would have realized that the Skeleton King’s power possessed a nature entirely different from ordinary magical power.

And it would have realized that the Skeleton King, who had absorbed a considerable amount of magical power after defeating the Arch Lich and Behemoth—both named monsters among the S-rank monsters—was not far beneath Leviathan in standing.

But the Leviathan of today was different.

For the mythical monster that had awoken from a long sleep only days ago, been gravely wounded, and grown exhausted, the entire situation was simply too confusing to believe.

Confusing enough to make it forget reality for one brief moment.

Then the horrific searing pain arrived and jolted Leviathan’s hazy mind awake.

*Fwoosh. Sizzle-sizzle!*

Leviathan gritted its teeth, half of which had already fallen out.

It had fought countless humans called Hunters during the Great Cataclysm, but it had never experienced pain like this.

Even when cut by a blade cloaked in aura, it had felt no more than a faint sting. And its worst injuries had always healed quickly after it absorbed another monster’s magical power and rested.

But the flames tearing through its enormous head even now, turning flesh and bone to ash, were different.

So was that tiny human.

“Fifty. Fifty-one. Fifty-two. Fifty-three…”

*Thrust-thrust-thrust!*

He was different from the humans Leviathan had fought before.

No—his level was different.

He kept muttering without pause as he drove weapons of unknown origin into various parts of Leviathan’s body and twisted them around. There was even a madness in his muttering that not even monsters could approach.

“We’re halfway there already. Come on, let’s keep it up a little longer.”

“Sir, just one more set.”

“Don’t move. Hold still, or you’ll break a bone.”

“Of course, it’ll break even if you don’t move. If you want to die in even more pain than this, go ahead and try something.”

—GRAAAAAAAAAH!

Leviathan let out a horrible cry.

No.

It was not a roar.

It was a scream.

The Fear that had once shaken the shores of the continent beyond the five oceans had become true terror, binding Leviathan itself.

And it was being caused by a single human who was unimaginably small compared to it.

*Die? I’m going to die? Me?*

The survival instinct it had forgotten after living as a predator for its entire life awakened.

One eye had already been crushed so badly that Leviathan could no longer properly distinguish its surroundings. Its body was drawing closer to death with every passing moment.

As the pain gradually grew duller, Leviathan swiftly judged the reality of its situation.

*Just once. I need to find a single opening, shake them off, and run as far away as possible.*

Fortunately, hope still remained.

Its tenacious vitality.

The magical power it had only used up halfway.

And the fact that its enemies were different from when it had first encountered them.

Especially that human who had dealt it such devastating damage with a single attack the day before.

*If he could display the same power as then, I would already be dead. Something must have happened to him too.*

Leviathan was a highly intelligent monster. Its judgment was accurate enough to be cunning, and its decision to risk its life was swift.

—Kwoooooo!

Its massive body, hundreds of meters in diameter, writhed with all its strength and released its magical power. A tremendous force surged outward like something inflating, pushing away everything around it.

*Kwaaaaaa!*

Dozens of whirlpools formed amid the enormous water pressure.

Leviathan shook off the Skeletons that had clung to it like leeches and were draining its magical power, then charged in a single direction.

*Whoooooosh!*

The water flowing over its enormous body became violent whirlpools and churned wildly.

The Skeleton King narrowly missed Leviathan and cried out like a scream.

—Human! Get out of the way!

It was already too late.

Swallowing those words, Leviathan shot forward with all its strength.

Toward a cliff that had taken root deep beneath the seabed thousands of years ago.

Toward the wall it needed to use to shake off this wretched human.

And then—

*Ruuuuumble!*

An enormous wave shook the sea as the two collided.

* * *

I had tried to avoid it.

I could have avoided it easily.

I had simply forgotten one important fact in the heat of battle.

Some of the powers I possessed had an expiration date.

*Beep.*

> **System**
>
> - The duration of the **Aquatic Rescue Worker** Title has ended!
>
> - The effects of the **Aquatic Rescue Worker** Title have disappeared!
>
> - The **Webbed Feet of the Aquatic Rescue Worker** have disappeared!
>
> - The **Gills of the Aquatic Rescue Worker** have disappeared!
>
> - Reactivation will be possible in **6 days 23 hours 59 seconds**!

Damn it.

Before I could even spit out that single curse, a massive boulder covered in green moss and seaweed had come up right behind me.

*Crack!*

“Urgh!”

A powerful impact.

Then pain squeezed my entire body.

Through the momentarily whitened field of vision, I saw Leviathan’s back as it staggered toward the surface, fleeing despite being unable to fully absorb the force of the collision.

I also saw the Skeleton King chasing after it while riding a half-dismembered shark.

*Clatter-clatter-clatter!*

Bone Binding.

A net of bones shot across the current and blocked the enormous body, but it could not restrain the monster thrashing with a desperate will to survive.

*Crunch!*

The bones shattered and scattered in every direction.

But it was not over yet.

I resisted the water pressure crushing my entire body and tightened my grip around the spear shaft.

*Craaaaack.*

Dark, freezing seawater seeped toward my mouth and nose, but I was fine.

My sharpened five senses were still fixed on the target.

The blue-white hellfire burning along the transparent spearhead was aimed at the body of the enormous monster fleeing in the distance.

So were my muscles, taut and ready to erupt.

*Shhhhhhh.*

Every sensation in my body sharpened.

The situation was the same as yesterday.

But a certainty took hold of my body and mind.

This time would be different.

*There won’t be a second time.*

Faith in myself.

And with the will to deliver a killing blow, I launched the spear with all my strength.

*Shhwaaaak!*

A single streak of flame crossed the sea.

At its tip waited the scream I had been expecting.

—GRAAAAAAAAAH!

The hunt was over.
```
