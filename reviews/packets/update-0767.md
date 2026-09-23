<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0767.txt",
      "sha256": "841137c1f48259c8e5a593e9f5b0da7ed1d0ffa6262ed45cd6cb535eb88f8542",
      "bytes": 14718
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4d8c05d52220b62414728863f35e0f7d634cd3c24c519deb8ec9d73ba73aff44",
      "bytes": 1866
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91d7835d1b084fd8ea57013f34b2233f8c1857d3412658bb203f956986c3e1d3",
      "bytes": 221498
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "01d8ea207aa68935def1a8b0b55c1e4dcdc7a298234364c116603f01707e8b03",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "2cacdc733f8679209ca0a913dccf1189f5dde5da7d3151bf5035bfc4b614a35d",
      "bytes": 817
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3229021d56dd39d07c195b777a7de3a763d74c65488ac5f8b991fae00b223efe",
      "bytes": 2017
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e22094b6b3e61f1dc84cba4274e01feb1b4ccaaece3a461b18e5a44b9c6dd6e9",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "a0e43c523ebdc702b05d9772b86a5da09ac9c43cfa475f80285cf46d7d0e5a21",
      "bytes": 666
    },
    {
      "path": "characters/Michael.md",
      "sha256": "6e785b88d69c053f19b6a641ddc97464637d56373aec83a7221c219f5060f47c",
      "bytes": 1219
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "211a41e4104712a537e61374988b20e4b93131e8466a2c2183704d42ea7225ef",
      "bytes": 405
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "34fbfe60df1915cf2cb8d821369e632c3c7c3c0e1d10e88e3a4257e1f03bf7c0",
      "bytes": 238102
    }
  ],
  "estimated_tokens": 11747
}
-->

# Durable State Update — Chapter 767

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 767. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 767. Profile updates may replace only one
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
  "chapter": 767,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 767,
    "continuity_sources": [767],
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
    "Michael intends to establish the World Hunter Federation and become its Alliance Leader through a staged succession involving Cheon Taemin and Jin.",
    "Michael knows the Skeleton King's identity and can use Jin's attachments and concern for his people as leverage.",
    "Jin regards Michael as a power-hungry monster and refuses to accept his proposal or offered alliance.",
    "Jin recognizes that killing Michael immediately would endanger the people Jin has accumulated and protects.",
    "Michael regards Jin as the greatest obstacle to his path toward dominion after Cheon Taemin.",
    "Michael plans to complete the current succession operation within days and believes Jin will cooperate.",
    "Huginn doubts Michael's decision to release Jin and fears an irreversible mistake.",
    "Jin has briefed Team Leader Choi and the Skeleton King on Michael's leverage.",
    "The Skeleton King has been injured by Jin for joking about losing access to clubs.",
    "An unidentified visitor has arrived at the suite."
  ],
  "continuity_sources": [
    766
  ],
  "open_questions": [
    "Will Jin submit to Michael's coercion or find a way to protect his people while opposing him?",
    "Who is the visitor who arrives at the suite?",
    "What action will Michael take against Jin after identifying him as a major obstacle?",
    "Can Michael complete his staged succession and seize the World Hunter Federation within days?",
    "Will Huginn's fear that releasing Jin was an irreversible mistake prove justified?"
  ],
  "safe_through": 766,
  "temporary_decisions": [
    "Render 맹주 as Alliance Leader.",
    "Render 추대 as elevation to power in this political context.",
    "Render 친위대 as personal guards.",
    "Keep Michael's 자네 address to Jin familiar, polite, and coercive."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 뮌헨 | **Munich** | Second word in one of the necromantic chants. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 도쿄 | **Tokyo** | City visible behind Huginn's departing ship. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 도쿄만 | **Tokyo Bay** | Port area where Sugihara Gyoiku works. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |
| 시몬 | **Simon** | Reporter working under the news director. |
| 독일 | **Germany** | Country requesting assistance with the Berlin Monster Wave. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 진태경 | 레비아탄 | enemy and hunted monster | Leviathan; you | insulting-casual | Jin orders Leviathan to leave and dismisses its attempt to kill the Skeleton King. |
| 레비아탄 | 진태경 | attacking enemy | you bastard | enraged-insulting | Leviathan directly curses Jin while resisting his attacks. |
| 기자 | 진태경 | Japanese reporter to celebrated foreign Hunter | Jin-sama | formal and reverent | Japanese reporters repeatedly address Jin with the honorific 사마. |
| 진태경 | 기자 | Hunter to Japanese reporter | reporter; you | blunt and insulting | Jin rebukes a reporter for talking back after criticizing Yamamoto's delayed arrival. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 766
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 751
- **Aliases:** Team Leader Seok
- **Role:** Go Jun was Ares Guild's Vice Guild Master, Lee Jungryong's Disciple and former Head of Security, the de facto successor to Lee's Ares legacy, and a mutated monster who was killed by Jin Taekyung in Area A.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Go Jun inherited Lee Jungryong's Ares legacy after becoming his Disciple and regarded Jin Taekyung and Choi Minwoo as enemies before his death.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 766
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 766
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 762
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 766
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, the hidden architect of a coordinated terrorist campaign designed to isolate Ares Guild, the leader of a Guild controlling more than two hundred effectively owned Gates through permanent leases, and a feared rival who has publicly declared a second Great Cataclysm imminent, proposed resurrecting the World Hunter Federation as an organization beyond ordinary laws in order to establish his own rule, and discovered the Skeleton King's identity to use it as leverage against Jin Taekyung.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 757
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter whose delayed arrival during the Leviathan incident became a subject of post-raid media discussion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Not established.

## Korean source

```text
＃767화



지이잉.

갑작스럽게 울려 퍼진 진동음에 최 팀장이 품에서 스마트폰을 꺼내 들었다.

하나도 아니고, 무려 다섯 개나 되는 기기 중 하나를 확인한 그는 나를 향해 입술을 달싹였다.

- 진태경 씨.

굳이 소리 내어 말하지 않는 이유는 불 보듯 뻔하다. 나는 신속하게 공력을 끌어 올려 주위로 퍼트렸다.

솨아아아.

보이지 않는 기의 막이 스위트룸 내부를 물샐 틈 없이 감싼 그 순간.

지잉.

테이블 위에 놓인 스마트폰의 화면에서 푸른 빛이 뿜어졌다.

그리고 눈 깜짝할 사이에 사람 형태로 모여든 홀로그램 속에서, 굵은 저음의 목소리가 울려 퍼졌다.

- 늦어서 미안해. 지금 막 연락을 확인했…… 그런데 저 친구는 왜 저래? 설마 벌써 전투라도 벌어진 거야?

매직 존슨.

가슴을 부여잡고 쓰러진 스켈레톤 킹을 보며 눈을 깜빡이는 거구의 대마도사를 향해, 나는 힘없이 대답했다.

“말하자면 길어요.”



* * *



스켈레톤 킹이나 최 팀장과 달리, 매직 존슨의 반응은 짧고 명확했다.

- Fuck.

물론 그걸로 끝은 아니었다.

아들과 해변이라든지, 평소에는 다른 사람이 볼 수 없게 숨겨 둔 제3의 구멍에 대해서도 쉴 새 없이 중얼거리던 매직 존슨은 모근 하나 없이 매끈한 정수리를 문질렀다.

- 이건…… 정말이지 최악이군.

그제야 미처 생각하지 못하고 있던 한 가지 사실이 떠올랐다.

만약 스켈레톤 킹의 존재가 밝혀질 경우, 심각한 타격을 입는 것은 나와 최 팀장뿐만이 아니라는 것을.

“죄송합니다. 더 주의했어야 했는데.”

- 사과할 필요 없어, 진. 난 그저 스스로의 판단으로 너희를 도운 거였으니까.

내 뒤늦은 사과에 손사래를 친 매직 존슨이 문득 눈살을 찌푸렸다.

- 그런데 놈은 어떻게 그 사실을 알아차린 거지? 분명 내 환영 마법은 완벽했을 텐데.

세계에서 단 셋. 아니, 이제는 둘밖에 남지 않는 대마도사인 매직 존슨이 공들여 각인한 환영 마법인 만큼, 그 효과와 은밀함은 타의 추종을 불허하는 수준이다.

때문에 지금 매직 존슨의 표정은 여러 감정으로 복잡하게 뒤섞여 있었다.

- 지크프리트가 죽은 이상 내 환영 마법의 실체를 간파할 수 있는 수준의 마법사는 이제 한 사람뿐인데…… 장담하지만, 제아무리 미카엘이라고 해도 그녀를 움직일 수는 없어.

매직 존슨이 저렇게까지 말한다면 틀림없는 사실일 것이다.

또 다른 대마도사에 관한 이야기는 나 역시 익히 들어 보았고, 수십여 년의 시간을 거쳐 그중 대부분이 소문이 아닌 사실로 밝혀졌으니까.

그러나 그 부분을 제외하더라도 이미 짚이는 구석은 충분했고, 순간 그에 관련된 생각을 떠올린 것은 나 혼자만이 아니었다.

“일본.”

“레비아탄.”

두 개의 목소리가 겹친다.

비록 단어는 다르지만 같은 의미로 나와 동시에 입을 연 최 팀장이 모두의 시선 속에서 천천히 말을 이어 갔다.

“모두 아시다시피, 일본에서의 일은 단순한 테러나 몬스터 웨이브가 아니었습니다.”

- 그에 관해서는 나도 최의 연락을 받았지. 개인적인 생각으로도 미카엘 실베르트의 소행이 유력해.

“하지만 이 시점에서 우리가 다시 한번 생각해 보아야 할 점은, 그의 목적입니다.”

- 목적?

“미카엘 실베르트가 무엇을 위해 심해 깊은 곳에 잠들어 있던 레비아탄을 깨웠는지. 그리고…….”

“왜 그 많은 나라 중, 레비아탄을 굳이 일본으로 유인했는지.”

최 팀장의 말을 이어받은 나는 생각했다.

이 지구에서 다섯 개의 대양이 차지하는 면적은 무려 71%에 달하고, 바다와 인접한 나라는 차고 넘친다.

그런데 어째서 놈은 레비아탄이 날뛸 전장으로 일본을 선택한 것일까.

‘게다가 같은 날 전 세계 곳곳을 강타한 2차 테러까지.’

그리고 의문에 대한 답은 이미 나와 있었다. 다음 순간 흘러나온 최 팀장의 한 마디처럼.

“처음부터 치밀하게 계산했던 겁니다. 당시 일본의 상황 및 모든 것을 고려해서.”

그 말에 담긴 의미를 깨달은 매직 존슨이 신음하듯 중얼거렸다.

- 그럼 2차 테러를 비롯한 그 모든 일이, 너희를 끌어들이기 위해서였다?

“예. 분명합니다.”

- 하지만 왜 하필 일본이지? 그게 목적이었다면, 차라리 한국으로 유인하는 것이 더 간단했을 텐데.

고개를 저은 최 팀장이 침착한 목소리로 말을 이었다.

“미카엘 실베르트의 입장에서는 그럴 수밖에 없었을 겁니다. 한국 헌터의 수준이 월등히 높다는 것을 제외하더라도, 우리 정부는 석고준이 인위적으로 벌인 두 번의 몬스터 웨이브 이후부터는 언제나 촉각을 곤두세우고 있었습니다. 이런 상황에서 마력 수치가 갑작스럽게 급상승한다면 금세 알아차렸겠죠.”

- 마정석……!

“맞습니다. 하지만 얼마 전 1차 테러의 타겟이 되었던 일본. 정확히는 도쿄 인근은 여러모로 적합한 장소로 여겨졌을 겁니다.”

그냥 마정석도 아닌, 정제되지 않은 S급 마정석.

그것이 흩뿌리는 마력의 양과 농도는 저 멀리 바다 깊숙한 곳에 잠들어 있던 레비아탄이 깨어날 만큼 엄청났다.

하지만 이미 1차 테러로 발생한 몬스터 웨이브로 마력 수치가 미쳐 날뛰는 수준이었던 도쿄 인근에서는 쉽게 알아차리지 못했을 것이다.

결정적으로 레비아탄에 의해 파괴된 도쿄만 인근에는 경계할 만한 게이트 자체가 없었으니까.

- 그래, 그랬군. 모든 것이 맞아떨어져.

“처음부터 이를 바탕으로 밑그림을 그린 뒤 2차 테러로 색을 입힌 겁니다. 헌터 강대국과는 제법 거리가 있는 일본이니, 내부 전력으로는 레이바아탄이라는 네임드 몬스터를 쉽게 막지 못할 것이란 예측도 어렵지 않았겠죠.”

무림의 초절정 고수들만 봐도 알 수 있듯이, 현대의 S급 헌터들도 그 수준에서 현격한 차이를 보인다.

그런 의미에서 일본의 S급 헌터, 야마모토 겐지는 힘의 법칙으로 세워진 이 피라미드에서 아래층을 벗어나지 못했다.

일본 네티즌과 일뽕들이 열심히 빨아 재끼는 그 실력이 사실이라면, 왜 하루라는 시간이 있었음에도 레비아탄이 쓰러진 후에야 느지막이 도착했겠나.

‘뻔하지.’

모르긴 몰라도 일본 정부 역시 그 사실을 알고 있었을 것이다. 그렇기에 자존심을 굽혀서라도 도움의 손길을 구해야 했다.

전 세계를 휩쓴 두 번의 테러에도 별다른 피해를 입지 않은 나라.

누구도 부정할 수 없는 헌터 강대국이자, 가장 빠르게 자신들을 구원해 줄 수 있을 만큼 가까운 인접국.

그것이 한국이었고, 한국에는 바로 내가 있었다.

아니, ‘우리’가.

“……!”

서늘한 한기가 등골을 타고 흘렀다. 지금 막 잠에서 깬 사람처럼 불현듯 고개를 치켜든 나는 스켈레톤 킹을 응시했다.

탈구된 뼈를 끼워 맞추는 것도 잊은 채, 멍하니 대화를 듣고 있던 녀석이 내 시선에 화들짝 놀라며 몸을 움츠렸다.

“나, 난 가만히 있었다.”

“…….”

“너무 심각한 것 같아서 한 농담이었다니까! 분위기 전환이라는 것도 모르나!”

“그게 아냐.”

“그, 그럼 왜?”

빌어먹을.

나도 모르게 악물어진 잇새 사이로, 억눌린 목소리가 흘러나왔다.

“너였어. 처음부터.”

“처음부터 이 몸이었다니. 도대체 그게 무슨 소리냐?”

그리고 스켈레톤 킹이 눈살을 찌푸린 그때. 최 팀장이 깊게 가라앉은 얼굴로 입을 열었다.

“미카엘 실베르트가 처음부터 노렸던 목표는 진태경 씨가 아닌 바로 당신입니다.”

“……뭐?”

“아직도 모르겠습니까? 2차 테러도, 레비아탄도. 모든 것이 당신을 노리고 벌인 일이었습니다.”

“……!”

스켈레톤 킹의 동공이 파르르 떨렸다. 굳게 입을 다문 채 무언가를 생각하던 매직 존슨이 탄식하듯 중얼거렸다.

- 이미 이전부터 의심하고 있었다는 뜻이군.

“그 의심을 확신으로 뒤바꿀 증거가 필요했을 테고요.”

- 이 정도로 엄청난 인명 피해를 감수할 만큼?

“아직도 그를 모르십니까? 설령 수백, 수천만이 죽는다고 해도 미카엘 실베르트는 눈 하나 깜짝하지 않을 겁니다.”

깊게 가라앉은 최 팀장의 시선이 나를 향한다.

평소와는 다른, 쇳가루처럼 거친 목소리가 그의 입술 사이를 비집고 흘러나왔다.

“자신의 목적만 달성할 수 있다면. 확신을 얻을 증거만 있다면 당장 이 모든 걸 끝낼 수 있을 테니까요.”

“……!”

맞다.

놈이 원한 것은 단지 그뿐이었다. 나와의 전쟁에서 확실한 승리를 가져다줄 결정적인 약점.

그렇기에 처음부터 끝까지 모든 무대를 꾸몄고, 타국의 지원군이 끼어들 여지를 제거하여 스켈레톤 킹이 나설 수밖에 없는 환경을 조성했다.

‘그리고…… 마침내 그 약점을 틀어쥐었지.’

뿐만이 아니다. 놈이 이토록 과감히 2차 테러를 감행할 수 있었던 이유는, 세계 헌터 연맹과도 밀접한 연관이 있었을 것이다.

‘피해가 크면 클수록, 연맹의 재설립 가능성도 높아질 테니까.’

도대체 놈은, 미카엘 실베르트의 계산은 어디까지 끝나 있던 것일까.

문득 떠오른 의문에 숨이 막혔다.

보이지 않는 끈이 목을 조여 오는 듯한 착각에, 깊게 심호흡한 나는 주위를 둘러보았다.

최 팀장, 매직 존슨. 마지막으로 스켈레톤 킹까지.

어느샌가 대화를 멈춘 그들 모두가 나를 바라보고 있다.

아니, 정확히는 기다리고 있었다.

굳게 다물어진 내 입이 열리기를, 자신들이 나아갈 방향을 제시해 줄 결정을.

그리고 순간 뇌리를 스치는 수많은 생각과 고민 끝에, 나는 긴 침묵을 깨트리며 말문을 열었다.

“나는…….”



* * *



사흘이 지났다.

그러나 한바탕 재앙이 스쳐 지나간 며칠 전의 그날 밤, 오딘 길드장의 전용기가 내려앉았던 뮌헨 외곽의 공터에서 울려 퍼진 거대한 굉음에 관해서는 모두가 잠잠했다.

물론 그보다 앞서 쫓겨나다시피 현장을 떠났던 취재진들은 멀리서나마 희미하게 들었던 그 굉음의 정체를 알고 싶어 했으나, 뮌헨 일대를 통제하는 독일 연방군에게서 돌아온 대답은 단호했다.

첫째. 쓸데없는 질문 및 접근 거부.

둘째. 만약 이에 불응할 시, 즉각 국외 추방.

첫 번째 조항에서 발끈하던 열혈 기자들조차 두 번째 조항에 이르러서는 입을 다물 수밖에 없었다.

세계 헌터 연맹의 재설립이라는 엄청난 화두가 전 세계를 뒤흔들고 있는 지금, 괜한 긁어 부스럼으로 추방당하는 것은 그야말로 미친 짓이었다.

현재 뮌헨에는 이 논의에서 결코 빼놓을 수 없는 핵심 인물이 둘이나 남아 있었으니까.

한 사람은 어젯밤 카메라 앞에서 이해하지 못할 행동을 취했던 진태경이었고, 또 다른 하나는 이 화약고에 불을 붙인 장본인인 미카엘 실베르트였다.

“저기, 미안한데 그 두 사람 동향 파악된 거 있어요?”

“없소.”

“그 대답은 정말 없어서 하는 말입니까, 아니면 있는데도 없다고 하는 겁니까?”

“흠. 둘 다?”

“이런 상황에서는 동업자끼리 좀 돕고 삽시다. 저 농담도 모르는 독일 놈들이 어지간히 깐깐하게 굴어야 말이지. 그런데 이름이 뭡니까?”

“프란츠 마이어.”

“……혹시 독일 사람은 아니겠죠?”

“맞을 거요. 농담도 모르는 주제에 깐깐하고 성격까지 더러운 독일 놈이 바로 나지.”

“성격 더럽다는 말은 안 했는…… 젠장. 미안합니다. 본심은 아니었어요.”

“본심이어도 상관없소. 다만 정 미안하면 괜찮은 소스라도 하나 던져주든지.”

“괜찮은 소스라. 그럼 UN 총회 긴급 소집은 어때요?”

턱수염을 기른 독일 기자가 피식 웃었다.

“장난하시오? 그거 모르는 사람이 어디 있다고. 벌써 회의 시작한 지 한참 지났잖소.”

그 말은 사실이었다.

대격변 이후 새롭게 개편된 UN은 뮌헨 사태가 있었던 사흘 전 자정을 기점으로 총회를 긴급 소집했고, 여섯 개의 상임이사국을 중심으로 한 185개국의 정상들이 화상회의를 통해 치열한 갑론을박을 벌이고 있었다.

그리고 그들이 모인 이유는 단 하나.

세계 헌터 연맹의 재설립 안건이었다.

이번 긴급 총회는 사안이 사안인 만큼 이례적으로 극비리에 진행되었다.

그러나 말은 어디에서나 새어 나가는 법이었고 영향력 있는 언론들은 이미 정보를 입수한 뒤 촉각을 곤두세우고 있었다.

“그런데 어지간한 사람들은 다 아는 사실을 괜찮은 소스랍시고 내놓다니. 보기보다 유머 감각이 형편없군. 당신도 독일인 운운할 처지가 아니야.”

“음, 그래요? 곧 표결이 시작된다는 것도?”

멈칫.

돌아서려던 독일 기자가 까슬까슬한 턱수염을 쓰다듬었다.

“……이건 좀 재미있군.”

“재밌다니 다행이지만, 농담은 아니에요.”

“그 정보, 확실한 거요?”

“이 세상에 확실한 게 어디 있겠어요. 굳이 확률을 말하자면 99.9% 정도지만.”

99.9%.

완전에 가까운 그 숫자를 작게 중얼거린 독일 기자가 침을 꿀꺽 삼켰다.

“그렇다는 건…….”

“예. 맞아요. 곧 UN에서 공표할 겁니다.”

눈앞의 독일 기자보다 십 년은 어려 보이는 기자, 시몬이 천천히 말을 이었다.

“세계 헌터 연맹. 전 세계를 아우르는 그 거대한 단체의 탄생에 관한 표결 결과를.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 767

*Bzzzt.*

At the sudden vibration, Team Leader Choi pulled a smartphone from inside his coat.

After checking one of the five—yes, five—devices he carried, he moved his lips toward me.

“Mr. Jin Taekyung.”

The reason he did not say it aloud was obvious. I quickly drew up my internal energy and spread it around us.

*Fwoooosh.*

The moment an invisible barrier of qi sealed the suite without leaving so much as a gap—

*Bzzzt.*

Blue light poured from the screen of the smartphone lying on the table.

In the blink of an eye, it gathered into the shape of a person, and a deep, resonant voice rang out from the hologram.

“I’m sorry I’m late. I just checked your message… But what’s wrong with that guy? Don’t tell me you’ve already gotten into a fight?”

Magic Johnson.

Looking at the towering Grand Mage blinking at the Skeleton King, who had collapsed while clutching his chest, I answered weakly.

“It’s a long story.”

* * *

Unlike the Skeleton King or Team Leader Choi, Magic Johnson’s reaction was brief and clear.

“Fuck.”

Of course, that was not the end of it.

After muttering nonstop about a son and a beach, as well as a certain third hole he normally kept hidden from other people, Magic Johnson rubbed his perfectly smooth, hairless crown.

“This… is truly the worst.”

Only then did one fact I had failed to consider occur to me.

If the Skeleton King’s existence were exposed, I would not be the only one to suffer a serious blow. Neither would Team Leader Choi.

“I’m sorry. I should have been more careful.”

“There’s no need to apologize, Jin. I helped you all of my own accord.”

Magic Johnson waved away my belated apology, then suddenly furrowed his brow.

“But how did he realize it? My illusion Magic should have been perfect.”

Magic Johnson was one of only three Grand Mages in the world.

No—now there were only two.

Given that his meticulously inscribed illusion Magic was involved, its effectiveness and secrecy should have been beyond comparison.

That was why his expression was so tangled with conflicting emotions.

“With Siegfried dead, there’s only one mage left who could see through the true nature of my illusion Magic… But I guarantee you, even Michael couldn’t make her act.”

If Magic Johnson was speaking with such certainty, it had to be true.

I had heard plenty about the other Grand Mage myself, and after decades had passed, most of what I had heard had turned out to be fact rather than rumor.

But even setting that aside, there were already enough clues to point us in the right direction.

And I was not the only one to reach the relevant conclusion at that moment.

“Japan.”

“Leviathan.”

Two voices overlapped.

Although the words were different, they meant the same thing. Team Leader Choi, who had spoken at the same time as me, continued slowly as everyone’s eyes turned toward him.

“As you all know, what happened in Japan was not a simple terrorist attack or Monster Wave.”

“I heard about that from Choi as well. Personally, I believe Michael Silbert is the most likely culprit.”

“But at this point, we need to think about his objective once more.”

“His objective?”

“Why did Michael Silbert awaken Leviathan, which had been sleeping in the depths of the deep sea? And…”

“Why did he deliberately lure Leviathan to Japan when there were so many other countries?”

Taking over from Team Leader Choi, I thought.

The five oceans covered a staggering seventy-one percent of the Earth’s surface, and there was no shortage of countries bordering the sea.

So why had he chosen Japan as the battlefield where Leviathan would run wild?

*And then there was the second terrorist attack that struck places all over the world on that same day.*

The answer to that question already existed.

Just as Team Leader Choi’s next words made clear.

“He calculated everything meticulously from the beginning, taking Japan’s situation at the time and every other factor into account.”

Magic Johnson grasped the meaning behind his words and muttered with a groan.

“Then all of it—including the second terrorist attack—was meant to draw you in?”

“Yes. Without a doubt.”

“But why Japan? If that was the objective, it would have been simpler to lure Leviathan to Korea.”

Team Leader Choi shook his head and continued in a calm voice.

“From Michael Silbert’s perspective, it was the only possible choice. Even setting aside the fact that Korean Hunters are far stronger, our government has been on high alert ever since Go Jun artificially caused two Monster Waves. If magical power had suddenly surged, they would have noticed immediately.”

“The Magic Gem…!”

“That’s right. But Japan had recently been targeted by the first terrorist attack. More precisely, the area around Tokyo must have seemed suitable in many ways.”

This was no ordinary Magic Gem, either. It was an unrefined S-rank Magic Gem.

The amount and concentration of magical power it scattered had been enormous enough to awaken Leviathan, which had been sleeping far away in the depths of the sea.

But around Tokyo, where magical power was already running wild because of the Monster Wave caused by the first terrorist attack, it would not have been easy to notice.

Most importantly, there had been no Gate worth worrying about near Tokyo Bay, which Leviathan had destroyed.

“Yes. Now it all fits together.”

“He drew the outline based on that from the start, then colored it in with the second terrorist attack. Since Japan was fairly far from the major Hunter powers, it would not have been difficult to predict that its own forces would be unable to stop a named monster like Leviathan.”

You could tell just by looking at the Supreme Peak masters of the Murim. Even modern S-rank Hunters differed enormously in strength among themselves.

In that sense, Japan’s S-rank Hunter, Yamamoto Genji, had never managed to leave the lower levels of this pyramid built on the law of strength.

*If he was really as strong as all those Japanese netizens and Japan-worshipping fanboys dickriding him claimed, why had he shown up so late that Leviathan was already dead when he’d had an entire day to get there?*

*It was obvious.*

The Japanese government must have known that, too. That was why they had been forced to swallow their pride and ask for help.

A country that had suffered little damage despite the two terrorist attacks that swept across the world.

An indisputable Hunter powerhouse—and a neighboring country close enough to rescue them faster than anyone else.

That country was Korea, and Korea had me.

No.

*Us.*

“……!”

A chill ran down my spine. I abruptly raised my head as though I had just woken up and stared at the Skeleton King.

He had been listening to the conversation blankly, having even forgotten to set his dislocated bones back into place. At my gaze, he flinched and hunched over.

“I—I was just sitting here.”

“……”

“It was only a joke because things seemed so serious! Don’t you know what changing the mood means?”

“That’s not it.”

“Th—then why?”

Damn it.

A restrained voice slipped through my clenched teeth.

“It was you. From the beginning.”

“You mean this body was the target from the beginning? What in the world are you talking about?”

At that moment, the Skeleton King furrowed his brow.

Team Leader Choi spoke with a deeply grave expression.

“Mr. Jin Taekyung was not Michael Silbert’s target from the beginning. You were.”

“……What?”

“Do you still not understand? The second terrorist attack, Leviathan—everything was carried out with you as the target.”

“……!”

The Skeleton King’s pupils trembled.

Magic Johnson kept his mouth firmly shut as he considered something, then muttered like a sigh.

“So he had already suspected it.”

“He would have needed evidence to turn that suspicion into certainty.”

“Enough evidence to justify casualties on this scale?”

“Do you still not know what kind of man he is? Even if hundreds died—or tens of millions—Michael Silbert would not bat an eye.”

Team Leader Choi’s heavily lowered gaze turned toward me.

His voice was rough, like iron filings scraping against one another, as it forced its way between his lips.

“If he could accomplish his goal. If he could obtain evidence that gave him certainty. He would be able to end all of this immediately.”

“……!”

He was right.

That was all the bastard had wanted: a decisive weakness that would guarantee victory in his war against me.

That was why he had built the entire stage from beginning to end, eliminating any possibility of aid from other countries and creating a situation in which the Skeleton King had no choice but to step in.

*And then… he finally got his hands around that weakness.*

That was not all.

There must also have been a close connection between the reason he had been able to carry out the second terrorist attack so boldly and the International Hunter Federation.

*The greater the damage, the greater the chance that the Federation would be reestablished.*

Just how far had Michael Silbert’s calculations gone?

The question suddenly occurred to me, and I found it difficult to breathe.

It felt as though invisible strings were tightening around my neck. After taking a deep breath, I looked around.

Team Leader Choi. Magic Johnson.

And finally, the Skeleton King.

At some point, all three of them had stopped talking and were looking at me.

No.

More precisely, they were waiting.

Waiting for my tightly closed mouth to open.

Waiting for me to show them the direction they should take.

And after countless thoughts and worries flashed through my mind, I broke the long silence and began to speak.

“I…”

* * *

Three days passed.

Yet everyone remained silent about the enormous boom that had echoed across the vacant lot on the outskirts of Munich, where the Odin Guild Master’s private aircraft had landed a few nights earlier, on the night when a full-blown disaster had swept through.

Of course, the reporters who had left the scene as though they had been thrown out wanted to know what the faint rumble they had heard from a distance really was.

But the German Federal Army controlling the Munich area had given them a firm response.

First: useless questions and attempts to approach the area would be rejected.

Second: anyone who refused to comply would be expelled from the country immediately.

Even the hot-blooded reporters who had bristled at the first clause could only shut their mouths when they reached the second.

With the enormous issue of reestablishing the World Hunter Federation shaking the entire world, getting deported over a needless provocation would have been nothing short of madness.

There were still two key figures in Munich who could not possibly be excluded from the discussion.

One was Jin Taekyung, who had behaved incomprehensibly in front of the cameras the previous night.

The other was Michael Silbert, the one who had lit the fuse on this powder keg.

“Hey, sorry, but have you managed to learn anything about those two?”

“No.”

“Are you saying that because you really don’t know anything, or because you do know something but are saying you don’t?”

“Hmm. Both?”

“In a situation like this, colleagues should help each other out. Those Germans who don’t know how to take a joke are being ridiculously strict. What’s your name, by the way?”

“Franz Meyer.”

“…You’re not German, are you?”

“Most likely. I’m the German who’s strict, foul-tempered, and incapable of understanding jokes.”

“I didn’t say you were foul-tempered—damn it. Sorry. I didn’t mean it.”

“It wouldn’t matter even if you did. But if you’re really sorry, throw me a decent scoop.”

“A decent scoop? Then how about the emergency convening of the UN General Assembly?”

The bearded German reporter let out a short laugh.

“You’re joking, right? Who doesn’t know about that? The meeting started ages ago.”

That was true.

Following the Great Cataclysm, the newly reorganized UN had urgently convened its General Assembly at midnight three days earlier, immediately after the Munich incident. The heads of 185 nations, centered around the six permanent member states, were engaged in fierce debate through a videoconference.

And they had gathered for only one reason.

The proposal to reestablish the World Hunter Federation.

Given the circumstances, this emergency General Assembly was being conducted under exceptionally tight secrecy.

But words had a way of leaking out wherever they went, and influential media outlets had already obtained the information and were keeping a close eye on developments.

“And yet you offer something everyone with half a brain already knows as a decent scoop. Your sense of humor is worse than I expected. You’re in no position to talk about Germans.”

“Hmm, is that so? What if I told you the vote would begin soon?”

The German reporter stopped short.

He stroked his rough beard.

“…Now that’s interesting.”

“I’m glad you think so, but I’m not joking.”

“Are you certain about that information?”

“What in this world can ever be certain? If I had to give you a probability, I’d say about 99.9 percent.”

99.9 percent.

The German reporter quietly repeated the number, so close to perfect, and swallowed.

“That means…”

“Yes. That’s right. The UN will announce it soon.”

The reporter who spoke, Simon, looked about ten years younger than the German reporter standing before him. He continued slowly.

“The World Hunter Federation. The result of the vote concerning the birth of that enormous organization spanning the entire world.”

“……!”
```
