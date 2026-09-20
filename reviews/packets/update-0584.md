<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0584.txt",
      "sha256": "28d65a56d80ad4258680c366265f6c093b784c5274b31aa8212b893cc44af4a4",
      "bytes": 15662
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e988fb8c51d360a0bd733ba0290d657f2e5e41cec86d0394bade4a49efe17d22",
      "bytes": 2708
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15a04230fedce4ec9e1decc68aa5d6aa29e76470ecee3a99af66065d50dc28e6",
      "bytes": 182881
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "d7cf1436ef450b50f2036dba76686395b0c88276bcd7abc881f8842045956291",
      "bytes": 730
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "0cc946b7f22e445d6bea9e0ce915525a48c390a456b8cae843cf738044f6bc01",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "02dff2b1ff66bbf07bf3d53ec7ab3c79ca7c789209550680a3fd5a4b5aede217",
      "bytes": 553
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "6022224da1a44b21141f63a9344951a4b55daa148708549f38206b15f1f8f01a",
      "bytes": 643
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "69e8d4b89e2723d0696e461f9345b09f84fe025a73c6f91c57d460dc5b6bdce4",
      "bytes": 619
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "af4a14f48749002a97d20b0ebb440743d350ce3cbda013bc5ff43c8987683cd4",
      "bytes": 1035
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "dcbc510e8c96470625d557fe975e740066d0b7b12eb329d73b83d9af4385b87e",
      "bytes": 180637
    }
  ],
  "estimated_tokens": 10732
}
-->

# Durable State Update — Chapter 584

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 584. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 584. Profile updates may replace only one
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
  "chapter": 584,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 584,
    "continuity_sources": [584],
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
    "The Pyeongchang Gate's Behemoth killed more than half of the twenty-two Peace Guild Hunters; Choi Minwoo collapsed after severing two forelegs, and Kim Hwajong lost his left arm rescuing him before remaining behind to fight."
  ],
  "continuity_sources": [
    583,
    582
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept unused in his pocket, and what did its release of darkness and light accomplish?",
    "Did Choi Minwoo survive Behemoth's attack, and can Kim Hwajong survive the confrontation after sending the other Hunters away?"
  ],
  "safe_through": 583,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Stone King for 스톤 킹 and Skeleton King for 스켈레톤 킹.",
    "Use Area A for A구역.",
    "Use Hwa-jong for 화종.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, and Hell Fire for 헬 파이어."
  ],
  "version": 1
}
```

## Exact glossary matches

| 김화종    | **Kim Hwajong**   |
| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 그리스 | **Grease** | Spell used to make the ogres lose their footing. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 베히모스 | **Behemoth** | Mythical monster emerging from the Pyeongchang Gate. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 화종 | 최민우 | butler_to_Young_Master | Young Master | formal and deferential | Butler Kim consistently addresses Choi Minwoo with the established deferential title. |
| 최민우 | 화종 | Young Master to butler | Butler Kim | formal and respectful | Choi refers to Hwa-jong as 김 집사님 while discussing the concealed truth. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 582
- **Aliases:** Slayer
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he is believed to remain alive after more than twenty years of unconsciousness, with Area A only suspected as his location.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 583
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 583
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 583
- **Aliases:** Butler Kim
- **Role:** Hwa-jong is Choi Minwoo's loyal butler and personal escort; after losing his left arm rescuing Choi, he remains behind to confront Behemoth.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 583
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong is a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort; after losing his left arm rescuing Choi, he remains behind to confront Behemoth.
- **Personality:** Gentle and composed
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 583
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative, a formidable aura-wielding swordsman who wields Hero's Soul, and is mobilizing every available power to unseat Go Jun from Ares Guild leadership; he was rendered unconscious in the Pyeongchang battle and carried away by Hwa-jong.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Choi Minwoo is Cheon Taemin's maternal grandson and only living blood relative, was kept out of public knowledge by Lee Jungryong, is closely integrated with Jin Taekyung's family, seeks to acquire the Ares Guild intact, and now knows that Song Cheonwoo and Lee concealed Taemin's collapse and purged aides while he investigates Taemin's fate.

## Korean source

```text
＃584화



구구구구궁!

불기둥이 솟구쳤다. 산이 흔들렸다. 반경 수백 미터에 달하는 공간이 초고온의 열기로 들끓고 눈과 흙, 바위가 녹아 내린다.

용암이 흘러넘치는 죽음의 땅. 모든 것이 증발해 버린 그 위에 첱탑처럼 우뚝 선 두 존재가 있었다.

- 인. 간. 따. 위. 가. 감. 히!

검게 그을린 채 분노하는 신화 속 마수를, 반백의 노집사는 담담한 눈빛으로 바라보았다.

헬 파이어(Hell Fire).

지옥에서 불러온 겁화조차 베히모스를 쓰러트리지 못했다. 거대한 엄니 하나가 흔적도 없이 녹아내리고, 전신이 검게 그을렸지만, 놈은 여전히 건재했다.

하지만…….

“더럽게 단단한 놈이로구나.”

김화종은 물러서지 않았다. 물러설 수 없었다.

그는 하나밖에 남지 않은 손으로 매직 스태프(Magic Staff)를 힘주어 붙잡았다.

화륵.

짧고 가느다란 형태의 스태프가 불길에 휩싸였다. 화염이 훑고 지나간 자리에는 더욱 굵고, 길어진 스태프가 새롭게 모습을 드러냈다.

혼란했던 대격변의 시기. 수많은 몬스터를 잿더미로 만들며 주인에게 겁화(劫火)의 마법사라는 이명을 붙여 주었던 애병이다.

김화종은 붉은빛이 감도는 스태프를 베히모스에게 겨누며 뇌까렸다.

“멈추어라. 네놈은 어디에도 가지 못한다.”

- 노. 옴!

베히모스가 울부짖었다. 동시에 자욱하게 내려앉은 검은 안개가 살아 있는 생물처럼 움직여 김화종을 향해 쏘아졌다.

쉬이이익!

그것은 전신을 옭아맬 밧줄인 동시에, 피륙을 찢고 부술 칼날이었다.

그러나 김화종은 사방을 에워싸고 들이닥치는 안개를 침착한 눈빛으로 바라보았다.

순간, 그의 피 묻은 손에 들린 스태프가 지면을 찍었다.

쿠궁!

깊은 울림과 함께 파동이 퍼져 나갔다. 김화종을 중심으로 피어오른 불꽃이 하나의 고리가 되어 주위를 에워쌌다.

화륵, 콰아아아!

불은 파괴의 상징이기 이전에, 정화(淨化)의 힘.

그를 향해 쏘아지던 검은 안개가 불길에 닿은 순간 잿더미처럼 사그라들었다.

지상을 굽어보는 마수의 거대한 눈동자에 우뚝 선 인간의 모습이 고스란히 비쳤다.

- 이. 게. 무. 슨?

그것은 베히모스에게도 뜻밖의 상황이었다.

상대는 한낱 인간. 그러나 저 자그마하고 하찮은 존재는 자신에게 상처를 입힌 것으로도 모자라, 공격을 무효화시켜 버렸다.

- 너. 인. 간. 이. 여!

강력한 피어(Fear)가 담긴 포효가 온 사방을 뒤흔들었다. 그러나 불길이 일렁이는 눈빛과 달리 김화종의 마음은 지극히 평온했다.

눈앞의 마수는 한 가지를 오판했다.

누구나 마음 깊숙한 곳에 간직하고 있는 두려움이, 지금 마주한 늙은 인간에게는 존재하지 않는다는 것을.

‘다행입니다. 도련님.’

닿지 않을 중얼거림과 함께 김화종은 빙긋 웃었다. 그의 유일한 두려움은 지금 이 순간에도 재앙으로부터 멀어지고 있었다.

그 아이, 최민우가 살아남을 수만 있다면…… 어떻게 되어도 좋았다.

‘설령 이 자리에서 죽는다 할지라도.’

마수의 발에 짓밟혀 으스러져도, 엄니에 꿰인 채 유언 한 마디 남기지 못하고 절명해도, 마나와 육신을 한계까지 쥐어 짜낸 끝에 잿더미처럼 스러진다 하여도 괜찮다.

‘도련님께서 무사하시다면, 저는 그것으로 족합니다.’

그렇기에 김화종은 기쁜 마음으로 스태프를 쥐었다.

불그스름한 빛이 감도는 애병의 끄트머리로, 이미 한계를 벗어난 막대한 마나가 밀려들었다. 열기를 띤 마나가 화염이 되어 터져 나왔다.

“휩쓸어라.”

파이어 웨이브(Fire Wave).

짧은 영창과 함께 불의 파도가 넘실거리며 뻗어 나갔다.

그 끝에 선 존재, 베히모스가 노한 외침과 함께 코끼리의 그것처럼 길고, 그보다 수십 배는 거대한 코를 휘둘렀다.

화아악!

강맹한 파공성과 함께 일어난 바람이 불의 파도를 덮쳤다. 초고온의 열기가 단번에 사그라들고, 보이지 않는 바람의 칼날이 날아들어 사방을 할퀴었다.

쉬쉬쉬쉭! 서걱!

종잇장처럼 갈라지고 찢겨 나간 지면. 그러나 김화종은 이미 아슬아슬하게 그 자리를 벗어난 후였다.

베히모스의 측면을 향해 쇄도하는 노집사의 입술 사이로 낮은 목소리가 흘러나왔다.

“쏘아져라.”

블레이즈(Blaze).

퍼엉!

그가 내디딘 발끝을 따라 화염이 터져 나왔다.

순간적인 폭발과 함께 한 줄기 불꽃이 되어 쏘아지던 김화종의 머리 위로, 짙은 그림자가 드리워졌다.

후우웅!

“……!”

이성보다 본능이 반 박자 빨랐다. 파이어 실드. 소리 없는 무영창 주문과 함께 김화종의 머리 위로 불의 방패가 겹겹이 덧씌워졌다.

그리고 찰나라고 부를 만큼 짧은 시간, 이십여 개로 중첩된 불의 방패 위를 엄청난 압력이 짓눌렀다.

콰드드드득!

모든 것이 부서지고, 흩어진다.

압도적인 힘과 무게. 거기에 더하여 도무지 끝을 짐작할 수 없는 강대한 마력(魔力)은 중첩된 불의 방패를 깨트리고 시전자의 마나를 뒤흔들었다.

푸우웃!

김화종의 입술 사이로 검붉은 핏물이 뿜어져 나왔다.

마법이 흩어진 여파로 인하여 순간 아득해지는 시야. 하지만 그는 제 자리에서 허물어지는 대신, 이를 악문 채 넘어지듯 신형을 날렸다.

콰직! 푸푹!

방어 마법이 벌어 준 찰나의 시간.

아슬아슬한 차이로 스쳐 지나간 베히모스의 코가 지면을 부수었다. 동시에 사방으로 튄 수백 개의 파편이 김화종의 종아리를 할퀴고 지나갔다.

불에 덴 듯한 고통. 그러나 노집사는 고통에 찬 신음 대신, 피에 젖은 이빨을 드러내며 웃었다.

“말하지 않았느냐. 어디에도 가지 못한다고.”

순간, 그의 손에 쥔 스태프가 초고온의 열기를 내뿜었다. 허공으로부터 생성된 화염의 구(球)가 크기를 부풀렸다.

김화종이 울컥, 핏물을 토해 내며 뇌까렸다.

“터트려라. 불의 포화여.”

플레임 캐논(Flame Cannon).

완성된 주문과 함께 눈부신 광염(光焰)이 터져 나왔다.

그 어떤 대포보다 빠르고 강대한 힘이 실린 최상위의 화염 마법이 향하는 곳에는, 앞서 최민우에 의해 반쯤 잘려 나갔던 마수의 두 앞발이 있었다.

- 놈……!

화악, 퍼어어어엉!

다음 순간. 사방을 떨어 울리는 굉음에 베히모스의 외침이 파묻혔다.

공간을 지우며 날아간 화염은 미처 아물지 않은 상흔(傷痕)을 터트리고 내부를 휩쓸었다.

치지직. 숯처럼 검게 타들어 간 앞발로부터 전해지는 끔찍한 통증에, 베히모스가 고통에 찬 포효를 내질렀다.

- 그아아아아아아!

쿠우우웅!

마침내 굽혀졌다. 두 개의 앞발이.

심연을 거슬러 현세에 강림한 신화 속 마수는 신전이 무너지는 것처럼 두 앞발을 꿇었다.

엄청난 무게가 땅을 뒤흔들고 거대한 먼지구름이 피어올랐다.

그리고 베히모스를 무릎 꿇린 한 인간은 피를 토해 내며 웃고 있었다.

“으하! 으하하하!”

그것은 한때 최고의 화염 마법사라 불렸던 헌터의 웃음이었고, 자신의 책무를 다한 집사의 후련함이었다.

‘이것으로 됐다. 이것으로.’

네 개의 다리 중 절반을 불능으로 만들었다.

이제 날개를 만들어 달지 않는 이상, 베히모스는 최민우를 쫓아가지 못할 것이다.

그로 인해 살아남을 생명도 적지 않을 터였다.

김화종은 미소 지은 채 자신을 향해 날아드는 짙은 그림자를 보며 생각했다.

‘그래도 아주 조금은. 아쉽…….’

뻐억! 쐐애애액!

눈앞이 하얗게 물들었다. 김화종은 전신을 덮치는 엄청난 충격과 통증을 느끼며 포탄처럼 쏘아졌다.

꽈앙!

굉음과 함께 단단한 암석에 틀어박힌 등이 부서지고, 막을 수 없는 무언가가 내부 깊숙한 곳에서부터 솟구쳐 올랐다.

“쿠에에에엑!”

노집사는 꺼질 듯한 눈빛으로 자신이 토해 낸 핏물을 내려다보았다. 검붉은 피 웅덩이에 작은 내장 조각이 섞여 있었다.

고막이 터져 나갔는지 귀가 먹먹했고, 흐릿한 시야 속에서는 오래전. 어느 날의 기억이 아지랑이처럼 피어올랐다.



‘화염 마법의 위력이 대단하던데. 혹시 전직이 방화범이었나?’

‘……이건 또 뭔 미친 소리야. 도와줄 거 아니면 꺼지쇼.’

‘다행히 안 꺼져도 되겠군. 자네와 여기 있는 사람들을 도와줄 거거든.’

‘흠. 그렇다면 약간 얘기가 달라지지. 이름이?’

‘천태민.’



처음 만났을 때는 알지 못했다. 나이에 비해 터무니없이 젊어 보이는 그가, 평생토록 충성을 바칠 우상이 될 것이라고는.

하지만 그것은 얼마 지나지 않아 현실이 되었다.

일 년, 이 년, 오 년……. 길고도 끔찍했던 대전쟁이 끝났을 때. 김화종은 천태민의 그림자가 되어 있었다.



‘전 이제 뭘 해야 합니까?’



다른 이들에게도 그랬지만, 대격변은 김화종의 인생을 송두리째 바꿔 놓은 사건이었다.

그 시절, 그토록 기다렸음에도 마침내 찾아온 평화에 혼란스러워하는 그에게 우상은 담담하게 되물었다.



‘뭘 하고 싶은데?’

‘모르겠습니다. 하지만 시키시는 것이라면 뭐든 하겠습니다.’

‘그럼 길드에 들어와라. 네가 필요해. 정룡이와 천우도 받아들였다.’

‘그, 평화 길드인가 하는 그거요?’

‘그래.’

‘이름이 너무 구린 것 같은데요. 차라리 아레스 어떠세요? 그리스 로마 신화에 등장하는 전쟁의 신. 아레스.’

‘아레스라, 나쁘지 않네. 그럼 네 말대로 할 테니까 길드에 들어와. 노후 걱정은 안 하게 해 주마.’

‘……제가 사무직은 영 적성에 안 맞는데. 알겠습니다, 길드장님.’

‘지난 오 년 동안 형님으로 부르라고 오천 번쯤은 말한 것 같은데. 넌 도무지 변하지 않는구나.’



그때 했던 말처럼, 김화종은 변하지 않았다.

신뢰하는 전우이자 절친했던 두 의형(義兄)과의 관계가 희미해지고, 천태민의 얼굴을 보기 힘들어진 후에도 마찬가지였다.

평화가 찾아와도 불같은 성격은 여전했고 입에는 늘 욕을 달고 살았다.

그가 변하기로 결심한 것은, 모두의 축복 속에 탄생한 한 아이가 불의의 사고로 부모를 잃은 직후였다.



‘안녕.’

‘……안녕하세요.’



몇 사람만 모인 장례식장에서, 이제 고작 네다섯 살밖에 되지 않은 사내아이는 외로워 보였다.

이제 유일한 가족이 된 외할아버지의 다리를 붙잡고 어두운 얼굴로 인사를 건네던 그 모습이, 조금씩 늙어 가던 김화종의 마음을 아프게 했다.

어쩌면 그 때문이었을지도 몰랐다. 며칠 뒤 찾아온 천태민의 제안을 선뜻 수락한 것은.



‘민우를. 그 아이를 맡아 줄 수 있겠나?’



인류의 상징이 되어 버린 불멸의 영웅은 늘 바빴다.

김화종은 대격변이 끝난 직후에도 마치 뭔가에 쫓기는 듯 살아가는 그를 대신하여, 홀로 남겨진 한 아이의 가족이 되었다.



‘안녕하십니까, 도련님.’



머리와 복장은 단정하게. 목소리는 부드럽게. 입가에는 미소를.

대격변의 한 페이지를 불태웠던 겁화(劫火)의 마법사는 그렇게 김 집사가 되었다.



‘도련님. 뛰시면 안 됩니다! 그러다 다치시면, 어이쿠.’

‘도련님. 편식은 몸에 안 좋습니다. 어서 드세요.’

‘도련님. 울지 마십시오.’



도련님. 도련님. 도련님…….

시간은 강물처럼 흘렀다.

아이는 자라 청년이 되었고, 김화종의 머리에는 새하얀 서리가 내려앉았다.

천태민이 종적을 감춘 이후에도 김화종은 변함없이 자리를 지켰다.

그의 도련님은 더이상 성급하게 뛰지도 않았고, 모든 음식을 골고루 먹었으며, 일찍 떠난 부모를 생각하며 울지도 않았다.

그리고 장성한 청년의 얼굴에서 오랫동안 만나지 못했던 누군가의 흔적을 발견한 어느 날이었다.



‘길드를 만드신다고 하셨습니까.’

‘예. 죄송하지만 김 집사님께서 길드장을 맡아 주셔야겠습니다.’

‘도련님께서 원하신다면, 무엇이든 하겠습니다. 그런데 길드 이름은 무엇으로 하실 생각이십니까?’

‘평화 길드. 평화 길드로 하겠습니다.’

‘……!’

‘김 집사님 표정이 왜…… 그렇게 별로인가요?’



무슨 말을 해야 할까. 순간 떠오르는 많은 생각에 망설이던 노집사는, 이내 크게 소리 내어 웃었더랬다.



‘아닙니다. 평화 길드. 참 멋있는 이름이군요.’



그렇게 과거와 현재가 만났다.

김화종은 평화 길드가 설립된 이후 하루하루를 기쁨과 추억에 젖은 채 마주했다.

차갑고 딱딱한 가면을 쓰고 있던 도련님은 난생처음으로 ‘동료’를 만나 부드러워졌고, 평화 길드는 나날이 성장을 거듭했다.

좋은 일만 가득할 것이라고 생각했다. 앞으로도 쭉. 영원히.

성장해 가는 도련님을 옆에서 지켜볼 수 있을 것이라고. 그렇게 생각했었다.

‘분명 오늘은…… 내 인생 최고의 날이었는데.’

쿨럭. 김화종은 내장 조각이 섞인 핏물을 토해 내며 웃었다.

죽어 가면서도 웃을 수 있는 유일한 이유는, 그가 오늘 들었던 한 마디 때문이다.



‘감사합니다. 제 유일한 가족이 되어 주셔서.’



그리고 또, 도련님께서 뭐라고 말씀하셨더라.



‘항상 이 말씀을 드리고 싶었습니다.’



그래. 그러셨었지.

김화종은 기침을 토해 내며 고개를 들었다. 꺼질 듯한 시선이 향한 곳에는 검은 안개가 자욱했다.

아마도 보이지 않는 안개 너머 어딘가에, 그의 유일한 희망이자 두려움이 살아남아 이곳을 떠나고 있을 것이다.

“뵙고…… 싶은데.”

피에 젖은 입술 사이로 떨리는 음성이 흘러나왔다.

죽음을 앞둔 노집사의 모습에 신화 속 마수가 만족스럽게 웃으며 아가리를 벌린다.

화아아아악.

거대한 돌풍이 사방을 휩쓸었다.

미처 꺼지지 않은 불길도, 땅에 널브러진 누군가의 사지와 핏물. 암석도 함께.

토네이도처럼 빨려 들어간 모든 것들이 베히모스의 입 안에서 회오리쳤다.

“도련……님.”

아니. 아니다. 비록 닿지는 않겠지만, 이건 그에게 건네는 마지막 인사였다.

주름진 입가에 희미한 웃음이 번졌다.

“민우야.”

꺼질 듯한 목소리가 흘러나온 바로 그 순간.

쐐애애애액, 번쩍!

허공으로부터 터져 나온 섬광이, 온 세상을 하얗게 물들였다.
```

## Final English reading copy

```markdown
# Chapter 584

Kwooooom!

A pillar of fire shot into the sky. The mountain shook. An area spanning hundreds of meters boiled with ultrahigh heat as snow, dirt, and rock melted away.

A land of death, overflowing with lava. Standing like towers above the ground where everything had evaporated were two beings.

—Hu. Man. How. Dare. You!

The mythical monster raged, its body charred black, while the gray-haired old butler calmly gazed at it.

**Hell Fire.**

Even the hellfire summoned from the depths of hell had failed to bring Behemoth down. One of its enormous tusks had melted away without a trace, and its entire body was charred black, but the monster remained standing.

And yet…

“What a bastardly tough one you are.”

Kim Hwajong did not retreat. He could not retreat.

With his only remaining hand, he gripped his Magic Staff tightly.

Fwoosh.

The short, slender staff was engulfed in flames. Once the fire passed over it, a new staff emerged—thicker and longer than before.

It was the cherished weapon that had turned countless monsters into ash during the chaotic era of the Great Cataclysm and earned its master the title of Hellfire Mage.

Kim Hwajong pointed the reddish staff at Behemoth and muttered,

“Stop. You’re not going anywhere.”

—You. Wretch!

Behemoth roared. At the same time, the thick black mist that had settled over the area moved like a living creature and shot toward Kim Hwajong.

Sssshhhh!

It was both a rope meant to bind his entire body and a blade meant to tear through flesh and bone.

But Kim Hwajong calmly watched the mist closing in from every direction.

In that instant, the staff in his blood-covered hand struck the ground.

BOOM!

A wave spread outward with a deep rumble. The flames rising around Kim Hwajong formed a single ring that enclosed him.

Fwoosh—FWOOSH!

Before fire was a symbol of destruction, it was a force of purification.

The moment the black mist shooting toward him touched the flames, it withered away like ash.

The enormous eyes of the monster looking down upon the earth reflected the figure of a lone human standing tall.

—What. Is. This?

Even Behemoth had not expected this.

Its opponent was nothing more than a human. And yet this small, insignificant creature had not only wounded it, but nullified its attack.

—You. Hu. Man!

A roar filled with powerful Fear shook the entire area. But unlike the flames flickering in his eyes, Kim Hwajong’s heart was utterly calm.

The monster before him had made one mistake.

It did not realize that the old human standing before it possessed none of the fear that everyone carried deep in their hearts.

*I’m glad, Young Master.*

Along with a murmur that would never reach him, Kim Hwajong smiled faintly. His one and only fear was moving farther away from the disaster even now.

As long as that child, Choi Minwoo, could survive… it did not matter what happened to him.

*Even if I die here.*

It would be fine if he were crushed beneath the monster’s feet, pierced by its tusks and killed without being able to leave even a final word, or reduced to ash after squeezing his mana and body past their limits.

*If the Young Master is safe, that is enough for me.*

And so Kim Hwajong gripped the staff with joy in his heart.

An immense amount of mana, already beyond its limits, surged into the tip of his cherished weapon, which glowed with a reddish light. The heated mana erupted as flame.

“Be swept away.”

**Fire Wave.**

With the short incantation, a wave of fire rolled forward.

At its end, Behemoth swung the trunk it had raised with an enraged cry. It was long like an elephant’s trunk—and dozens of times larger.

FWOOSH!

The wind that arose with a mighty crack of splitting air slammed into the wave of fire. The ultrahigh heat died away in an instant, and invisible blades of wind flew in and raked the area from every direction.

Ssshhh-shhk! Slash!

The ground split and tore apart like sheets of paper. But Kim Hwajong had already slipped out of the area by the narrowest margin.

A low voice escaped between the old butler’s lips as he charged toward Behemoth’s flank.

“Shoot forth.”

**Blaze.**

BOOM!

Flames burst from the tip of the foot he planted.

With the instantaneous explosion, Kim Hwajong shot forward as a streak of flame. Then a dense shadow fell over his head.

Whoooosh!

“……!”

His instincts moved half a beat faster than his reason. **Fire Shield.** Alongside a silent, wordless spell, layers of fiery shields formed above Kim Hwajong’s head.

And in an instant so brief it could barely be called a moment, tremendous pressure crushed down upon the more than twenty overlapping shields.

CRRRRUNCH!

Everything shattered and scattered.

Overwhelming force and weight. On top of that, the immense magic power whose end could not be fathomed shattered the layered fiery shields and shook the caster’s mana.

Ptooey!

Dark red blood sprayed from between Kim Hwajong’s lips.

His vision went hazy for a moment in the aftermath of the dispersing magic. But instead of collapsing where he stood, he clenched his teeth and threw himself aside as though falling.

CRACK! THUD!

The defensive magic had bought him a brief moment.

Behemoth’s trunk swept past him by the narrowest margin and smashed into the ground. At the same time, hundreds of fragments flew in every direction, scraping across Kim Hwajong’s calf.

The pain felt like a burn. But instead of groaning, the old butler exposed his bloodstained teeth and smiled.

“Didn’t I tell you? You’re not going anywhere.”

In that instant, the staff in his hand emitted ultrahigh heat. A sphere of flame formed in midair and swelled in size.

Kim Hwajong coughed up a mouthful of blood and muttered,

“Explode. Artillery of flame.”

**Flame Cannon.**

With the completed spell, dazzling light-flames burst forth.

The ultimate fire spell, carrying power faster and more formidable than any cannon, shot toward the monster’s two forelegs—the same forelegs that Choi Minwoo had already cut halfway through.

—You…!

FWOOSH—BOOOOOOM!

The next moment, Behemoth’s cry was swallowed by a thunderous boom that shook the entire area.

The fire that tore through space burst open the wounds that had not yet healed and swept through the inside of the legs.

Sizzle.

Terrible pain spread from the forelegs, blackened like charcoal. Behemoth let out a roar filled with agony.

—GRAAAAAAAAAAH!

Ruuuuumble!

At last, the two forelegs bent.

The mythical monster that had risen into the mortal world from the depths of the abyss dropped both forelegs to its knees as if a temple were collapsing.

Its tremendous weight shook the earth, and an enormous cloud of dust rose into the air.

And the human who had forced Behemoth to its knees was laughing as he spat blood.

“Ha! Hahahaha!”

It was the laughter of the Hunter once called the greatest fire mage—and the relief of a butler who had fulfilled his duty.

*This is enough. This is enough.*

Half of Behemoth’s four legs had been rendered useless.

Unless someone gave it wings, Behemoth would not be able to chase Choi Minwoo now.

And because of that, no small number of lives would survive.

Kim Hwajong smiled as he watched the dense shadow flying toward him.

*Still, just a little… I wish…*

CRACK! Sssshhhh!

His vision turned white. Kim Hwajong felt tremendous impact and pain engulf his body as he shot through the air like a cannonball.

BOOM!

With a thunderous crash, his back smashed into solid rock and broke. Something unstoppable surged up from deep inside him.

“Gueeeeeegh!”

The old butler looked down at the blood he had vomited, his eyes dimming. Small pieces of his organs floated in the pool of dark red blood.

His ears felt blocked, as though his eardrums had burst. Through his blurred vision, a memory from long ago rose like a haze.

*“Your fire magic is incredible. Were you a former arsonist?”*

*“……What kind of crazy shit are you talking about? If you’re not going to help, then get lost.”*

*“Fortunately, I won’t have to ‘go out,’ then. I’m going to help you and everyone here.”*[^1]

[^1]: The same verb means both “get lost” and for a flame to “go out.”

*“Hmm. In that case, the story changes a little. What’s your name?”*

*“Cheon Taemin.”*

When they first met, Kim Hwajong had not known.

He had not known that this man, who looked absurdly young for his age, would become the idol to whom Kim Hwajong would devote his entire life.

But that became reality soon enough.

One year, two years, five years… When the long and terrible Great War finally ended, Kim Hwajong had become Cheon Taemin’s shadow.

*“What am I supposed to do now?”*

Like it had for everyone else, the Great Cataclysm had completely changed Kim Hwajong’s life.

In those days, despite having waited so long, he was confused by the peace that had finally arrived. His idol calmly asked him in return,

*“What do you want to do?”*

*“I don’t know. But I’ll do anything you tell me to do.”*

*“Then join the Guild. I need you. I’ve brought Jungryong and Cheonwoo in too.”*

*“The Peace Guild, or whatever it’s called?”*

*“Yes.”*

*“The name sounds pretty damn lame. How about Ares instead? The god of war from Greek mythology. Ares.”*

*“Ares, huh? Not bad. Then I’ll go with your suggestion. Join the Guild. I’ll make sure you don’t have to worry about your old age.”*

*“……I’m not really suited for office work. All right, Guild Master.”*

*“I think I’ve told you about five thousand times over the past five years to call me hyung. You really never change.”*

Just as he had said then, Kim Hwajong did not change.

Not even after his relationship with his two trusted comrades and closest sworn brothers grew distant, and after it became difficult to see Cheon Taemin’s face.

Even after peace arrived, his fiery temperament remained, and he continued to swear constantly.

The moment he decided to change came just after a child born amid everyone’s blessings lost his parents in an unfortunate accident.

*“Hello.”*

*“……Hello.”*

At the funeral, attended by only a few people, the little boy—no more than four or five years old—looked lonely.

The sight of him clinging to the leg of his maternal grandfather, now his only family, and offering a greeting with a dark expression pained Kim Hwajong’s aging heart.

Perhaps that was why he readily accepted Cheon Taemin’s proposal when he came to visit a few days later.

*“Can you take care of Minwoo? That child?”*

The immortal hero who had become a symbol of humanity was always busy.

Instead of Cheon Taemin, who continued living as though he were being chased by something even after the Great Cataclysm ended, Kim Hwajong became the family of a child who had been left alone.

*“Good day, Young Master.”*

His hair and clothes had to be neat. His voice had to be gentle. A smile had to rest at the corners of his mouth.

And so the Hellfire Mage who had burned through a page of the Great Cataclysm became Butler Kim.

*“Young Master. You mustn’t run! You might get hurt. Oh, dear.”*

*“Young Master. Being a picky eater is bad for your health. Please eat.”*

*“Young Master. Please don’t cry.”*

Young Master. Young Master. Young Master…

Time flowed like a river.

The child grew into a young man, and white frost settled over Kim Hwajong’s hair.

Even after Cheon Taemin vanished without a trace, Kim Hwajong remained steadfast in his place.

His Young Master no longer ran about recklessly, ate every kind of food without complaint, or cried while thinking of the parents who had left him too soon.

And then came the day when Kim Hwajong discovered traces of someone he had not seen in a long time on the face of the grown young man.

*“You said you were going to create a Guild.”*

*“Yes. I’m sorry, but I’ll need you to serve as the Guild Master, Butler Kim.”*

*“If that is what you wish, Young Master, I will do anything. But what do you intend to name the Guild?”*

*“The Peace Guild. I’ll call it the Peace Guild.”*

*“……!”*

*“Why does your expression look so… unhappy, Butler Kim?”*

What should he say? Hesitating over the many thoughts that flashed through his mind, the old butler soon burst into loud laughter.

*“Not at all. The Peace Guild. That’s a wonderful name.”*

And so the past met the present.

After the Peace Guild was founded, Kim Hwajong faced each day immersed in joy and memories.

The Young Master, who had worn a cold, rigid mask, softened after meeting “comrades” for the first time in his life, and the Peace Guild continued to grow with every passing day.

Kim Hwajong thought that nothing but good things lay ahead. From then on. Forever.

He thought he would be able to watch his Young Master grow from his side.

*Today really was… the best day of my life.*

Cough.

Kim Hwajong laughed as he vomited blood mixed with pieces of his organs.

The only reason he could still laugh while dying was because of one thing his Young Master had said today.

*“Thank you. For becoming my only family.”*

And then… what else had his Young Master said?

*“I’ve always wanted to say this to you.”*

Yes. That was what he had said.

Kim Hwajong raised his head through a fit of coughing. Dense black mist filled the direction of his fading gaze.

Somewhere beyond that invisible mist, his only hope—and his only fear—was probably still alive and leaving this place.

“I want to… see you.”

A trembling voice slipped between his bloodstained lips.

Pleased by the sight of the old butler facing death, the mythical monster opened its jaws with a satisfied smile.

FWOOSH.

A tremendous gust swept through the entire area.

The flames that had not yet gone out, someone’s limbs and blood scattered across the ground, and even the rocks were sucked in together.

Everything drawn in like a tornado spun inside Behemoth’s mouth.

“Young… Master.”

No. That was not it. Though his words would never reach him, this was his final greeting.

A faint smile spread across his wrinkled lips.

“Minwoo.”

At the very moment his fading voice escaped—

Sssshhhh—FLASH!

A burst of radiance erupted from midair and bathed the entire world in white.
```
