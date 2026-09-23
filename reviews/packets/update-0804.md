<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0804.txt",
      "sha256": "f64e1a5a40fec265dea3def3400e760c4b4bad8846fa95342731ba0a4c9b8e80",
      "bytes": 12990
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2e1c982bc1ac5e620261e0188c73f7654dd03e18cebee0a8f2936e350857ad54",
      "bytes": 1310
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "df9f16b523aad142a46fe7e62a8e000c176547aa66fbca278960ebb7783a7de7",
      "bytes": 224738
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "296bdaf78167c3db7bb61ff250aeffb2ae385ca0157989ac32873076ddabaa7b",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cff1e04b71a3146d0e37fb1cfc0c72c77b1e3db1483030af3e73978c9df4fb3f",
      "bytes": 553
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "d7318962a5a626a8aad1cc1c038513340e22eaffc767ee5e3336ed2d1c314d38",
      "bytes": 645
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "81871f049a3bcfcbf96065a9b2261893558a8eb055e7392f388749b8e211111b",
      "bytes": 707
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "11e25eb6953312f72ea652c435a32e565bd345d502faae78d12f8aeabf29a2f7",
      "bytes": 574
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8bd8b3dadce9eb815c5d9dd06390882ed0e507ef0582faa521024fa16dde0508",
      "bytes": 247238
    }
  ],
  "estimated_tokens": 9179
}
-->

# Durable State Update — Chapter 804

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 804. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 804. Profile updates may replace only one
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
  "chapter": 804,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 804,
    "continuity_sources": [804],
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
    "Jin’s force is fighting a monster army of more than ten thousand in the Rub’ al Khali; he orders the Hunters to hold formation and minimize losses.",
    "The Prophet and the S-rank monsters remain unseen as the battle unfolds.",
    "The Skeleton King’s undead fight the monsters and can raise fallen monsters as soldiers, but their existence is limited by the magical power he bestowed.",
    "Amir and Hamid lead desert fanatics who have begun advancing toward their promised land, believing the time foretold by the Prophet has arrived.",
    "A distant, immense surge of magical power is shaking the desert."
  ],
  "continuity_sources": [
    802,
    803
  ],
  "open_questions": [
    "Where are The Prophet and the S-rank monsters, and when will they enter the battle?",
    "What is causing the immense magical-power surge?",
    "Are Amir’s fanatics the non-monster enemy that attacked Chuck Hagel’s search party, and what is their intended target?"
  ],
  "safe_through": 803,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 최민우    | **Choi Minwoo**   |
| 천태민    | **Cheon Taemin**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 경험치              | **EXP**                        |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 그리폰 | **Griffon** | Flying monster species attacking the airport. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 일기당천 | **One Against a Thousand** | Title that temporarily increases Taekyung’s attributes and Intimidation when facing many enemies. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 802
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 803
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 790
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 803
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 801
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and J1’s sole survivor.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃804화



자욱한 안개가 바다를 가리고 있어도, 누구나 저 안개 너머에 바다가 있다는 사실을 알 수 있다. 희미하게 들려오는 갈매기의 울음소리와 소금기를 머금은 바람을 느낄 수 있기 때문이다.

전장(戰場)도 그와 같다.

사방에서 비명과 핏물이 난무하고 무수한 날붙이가 서로를 향해 부딪치며 불꽃을 튀기는 와중에도, 특별한 힘을 지닌 무언가는 존재 자체만으로도 전장의 공기를 바꾼다.

바로 지금처럼.

고오옹.

파르르 떨리는 공기.

저 멀리서부터 뻗어 나온 깊은 울림이 사막을 뒤흔든다.

동족의 시체를 넘어 돌격하려던 몬스터들이 약속이라도 한 것처럼 제자리에 멈춰 서고, 사람들의 몸이 흠칫 굳었다.

지금 이 순간 저들은 무엇을 느끼고 있을까.

등골을 타고 흐르는 오한? 아니면 잠시 잊고 있던 두려움?

그것이 정확히 무엇인지는 모르겠지만, 적어도 나는 둘 중 어느 것에도 해당하지 않았다.

서 있는 위치에 따라 보이는 풍경도 다르다.

그런 의미에서 나는 저들과 달리 봉우리에 선 존재다. 더 멀리, 많은 것을 보고 느낄 수 있는.

그리고 그것은 나 혼자만이 누릴 수 있는 특권이 아니었다.

“이건…….”

어느덧 옆으로 다가온 스켈레톤 킹이 신음처럼 중얼거렸다.

후방에서 방어에만 주력하며 힘을 아끼던 매직 존슨도, 명색이 S급 헌터라 할 수 있는 야마모토 겐지와 그에 버금갈 만큼 예리한 기감을 지닌 최 팀장도 얼굴을 굳혔다.

“Fuck.”

“칙쇼. 이건 미친 짓이야. 난 이곳을 빠져나가야겠어.”

“드디어 우두머리들이 나서는군요.”

빡!

“악!”

처맞는 새끼들은 꼭 이유가 있다.

이 와중에도 헛소리를 지껄이는 야마모토 겐지의 정강이를 걷어찬 나는, 돌아섬과 동시에 공력을 일으켜 진각(震脚)을 밟았다.

쿠우웅!

나를 중심으로 지면이 흔들리고 모래의 벽이 솟구친다.

떨어져 내리는 무수한 모래알 사이로 찬물을 뒤집어쓴 듯한 표정을 짓고 있는 헌터들이 보였다.

“뭘 쫄고들 있어. 다들 뒈지고 싶어서 환장했나?”

“하, 하지만 이건…….”

“아무리 등급을 나눠도 결국 상대는 몬스터다. 우리도 마찬가지로 똑같은 헌터고. 그러니까 곧 죽을 놈들처럼 얼어붙어 있지 말고…….”

푹!

질긴 목숨줄을 부여잡고 꿈틀거리던 오우거 한 마리의 머리통에 단검을 박아 넣으며, 나는 힘주어 말을 이었다.

“싸워. 헌터답게.”

띠링.



- [Lv.95 오우거]를 처치했습니다!

- 극소량의 경험치를 획득했습니다!

- 칭호, [일기당천(一騎當千)]의 효과가 발동됩니다!

- [위압]이 크게 상승합니다!

- 당신의 [위압]으로 인해 적들이 급격히 위축됩니다!

- 다수의 아군에게 적용되었던 상태 이상, [피어]가 해제됩니다!

- 아군의 사기가 크게 상승합니다. 당신의 통솔을 따르는 이들은 끈끈한 결속력을 지니며, 더욱 뛰어난 활약을 펼칠 것입니다!

- 다수의 적을 상대할 시 일정 스탯이 상승합니다!



일기당천은 쓰촨성에서 아크 리치의 대군을 상대하며 얻었던 칭호. 희귀한 업적을 달성하고 얻은 보상답게, 그 효과는 확실했다.

“으아아아아!”

지금까지도 마른침을 삼키고 있던 몇몇 헌터들이 충혈된 눈동자로 포효하자, 이내 거대한 함성이 터져 나와 주위의 공기를 뜨겁게 달구었다.

물론, 어디에나 예외는 있는 법이지만.

“아니, 아무리 그래도 저건 좀 심한데…….”

조인트에 까인 정강이를 문지르며 눈치를 살피는 야마모토 겐지의 모습에 작게 혀를 찬 나는, 드넓은 사막에 끝없이 늘어선 몬스터 군단을 향해 시선을 돌렸다.

척, 처척.

조금 전까지와는 다른 질서정연한 움직임.

일만을 훌쩍 뛰어넘는 대병력이 자로 잰 듯한 걸음으로 좌우로 비켜서자, 세 갈래의 길이 생겨남과 동시에 막강한 존재감을 뿜어내는 존재들이 비로소 모습을 드러냈다.

‘S급 몬스터들.’

어떤 것은 거대하면서도 흉측하고, 어떤 것은 주위의 몬스터들에 비하면 눈에 띄지 않을 만큼 작았다.

그러나 놈들이 발산하는 저 강대한 마기와 피어(Fear)는, 이 수많은 괴물을 합친 것만큼이나 엄청난 것이었다.

제아무리 겁쟁이에 실력이 떨어진다고는 하나, 명색이 S급 헌터인 야마모토 겐지마저 두려워할 만큼.

“저놈들이군, 이 몬스터 군단을 이끄는 지휘관들이.”

스켈레톤 킹의 중얼거림에 내가 입을 열었다.

“하지만 가장 중요한 한 놈이 남았지.”

“……선지자.”

“그래, 선지자가 바로 머리야. 저놈들은 손발이고.”

“하지만 놈이 지금 이곳에 있을까? 자존심 상하는 이야기지만…… 이 몸은 선지자로 짐작되는 존재를 보거나 느끼지 못했다.”

솔직히 대답하자면, 그건 나 역시 마찬가지다.

하지만 한 가지만큼은 확신할 수 있었다.

이 전장 어딘가에 선지자가 있다고.

주도면밀하기 짝이 없는 놈의 성격상, 어느 정도 떨어진 거리에서라도 지금의 상황을 모두 지켜보고 있을 거라고.

‘가까이 접근한다면 곧장 알아차릴 수 있을 텐데.’

[기감]으로 파악하기에는 적들의 머릿수도, 전장의 면적도 광활하다.

더군다나 지휘관이라 할 수 있는 S급 몬스터들의 등장과 함께 뒤바뀐 몬스터 군단의 기세 역시 조금 전과는 비교할 수 없었다.

“진.”

매직 존슨의 나직한 목소리가 귓가를 파고든다. 깊숙하게 가라앉은 그의 눈빛은, 곧 다시 시작될 전투에서 치러야 할 희생을 짐작하는 듯했다.

그리고 그 모든 것을 감당해야 할 나를 걱정하는 마음도 함께.

“허락해 준다면, 내가 대신 지휘했으면 해.”

짧은 순간, 매직 존슨을 말없이 응시하던 나는 고개를 저었다.

“아뇨. 제가 지휘합니다.”

물론 매직 존슨은 능력과 자격이 충분하다. 그는 대격변을 겪은 역전의 용사고, 그 속에서 십여 차례의 대규모 전투를 승리로 이끈 훌륭한 지휘관이다.

하지만…….

“감당해야 할 일이 있다면, 다른 누군가에게 떠넘기지 않겠습니다.”

“……!”

“그게 제가 이 자리에 있는 이유 중 하나잖아요. 아닙니까?”

크게 뜨인 눈으로 나를 바라보던 매직 존슨이 이내 작게 고개를 끄덕였다.

뒤이어 들려오는 그의 목소리에는 굳은 신뢰와 희미한 웃음기가 담겨 있었다.

“좋아, 젊은 친구. 이제 우리에게 명령을 내려 줘.”

크게 심호흡한 나는 모두를 바라보았다.

도합 일천에 달하는 헌터들. 나는 저들 모두의 이름도, 얼굴도 모른다.

하지만 누군가 이 자리에서 쓰러져 영영 일어나지 못하게 된다면, 나는 죽을 때까지 그들의 모든 것을 기억할 것이다.

그래, 그거면 충분하다.

내가 죽는다면 그들 역시 그러할 테니.

“지금부터 존칭은 생략합니다, 매직 존슨.”

“Yes. young boss.”

“공중을 견제하고 아군 보호에 주력한다. 예하 헌터들은 내 명령이 떨어지기 전까지 매직 존슨의 지시에 따르도록.”

“Yes, Sir!”

함성처럼 내지른 대답과 함께 매직 존슨이 허공으로 몸을 띄웠다.

날카로운 예기를 뿜어내는 대마도사의 눈은, 구름 한 점 없는 하늘을 천천히 가로지르는 수백 개의 점과 그 선두에서 날갯짓하는 한 마리의 독수리를 바라보고 있었다.

정확히는 수십여 미터에 이르는 거대한 날개와 사자의 하반신을 지닌 괴물, 그리폰(Griffon)을.

“최민우.”

“예.”

“병력 일백과 함께 가장 앞에서 전열을 지킨다. 탱커들 대열 무너지면 검 반납하고 은퇴해.”

최 팀장이 투명하게 빛나는 [영웅의 검]을 들어 올리며 대답했다.

“그럴 일은 없을 겁니다.”

천태민이라는 대영웅의 유일한 핏줄인 동시에 아레스 길드의 주인이면서도, 단 한 번도 노력을 게을리하지 않는 최 팀장이다.

아마도 가까운 시일 내에 새로운 S급 헌터가 탄생한다면, 바로 그가 아닐까 하는 생각이 들 정도로.

그런 최 팀장의 담담하면서도 자신감 넘치는 모습에 실소를 흘린 나는 아직 남은 이들을 향해 고개를 돌렸다.

“스켈레톤 킹. 야마모토 겐지. 너희는…….”

“시간 아깝게 말할 필요 없다. 지상에 남아 있는 S급 몬스터가 셋이니까, 사이좋게 한 놈씩 맡으면 충분하겠군.”

“저, 저도 말입니까?”

지그시 노려봄으로써 야마모토 겐지의 입을 닥치게 만든 나는, 앞서 했던 스켈레톤 킹의 말을 정정해 주었다.

“너랑 저놈이 한 마리씩 맡고, 나는 두 마리.”

“뭐?”

“에?”

두 녀석이 동시에 반문한 그 순간. 나는 돌아섬과 동시에 마음속으로 뇌까렸다.

‘인벤토리 오픈, 소환.’

근접전에서 제 몫을 톡톡히 해낸 두 자루의 단검이 사라지고, 단단하면서도 서늘한 창대의 촉감이 잠시 비었던 손아귀를 가득 채운다.

공간을 일그러트리는 화염과 함께.

화륵.

투명한 창날을 휘감으며 완성된 강기(罡氣).

그리고 찰나를 쪼개고 쪼갠 그 짧은 순간. 나는 역수로 움켜잡은 창을 한 줄기의 섬광처럼 내리꽂았다.

사막 깊숙한 곳에서 아무도 모르게 다가온, 보이지 않는 적을 향하여.

서걱. 콰아아아아아!

뜨거운 열기를 머금은 지면이 두부처럼 갈라진다.

발아래에 깔려 있던 단단한 모래와 흙이 높게 솟구치고, 거대한 크레이터처럼 파인 땅속에서 우글거리는 무수한 생명체들이 시야에 잡혔다.

그중에서도 가장 거대하고, 붉게 번들거리는 괴물도 함께.

‘저건.’

머릿속에 켜진 경고등.

동시에 창날과 함께 뻗어 나간 [기감]의 푸른 원이 놈의 단단한 몸뚱어리에 닿았다.

띠링. 띠링. 띠링.



- 현재 [기감]의 경지는 팔 성입니다.

- [기감]으로 범위 안의 대상을 파악했습니다!

[Lv.87 병졸 스콜피온]

[Lv.76 일꾼 스콜피온]

[Lv.99 정예 스콜피온]



눈과 귀로 전해지는 무수한 정보들.

그러나 내 신경은 오직 한 놈에게 집중되어 있었다.



[Lv.140 스콜피온 킹]



성인 남성만큼이나 커다란 무수한 전갈들과 그 수십 마리를 합한 것보다 거대한 단 한 마리의 전갈.

‘스콜피온 킹.’

저놈이 바로, 내가 가장 먼저 쓰러트려야 할 적이다.

콰아아아, 퍼걱!

초고온의 화염이 지면 깊숙한 곳에 만들어진 괴물들의 서식지를 불살랐다.

단단한 갑각도, 날카로운 집게와 꼬리에 달린 독침도 모조리 녹아내렸다.

- 끼이이이잇!

전갈들이, 아니 괴물들이 내지르는 고통 섞인 단말마가 구덩이를 타고 세상 밖으로 흘러넘친다.

인간과 몬스터.

몬스터와 인간.

모두가 놈들의 비명을 들을 수 있었고, 동시에 반응했다.

- 인. 간. 들. 을. 죽. 여. 라!

S급 몬스터가 내지른 포효와도 같은 마계어(魔界語)가 터져 나오자, 거대한 진동이 사방을 휩쓸었다.

쿠구구구궁!

머릿수가 문제가 아니다.

기세도, 뿜어내는 마기의 양과 질도 전과는 비교할 수 없었다.

S급 몬스터를 선두로 후방에서 대기하고 있던 정예 몬스터들이 자신들의 지휘관을 따라 돌격하고, 일만이 넘는 괴물들이 파도가 되어 그 뒤를 따랐다.

- 크아아아아!

지상에서는 세 마리의 S급 몬스터가 이끄는 대병력이. 그리고 모두의 머리 위에서는 유독 커다란 날개를 펼친 그리폰을 선두로 한 수백 마리의 비행 몬스터가 괴성을 토해 냈다.

- 끼아아악!

하늘과 땅을 아우르며 시작된 공격.

그러나 나는 두려워하지도, 머뭇거리지도 않았다.

- 키아아앗!

비명을 내지르며 솟구치듯 구덩이를 빠져나온 스콜피온 킹을 향해, 단호하고도 확실한 일격을 꽂아 넣을 뿐.

퍼걱! 푸화아아악!

산성(酸性)을 머금은 핏물이 불길에 녹아내린 그 순간.

띠링.

기다렸던 시스템 알림과 함께, 나는 S급 몬스터들을 향해 맹수처럼 달려들었다.

콰아아아!
```

## Final English reading copy

```markdown
# Chapter 804

Even when a thick fog hides the sea, anyone can tell there’s an ocean beyond it. They can hear the faint cries of gulls and feel the salt in the wind.

A battlefield is the same.

Screams and blood fly in every direction. Countless blades clash, throwing off sparks. And yet, something with a special power can change the air of a battlefield simply by existing.

Just like now.

*Rrrrmmm.*

The air trembled.

A deep rumble rolling in from far away shook the desert.

The monsters that had been charging over the bodies of their own kind came to a halt as if on cue. People stiffened with a start.

What were they feeling at that moment?

A chill creeping down their spines? Or fear they’d briefly forgotten?

I didn’t know exactly what it was, but at least I wasn’t feeling either one.

What you saw depended on where you stood.

In that sense, unlike them, I was standing on the peak. I could see and feel more, and from farther away.

And that wasn’t a privilege I enjoyed alone.

“This is…”

The Skeleton King, who’d come up beside me at some point, murmured as if groaning.

Magic Johnson, who’d been saving his strength by focusing on defense in the rear, had a grim look on his face. So did Yamamoto Genji, an S-rank Hunter at least in name, and Team Leader Choi, whose Qi Sense was nearly as sharp.

“Fuck.”

“Chikushō. This is insane. I have to get out of here.”

“So the leaders are finally making their move.”

*Whack!*

There’s always a reason when some bastard gets hit.

I kicked Yamamoto Genji in the shin for spouting nonsense at a time like this. As I turned away, I stirred my internal energy and stamped down with a quake step.

*Boom!*

The ground shuddered around me, and a wall of sand surged upward.

Through the countless grains falling back down, I saw the Hunters’ faces. They looked as if they’d just been doused in cold water.

“What are you all scared of? You all that eager to die?”

“B-but this is…”

“Call them whatever rank you like—they’re still monsters. And we’re all still Hunters. So quit freezing up like you’re about to die and…”

*Thud!*

I drove a dagger into the head of an ogre that was still writhing, stubbornly clinging to its life, then continued with emphasis.

“Fight. Like Hunters.”

*Ding.*

> **System**
>
> Defeated Lv. 95 Ogre!
>
> Gained a tiny amount of EXP!
>
> The effect of the Title **One Against a Thousand** activates!
>
> **Intimidation** has greatly increased!
>
> Enemies are rapidly losing confidence due to your **Intimidation**!
>
> The status effect **Fear**, which had been applied to numerous allies, has been removed!
>
> Ally morale has greatly increased. Those who follow your leadership will have a strong bond and perform even better!
>
> Certain stats increase when facing numerous enemies!

One Against a Thousand was the Title I’d earned while fighting the Arch Lich’s army in Sichuan Province. As a reward for accomplishing such a rare feat, it was definitely effective.

“GRAAAAAH!”

A few Hunters who’d been swallowing nervously until now roared, their eyes bloodshot. A tremendous cheer soon erupted, heating the air around us.

Of course, there were always exceptions.

“No, even so, that was a bit much…”

I clicked my tongue softly at the sight of Yamamoto Genji rubbing his shin where I’d kicked it, watching me warily. Then I turned my eyes toward the monster army stretching endlessly across the vast desert.

*Clack. Clack-clack.*

Their movements were orderly now, unlike before.

A force of well over ten thousand marched with measured precision, splitting to the left and right. Three paths opened, and at last, the beings radiating an overwhelming presence appeared.

*The S-rank monsters.*

Some were huge and grotesque. Others were so small compared to the monsters around them that they barely stood out.

But the powerful demonic qi and Fear pouring from them were as immense as that of all these countless monsters combined.

Enough to make even Yamamoto Genji afraid, despite his cowardice and lack of skill—or, at least, despite his being an S-rank Hunter in name.

“So those are the commanders leading this monster army.”

At the Skeleton King’s murmur, I spoke up.

“But the most important one is still missing.”

“…The Prophet.”

“Right. The Prophet’s the head. Those guys are the hands and feet.”

“But is he here now? It pains me to admit it, but… I haven’t seen or sensed anyone I’d take to be The Prophet.”

To be honest, the same was true for me.

But there was one thing I was sure of.

The Prophet was somewhere on this battlefield.

Given how meticulous the bastard was, he was probably watching everything unfold from some distance away.

*If he came close, I’d sense him right away.*

The enemies were too numerous, and the battlefield too vast, for me to get a clear read with Qi Sense.

On top of that, the monster army’s momentum had changed with the arrival of the S-rank monsters who could only be called its commanders. It was nothing like before.

“Jin.”

Magic Johnson’s low voice reached my ears. His eyes had sunk deep, as if he could already guess what the battle about to begin again would cost us.

And he was worried about me, the one who would have to bear the weight of it all.

“If you’ll let me, I’d like to take command instead.”

I stared silently at Magic Johnson for a brief moment, then shook my head.

“No. I’m in command.”

Of course, Magic Johnson had all the skill and qualifications for it. He was a veteran who’d lived through the Great Cataclysm and a fine commander who’d led his forces to victory in around a dozen major battles.

But…

“If there’s something I have to bear, I won’t push it onto someone else.”

“…!”

“That’s one of the reasons I’m here, isn’t it?”

Magic Johnson looked at me with wide eyes, then gave a small nod.

The voice that followed held firm trust and the faintest trace of a smile.

“All right, young friend. Give us our orders.”

I took a deep breath and looked around at everyone.

A thousand Hunters in all. I didn’t know all their names or faces.

But if someone fell here and never got back up, I’d remember everything about them for the rest of my life.

Yeah. That was enough.

If I died, they would, too.

“From now on, I’ll dispense with the formalities, Magic Johnson.”

“Yes, young boss.”

“Keep the enemies in the air in check and focus on protecting our allies. All subordinate Hunters are to follow Magic Johnson’s orders until I give them another command.”

“Yes, sir!”

With that answer, shouted like a cheer, Magic Johnson rose into the air.

The Grand Mage’s eyes, sharp as blades, watched hundreds of specks slowly crossing the cloudless sky—and the eagle beating its wings at their head.

More precisely, he was watching a monster with enormous wings tens of meters across and a lion’s lower body: a Griffon.

“Choi Minwoo.”

“Yes.”

“Take a hundred troops and hold the front line. If the tanks break formation, hand in your sword and retire.”

Team Leader Choi raised the **[Hero’s Sword]**, its blade shining with transparent light, and answered.

“That won’t happen.”

Team Leader Choi was the sole blood descendant of the great hero Cheon Taemin and the master of the Ares Guild, yet he’d never once slacked off in his efforts.

Sometimes I thought that if a new S-rank Hunter emerged anytime soon, it would be him.

I let out a quiet laugh at Team Leader Choi’s calm confidence, then turned to the others still waiting.

“Skeleton King. Yamamoto Genji. You two…”

“No need to waste time saying it. There are three S-rank monsters on the ground, so we can each take one.”

“M-me too?”

I silenced Yamamoto Genji with a hard stare, then corrected what the Skeleton King had just said.

“You and him take one each. I’ll take two.”

“What?”

“Huh?”

The two of them questioned me at the same time. At that very moment, I turned away and muttered inwardly.

*Open Inventory. Summon.*

The two daggers that had served me so well in close combat disappeared. The cool, solid feel of a spear shaft filled my hand, which had been empty for an instant.

A flame warped the space around it.

*Fwoosh.*

Force formed around the transparent spearhead, wrapping it in a clear sheen.

And in that brief instant, split into ever-smaller fragments, I drove the spear down like a streak of light, gripping it in reverse.

At the unseen enemy who’d crept up from deep in the desert without anyone noticing.

*Shhk. KRAAAAAASH!*

The ground, filled with searing heat, split like tofu.

Hard sand and earth beneath my feet shot high into the air. In the ground, gouged out like a vast crater, countless writhing life-forms came into view.

Among them was a monster larger than all the rest, gleaming red.

*That’s…*

A warning light flashed in my mind.

At the same time, the blue circle of **[Qi Sense]** that extended with my spearhead reached the monster’s hard body.

*Ding. Ding. Ding.*

> **System**
>
> Your **Qi Sense** is currently at eight stars.
>
> You have detected targets within range using **Qi Sense**!
>
> Lv. 87 Soldier Scorpion
>
> Lv. 76 Worker Scorpion
>
> Lv. 99 Elite Scorpion

Countless details came to me through my eyes and ears.

But my attention was fixed on only one of them.

> **System**
>
> Lv. 140 Scorpion King

Countless scorpions as large as adult men—and one scorpion larger than dozens of them put together.

*The Scorpion King.*

That was the enemy I had to take down first.

*KRAAAAAASH! Crunch!*

Superheated flames scorched the monsters’ lair, deep beneath the ground.

Their hard carapaces, sharp pincers, even the stingers on their tails—all of it melted away.

*Kiiiiieeet!*

The scorpions—or rather, the monsters—screamed in agony, their dying cries spilling out of the pit and into the world.

Humans and monsters.

Monsters and humans.

Everyone could hear their screams, and everyone reacted.

“Kill. The. Humans!”

The Demon Realm language erupted like a roar from an S-rank monster, and a massive tremor swept in every direction.

*Rumble, rumble, rumble!*

Their numbers weren’t the problem.

Their momentum, and the quantity and quality of the demonic qi they emitted, were beyond comparison with what we’d faced before.

The elite monsters waiting in the rear charged after their commanders, the S-rank monsters at their head. More than ten thousand monsters surged behind them like a wave.

*KRAAAAAH!*

On the ground, an enormous force led by three S-rank monsters. Over everyone’s heads, hundreds of flying monsters shrieked, led by the Griffon spreading its unusually large wings.

*Kiaaaak!*

The attack began across both sky and ground.

But I didn’t feel afraid or hesitate.

*Kiaaaat!*

I simply drove a decisive, certain strike into the Scorpion King as it screamed and shot up out of the pit.

*Crunch! Fwoooooosh!*

At that moment, the flames melted the acidic blood spilling out of it.

*Ding.*

With the System alert I’d been waiting for, I charged like a beast toward the S-rank monsters.

*KRAAAAAASH!*
```
