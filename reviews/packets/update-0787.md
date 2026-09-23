<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0787.txt",
      "sha256": "9473fffd18d34f0da598b905d17a8ef6bb8e4aa437b26ee13e8b3152001a5814",
      "bytes": 16602
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ed35852fef6ee14bfbc160def58af9f3b2083ed944b7cd596338c7a61e32763f",
      "bytes": 845
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "47349c578ce3a378dc53173dec4002c0828b8095d08eadab83cdfaafdabfc433",
      "bytes": 223666
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "be253f75eb53c671a452fc3b1fadaf92afb654044052425ffe6452a6d59f7777",
      "bytes": 553
    },
    {
      "path": "characters/Felix.md",
      "sha256": "3122316685abd4a2f6d8e16d7a3acb6fa5c82b1e28c0bc20b87c7a6444353a6f",
      "bytes": 464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bdd962856af38620a3b58edda2d6a516cb359740537473602e928fdd545c7423",
      "bytes": 2112
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ee0c5ffa605342a4350269df24e195d80789182025957a64717d571587f68549",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "c57bd206060f3622c2b78fb63eb9a572dbbbb509aef97af1b93657f2ffae0f5a",
      "bytes": 820
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "58736b3b9890709acf99d2a7df88eb0e03aa5b58dacc65ac63d318d4e5de364e",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "19217df2fb1c9d82edef7910e7e76577ea1cc92ccaac707e1a08562d78b4e35e",
      "bytes": 243802
    }
  ],
  "estimated_tokens": 11625
}
-->

# Durable State Update — Chapter 787

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 787. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 787. Profile updates may replace only one
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
  "chapter": 787,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 787,
    "continuity_sources": [787],
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
    "The Skeleton King accepts his identity as both monster and companion to humans; he shares his first name in this world only with Jin Taekyung.",
    "Michael Silbert was executed by Jin after the World Hunter Federation’s first resolution.",
    "Huginn was captured alive; the rest of Michael’s forces were killed or captured.",
    "The World Hunter Federation has been established, with its first resolution carried out against Michael.",
    "Jin recognizes that Michael’s defeat does not eliminate the deeper roots of his plans."
  ],
  "continuity_sources": [
    786
  ],
  "open_questions": [
    "What deeper roots of Michael’s plans remain, and how will Jin address them?"
  ],
  "safe_through": 786,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 제자     | **Disciple**                                 |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 보상               | **Reward**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 불굴 | **Indomitable** | Temporary special effect manifested by Jin's strong will. |
| 골골 | **Golgoli** | Jin's nickname for the Skeleton King. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 골골 | captor_to_subordinate_undead | Bones | mocking-casual | Jin uses the mocking nickname while treating the Skeleton Warlord like a pet. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 골골 | 진태경 | subordinate_undead_to_captor_and_master | human | mocking, reluctant, and familiar | Calls Jin 인간 and 간악한 인간 while complaining about being deceived into searching Area A. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 필릭스 | 존슨 | prince_to_allied_grand_mage | Mr. Johnson | formal-polite | Felix uses a respectful address while speaking with Magic Johnson. |
| 최민우 | 필릭스 | allied_operations_lead_to_prince | Your Highness | polite-formal | Choi greets Felix during the secret meeting. |
| 최민우 | 존슨 | allied Hunter to allied Grand Mage | Mr. Johnson | formal-polite | Minwoo calls out to Johnson during the battle. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 786
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 786
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 786
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the Hunter who exposed Michael Silbert's ability to absorb monsters' magical power.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 786
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 786
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 785
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, and the maternal grandson of Cheon Taemin.

## Korean source

```text
＃787화



“아.”

진태경은 외마디 탄성을 토해 냈다.

지금 이 순간. 그는 자신에게 찾아온 이능(異能)의 축복을 고스란히 느끼고 있었다.

귓가에는 오직 한 사람만이 들을 수 있는 맑은 종소리가 끊임없이 울려 퍼졌고, 폐허 위로 솟아오른 무수한 홀로그램 창이 눈 앞을 가렸다.

띠링. 띠링. 띠링.



― [Lv.175 미카엘 실베르트]를 처치했습니다!

― 막대한 경험치와 명성을 획득했습니다!

― 희귀한 업적, [참초제근(慘草除根)]을 달성하셨습니다!

― 모두가 함께 살아가는 숲을 위해 병든 풀을 베고, 그 뿌리를 뽑은 당신의 과감한 결단에 아낌없는 찬사를 보냅니다.

― 그러나 명심하십시오. 숲을 집어삼킬 거대한 화염은 그 어떤 병균보다 위협적이라는 사실을.

― 업적 달성 보상으로 막대한 경험치와 명성을 획득했습니다!

― 특별 추가 보상으로 20포인트를 획득했습니다!

― 레벨 업!

― 레벨 업!

― 레벨 업의 중첩 효과로 대부분의 부상 및 체력이 회복됩니다!

― 특수 디버프, [부서진 신체]가 치유의 힘을 거부합니다!

.

.

.

눈과 귀를 점령한 무수한 알림들.

그와 동시에 다른 이들은 볼 수도, 느낄 수도 없는 따스한 광휘가 진태경의 몸속 깊숙한 곳에서 샘솟았다.

화악.

치유를 넘어 정화(淨化)라 부르기에 조금의 부족함도 없는 기운이 소나기처럼 전신을 씻어 내려간다.

자연스럽게 쌓인 몸 안의 노폐물과 망가진 혈관, 장기, 부서지고 베여 나간 뼈와 피부를 감싸 안으며.

솨아아아.

몸 곳곳에서 전해지던 격통이 빠르게 가라앉는다.

머리부터 발끝까지 뒤덮은 끈적한 핏물들 아래로, 사람들이 미처 보지 못하는 상처가 씻은 듯이 아물었다.

그러나 진태경에게 있어 이 모든 것들은 아무것도 아니었다.

지금 이 순간 그가 느끼고 있는 안도감에 비하면.

‘끝이다.’

진태경은 참았던 숨을 토해 냈다.

눈을 부릅뜬 채 숨이 끊긴 미카엘 실베르트에게서는 더 이상 어떤 생명의 기운도 느껴지지 않았다.

틀림없다.

놈은 확실히 죽었다.

지금까지 상대한 그 어떤 적보다 교활하고, 그의 마음을 뒤흔들었던 간웅(奸雄)은 인간으로 태어나 괴물의 모습으로 이 세상을 떠났다.

아니, 어쩌면 지금쯤 놈의 영혼은 저 부릅뜬 눈동자에 담긴 심연(深淵)으로 굴러떨어졌을지도 모른다.

서늘한 창날이 목젖을 파고들던 그 순간, 진태경이 건넨 마지막 인사처럼.

“……지옥으로 꺼져라.”

씹어뱉듯 토해 낸 한 마디와 함께 진태경이 창대를 쥐었다. 그리고 힘주어 비틀 듯 괴물의 목을 갈랐다.

촤악. 철벅.

솟구치는 녹색 핏줄기와 함께 몸뚱어리에서 완전히 분리된 미카엘 실베르트의 목이 피 웅덩이 위를 굴렀다.

동시에 약속이라도 한 것처럼 거대한 굉음이 터져 나왔다. 아니, 그것은 굉음인 동시에 함성이었다.

쿵! 쿵쿵쿵!

드드드득!

살아남은 수백여 명의 헌터들은 너 나 할 것 없이 포효를 내질렀다.

마나가 실린 함성에 압축된 공기가 터져 나갔고, 쉼 없이 지면을 두드리는 발과 병장기에 국회 의사당이 뒤흔들렸다.

누군가는 순수하게 기뻐했고, 누군가는 채 가시지 않은 분노로 치를 떨었으며, 그런 그들의 모습을 멍하니 바라보던 또 다른 누군가는 눈물을 흘렸다.

모든 것을 끝낸 창 한 자루를 힘없이 늘어트린 채로.

“……씨발.”

이게 뭐라고. 이깟 게 도대체 뭐라고.

진태경 스스로도 그 이유를 잘 몰랐다.

왜 갑자기 욕이 튀어나왔는지. 모두가 기뻐하고 있을 때, 왜 자신은 병신처럼 울고 있는지.

하지만 다음 순간 귓가에 닿은 누군가의 목소리가 그를 대신하여 정답을 알려주었다.

“네놈이 지금 어떤 머저리 같은 생각을 하고 있는지는 모르겠지만, 이것 하나만 말해 주마.”

스켈레톤 킹이 진태경의 어깨를 짚으며 말을 이었다.

“사람들이 죽은 건 네 잘못이 아니다. 이 몸의 의지와는 상관없이 몬스터가 되었듯이.

“……!”

“그러니 병신처럼 질질 짜는 것은 그만둬라. 누구도 너를 비난하거나 탓하지 않으니까.”

까칠하지만 따뜻한 그 말에 진태경은 침묵했다.

그리고 끊임없이 울려 퍼지는 함성과 진동 속에서 문득 실소를 흘렸다.

“야.”

“으흠. 불렀느냐.”

“왜 갑자기 무게를 잡고 난리야, 몬스터 새끼가.”

“……!”

“뭘 봐. 눈 착하게 안 떠?”

안 그런 척하면서도 은근히 대답을 기대하고 있던 스켈레톤 킹이 충격받은 얼굴로 중얼거렸다.

“이게 진정 사람의 인성이란 말인가……?”

“다 들린다.”

“들으라고 한 소리다.”

“몬스터가…… 말대꾸?”

“아, 그만하라고!”

스켈레톤 킹을. 아니, 친구를 놀리는 건 언제나 즐거운 일이다.

발작하는 스켈레톤 킹의 모습에 진태경은 낄낄거리며 웃었다. 피에 젖은 소매로 눈물까지 닦아 가면서.

“그러면서 은근슬쩍 눈물 닦지 마라. 이미 늦었으니까.”

“……이 새끼 허위 사실 유포하네. 내가 언제. 증거 있어?”

“증거는 없어도 증인은 있지. 이 몸 말고도 본 사람이 수두룩, 어?”

덥석.

순간 휘청거리는 진태경의 팔을 붙잡은 스켈레톤 킹이 눈을 동그랗게 떴다.

“너…….”

“아. 핏물 때문에 바닥이 미끄러워서.”

진태경이 씩 웃으며 대답했다. 하지만 파르르 떨리는 입꼬리와 반쯤 감긴 눈동자에 담겨 있는 극심한 피로만큼은 숨길 수 없었다.

당연한 일이었다.

두 번의 레벨 업 효과는 그가 입은 대부분의 상처를 회복시켜 주었지만, 지금 이 순간에 이르기까지 있었던 수많은 사건과 정신적 피로는 고작 이십 대에 불과한 청년이 홀로 감당할 수 있는 것이 아니었으니까.

미카엘 실베르트의 추악한 실체와 야망을 깨달은 그 날부터 시작된 불면(不眠)의 밤과 숱한 전투들.

지난 몇 주간 진태경은 밤낮을 가리지 않고 싸워야 했다.

그리고 그가 쓰러트려야 했던 적은 미카엘 실베르트와 헤아릴 수 없이 많은 몬스터 군단뿐만이 아니었다.

나날이 거세지는 세상의 극심한 비난. 뉴스를 통해 전해 들었던 전 세계 곳곳의 재앙들과 그들의 죽음 앞에 무력했던 스스로에 대한 자괴감까지.

진태경은 자기 자신과 싸웠고, 이 세상과 싸웠다.

마침내 미카엘 실베르트를 꺾은 지금. 그저 제자리에 서 있는 것만으로도 초인적인 인내심을 발휘해야 할 만큼.

하지만…….

‘안 돼.’

진태경은 자꾸만 감겨 오는 눈꺼풀을 애써 들어 올렸다.

지금은 아니다. 조금만, 조금만 더 버텨야 했다.

자신이 시작한 것을 끝맺을 때까지.

어느샌가 사람들의 함성에 뒤섞여 들려오기 시작한 저 사이렌 소리가 더 가까워지고, 오늘 이 자리에서 있었던 모든 진실을 세상에 밝히기까지 쓰러질 수 없었다.

‘절대로.’

푹.

지면에 박아 넣은 창을 지팡이 삼아 몸을 기댄 진태경이, 꺼질 듯한 목소리로 중얼거렸다.

“조온나게 고맙다. 황 조교 이 씹새끼야…….”

“너 정말 괜찮은 거 맞……. 그런데 지금 뭐라고?”

“야, 골골아.”

“어?”

“너도 창 써라. 검 쓰지 말고.”

아니, 갑자기?

도무지 상황을 받아들이지 못한 스켈레톤 킹이 눈을 껌뻑거렸다.

“왜?”

“검보다…….”

“검보다.”

“창이…….”

“창이.”

“멋있어.”

“멋있……. 시팔.”

스켈레톤 킹은 탄식했다.

도대체 저 인간 같지도 않은 새끼의 말을 왜 귀 기울여 들었단 말인가.

어차피 하는 말이라고는 개소리가 절반이고 나머지 반은 자신을 갈구는 쌍욕일 텐데.

‘내가 병신이지.’

하지만 스켈레톤 킹은 아무 말 없이 한숨만 푹 내쉬었다.

지면 깊숙이 박아 넣은 창 한 자루에 몸을 기댄 채, 마치 기절하듯 깊은 잠에 빠져 버린 친구를 깨우고 싶지 않았기 때문이었다.

‘고생했다. 쉬어라.’

아마도 모두가 같은 마음이었을 것이다.

도대체 언제 함성을 내질렀냐는 듯, 약속이라도 한 것처럼 굳게 입을 다문 수백여 명의 헌터들은 그저 말없이 바라보았다.

오늘 이 자리의 누구보다 용감하고 빛났던 청년을.

한 치 앞도 보이지 않는 어두컴컴한 진실 속에서, 온 세상과 맞서 싸우며 묵묵히 자신이 가야 할 길로 나아간 초인을.

‘만약 나였다면 그처럼 할 수 있었을까.’

모두가 스스로에게 묻고, 이내 답했다.

이 자리의 누구도 그럴 수 없었을 것이라고.

넘어지고, 긁히고, 깨지고, 부서지다가 마침내 쓰러져 두 번 다시 일어나지 못했을 것이라고.

그러나 고작 이십 대에 불과한 저 청년은, 진태경은 그것을 해냈다.

수없이 넘어져도 일어났고, 깨지고 부서질지언정 쓰러지지 않았다.

오직 그만이 어둠 속에서 헤매던 이들에게 이정표이자 길을 밝히는 등불이 되어 주었다.

가장 앞에서 모두를 이끄는 자.

상처 입은 이들을 보며 함께 아파하나 결코 나약하지 않으며, 꺾이지 않는 불굴(不屈)의 의지로 용맹하게 나아가는 자.

그리고 사람들은 바로 그런 이를 이 세상의 모든 경의와 사랑을 담아 이렇게 칭한다.

‘영웅(英雄).’

그 짧은 한 단어가 뇌리에 가득 찬 순간.

이 자리의 모두는 형용할 수 없는 감정에 사로잡혔다.

영웅. 더없이 익숙한 단어다.

어느 날부터 온 세상이 그들을 영웅이라 불러 주었으니까. 평소와 다를 것 없던 어느 날 예기치 못한 힘을 얻었고, 몬스터와 싸우며 인류의 검과 방패가 되었으니까.

하지만 어째서일까.

귀에 못이 박히도록 들었던 그 단어에 이토록 가슴이 벅차오르는 이유는.

지난날의 모든 순간이 부끄러우면서도 먹먹해지는 까닭은.

다만…… 계속해서 눈앞에 떠올랐다.

수백 개의 무기에 둘러싸인 상황에서도 두려움 없이 진실을 외치던 그 눈빛이.

치열했던 전투가 막을 내리고 모두가 환호할 때, 홀로 하염없이 눈물 흘리던 한 청년의 모습이.

아마도 그런 이유에서였을 것이다.

어느샌가 처참한 폐허가 되어 버린 국회 의사당 내부로 진입한 수많은 지원 병력이 자신들도 모르게 발걸음을 멈추고 숨을 죽인 것은.

그리고 바늘 하나 떨어지는 소리도 들릴 것 같은 고요함 속, 누군가가 참았던 숨을 토해 낸 것은.

“Fuck.”

갑작스럽게 깨진 침묵에 고개를 돌린 사람들은 세 번 놀랐다.

욕을 저렇게 고풍스러운 어조로 할 수 있다는 것에 한 번.

욕이 이토록 어색할 수 있다는 것에 또 한 번.

그리고 이 어려운 일을 동시에 해낸 사람이, 전혀 생각지도 못한 인물이었다는 것에 마지막으로 한 번.

하지만 당사자인 필릭스 왕자는 자신을 향해 모여든 사람들의 시선에도 아랑곳하지 않았다.

아니, 이제 아무래도 상관없었다.

“Fuck. Fuck. Fuck.”

후련하다.

아직 어설프기 짝이 없는 발음이었지만, 연달아 욕을 뱉고 나니 가슴에 응어리진 무언가가 풀어지는 듯했다.

필릭스 왕자는 자신도 모르게 킥킥대며 웃었다.

‘빌어먹을. 그까짓 게 전부 뭐라고.’

혈통. 품위. 체면. 예법.

그가 삼십 년이 넘는 세월 동안 자랑스럽게 여겼던 모든 가치가 덧없고, 무겁게만 느껴졌다.

지금 당장이라도 훌훌 벗어던져 버리고 싶을 만큼.

그래서 그렇게 했다.

부둣가의 노동자처럼 난생처음 상스러운 욕을 지껄이고, 왕가(王家)의 문장이 아로새겨진 갑옷도 벗어 던졌다.

과연 아버지인 국왕 폐하께서 이 광경을 보셨다면 어떤 표정을 지었을까 하는 생각이 문득 들었지만, 뭐.

‘그게 그렇게 중요한가.’

저벅. 저벅.

사람들의 시선 속, 폐허가 되어 버린 공간을 천천히 가로지른 필릭스 왕자는 걸음을 멈췄다.

그리고 불쑥 입을 열었다.

“손이 부족해 보이는데, 실례가 안 된다면 내가 도울 수 있겠나?”

그 어느 때보다 정중한 필릭스 왕자의 제안에, 창대에 기댄 채 쓰러지듯 잠이 들어 버린 진태경을 부축하고 있던 스켈레톤 킹이 고개를 끄덕였다.

“원한다면 그렇게 해라, 인간 왕자.”

그리고 곧이어 들려온 필릭스 왕자의 대답은, 곁에서 그들을 지켜보던 모두를 놀라게 하기에 충분했다.

“부디 필릭스라고 불러 주게, 미스터 킹. 내 친구여.”

“……!”

자신을 멍하니 바라보는 사람들의 시선에 희미하게 웃어 보인 필릭스 왕자가 진태경의 한쪽 어깨를 부축한 그때, 또 다른 손이 뻗어 나와 그를 도왔다.

“그대는…….”

“옆에서 보고 있자니, 지금도 손이 부족해 보여서 말입니다.”

담담하게 대답한 최민우에 이어 또 다른 손들이 더해졌다.

덜덜 떨리는 손은 이미 금단 현상에 접어든 척 헤이글의 것이었고, 유난히 굳은살이 많고 자그마한 손은 파이 첸의 것이었다.

그리고 매직 존슨은, 손에 든 스태프를 물끄러미 바라보다 문득 씩 웃어 보였다.

“종종 내가 익힌 모든 것들이 쓸모없게 느껴질 때가 있지. 바로 지금처럼.”

스태프를 품에 집어넣은 매직 존슨이 성큼성큼 걸어와 손을 보탰다.

언뜻 보면 이해할 수 없는 일이었다.

수백 개가 넘는 마법을 익힌 대마도사가, 수 톤에 달하는 콘크리트 더미를 단숨에 베어 버릴 수 있는 최고의 헌터들이 한 청년을 들어 올리기 위해 모여 있었으니까.

하지만 그것이야말로 그들이 진심으로 경의를 표하는 방식이었다.

슥. 스륵.

옷깃 스치는 소리만이 조용히 울려 퍼졌다. 어느새 수백 개로 불어난 손길이 호수 속 작은 물결이 되어, 깊은 잠에 빠진 젊은 영웅을 자신들의 머리 위로 천천히 움직였다.

유리를 다루는 것처럼 조심스럽게.

잠시나마 그에게 찾아온 평온이 깨지지 않도록.

그리고 마침내 진태경의 신형을 지면에 기대어 눕혔을 때, 사람들은 불현듯 깨달았다.

인류의 역사에 기록될 신(新) 세계 헌터 연맹의 발족식은 아직 끝나지 않았다는 사실을.

자신들의 눈앞에 있는 이 청년이야말로, 이후 벌어질 대전쟁의 시작과 끝이 되리라는 것을.

스릉.

적막을 가르며 울려 퍼지는 서늘한 마찰음.

그와 동시에 천천히 뽑혀 나온 검이 허공을 겨누었다.

이내 수십, 수백으로 불어난 무수한 병장기가 산산조각 난 스테인드 글라스(Stained glass) 사이로 흘러나온 석양을 받아 번뜩였다.

화염처럼 불그스름한 온기에 물든 폐허 속, 누구도 깨트릴 수 없는 평안에 젖어 있는 한 청년을 향해.

아니.

그들의 새로운 맹주(盟主)를 향해.

띠링. 띠링. 띠링.



― 믿을 수 없는 업적, [오직 한 사람을 위한 대관식]을 달성하셨습니다!

― [세계 헌터 연맹]이 당신을 [맹주]로 추대합니다!

― 막대한 경험치와 명성을 획득했습니다!

.

.

.

오직 한 사람만이 들을 수 있는 그 종소리는 어느 때보다 크고, 맑게 울려 퍼졌다.

깊은 잠에 빠진 누군가의 입가에 미소가 스칠 만큼.

여전히 그의 마음 한구석에 남아 있는 죄책감을 녹여 낼 만큼.

그렇게 길고도 치열했던 하루 끝에, 새로운 역사의 한 페이지가 넘어가고 있었다.
```

## Final English reading copy

```markdown
# Chapter 787

“Ah.”

Jin Taekyung let out a single exclamation.

At that very moment, he could feel the full blessing of the supernatural power that had come to him.

Clear chimes, audible to him alone, rang incessantly in his ears, while countless holographic windows rose above the ruins and filled his vision.

*Ding. Ding. Ding.*

> **System**
> You have defeated Lv. 175 Michael Silbert!
> You have gained a tremendous amount of EXP and Fame!
> You have achieved the rare feat Cut the Weeds and Pull Up the Roots!
> We offer our unreserved praise for your bold decision to cut down the diseased grass and pull out its roots, for the sake of the forest where everyone lives together.
> But remember: the great fire that could consume the forest is more dangerous than any disease.
> You have gained a tremendous amount of EXP and Fame as a reward for your achievement!
> You have gained 20 points as a special bonus reward!
> Level Up!
> Level Up!
> Most of your injuries and Stamina have been restored by the stacked effects of leveling up!
> The special debuff Broken Body rejects the power of healing!

…

…

…

Countless notifications filled his eyes and ears.

At the same time, a warm radiance no one else could see or feel welled up from deep inside Jin Taekyung.

*Whoosh.*

An energy that could only be called purification, not merely healing, washed over his entire body like a downpour.

It embraced the waste that had naturally built up inside him, his damaged blood vessels and organs, and his broken and slashed bones and skin.

*Shhhhh.*

The excruciating pain that had been coming from every part of his body quickly faded.

Beneath the sticky blood covering him from head to toe, the injuries no one had noticed healed as if they’d never been there.

But none of that mattered to Jin Taekyung.

Not compared to the relief he felt at that moment.

*It’s over.*

Jin Taekyung let out the breath he’d been holding.

No trace of life remained in Michael Silbert, whose eyes were wide open even as he lay dead.

There was no doubt.

The bastard was dead for sure.

The scheming mastermind, more cunning than any enemy Jin had ever faced, the man who had shaken him to his core, had been born human and left this world in the form of a monster.

No—or perhaps, by now, his soul had fallen into the abyss held in those wide-open eyes.

Just like Jin’s final farewell to him, in the moment the cold spearhead pierced his throat.

“……Go to hell.”

With that one line, spat out between clenched teeth, Jin Taekyung gripped the spear shaft. Then he twisted it with all his strength, slicing through the monster’s neck.

*Slash. Splash.*

Along with a jet of green blood, Michael Silbert’s head came completely free of his body and rolled across the pool of blood.

At the same moment, as if on cue, a tremendous roar erupted. No—it was both a roar and a cheer.

*Boom! Boom-boom-boom!*

*Rumble!*

The hundreds of surviving Hunters roared as one.

Their mana-charged shouts burst through the compressed air, while the feet and weapons pounding the ground without pause shook the National Assembly building.

Some were simply overjoyed. Others trembled with anger that had yet to fade. And still others, staring blankly at them, began to cry.

Jin Taekyung let the spear that had ended it all hang limply at his side.

“……Fuck.”

Why was this such a big deal? Why did this little thing matter so damn much?

Even Jin Taekyung didn’t know.

Why had the curse suddenly slipped out? Why was he crying like an idiot while everyone else was celebrating?

But the voice that reached his ears a moment later supplied the answer for him.

“I don’t know what kind of stupid thought you’re having right now, but I’ll tell you one thing.”

The Skeleton King rested a hand on Jin Taekyung’s shoulder and continued.

“It isn’t your fault that people died. Just as this body became a monster against its own will.”

“……!”

“So stop bawling like an idiot. No one is blaming you or holding you responsible.”

At those prickly but warm words, Jin Taekyung fell silent.

Then, amid the endless cheering and rumbling, he suddenly let out a wry chuckle.

“Hey.”

“Hmm? Did you call?”

“Why are you suddenly acting all serious, you monster bastard?”

“……!”

“What are you looking at? Keep your eyes nice and polite.”

The Skeleton King had been quietly hoping for a response, though he’d tried not to show it. Now, he muttered with a stunned look on his face.

“Is this what human nature is really like……?”

“I can hear you.”

“I meant you to.”

“A monster……talking back?”

“Ah, enough already!”

Teasing the Skeleton King. No, teasing his friend was always fun.

At the Skeleton King’s fit of outrage, Jin Taekyung chuckled and laughed, even wiping away his tears with his blood-soaked sleeve.

“And don’t try to sneakily wipe your tears. It’s too late for that.”

“……You’re spreading false rumors, you bastard. When did I do that? Got proof?”

“No proof, but I’ve got witnesses. Plenty of people saw it besides me—huh?”

*Grab.*

The Skeleton King’s eyes widened as Jin Taekyung suddenly staggered and he caught him by the arm.

“You……”

“Ah. The floor’s slippery with blood.”

Jin Taekyung answered with a grin. But he couldn’t hide his quivering lips or the exhaustion in his half-closed eyes.

It was only natural.

The effects of leveling up twice had healed most of his injuries. But all the events that had led to this moment, along with the mental strain, were more than a young man barely in his twenties could bear on his own.

The sleepless nights and countless battles had begun the day he learned the truth about Michael Silbert’s hideous nature and ambitions.

For the past few weeks, Jin Taekyung had fought day and night.

And Michael Silbert and the countless monster hordes weren’t the only enemies he’d had to bring down.

There was the world’s harsh, ever-growing condemnation. There were the disasters he’d heard about from every corner of the world on the news, and his own self-loathing at being powerless in the face of all those deaths.

Jin Taekyung had fought himself, and he had fought the world.

Now that he’d finally defeated Michael Silbert, even standing still demanded superhuman patience.

But……

*I can’t.*

Jin Taekyung struggled to lift his eyelids as they kept drooping shut.

Not yet. He had to hold on a little longer. Just a little longer.

Until he finished what he’d started.

The sirens, now mingling with the people’s cheers, were getting closer. He couldn’t collapse before he told the world the whole truth about what had happened here today.

*No matter what.*

*Thump.*

Using the spear he’d driven into the ground as a cane, Jin Taekyung leaned against it and murmured in a voice that seemed about to fade away.

“Thanks so fucking much, Assistant Hwang, you son of a bitch……”

“Are you really okay……? Wait, what did you just say?”

“Hey, Golgoli.”

“Huh?”

“You should use a spear too. Not a sword.”

What? Out of nowhere?

The Skeleton King blinked, utterly unable to process the situation.

“Why?”

“Compared to a sword……”

“Compared to a sword.”

“A spear……”

“A spear.”

“Looks cooler.”

“Looks coo……Fuck.”

The Skeleton King sighed.

Why had he ever listened to that human bastard who wasn’t even human?

Half the time he spouted nonsense, and the other half he chewed him out with profanity.

*I’m the idiot.*

But the Skeleton King said nothing. He only sighed.

He didn’t want to wake his friend, who had fallen into a deep sleep as if he’d passed out, leaning against the spear driven deep into the ground.

*You’ve worked hard. Rest.*

Perhaps everyone felt the same way.

As if they’d never cheered at all, the hundreds of Hunters pressed their lips together in silence and simply looked on.

At the young man who had been braver and brighter than anyone else here today.

At the superhuman who had faced the whole world and steadily walked the path he had to follow, in the darkness of a truth where he couldn’t see even an inch ahead.

*If it were me, could I have done what he did?*

Everyone asked themselves, then arrived at the same answer.

No one here could have done it.

They would have fallen, scraped themselves raw, shattered and broken, then finally gone down and never risen again.

But that young man, barely in his twenties—that Jin Taekyung—had done it.

No matter how many times he fell, he got back up. No matter how badly he was battered and broken, he refused to go down.

He alone had become a signpost and a beacon, lighting the way for those who had been lost in the darkness.

The one who led everyone from the front.

The one who felt the pain of the wounded alongside them, but was never weak—and pressed bravely onward with an unbreakable will.

And that was what people called such a person, with all the reverence and love in the world:

*Hero.*

The moment that short word filled their minds, everyone there was seized by an indescribable emotion.

Hero. It was a word they knew all too well.

At some point, the whole world had begun calling them heroes. One ordinary day, they’d gained unexpected powers, fought monsters, and become humanity’s sword and shield.

But why?

Why did that word, heard so often it had nearly worn grooves in their ears, make their hearts swell like this?

Why did every moment of the past feel both shameful and achingly poignant?

All they could see, over and over, was the look in his eyes as he shouted the truth without fear, surrounded by hundreds of weapons.

And the sight of a young man weeping alone, while everyone cheered at the end of the fierce battle.

That was probably why the many reinforcements entering the National Assembly, now a ruin, stopped in their tracks without realizing it and held their breath.

And why, in a silence so deep it seemed you could hear a needle drop, someone let out the breath they’d been holding.

“Fuck.”

People turned their heads at the sudden break in the silence and were surprised three times.

First, that anyone could curse in such a refined manner.

Second, that a curse could sound so awkward.

And finally, that the person who’d managed both at once was someone they’d never expected.

But Prince Felix himself paid no attention to the eyes gathering on him.

No—he didn’t care anymore.

“Fuck. Fuck. Fuck.”

It was a relief.

His pronunciation was still far from perfect, but after spitting out one curse after another, it felt as though something knotted in his chest had loosened.

Prince Felix found himself chuckling.

*Damn it. What was so important about all that?*

Bloodline. Dignity. Appearances. Etiquette.

Every value he’d proudly held onto for more than thirty years felt empty and burdensome.

So much so that he wanted to cast them all off right then and there.

So that was what he did.

For the first time in his life, he let loose a filthy curse like a dockworker and threw off the armor engraved with the royal crest.

For a moment, he wondered what expression His Majesty the King—his father—would have worn if he’d seen him like this. But, well.

*Was that really so important?*

*Clop. Clop.*

Under the gaze of the people, Prince Felix slowly crossed the ruined space and stopped.

Then he spoke without preamble.

“It looks as though you could use another pair of hands. If you don’t mind, may I help?”

At Prince Felix’s most courteous offer yet, the Skeleton King nodded. He was supporting Jin Taekyung, who had collapsed into sleep against the spear shaft.

“If you wish, then do so, human prince.”

And Prince Felix’s response was enough to astonish everyone watching them from nearby.

“Please call me Felix, Mr. King. My friend.”

“……!”

Prince Felix smiled faintly at the people staring blankly at him. Just as he took one side of Jin Taekyung’s shoulder, another hand reached out to help.

“You……”

“Watching from the side, it seemed you could use another pair of hands.”

Choi Minwoo answered calmly, and more hands joined in.

One trembling hand belonged to Chuck Hagel, who was already acting as if he were going through withdrawal. The unusually small, heavily callused hand belonged to Faye Chen.

As for Magic Johnson, he stared at the staff in his hand for a moment, then suddenly grinned.

“Sometimes I feel like everything I’ve learned is useless. Like right now.”

Magic Johnson tucked the staff away and strode over to lend a hand.

At first glance, it was hard to understand.

A Grand Mage who had mastered hundreds of spells, and the finest Hunters, capable of slicing through tons of concrete in an instant, had all gathered to lift one young man.

But that was how they truly showed their respect.

*Rustle. Rustle.*

The only sounds were the quiet brushing of clothes. The helping hands had multiplied until there were hundreds, sending ripples across a lake as they slowly lifted the sleeping young hero above their heads.

As carefully as if he were made of glass.

So that the peace that had come to him, if only for a little while, wouldn’t be disturbed.

And when at last they laid Jin Taekyung down against the ground, everyone suddenly realized:

The inaugural ceremony of the New World Hunter Federation, which would be recorded in the history of humanity, was not over yet.

That the young man before them would be both the beginning and the end of the Great War to come.

*Shing.*

A cold scrape cut through the silence.

At the same time, a sword slowly slid free and pointed toward the sky.

Soon, countless weapons—dozens, then hundreds—glinted in the sunset streaming through the shattered stained glass.

In the ruins, steeped in the reddish warmth of flames, they were turned toward the young man immersed in an unbreakable peace.

No.

Toward their new Alliance Leader.

*Ding. Ding. Ding.*

> **System**
> You have achieved the unbelievable feat A Coronation for One Person Alone!
> The World Hunter Federation appoints you as its Alliance Leader!
> You have gained a tremendous amount of EXP and Fame!
>
> …

…

…

The chimes, audible to just one person, rang clearer and louder than ever.

Loud enough for a smile to brush the lips of someone deep in sleep.

Loud enough to melt the guilt still lingering in a corner of his heart.

And so, at the end of a long and fierce day, a new page of history was turning.
```
