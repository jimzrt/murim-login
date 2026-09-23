<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0790.txt",
      "sha256": "cd594348abfd74d23138b979b2548670a7bf47951328f012f0aef19296f2c029",
      "bytes": 12866
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "039fe963f276a2c3e626d1607267a996a70137f9e3246788aef94ee640bf4914",
      "bytes": 1068
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1cdb7321521fc0fa7ea0c4782e2f2dfdb5a3d3aff2659ffca9e42c35a3de25f4",
      "bytes": 223834
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "80d37e531a44b97271c558eab252db01d87bf2bd668aebeac7ad1a186730e762",
      "bytes": 553
    },
    {
      "path": "characters/Emmanuel.md",
      "sha256": "f3d19921eceb2cd919e029ff3aa03485b765567f88863c5eb56369855d30ff68",
      "bytes": 574
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "487d1f35cc58ee9397823f0e935640883b604e88aba8b14b73081acdf1698325",
      "bytes": 1921
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "dc2bbaa3ce11800ed527ce4ae271e5d3bf4847c5dffcfa56e51d3e5c956612eb",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "de0c89048ec9e723011f603b722f93027088c9d60466984073e893933c82ed88",
      "bytes": 820
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "5af2066219866a3b10d219a6f405ef821cf3c50fb855818a2adf99722672b385",
      "bytes": 645
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "8ad56fa94fcb0f1604f9358bd85977c28dc9fe73d1eabf3e60301cb143d8b7d7",
      "bytes": 693
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ce37c4566435af26d5f9e0f8c3be8f18f1a8865dea42552bf6278747296528c8",
      "bytes": 244692
    }
  ],
  "estimated_tokens": 9947
}
-->

# Durable State Update — Chapter 790

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 790. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 790. Profile updates may replace only one
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
  "chapter": 790,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 790,
    "continuity_sources": [790],
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
    "Michael Silbert is dead; Huginn was captured alive, and Michael’s forces were killed or captured.",
    "Jin Taekyung has awakened and accepted the World Hunter Federation’s appointment as Alliance Leader.",
    "The Federation’s operation against Michael Silbert’s associates has led to arrests of major political and business figures.",
    "Jin’s nightmare showed a world-ending fire and a rift in the sky and space; their significance is unresolved.",
    "Jin’s sister Hayeon and mother were with him when he woke.",
    "The Prophet’s whereabouts are unknown; Jin has asked Team Leader Choi about them."
  ],
  "continuity_sources": [
    788,
    789
  ],
  "open_questions": [
    "Where is The Prophet?",
    "Was Jin’s nightmare of fire and a rift a warning of an actual catastrophe?"
  ],
  "safe_through": 789,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Treat the fire and rift in Jin’s nightmare as ominous imagery, not established future events."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 임마누엘 | **Emmanuel** | The President of France who congratulates Michael Silbert directly. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 스위스 | **Switzerland** | Country associated with the watchmaker. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 대통령 | **President** | Title for Korea's head of state. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 펜타곤 | **Pentagon** | Headquarters of the United States Department of Defense and source of intelligence about terrorist experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 브라질 | **Brazil** | Country containing Rio de Janeiro. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 한국 | **Korea** | Destination of the international Hunters and Guild Masters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 788
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Emmanuel.md

# Emmanuel (임마누엘)

- **Safe through:** Chapter 789
- **Aliases:** None
- **Role:** Emmanuel is the arrested former President of France and a longtime political beneficiary of Michael Silbert.
- **Personality:** Ambitious, opportunistic, and willing to trade absolute loyalty for power and wealth.
- **Voice:** Formal and deferential toward powerful allies, with self-important ambitions.
- **Relationships:** He served Michael Silbert with absolute loyalty and was arrested after Michael’s death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 789
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 789
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 789
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 788
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 789
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃790화



“선지자는, 어디에 있습니까.”

그 한 마디에 최 팀장의 입가에 맺혀 있던 미소가 흐릿해진다.

어떻게 되었느냐, 가 아닌 어디에 있느냐.

명석한 두뇌의 소유자인 그는 이 간단하면서도 명확한 차이를 즉각 깨달았고, 나는 이 짧은 침묵이 뜻하는 바를 이미 알고 있었다.

“아직이군요.”

굳은 얼굴로 나를 응시하던 최 팀장이 고개를 끄덕였다.

“예.”

“위치도 드러나지 않은 겁니까?”

최 팀장은 대답하지 않았고, 무언(無言)은 곧 긍정이다.

‘빌어먹을.’

나는 튀어나오려는 욕설을 삼키며 밤하늘을 바라보았다.

같은 곳에 있다고 해서, 모두가 같은 방향을 바라보는 것은 아니다.

지금 이 순간 나와 최 팀장이 각기 다른 풍경을 바라보는 것처럼.



퀘스트



[격변]



어느덧 새로운 시대는 눈앞까지 다가왔고, 이 길고도 치열한 이야기의 마지막 단어는 아직 정해지지 않았습니다.

희망. 혹은 절망.

그리고 지금 이 순간, 펜을 쥔 유일한 사람은 당신입니다.

무운(武運)을 빕니다.



등급 : 메인 퀘스트

제한 : 진태경

임무 : ???

보상 : ???

실패 : ???





나는 물음표로 점철된 홀로그램 창을 바라보며 마음속으로 뇌까렸다.

‘아직도 퀘스트가 완료되지 않았다는 건…….’

바로 한 가지 사실만을 의미한다.

퀘스트 창에 적힌 저 물음표가 뜻하는 존재는, 처음부터 미카엘 실베르트가 아니었다는 것.

‘도대체, 도대체 어째서?’

나로서도 예상치 못한 상황이었다.

미카엘 실베르트를 제거하는 것만이 이 퀘스트를, 새로운 격변(激變)을 해결할 수 있는 열쇠라는 확고한 믿음이 있었으니까.

하지만 내가 틀렸다. 완전히 잘못 짚었다.

‘선지자(先知者).’

스스로를 신의 사자이자 예언가라 칭하는 그 미친 광신도가, 미카엘 실베르트의 명령을 따르는 하수인으로 생각했던 테러리스트가 이번 메인 퀘스트의 진짜 열쇠였다.

혹은…….

곧 다가올 격변의 시작점이거나.

띠링.



- 메인 퀘스트, [격변]의 정보가 갱신되었습니다.

- 당신의 자각에 따라 임무가 변경됩니다.

- 임무 : 제한 시간 내에 [선지자] 처치 (미완료).



갑작스러운 알림과 함께 시야를 채운 새로운 홀로그램 창들.

동시에 나는 깨달았다.

곧 세상을 뒤흔들, 격변이라는 폭탄의 시계 초침은 지금 이 순간에도 움직이고 있다는 것을.



* * *



지구촌이라는 말도 구식이 되어 버린 현재.

세상에는 단 하루에도 헤아릴 수도 없을 만큼 수많은 이슈가 발생한다.

그러나 TV와 인터넷을 통해 온갖 뉴스를 접하고, 이내 잊어버리는 것에 익숙해진 현대인들에게도 일주일 전의 사건은 충격 그 자체였다.

마치 지뢰가 터지듯, 헌터들에 의해 전 세계 곳곳에서 시작된 무력 진압과 체포.

그중에는 대통령을 필두로 한 고위 정치인들, 세계에서도 손꼽히는 부호들과 헌터 역시 포함되어 있었다.

그들 모두가 특정 지방과 국가를 넘어 전 세계의 정치, 경제, 안보에 영향을 끼칠 수 있는 거물들.

역사에 길이 남을 새로운 세계 헌터 연맹의 발족식만을 기다리던 사람들은 혼란에 빠졌고, 그 혼란은 이내 경악으로 뒤바뀌었다.

- 이 안에, 모든 진실이 담겨 있습니다.

임시 대변인의 자격으로 카메라 앞에 선 최민우의 손에 들려 있던 것은 손톱보다 작은 마이크로 칩(Micro chip)이었다.

그것은 역사의 한순간을 담기 위해 국회의사당 곳곳에 설치되었던 많은 카메라 중, 엄청났던 전투의 여파를 이겨 내고 살아남은 유일한 것이었다.

그와 동시에, 차마 마주할 수 없는 진실이 담긴 판도라의 상자이기도 했다.

불과 세 시간 남짓한 영상.

하지만 모두가 볼 수 있는 스트리밍 사이트에 올라온 그 영상은 전 세계를 침묵의 구렁텅이에 빠트렸다.

최민우의 말은 사실이었다. 그 안에 모든 진실이 담겨 있었다.

그 어떤 편집도, 거짓도 없었다.

다만 명백한 사실만이 있을 뿐이었다.

그렇게 수십억의 인류는 믿을 수 없는 진실과 마주했고, 갑작스럽게 열린 이 판도라의 상자 속에 남아 있는 무언가를 발견했다.

그건 희망이었다.



한 가지는 확실해. 난 저들에게 내 가족들의 목숨까지 맡길 수 있어.

└ 동의한다.

└ 진정한 영웅들이지. 진정한 헌터고.

└ 맞아. 그중에서도 Jin은 영웅 중의 영웅이야.

└ 빌어먹을. 도대체 어떤 얼간이가 저 젊은 구세주를 욕한 거야?

└ 미안하지만 얼마 전까지의 내가 그랬어. 하지만 얼간이라는 걸 인정할 수밖에 없군. 병신이라고 불러도 할 말이 없어.

└ 이 병신 같은 대머리 새끼.

└ 대머리는 빼. 네 머리통에 총알을 박아 넣기 전에.

└ 알겠다, 이 병신아.

└ God bless you.



결심했어. 곧 태어날 내 아이의 이름을 Sibal이라고 지을 거야. 진태경의 별명을 딴 아주 훌륭한 이름이지.

└ 지나가던 한국인으로서 충고하자면, 그건 썩 좋은 선택이 아니야.



잠깐. 지금 나만 저 fucking 몬스터의 존재를 알고 있는 거야? 왜 다들 아무 말도 없지?

└ 스톤 킹 얘기를 하는 거라면, 물 흐리지 말고 꺼져.

└ 미쳤군. 그는 몬스터라고.

└ Oh. 그래서?

└ 잘 들어. 내 사촌은 흑인에게 총격당해서 죽었지만, 나는 내 흑인 친구들을 살인범 취급하지 않아.

└ 미카엘 실베르트는 수많은 사람을 죽였고, 스톤 킹은 그들을 위해 싸웠어. 자, 이제 누가 영웅이고 몬스터지?

└ Shit. 너희 같은 머저리들 때문에 세상이 망할 거다.

└ 좋아. 다 지껄였으면 꺼져.

└ 잘 가. 멍청이.



난 프랑스인인데, 처음에는 테러라도 벌어진 줄 알았어. SNS를 보고 있었는데 엘리제 궁 창문에서 대통령이 떨어지는 영상이 올라와 있더라고.

└ 임마누엘? 그 새낀 죽어도 싸. 미카엘 실베르트랑 붙어먹다니.

└ 스위스 내무부 장관이 체포당하는 영상 봤어? 매직 존슨이 그가 가진 크고 아름다운 스태프로 놈을 두들겨 패던데.

└ OMG…….

└ 친구. 네가 생각하는 그런 건 아니야. 괜히 이상한 상상하지 마.

└ 매우 신속하면서도 훌륭한 작전이었지. 세계 헌터 연맹은 불과 한 시간 만에 편제를 끝마치고 전 세계 곳곳에 심어진 배신자 놈들을 뿌리 뽑았어. 도망치거나 반항할 틈도 없었다고.

└ 작전 시작 전까지의 기밀 유지도 완벽했어. 아마 멕시코나 브라질이었으면 갱단을 통해 정보가 넘어갔을걸.



우리는 당신들을 지지하고 사랑합니다. 부디 여러분께 신의 가호가 있기를.

└ 아직 안심하기는 일러. 다들 광신도 테러리스트의 존재를 잊은 건 아니지?

└ 당연히 기억하고 있지. 하지만 세계 헌터 연맹이 우리를 지켜 줄 거야. 스스로를 선지자라고 부르는 그 미친놈도 바짝 엎드려서 눈치만 살피는 중이고.

└ 이미 테러가 멈춘 지 2주 째야. 선지자도 곧 빈 라덴처럼 죽을 테고, 비로소 진정한 평화가 찾아오겠지.

└ Jin. 어서 깨어나세요. 우리는 영웅을 기다리고 있습니다.



일주일이라는 시간은 전 세계가 느낀 충격을 상쇄하기에는 터무니없이 부족했지만, 인류는 빠르게 안정을 찾아가고 있었다.

세계 헌터 연맹을 향한 믿음과 모든 것이 나아지리라는 희망으로.

그러나 그들이 모르는 어딘가에서는, 이미 새로운 움직임이 시작되고 있었다.

혹은, 세상을 집어삼킬 불길이.

“동원할 수 있는 모든 전력을 중동에 집중시키십시오. 지금 당장.”

진태경의 한 마디는 최민우를 통해 곧장 세계 헌터 연맹의 수뇌부로 전달되었고, 누구도 의문을 표하지 않았다.

이건 부탁이 아닌 명령이다.

자신들이 추대한 맹주(盟主)가 내리는 첫 명령.

그리고 그들이 해야 할 대답은 처음부터 정해져 있었다.

“Yes, boss.”

세계 헌터 연맹이 움직이기 시작했다.



* * *



“놈들이 오고 있습니다.”

떨리는 목소리가 동굴 안을 울린다.

발치 아래에 엎드린 사내를 말없이 굽어보던 선지자가 입을 열었다.

“예상 전력은?”

“그, 그것이…….”

“답하라.”

망설이던 사내가 고개를 바닥으로 처박았다.

“적어도 10만 이상으로 추정됩니다.”

“……!”

“……!”

10만.

예상을 뛰어넘는 엄청난 숫자에, 그렇지 않아도 서늘하던 동굴 안의 공기가 얼어붙었다.

이 자리에 있는 이들은 안다. 저 10만이라는 숫자가, 단순한 보병을 의미하는 것이 아니라는 사실을.

‘세계 헌터 연맹.’

헌터는 등급을 떠나 그 존재 자체로 희귀하다.

천 명 중 한 사람만이 각성의 기회를 얻고, 특정한 훈련을 거쳐야 헌터로 인정받을 수 있으니까.

그러나 상대는 세계 헌터 연맹이었다.

그 명칭처럼 전 세계의 모든 헌터가 소속된 거대 단체. 수십억에 달하는 인류 중, 0.1%의 확률을 뚫고 신의 선택을 받은 수백 만의 헌터가 사막을 향해 짓쳐 들고 있다.

아니, 전 세계가.

“사막 전체가 감시받고 있습니다.”

“펜타곤에 심어 두었던 정보원들에게서 소식이 끊겼습니다.”

“인근 마을과 소도시의 주민들이 대피 중이라고 합니다.”

“미국이 항공모함을 움직였다는 정보가…….”

증폭된 불안감이 목소리로 흘러나온다. 그들은 한참 동안 자신들이 얻어낸 정보를 쏟아냈다. 그만큼 이미 상황은 최악을 향해 치닫고 있었으니까.

일주일 전, 생각지도 못했던 미카엘 실베르트의 죽음이 몰락의 시작이었다.

새롭게 탄생한 세계 헌터 연맹은 실로 파격적이고, 거침없이 움직였다. 발족식을 피로 물들인 것을 시작으로 미카엘 실베르트가 뿌려 둔 씨앗을 거두어들였고, 모든 진실을 한 치의 가감 없이 밝히며 전 세계의 지지를 얻었다.

순수한 정의(情意).

세계 헌터 연맹이 내리친 그 철퇴를 막을 수 있는 것은 아무것도 없었다. 일국의 대통령도, 세계 증권 시장을 좌지우지하는 거대기업의 총수도, 모두가 피를 흘리며 쓰러졌다.

지금으로부터 반세기 전, 오사마 빈 라덴의 테러 이후 미국의 영공 통과를 거부했던 파키스탄과 중동 국가들조차 감히 이번 조치에 반항하지 못할 것이다.

세계 헌터 연맹을, 전 세계를 적으로 돌리는 미친 짓을 할 수는 없으니까.

그랬다간 무수한 포화(砲火)와 함께 수많은 헌터들의 방문을 받게 될 테니까.

그러나 타협을 택할 수 있는 그들과는 달리, 이 동굴 안에 모인 이들에게는 일말의 선택지조차 주어지지 않았다.

“선지자시여!”

“부디, 부디 저희가 가야 할 길을 알려 주십시오!”

곳곳에서 울려 퍼지는 애타는 부르짖음.

광신(狂信)으로 무장한 그들은 오직 한 사람만을 향해 무릎을 꿇고 엎드렸다.

코앞까지 몰려온 적들이 두렵긴 했으나, 동시에 굳게 믿었다.

신을 위해 목숨을 바치고, 그분께서 내리신 예언자를 따라 걸었던 지난날들을.

선지자가 자신들에게 보여 준 그 놀라운 이적(異蹟)들을.

“이 길 잃은 종들에게 가르침을 내려 주소서!”

“저 이교도들을 무찔러, 온 세상에 신의 뜻을 알리시옵소서!”

화륵, 화르륵.

동굴 안을 밝히던 횃불이 바람에 흔들린다. 깊이 눌러쓴 로브 사이로, 성별도 나이도 짐작할 수 없는 선지자의 목소리가 울려 퍼졌다.

“너희의 바람대로, 나는 신의 뜻을 받들어 저들을 벌할지어다. 인샬라.”

“오, 오오……!”

“신은 위대하시다!”

“인샬라. 인샬라!”

터질 것만 같던 불안감이 환호로 뒤바뀐다. 그리고 신의 위대함을 부르짖으며 연신 엎드려 절하는 그들을 바라보며, 선지자는 생각했다.

자신의 긴 기다림이, 곧 결실을 맺을 것이라고.
```

## Final English reading copy

```markdown
# Chapter 790

“Where is The Prophet?”

At that single question, the smile lingering on Team Leader Choi’s lips faded.

Not *What happened to him?* but *Where is he?*

A man with a keen mind, he immediately grasped the simple but clear distinction. And I already knew what the brief silence meant.

“So you still haven’t found him.”

Team Leader Choi, who’d been watching me with a grave expression, nodded.

“That’s right.”

“You haven’t even uncovered his location?”

Team Leader Choi didn’t answer. Silence was as good as a yes.

*Damn it.*

I swallowed the curse that threatened to escape and looked up at the night sky.

Just because you’re in the same place doesn’t mean you’re all looking in the same direction.

Just like Team Leader Choi and I were looking at different scenery at that very moment.

> **System**
>
> **Quest**
>
> **Cataclysm**
>
> A new era has drawn near, and the final word of this long and fierce story has yet to be written.
>
> Hope. Or despair.
>
> And at this very moment, you are the only one holding the pen.
>
> May good fortune in battle be with you.
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Mission:** ???
>
> **Reward:** ???
>
> **Failure:** ???

I stared at the holographic window covered in question marks and muttered to myself.

*The Quest still hasn’t been completed…*

It could only mean one thing.

The being represented by those question marks in the Quest window had never been Michael Silbert in the first place.

*Why? Why the hell?*

Even I hadn’t seen this coming.

I’d firmly believed that eliminating Michael Silbert was the only key to completing this Quest and resolving the new Cataclysm.

But I’d been wrong. Completely wrong.

*The Prophet.*

That deranged fanatic who called himself God’s messenger and a prophet—the terrorist I’d thought was merely a lackey following Michael Silbert’s orders—was the real key to this Main Quest.

Or…

He was the starting point of the Cataclysm soon to come.

*Ding.*

> **System**
>
> Information for the Main Quest, **Cataclysm**, has been updated.
>
> The mission has changed in accordance with your realization.
>
> **Mission:** Eliminate **The Prophet** within the time limit (Incomplete).

New holographic windows filled my vision with a sudden notification.

At the same time, I realized:

The clock on the bomb called the Cataclysm, the one that would soon shake the world, was ticking even now.

* * *

These days, even the term “global village” had become outdated.

Countless issues arose around the world every single day—too many to keep track of.

But even people accustomed to seeing all kinds of news on TV and the internet, then promptly forgetting it, had been shaken to the core by what happened a week ago.

Like land mines detonating, armed crackdowns and arrests had begun in countries all over the world, carried out by Hunters.

Among those arrested were high-ranking politicians, including presidents, some of the wealthiest people in the world, and Hunters.

Every one of them was a heavyweight with influence over global politics, business, and security—not merely a particular region or country.

People who’d been waiting only for the new World Hunter Federation’s inaugural ceremony were thrown into confusion. Before long, that confusion turned to shock.

> “All the truth is in here.”

In Choi Minwoo’s hand as he stood before the cameras in his role as interim spokesperson was a microchip smaller than a fingernail.

Of all the many cameras installed throughout the National Assembly to capture a moment in history, it was the only one to survive the aftermath of the tremendous battle.

At the same time, it was a Pandora’s box containing a truth no one could bear to face.

The footage ran a little over three hours.

But once it was uploaded to a streaming site where the whole world could watch, it plunged the world into a pit of silence.

Choi Minwoo had been telling the truth. It contained all the truth.

Not a single edit. Not a single lie.

Only facts, plain and undeniable.

Billions of people were confronted with an unbelievable truth—and, within the Pandora’s box that had suddenly opened, they discovered something still left inside.

It was hope.

> One thing’s for sure. I’d trust them with the lives of my family.
>
> └ Agreed.
>
> └ Real heroes. Real Hunters.
>
> └ Yeah. And Jin’s the greatest hero of them all.
>
> └ Damn it. What kind of idiot talked shit about that young savior?
>
> └ Hate to admit it, but I did until recently. But I have to admit I was an idiot. Call me a fucking moron and I couldn’t argue.
>
> └ You bald piece of shit.
>
> └ Leave the bald part out before I put a bullet in your head.
>
> └ Fine, you fucking moron.
>
> └ God bless you.

> I’ve decided. I’m naming my unborn child Sibal.[^1] It’s a great name, taken from Jin Taekyung’s nickname.
>
> └ A Korean passing by here with some advice: that’s not a very good choice.

[^1]: “Sibal” sounds like *ssibal*, a common Korean profanity roughly equivalent to “fuck.”

> Wait. Am I the only one who knows that fucking monster’s out there? Why is everyone silent?
>
> └ If you’re talking about the Stone King, stop trying to derail the conversation and get lost.
>
> └ You’re insane. He’s a monster.
>
> └ Oh. So?
>
> └ Listen. My cousin was shot and killed by a Black man, but I don’t treat my Black friends like murderers.
>
> └ Michael Silbert killed countless people. The Stone King fought for them. So, which one’s the hero and which one’s the monster?
>
> └ Shit. The world’s going to end because of morons like you.
>
> └ Great. You done talking? Now get lost.
>
> └ Goodbye, idiot.

> I’m French, and at first I thought there’d been a terrorist attack or something. I was looking at social media when a video popped up of the president falling out of a window at the Élysée Palace.
>
> └ Emmanuel? He deserved to die. The bastard was in bed with Michael Silbert.
>
> └ Did you see the video of the Swiss interior minister getting arrested? Magic Johnson was beating him with that big, beautiful staff of his.
>
> └ OMG……
>
> └ Buddy. It’s not what you think. Don’t let your imagination run wild.
>
> └ It was a swift and brilliant operation. The World Hunter Federation had its ranks in order in just an hour, then rooted out the traitors planted all over the world. They didn’t have time to run or fight back.
>
> └ They kept the operation completely secret right up until it began, too. If this had been Mexico or Brazil, the information probably would’ve leaked through the gangs.

> We support you and love you. May God watch over you all.
>
> └ It’s too soon to relax. Nobody’s forgotten about the fanatical terrorist, right?
>
> └ Of course we remember. But the World Hunter Federation will protect us. That lunatic who calls himself The Prophet is keeping his head down and watching what happens.
>
> └ It’s already been two weeks since the terrorist attacks stopped. The Prophet will die soon, just like bin Laden, and then real peace will finally come.
>
> └ Jin. Please wake up soon. We’re waiting for our hero.

A week was nowhere near enough time for the whole world to recover from the shock.

Even so, humanity was quickly finding its footing again.

They had faith in the World Hunter Federation, and hope that things would get better.

But somewhere beyond their sight, a new movement had already begun.

Or perhaps it was a blaze that would devour the world.

“Concentrate every force we can mobilize in the Middle East. Now.”

Jin Taekyung’s words were relayed straight to the World Hunter Federation’s leadership through Choi Minwoo. No one questioned them.

This wasn’t a request. It was an order.

The first order from the Alliance Leader they had chosen.

And they’d known from the start what their answer would be.

“Yes, boss.”

The World Hunter Federation began to move.

* * *

“They’re coming.”

A trembling voice rang through the cave.

The Prophet silently looked down at the man prostrate at their feet, then spoke.

“What is their estimated strength?”

“Th-that is…”

“Answer.”

The hesitant man lowered his head to the floor.

“At least a hundred thousand.”

“……!”

“……!”

A hundred thousand.

The staggering number, far beyond their expectations, froze the already chilly air in the cave.

Those gathered here knew that the number didn’t mean an ordinary infantry force.

*The World Hunter Federation.*

Hunters were rare, regardless of their Grade.

Only one in a thousand had the chance to awaken, and even then, they had to undergo specific training before they could be recognized as a Hunter.

But their opponents were the World Hunter Federation.

As its name implied, it was a vast organization to which every Hunter in the world belonged. Out of humanity’s billions, millions of Hunters who’d beaten the 0.1 percent odds and been chosen by God were charging toward the desert.

No—the whole world was coming.

“The entire desert is under surveillance.”

“We’ve lost contact with our informants planted in the Pentagon.”

“The residents of nearby villages and small towns are being evacuated.”

“We have reports that the United States has moved an aircraft carrier…”

Their growing anxiety spilled out in their voices. For a long while, they poured out the information they’d managed to gather.

The situation was already hurtling toward its worst possible outcome.

A week ago, Michael Silbert’s unexpected death had marked the beginning of their downfall.

The newly born World Hunter Federation was truly bold, moving without hesitation. It had begun by bathing its inaugural ceremony in blood, then set about reaping the seeds Michael Silbert had sown. By revealing the whole truth without the slightest omission, it had won support from across the world.

Pure goodwill.

Nothing could stand against the hammer the World Hunter Federation had brought down. A president of a nation, the head of a massive corporation that could sway the world’s stock markets—every one of them had fallen, bleeding.

Half a century ago, after Osama bin Laden’s terrorist attack, Pakistan and the Middle Eastern countries that had refused to let the United States fly through their airspace would not dare oppose this action either.

They couldn’t do something as insane as making enemies of the World Hunter Federation—and the entire world.

They’d be met with countless artillery shells and a visit from countless Hunters.

But unlike those who could choose compromise, the people gathered in this cave hadn’t been given even the slightest choice.

“Prophet!”

“Please, please show us the way we must go!”

Desperate cries rang out from every corner.

Armed with fanaticism, they all knelt and prostrated themselves before one person alone.

They were afraid of the enemy closing in, but at the same time, their faith in the path they’d walked until now was unshaken.

They had devoted their lives to God and followed the prophet He had sent.

They had witnessed the Prophet’s astounding miracles.

“Teach these lost servants!”

“Defeat these infidels and proclaim God’s will to the whole world!”

*Fwoosh. Fwoosh.*

The torches lighting the cave flickered in the wind. From beneath the deeply drawn hood of a robe, the Prophet’s voice rang out—impossible to place by age or gender.

“As you wish, I shall carry out God’s will and punish them. Inshallah.”

“O-oh…!”

“God is great!”

“Inshallah. Inshallah!”

The anxiety that had threatened to burst turned to cheers. As the Prophet watched them repeatedly bow and cry out about God’s greatness, they thought:

Their long wait would soon bear fruit.
```
