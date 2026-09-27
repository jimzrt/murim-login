<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1165.txt",
      "sha256": "649cb9af394d7bd1f1663566b49662ba1837c5d4762145067fe038650f73d316",
      "bytes": 12382
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f49ea048964bc1d857a77493cb258c42d146fd2063ac0c38d14604e4b9133c42",
      "bytes": 982
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "629c127707aeb33bfd33dddf3e4142c30166c25d518472a55ae7f7af5cf583ca",
      "bytes": 247860
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9af2773544f28a58574bd1b8c46afcb79bfb412394dabef0fbb9fece4a72a830",
      "bytes": 760
    },
    {
      "path": "characters/Felix.md",
      "sha256": "1e3efcc36e1825aa844945bc5280a5777bb2a389bd058003882998a4c9c266ae",
      "bytes": 531
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "2d4f4e40707455c0e2902464cf25bfbe99e723b59b50bd5cd8f2034d569e29fc",
      "bytes": 545
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8211dd894ee9712df371a834b0c512042593ed89aa5c110d32bedc68a40fdde4",
      "bytes": 1602
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1cf870e6fd469e0b3e0dbee34efd08a66fdcfd9e1b8b45e3d2f0c74aa4de9401",
      "bytes": 623
    },
    {
      "path": "characters/Morgoth.md",
      "sha256": "8829ee9ed5f11a3886ff0430ffe9d56a23bc1f35a49bbec6c6ce5d6d526701bb",
      "bytes": 825
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "97b900dbb29a57db84ee2adbffd58479c504d0863bf1805451d09b1ed9be91d4",
      "bytes": 294489
    }
  ],
  "estimated_tokens": 9743
}
-->

# Durable State Update — Chapter 1165

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
1 and safe_through 1165. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1165. Profile updates may replace only one
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
  "chapter": 1165,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1165,
    "continuity_sources": [1165],
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
    "The Skeleton King’s sacrifice unleashed a power explosion that weakened Morgoth’s territory; his current condition is unresolved.",
    "Morgoth’s territory is losing its isolation, and numerous Warp formations bring reinforcements across the horizon.",
    "Morgoth has transformed into his Black Dragon form; a thousand Dragon-tooth soldiers and seven empowered Guardians remain arrayed against the exhausted Jin.",
    "Morgoth admits that he fears Jin, and their confrontation continues."
  ],
  "continuity_sources": [
    1163,
    1164
  ],
  "open_questions": [
    "Who has arrived through the Warp formations, and can they change the battle’s outcome?",
    "What is the Skeleton King’s condition after his sacrifice?",
    "Can Morgoth’s seven Guardians be freed from his control?",
    "What will happen in the confrontation between Jin and Morgoth?"
  ],
  "safe_through": 1164,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 용아병 | **Dragon-tooth soldiers** | Guardians born of Dragons and serving them. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 진태경 | 결사대 | commander_to_subordinates | you bastards | blunt and commanding | Jin orders the suicide squad to exploit the opening and wipe out the surrounding monsters. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 필릭스 | 존슨 | prince_to_allied_grand_mage | Mr. Johnson | formal-polite | Felix uses a respectful address while speaking with Magic Johnson. |
| 존슨 | 진태경 | allied friend and comrade-in-arms | Jin | familiar and conversational | Johnson calls Jin 진 while asking what he was thinking. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 모르고스 | 진태경 | enemy Dragon addressing a human opponent | you | formal, measured | Uses 자네 while addressing Jin. |
| 진태경 | 모르고스 | human opponent addressing an enemy Dragon | son | casual and mocking | Calls Morgoth 아들. |
| 모르고스 | 아스모데우스 | being summoned by Asmodeus | Asmodeus | formal and measured | Morgoth directly addresses Asmodeus while reflecting on his failure. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1164
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 801
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty and conscious of royal duty, but increasingly willing to set aside convention and connect with allies as equals.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1164
- **Aliases:** None
- **Role:** Magic Johnson is the United States' Grand Mage and a War Mage, one of the two remaining masters of Magic.
- **Personality:** Strategic and ambitious, with a sharp temper when others squander opportunities or act without consulting her.
- **Voice:** He speaks casually and directly, with colloquial phrasing and occasional profanity.
- **Relationships:** He is Jin Taekyung's friend.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1164
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he masks fear with anger and protects those he cherishes, while recognizing that his enemies fear him too.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the Skeleton King a friend; seven S-rank Hunter comrades presumed dead are now Morgoth’s soul-stolen Guardians.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1164
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Morgoth.md

# Morgoth (모르고스)

- **Safe through:** Chapter 1164
- **Aliases:** None
- **Role:** Morgoth is a Dragon and sovereign of a vast palace who collects powerful beings he kills or subdues as Guardians, including seven S-rank Hunters from Earth.
- **Personality:** Composed and intellectually curious, he treats powerful beings as trophies out of possessive desire and will use overwhelming force when challenged.
- **Voice:** He speaks in polished, courteous, formal phrasing, often asking measured questions while expressing condescension or fascination.
- **Relationships:** Asmodeus summoned Morgoth, though Morgoth says he is not devoted to him; Morgoth holds the Skeleton King as a trophy and commands seven soul-stolen S-rank Hunters as Guardians.

## Korean source

```text
＃1165화



드드드득!

빛이 액체가 되어 흘러넘친다면 이런 광경일까.

지진이라도 난 듯 요동치는 대지 위, 지평선을 물들이며 들이닥치는 오러(Auror)의 물결을 바라보며 모르고스는 직감했다.

만약 지금이 아니라면, 자신이 가진 모든 것을 쏟아부을 기회조차 없으리라는 사실을.

- 부름에 답하라.

나직하지만 깊게 퍼져 나가는 울림.

언어에는 힘이 있다.

그리고 강대한 마력을 머금은 고룡의 언령(言霊)은, 지금껏 그 어떤 종족도 침범하지 못한 영역에 닿아 있었다.

쩌어어억!

텅 비어 있던 허공이 갈라진다.

그와 동시에 어두컴컴한 공간의 틈새로, 무수히 많은 안광(眼光)이 흉흉하게 번뜩였다.

- 크워어어어!

살기 어린 포효와 함께 지상으로 떨어져 내리는 크고 작은 그림자들.

단 한 번의 워프(Warp) 마법으로 인근 곳곳의 도시를 점령하고 있던 잔여 전력을 집결시킨 모르고스는 차갑게 가라앉은 목소리로 명령했다.

- 모조리 죽여라.

그 한마디가 신호탄이다.

괴물이 인간에게, 인간은 괴물에게 달려들고 이내 빛과 어둠이 뒤섞였다.

카가가각!

퍼걱! 푸화아악!

예리한 강철의 소음과 소름 끼치는 파육음이 함성을 집어삼키고, 온 사방을 자욱하게 휘감은 피 안개를 응시하는 흑룡의 두 눈동자는 한 치의 흔들림도 없이 그 모든 광경을 지켜보고 있었다.

동요는 찰나였을 뿐이다.

이미 평정심을 되찾은 모르고스의 이성은 그 어느 때보다 냉철했다.

본거지를 지키고 있던 최정예 몬스터 군단이 막대한 피해를 입었다 한들, 그에게는 새로이 불러들인 병력이 남아 있었고 그것만으로도 충분했다.

아니, 저 몬스터들이 전부 몰살당하더라도 상관없다.

세상의 운명이 걸린 이 거대한 전투의 승패는, 한낱 머릿수 따위가 아닌 한 인간의 생사 여부로 결정지어질 테니까.

‘진태경.’

보인다.

빽빽한 숲처럼 사방을 포위한 일천의 용아병을 서서히 헤쳐 나가며 다가오는 검푸른 화염이.

동시에, 귓전에서 메아리친다.

앞서 저 작고도 하찮은 인간이 내뱉은, 그러나 그로 하여금 가슴 한구석을 서늘하게 만들었던 짧은 맹세가.

‘내가, 다른 누구도 아닌 이 모르고스가 그놈들과 똑같아질 거라고?’

흑룡은 눈부신 이빨을 드러내며 낮게 울었다.

틀렸다. 자신은 그 누구와도 다르다.

마왕 아스모데우스가 없는 지금, 오직 그만이 모든 세상을 아우를 진정한 지배자이며 분명 그리될 것이다.

- 파이어 랜스(Fire Lance).

화륵, 콰아아아!

허공에 불현듯이 나타난 십여 개의 화염창이 진태경을 향해 떨어져 내리려던 그 순간이었다.

“아이스 블래스터(Ice Blaster)!”

어디선가 울려 퍼진 다급한 외침과 함께, 공간을 찢으며 쏘아진 거대한 얼음송곳이 화염을 가로막은 것은.

꽈아아아앙!

공간이 뒤흔들렸다.

방향이 어긋난 불길이 애꿎은 대지를 강타하고, 반경 백여 미터를 뒤덮을 만큼 자욱한 수증기가 피어올라 사방의 시야를 가렸다.

그러나 번뜩이는 흑룡의 두 눈동자는 그 너머의 광경을 선명하게 바라보고 있었다.

피와 먼지를 전신에 뒤집어쓴, 그럼에도 형형하게 빛나는 눈을 한 일단의 무리를.

“길을……!”

가쁜 호흡을 삼킨 거구의 대마도사가, 이내 포효하듯 외쳤다.

“길을 열어라!”

쉬쉭, 쐐애애애액!

하늘을 찌를 듯한 함성과 함께, 가장 먼저 이 끔찍한 전장에 도착한 수천의 결사대가 용아병들을 향해 돌격했다.

아니.

그들의 맹주(盟主)이자 유일한 희망을 향해서.



* * *



그것은 누구도 겉잡을 수 없는 난전(亂戰)이었다.

퍼버버벙!

카캉! 콰드드득!

섬광과 굉음이 쉼 없이 터지고 뒤섞인다.

핏물이 분수처럼 솟구치고, 잘려 나간 팔과 다리는 힘없이 지면을 나뒹굴었다.

그리고 그 극심한 혼란의 틈새 사이로, 기다렸던 목소리가 내 귓가에 닿았다.

“윈드 커터(Wind Cuttur)!”

매직 존슨. 바로 그다.

동시에 들이닥친 바람의 칼날이, 내 측면을 노리며 쇄도하던 두 기의 용아병을 스치듯 지나쳤다.

슈확!

두둥실 떠오르는 두 개의 목.

만약 목을 제외한 다른 신체 부위를 노렸다면 제아무리 대마도사의 마법이라 해도 단숨에 숨통을 끊을 수 없었겠지만, 이미 중동에서의 경험이 있는 매직 존슨은 놈들의 약점을 정확히 알고 있었다.

길고 정다운 인사를 나누기에는, 지금의 상황이 썩 좋지 않다는 것도.

“Fuck.”

나는 짧은 한 음절로 인사를 대신한 그에게, 지금 막 인벤토리에서 소환한 비수를 쏘아 보냈다.

정확히는, 그의 어깨 너머로 짓쳐 들던 용아병을 향해서.

퍼걱!

평범한 무림인이 온 힘을 실어 쏘아 보낸 비수는 암기라고 불러야 마땅하지만, 내 근력은 어지간한 대형 몬스터조차 뛰어넘은 지 오래.

섬광처럼 나아간 비수는 정체 모를 금속으로 만들어진 투구는 물론 머리까지 박살 냈고, 적의 뇌수를 흠뻑 뒤집어쓴 매직 존슨은 다시 한번 욕설을 중얼거렸다.

“지옥이 따로 없군.”

“미안하지만, 돌아가기에는 이미 늦었어요.”

“그건 여기 있는 모두가 알아. 알면서도 왔고.”

그래, 그랬을 것이다.

목숨이 위태로우리라는 사실을 알았음에도, 저들은 내 부름에 기꺼이 응해 주었다.

전 세계를 통틀어 고작 스물, 아니 이제는 십여 명밖에 남지 않은 S급 헌터들이 오직 최정예만을 선별하여 세상 곳곳에서 달려온 것이다.

대륙을 넘고, 대양을 건너서.

그러나 인류의 모든 것이 걸린 이 대전쟁의 전황은, 아직도 머리 위에 떠 있는 저 먹구름처럼 어둡고 축축했다.

“빌어먹을, 도대체 뭐야? 저 끔찍한 놈들이 이렇게나 많다고?”

용아병을 한 번이라도 상대한 적 있는 사람이라면 당연한 반응이다.

A급 중에서도 최상위로 분류되는 데스 나이트보다 강한 마력에, 끔찍하리만치 단단한 신체와 질긴 생명력을 지녔으니까.

까다롭기로는 하나하나가 네임드 몬스터에 준한다고 해도 결코 과언이 아닐 만큼 강력한 존재들.

하지만 이러한 사실을 잘 알고 있는 매직 존슨조차, 아직 모르고 있는 것이 있다.

우리가 모르고스에게 닿기 위해 반드시 넘어야 할 장애물은 비단 저 용아병들만이 아니라는 것을.

쉬이이이잉!

찰나의 순간 빛살처럼 날아드는 무언가.

숨 돌릴 틈도 없이 날아든 그것을, 나는 비스듬히 세운 창날의 옆면으로 막아 냈다.

카앙!

분명 적지 않은 공력을 주입했음에도 부르르 떨리는 창대.

그 너머로 모습을 드러낸 낯익은 얼굴에, 매직 존슨이 낮게 신음했다.

“파이 첸?”

멍하니 벌어지는 입과 흔들리는 동공.

대격변을 시작으로 무려 수십 년의 세월을 알고 지낸 옛 전우를 발견한 매직 존슨은 그 어느 때보다 동요했고, 마침내 그 숫자가 일곱까지 늘어 나자 전신을 부르르 떨었다.

“이게 무슨.”

“가디언.”

“뭐?”

“그렇게 부르더군요. 모르고스가. 저들이 자신을 수호하는 가디언이라고.”

“……!”

내 말에 담긴 뜻을 알아차린 매직 존슨이 이를 악물었다.

마법에 문외한인 나조차도 그들을 지배하고 있는 마력을 선명히 느낄 수 있었으니, 대마도사인 그는 두말할 필요조차 없으리라.

“……가디언이라.”

씁쓸함, 분노, 슬픔.

여러 감정이 뒤섞인 목소리가 바람에 뒤섞이고, 이내 서서히 가라앉는다.

오직 하나.

분노만을 남긴 채.

그리고 그것은 매직 존슨만이 느끼고 있는 감정이 아니었다.

“대격변이 끝나갈 무렵, 모두가 함께한 자리에서 그런 이야기가 나왔었지.”

퍼엉!

포탄처럼 쏘아진 일권(一拳)을 따라 일어나는 굉음.

앞길을 막아서는 용아병들을 하나둘씩 짓뭉개며, 척 헤이글이 말을 이었다.

“만약 이 좆 같은 전쟁에서 살아남게 된다면, 늙어 죽는 그 날까지 세상 그 누구보다 행복하게 살아 보겠다고.”

쉼 없이 뻗어 나가는 주먹 끝에 실린 것은, 오러라는 이름으로 불리는 신비로운 힘뿐만이 아니다.

과거의 기억.

죽을 듯이 고통스러웠던, 그럼에도 머지않아 모든 것이 나아지리라는 희망에 가득 차 있던 그 날의 기억들이 오러와 함께 쏟아지고 있었다.

“그런데 왜!”

콰드드드득!

사방으로 터져 나간다. 흩뿌려진다.

산산조각 난 무기가, 용아병의 갑옷과 신체가.

그리고 오랜 벗들을 잃어버린 노장의 눈물이.

“왜 이런 모습이 되어 있나!”

슬픔과 분노로 가득 찬 포효에는 모든 것이 담겨 있었다.

어째서 이렇게 되어야만 했나.

저들은 왜 오랫동안 행복하고 싶다는 그 간단한 다짐조차 지키지 못하고, 죽어서까지 치욕을 당해야만 하는가.

하지만 그 물음에 답하는 목소리는 없었다.

돌아온 것이 있다면 오직 하나, 다시금 하늘을 뒤덮는 흑룡의 마법과 동시에 내디뎌진 옛 전우들의 발걸음뿐.

화악, 치지지직!

쉬이이이잉!

기가 라이트닝(Giga Lightning).

수십 줄기의 벼락이 신의 천벌처럼 내리꽂히고, 일곱 명의 가디언과 무수한 용아병이 칠흑빛 마력을 망토처럼 휘날리며 들이닥친다.

그 무엇으로도 막을 수 없을 것 같은 무시무시한 기세.

하지만, 그런 일은 벌어지지 않는다.

지금의 나는 혼자가 아니었으므로.

“스톤 월(Storn Wall)!”

굉음을 뚫고 울려 퍼지는 하나의 주문.

그리고 그 안에 담긴 수십의 목소리.

그 선두에는 매직 존슨이 있고, 그 뒤에는 인류 유일의 대마도사를 따르는 세계 최고의 마법사들이 있었다.

콰과과과과광!

하늘이 어두워지더니, 이내 번뜩인다.

불현듯 아군의 머리 위에 드리워진 암석의 천장과 벼락이 맞닥트리며 일어난 거대한 폭발.

아니, 상쇄.

그 여파를 이기지 못한 몇몇 마법사가 피를 토하며 무릎을 꿇고, 분노한 흑룡의 포효가 천둥처럼 울려 퍼진다.

- 감히!

구구구궁!

다시금 공간을 뒤흔들기 시작하는 거대한 마력 속, 나는 떨어져 내리는 암석을 뒤로한 채 정면으로 쏘아졌다.

지금껏 늘 그래 왔듯이.

그러나 한 가지 다른 점이 있다면, 그것은 내 뒤를 따르는 이들이 있다는 것이다.

쐐애애애액!

마침내 이 혼란스러운 전장을 비집고 나타난 또 다른 얼굴들.

그중 선두에 서 있던 갈색 머리의 외국인이 나를 향해 고개를 까딱였다.

“너무 늦었나?”

“전혀.”

“다행이군. 설령 그랬어도 사과할 생각은 아니었지만.”

기억 속 고스란히 남아있는 재수 없는 말투. 

네 명의 S급 헌터와 함께 합류한 필릭스 왕자가 덧붙였다.

“가라, 어서. 이곳은 우리가 맡을 테니까.”

나는 대답하지 않았다.

단지 가슴 깊숙한 곳에서 치밀어 오르는 뜨거운 무언가를 억누르며, 온 힘을 다해 앞으로 나아갔다.

일곱 명의 S급 헌터가 그들의 옛 동료들과 격돌하는 것을 뒤로한 채.

서걱!

베고, 또 베어 넘기며.

콰드드득!

계속해서, 멈추지 않고.

그렇게.

콰직!

이 모든 것의 시작이자 끝인 어느 괴물을 향해.

퍼어어엉!

한 줄기의 불꽃이 되어 쏘아졌다.

“모르고스-!”

번뜩이는 흑룡의 거대한 두 눈동자에, 허공을 짓밟으며 솟구치는 한 인간이 비치고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1165

*Rrrrrumble!*

If light could turn to liquid and overflow, would it look like this?

Watching the waves of aura wash across the horizon and surge toward him, the ground shuddering as if an earthquake had struck, Morgoth knew instinctively:

If he didn’t act now, he might never get another chance to unleash everything he had.

“Answer my call.”

A low voice, its reverberation spreading deep and far.

Language had power.

And the Dragon’s words, imbued with immense magical power, had reached a realm no other race had ever trespassed.

*Craaaack!*

The empty air split open.

At the same time, countless eyes gleamed ominously from within the dark rift in space.

“Gwoooar!”

Large and small shadows plummeted to the ground with bloodthirsty roars.

With a single Warp spell, Morgoth had gathered the remaining forces occupying cities across the region. His voice turned cold as he gave the order.

“Kill them all.”

That one command was the signal.

Monsters charged at humans, humans charged at monsters, and soon light and darkness blurred together.

*Clang-clang-clang!*

*Thwack! Splatter!*

The shriek of keen steel and the sickening sound of flesh being torn apart swallowed the shouts. The Black Dragon’s eyes watched it all without a flicker as he gazed upon the blood mist hanging thick over the battlefield.

His shock had lasted only an instant.

Morgoth had already regained his composure. His mind was colder than ever.

Even if his elite monster legion, the force that had guarded his stronghold, had suffered heavy losses, he still had the reinforcements he’d just summoned. That alone was enough.

No—even if every one of those monsters were wiped out, it wouldn’t matter.

The fate of the world would be decided in this great battle, and the victor would be determined not by mere numbers, but by whether one human lived or died.

*Jin Taekyung.*

There he was.

A blue-black flame advancing through the thousand Dragon-tooth soldiers surrounding him on every side like a dense forest.

At the same time, the short vow that small, insignificant human had spoken earlier echoed in Morgoth’s ears—and chilled a corner of his heart.

*Me? Morgoth? Becoming just like them?*

The Black Dragon bared his gleaming teeth and let out a low growl.

Wrong. He was nothing like anyone else.

With the Demon King Asmodeus gone, Morgoth alone was the true ruler destined to reign over every world—and that was exactly what he would become.

“Fire Lance.”

*Fwoosh—KABOOM!*

A dozen or so spears of flame appeared out of nowhere in the air, poised to fall on Jin Taekyung.

“Ice Blaster!”

A desperate shout rang out from somewhere. A massive icicle shot through space and blocked the flames.

*KABOOM!*

Space shook.

The deflected flames slammed into the ground, harmless to their intended target. A dense cloud of steam rose, spreading across a radius of roughly a hundred meters and blocking the view in every direction.

But the Black Dragon’s gleaming eyes saw clearly through it all.

A group of people, their bodies covered in blood and dust, yet their eyes shining fiercely.

“Clear a…!”

The towering Grand Mage caught his breath, then shouted like a roar.

“Clear a path!”

*Whoosh! Whoooooosh!*

With a sky-piercing battle cry, thousands of the suicide squad—the first to arrive at this dreadful battlefield—charged toward the Dragon-tooth soldiers.

No.

They were charging toward their Alliance Leader, their one and only hope.

* * *

It was a battle no one could control.

*BOOM!*

*Clang! Krrrunch!*

Flashes and explosions burst and mingled without pause.

Blood sprayed like fountains. Severed arms and legs rolled limply across the ground.

And through the chaos, a long-awaited voice reached my ears.

“Wind Cutter!”

Magic Johnson. It was him.

At the same time, the blades of wind that rushed in passed close by the two Dragon-tooth soldiers charging at my flank.

*Shwaa!*

Two heads floated into the air.

If he’d aimed anywhere but their necks, even the Grand Mage’s Magic wouldn’t have been enough to kill them in one blow. But Magic Johnson had fought them before, in the Middle East. He knew their weakness exactly.

And he knew this wasn’t the time for a long, friendly greeting.

“Fuck.”

I tossed a dagger I’d just summoned from my Inventory to the man who’d greeted me with a single syllable.

More precisely, I threw it at the Dragon-tooth soldier lunging over his shoulder.

*Thwack!*

A dagger thrown with all a normal Murim martial artist’s strength should properly be called a hidden weapon. But my Strength had long since surpassed that of most large monsters.

The dagger shot forward like a flash and shattered not only the helmet made of some unknown metal, but the head beneath it, too. Drenched in the enemy’s brain matter, Magic Johnson muttered another curse.

“This is a special kind of hell.”

“Sorry, but it’s too late to go back.”

“Everyone here knows that. We knew, and we came anyway.”

That was true.

They knew their lives would be in danger, and still they’d answered my call without hesitation.

There were only twenty S-rank Hunters left in the entire world—or rather, now only a dozen or so—and they’d chosen only the very best before racing here from all over the globe.

Across continents and oceans.

But the tide of this great war, with the fate of all humanity at stake, was still as dark and heavy as the storm clouds overhead.

“Damn it, what the hell are those things? There are this many of them?”

Anyone who’d ever faced a Dragon-tooth soldier would react the same way.

Their magical power surpassed that of even the strongest Death Knights, classified at the top of A-rank. Their bodies were horrifyingly tough, and they were stubbornly hard to kill.

Calling each one as formidable as a named monster would be no exaggeration.

But even Magic Johnson, who knew all this well, still didn’t know one thing.

The Dragon-tooth soldiers weren’t the only obstacle we’d have to overcome to reach Morgoth.

*Shiiiiing!*

Something shot toward us at the speed of light.

It came without giving me a moment to breathe. I blocked it with the side of my spear blade, held at an angle.

*Clang!*

Even with no small amount of internal energy poured into it, the shaft of my spear trembled.

Magic Johnson let out a low groan at the familiar face that appeared beyond it.

“Pai Chen?”

His mouth fell open. His eyes wavered.

The moment he recognized his old comrade, someone he’d known for decades, ever since the Great Cataclysm began, Magic Johnson was shaken more than ever. And when their number finally reached seven, his whole body trembled.

“What is this?”

“Guardians.”

“What?”

“That’s what Morgoth calls them. His Guardians. They’re supposed to protect him.”

“……!”

Magic Johnson clenched his teeth as he understood what I meant.

Even I, a complete outsider to Magic, could clearly sense the magical power controlling them. There was no need to ask what the Grand Mage could feel.

“……Guardians.”

Bitterness, anger, grief.

The voice, tangled with too many emotions, mingled with the wind and gradually quieted.

Leaving only one behind.

Anger.

And Magic Johnson wasn’t the only one feeling it.

“Near the end of the Great Cataclysm, we talked about it when we were all together.”

*Boom!*

A fist shot forward like a cannonball, followed by a roar.

Chuck Hagel crushed the Dragon-tooth soldiers blocking his path one by one as he went on.

“If we survived this goddamn war, we’d live happier than anyone else in the world until the day we died.”

The fists he kept throwing carried more than just the mysterious power known as aura.

Memories from the past.

The memories of those days, so painful they could have killed him, yet filled with hope that things would soon get better, poured forth with his aura.

“Then why?!”

*Krrrunch!*

They burst outward in every direction. They scattered.

Shattered weapons. The armor and bodies of the Dragon-tooth soldiers.

And the tears of an old man who had lost his longtime friends.

“Why are they like this now?!”

The roar, filled with grief and anger, contained everything.

Why had it come to this?

Why hadn’t they been allowed to keep even that simple promise to live happily for a long time? Why did they have to suffer this humiliation even after death?

But no voice answered his questions.

The only answer was the Black Dragon’s Magic once again filling the sky, and the footsteps of his old comrades as they advanced.

*Fwoosh, crackle!*

*Shiiiiing!*

Giga Lightning.

Dozens of bolts plunged down like divine punishment, while the seven Guardians and countless Dragon-tooth soldiers charged forward, their pitch-black magical power streaming behind them like cloaks.

An overpowering force that seemed impossible to stop.

But that wasn’t what happened.

Because I wasn’t alone anymore.

“Stone Wall!”

A single spell rang through the roar of battle.

And dozens of voices filled it.

At the front stood Magic Johnson. Behind him were the world’s greatest mages, following the only Grand Mage humanity had.

*KABOOM!*

The sky darkened, then flashed.

A ceiling of rock suddenly appeared over our allies’ heads. When it met the lightning, a tremendous explosion shook the battlefield.

No—cancellation.

Several mages, unable to withstand the backlash, coughed up blood and fell to their knees. The enraged Black Dragon’s roar thundered across the battlefield.

“How dare you!”

*Rrrrrumble!*

As immense magical power shook space again, I shot straight forward, leaving the falling rocks behind me.

Just as I always had.

But there was one difference.

This time, people were following me.

*Whoooooosh!*

Another group of familiar faces finally broke through the chaotic battlefield.

The brown-haired foreigner at the front gave me a slight nod.

“Too late?”

“Not at all.”

“Good. Though even if I were, I wasn’t planning to apologize.”

That irritating way of speaking, still exactly as I remembered it.

Prince Felix had joined us with four S-rank Hunters. He added, “Go. Now. We’ll handle things here.”

I didn’t answer.

I just suppressed the hot feeling rising deep in my chest and pushed forward with all my might.

Leaving the seven S-rank Hunters behind as they clashed with their old comrades.

*Slice!*

I cut them down, one after another.

*Krrrunch!*

Kept going, without stopping.

And then—

*Crack!*

Toward the monster who was the beginning and end of it all.

*BOOM!*

I shot forward like a streak of flame.

“Morgoth!”

In the Black Dragon’s vast, gleaming eyes, a human leaping upward, stomping on thin air, was reflected.
```
