<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0768.txt",
      "sha256": "3cafe89c500186cff611ca44612789e0757b46757a1737213a5097c052f355fb",
      "bytes": 12875
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "40e9d3f40f52317d641f13526b55788df0e5a438e625149b177182c34b767e72",
      "bytes": 2012
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1abf514d0484b3944b7c58787c1d6c0b66ee5a469b32a4c6898ec6c06b5474aa",
      "bytes": 221588
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "9508ad6ff7a2cdf6da5662fc16df78303e2f141dacf4accbf6daad98d70b7864",
      "bytes": 861
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a1e2d5290e91e0e72a35c8ac1b38498f1c0fa359ad47f89b1e2074be3f92af09",
      "bytes": 553
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "94abf44c414f8904887e9d4aead6e067e668326d333bad62551e217ad6b74049",
      "bytes": 2017
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "33a9149e01346763b9c643a7d7a5a094b7baf3c6e1cd2a5ab40bcf9d63cfbe22",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "b1e1d8a93bfffb0670a038a5e0a5ae3c68d859356baa1dc9f20e105d4363fabb",
      "bytes": 1159
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "47c1e32afcf73fa785d6d73d1a4af1b3697bed33d516d46f1cd95855061ad90b",
      "bytes": 572
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "62dfef7a1387e12bad96883ae0b19aca93fc615c81d7bcedf2769c9664b77a5d",
      "bytes": 238974
    }
  ],
  "estimated_tokens": 10890
}
-->

# Durable State Update — Chapter 768

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 768. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 768. Profile updates may replace only one
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
  "chapter": 768,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 768,
    "continuity_sources": [768],
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
    "Michael Silbert orchestrated the Japan operation, the second terrorist attack, and Leviathan's awakening and lure to Japan to expose the Skeleton King's identity.",
    "Michael sought evidence of the Skeleton King's identity as a decisive weakness in his war against Jin Taekyung.",
    "The Skeleton King has learned that he, rather than Jin, was Michael's original target.",
    "Jin, Team Leader Choi, the Skeleton King, and Magic Johnson are together in Munich and are awaiting Jin's decision.",
    "Magic Johnson believes only one other surviving Grand Mage could have seen through his illusion Magic, and Michael could not compel her to act.",
    "The UN General Assembly is secretly debating the reestablishment of the World Hunter Federation.",
    "The representatives of 185 nations, centered on six permanent member states, are expected to vote imminently.",
    "German authorities are restricting access to the Munich incident site and threatening expulsion for noncompliance.",
    "Simon has informed Franz Meyer that the UN vote will begin soon and that the result is almost certain to be announced."
  ],
  "continuity_sources": [
    767
  ],
  "open_questions": [
    "What decision will Jin make after learning that the Skeleton King was Michael's original target?",
    "How will Michael use the evidence and leverage gained from exposing the Skeleton King's identity?",
    "Will the UN vote reestablish the World Hunter Federation?",
    "Who will control the reestablished World Hunter Federation if the proposal passes?",
    "How will the Skeleton King respond to being the center of Michael's operation?"
  ],
  "safe_through": 767,
  "temporary_decisions": [
    "Render 세계 헌터 연맹 as World Hunter Federation.",
    "Render 마력 as magical power and 마정석 as Magic Gem.",
    "Render 대마도사 as Grand Mage.",
    "Render the UN's upcoming 표결 as the vote on reestablishing the World Hunter Federation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 대격변     | **Great Cataclysm**   |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 대통령 | **President** | Title for Korea's head of state. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 도람프 | **Doramp** | Parodic name for the U.S. president in a forum headline. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 고이즈미 | **Koizumi** | Japanese prime minister quoted in the news. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 전도 | **complete map of the realm** | Mae Jonghak's map marking terrain, place names, and sect locations. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |
| 백한성 | 최민우 | President_to_trusted_political_ally | Team Leader Choi | formal-polite, warm, and politically attentive | Baek addresses Choi as 최 팀장님 during the private Blue House breakfast. |
| 최민우 | 백한성 | political_subordinate_to_President | Mr. President | formal-polite | Choi addresses Baek as 대통령님 during the breakfast and departure. |
| 비서실장 | 백한성 | chief_secretary_to_President | Mr. President | formal and deferential | Calls Baek Hanseong 각하 while reporting the Guild Association's request. |
| 고이즈미 | 진태경 | Japanese Prime Minister to allied foreign Hunter | Jinsang | formal and cordial | Koizumi addresses Jin with the retained Korean pun and later uses Mr. Jin Taekyung. |
| 진태경 | 고이즈미 | foreign Hunter to Japanese Prime Minister | Prime Minister | casual, familiar, and coercively playful | Jin asks Koizumi to lend Japan's S-rank Magic Gems and promises to return them. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 747
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history who leads the government's public response to the Mutated Gate crisis, supports Jin Taekyung in public appearances, and publicly backs the national project to release Cheon Taemin's Mana Cultivation Method.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong who has established a cooperative relationship with Jin Taekyung and Choi Minwoo while seeking to restrain the power concentrated in their two Guilds.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 767
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 767
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 767
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 767
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, the hidden architect of a coordinated terrorist campaign, the leader of a Guild controlling more than two hundred effectively owned Gates through permanent leases, and a feared rival who orchestrated the Japan operation and Leviathan's awakening to expose the Skeleton King's identity, obtain leverage against Jin Taekyung, and advance his plan to reestablish the World Hunter Federation as an organization beyond ordinary laws.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 756
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead who investigates major Guilds and organizes strategic information.
- **Personality:** Calm, pragmatic, meticulous, and emotionally steady under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung.

## Korean source

```text
＃768화



마리 앙투아네트 증후군.

과거 18세기 프랑스 혁명 당시 마리 앙투아네트 왕비가 처형을 며칠 앞두고 갑작스럽게 머리가 백발로 변했다는 것에서 유래한 명칭이다.

비록 이 기묘한 현상에 관한 정확한 실체나 원인은 밝혀진 바 없었으나, 지금 이 순간 대한민국의 백한성 대통령은 그 원인이 극심한 스트레스라고 확신하고 있었다.

당장 자신이 처한 상황도 비슷했으니까.

‘씨발.’

누구보다 주목받았던 정계(政界) 데뷔 이후 자제해 왔던 욕설이 입안에서 회오리 친다.

국회의원 시절부터 함께해 온 눈치 빠른 비서가 입 모양을 가리라는 제스처를 취했지만, 백한성 대통령은 신경도 쓰지 않았다.

어차피 온 사방이 외국인들 천지다.

당연하게도 저들 중 입 모양만 보고 발음과 뜻을 유추할 만큼 한국어가 뛰어난 사람은 없었고, 하릴없이 자신의 입을 주시할 만큼 한가한 상황은 더더욱 아니었다.

당연한 일이다.

한 나라의 대통령들이 체면도 내려놓고 서로를 향해 삿대질해 대는 이 진귀한 광경을 놔두고, 뭐 하러 자신의 입 모양이나 구경하고 있겠나.

- 그걸 말이라고 하시오! 당연히 세계 헌터 연맹을 재설립해야지!

- 아니, 아예 설립하지 말자는 게 아니라니까? 일단 보류하자고. 보류 뜻 몰라?

- 지금 반말했소? 당신 미쳤어?

- 미친 건 당신이지. 연맹이 가진 막강한 권한. 그거 다 어쩔 건데? 수정 검토도 제대로 안 해 보고 이런 식으로 며칠 만에 얼렁뚱땅 승인할 만한 사안이 아니라니까?

- 이 개 같은…… 당신네 나라 GDP 몇이야?

통역기를 타고 오가는 고성과 시뻘겋게 달아오른 얼굴들.

대한민국의 명물인 국회의사당 난투극에서 3전 3승 무패의 전적을 보유한 백한성 대통령에게는 퍽 정겨운 광경이었지만, 며칠째 이와 같은 상황이 이어지자 머리가 터질 것 같았다.

‘무슨 애들도 아니고.’

물론 늘 이렇지는 않았다.

가끔은 국제 정세에 따라 날 선 말이 오가고, 불편한 분위기가 조성되더라도 UN 총회는 수준 높은 국격과 인격을 보여야 하는 자리니까.

그러나 최악으로 치닫는 상황 속에서, 안팎으로 막대한 스트레스와 중압감에 짓눌린 대통령들은 어느 순간부터 자신들이 쓰고 있던 가면을 벗어던지고 민낯을 드러낼 수밖에 없었다.

- 당장 다 죽게 생겼는데! 이 와중에도 연맹 설립을 보류한다면 어떻게 되겠소!

- 옳소! 우리 사우디아라비아는 세계 헌터 연맹 설립을 적극 지지…….

- 중동은 눈치껏 빠지지 그러나. 지금까지 기름 실컷 팔아먹고 이제는 테러리스트까지 전 세계에 수출했으면서 뭘.

- 뭐?

늙을 대로 늙은 러시아 대통령의 말에 터번을 쓴 중년인이 눈깔을 뒤집었다.

- 이 독재자가 어딜 감히!

- 독재자? 왕이라는 작자가 그렇게 말하니 웃기는군. 적어도 난 공정한 선거와 투표로 선출됐네. 누구처럼 왕족으로 태어나서 이 자리에 앉은 게 아니야.

- 아, 그 공정한 선거로 마지막 대선 때 투표율이 140%나 나왔던 거요?

- 뭐 살다 보면 종종 있는 일이지. 이미 지난 일이기도 하고.

지금으로부터 20여 년 전, 전체 인구를 뛰어넘는 경이로운 투표율로 러시아 종신 대통령이 된 블라디미르 푸린이 번뜩이는 눈동자로 주위를 둘러보았다.

이미 예전에 100세를 넘긴 나이였지만, 최첨단 의료기술과 마법 포션으로 건강을 유지 중인 그는 힘 있는 목소리로 말을 이었다.

- 중요한 건 내가, 우리 러시아가 세계 헌터 연맹 설립을 반대한다는 거야.

- 당신……!

- 까놓고 말하지. 나는 세계 헌터 연맹이 불필요하다고 생각하는 게 아니라, 그 자리에 누가 앉게 될지를 우려하고 있네.

툭. 툭.

주름진 손가락이 테이블을 두드린다. 홀로그램을 뚫고 고스란히 전해지는 박력에, 발끈하려던 찬성파가 일순간 입을 다물었다.

- 과거 처음으로 세계 헌터 연맹의 설립에 대해 논의했을 당시, 내가 찬성했던 이유는 스카이를 믿었기 때문일세. 직접 만나 본 바에 의하면 그는 권력에 별다른 욕심이 없는 사람이었거든.

- 그뿐만 아니라, 상황도 최악이었지요.

미국 대통령, 도람프 주니어의 말에 푸린이 고개를 끄덕였다.

- 그래, 그랬지. 그때만 해도 빌어먹을 아스모데우스가 전 세계를 휩쓸고 있었으니까.

- 현재도 심각한 상황이지만, 그때만큼은 아닙니다. 이렇게 빠른 결정을 내리기에는 세계 헌터 연맹이 가진 권한이 너무나도 막대하다는 것을 모두 생각해 주셨으면 합니다.

러시아와 미국의 냉전도 이미 100여 년 전의 일이다. 오랜 기간 깊어졌던 감정의 골이 완전히 메워졌다고 할 수는 없겠지만, 최소한 이 자리에서만큼은 두 대통령의 뜻이 통했다.

그리고 이는 가장 먼저 연맹 설립 보류를 주장한 백한성 대통령에게 있어 매우 반가운 소식이었다.

이미 대한민국과 함께하기로 약속한, 또 다른 조력자의 도움도.

- 우리 중화인민국 역시 다시 한번 깊은 우려를 표명하는 바요.

중국 주석, 샤오 양이 백한성 대통령을 바라보며 말을 이었다.

- 한국의 백 대통령도 줄곧 말씀하셨듯이, 세계 헌터 연맹의 설립은 신중하게 논의되어야 하오.

- 에에, 우리 일본도 한코쿠의 의견에 동의…….

- 감사합니다, 두 분 모두.

도대체 저 새끼가 또 무슨 헛소리를 하려고.

똥을 끼얹으려는 고이즈미 총리를 황급히 가로막은 백한성 대통령이 통역기가 부착된 마이크로 상체를 기울였다.

- 이미 여러 번 말씀드렸다시피 세계 헌터 연맹은 조심스럽게 다루어야 할 문제입니다. 고작 사흘 만에 결정하기에는 너무나도 성급한…….

- 고작 사흘? 성급?

불쑥 끼어든 프랑스 대통령이 코웃음 쳤다.

- 그 사흘 동안, 밖에서 무슨 일이 벌어졌는지 모르는 겁니까?

- 그건…….

- 한국의 사정은 모르겠지만, 우리 프랑스에서는 벌써 다섯 번의 대규모 폭동이 일어났습니다. 정신 나간 종말론자들이 거리로 뛰쳐나와 소리를 지르고, 이미 모든 업무와 생산은 마비 수준에 이르렀다는 말입니다.

- ……잠시만 제 얘기를 들어 주십시오.

- 이미 사흘 내내 들었던 그 이야기라면 정중하게 사양하겠습니다. 루브르 박물관까지 반쯤 불탄 마당에 더 무슨 말을 들어야 하겠습니까.

말문이 막힌 백한성 대통령은 자신도 모르게 지끈거리는 관자놀이를 문질렀다.

‘저 빌어먹을 놈.’

프랑스 대통령이 오딘 길드의 지원으로 지금의 자리에 올랐다는 건 익히 아는 사실.

하지만 쉽게 반박할 수 없는 이유는, 그의 말이 틀림없는 사실이었기 때문이었다.

‘미카엘 실베르트.’

대중들의 엄청난 지지를 받는 영웅의 한 마디는 불안과 공포로 가득 찬 화약고에 불을 질렀다.

전 세계의 인구 중 절반이 두 번째 대격변을 예고하는 그의 모습을 실시간으로 지켜보았고, 그 불길은 불과 하루도 지나지 않아 현실로 번졌다.

폭동에 가까운, 엄청난 규모의 시위대.

분노와 공포에 사로잡혀 거리로 뛰쳐나온 이들의 인내심은 그리 길지 못했고, 도시 곳곳에서 불길이 솟구치는 것은 당연한 수순이었다.

경찰? 군대?

무장을 갖춘 채 즉각 해산을 요구하라는 그들의 외침은 이미 반쯤 이성을 상실한 사람들의 귓가에 닿지 않았다.

세계에서 열 손가락 안에 드는 선진국인 프랑스가 그 정도니, 다른 나라는 불 보듯 뻔했다.

- 지금 국민이 원하는 건 결과입니다. 그들을 안심시켜 줄 결과. 자신과 가족들의 생명을 보장받을 만한 결과 말입니다.

- 만약 세계 헌터 연맹의 재설립이 무산된다면…… 우리나라는 끝장이오. 최소한 대통령 궁이 불타고 나 역시 온전치 못하겠지.

- 우리는 적극 찬성할 수밖에 없습니다. 당장 군부 세력의 동향이 심상치 않아요.

- 미쳤군. 이 상황에서 반대라니. 지금 남의 일이라고 강 건너 불구경하는 거요?

스포트라이트는 밝다. 그러나 그 주위는 어둡다.

소수의 선진국은 그 어느 때보다 발달된 문명 속에서 살고 있지만, UN에 가입한 185개국 중 몇이나 되는 국가가 그 모든 문명을 누리며 살 수 있을까.

마왕 아스모데우스가 쓰러졌어도 기아와 내전은 해결되지 않았고, 적지 않은 국가가 대격변이 할퀴고 간 깊은 상처를 부여잡고 정부를 유지하고 있다.

그리고 이러한 상황에 처한 이들에게 있어 이번 사태는 그저 화약고가 터진 수준이 아니었다.

이건 핵폭발이다.

머지않아 나라 전체를 집어삼킬 핵폭발.

이대로라면 몬스터가 아닌 분노에 찬 국민들과 쿠데타 세력이 대통령 궁을 불태울 것이 분명했다.

- 더 이상 지체할 수 없소!

- 표결합시다!

- 우리는 안전보장이사회와 상임이사국을 신뢰하지 않소. 전체 표결을 요구하오!

한둘이 아니다.

곳곳에서 동시다발적으로 터져 나오는 외침에 백한성 대통령은 이 길었던 회의가 끝에 다다랐음을 직감했다.

‘이건…… 더 이상 막을 수 없다.’

물론 여전히 UN 안보리의 권한은 막강하다.

2차 세계대전의 승전국인 미국, 영국, 프랑스, 러시아, 중국.

거기에 더해 대격변 이후 합류한 대한민국까지 총 여섯 개의 상임이사국이 존재하고, 이번 안건에서 각각 중립과 찬성을 택한 영국과 프랑스를 제외한다면 무려 네 개의 상임이사국이 보류에 가까운 반대파에 서 있다.

하지만 UN이 개편된 직후, 상임이사국이 지닌 거부권으로도 한계는 분명했다.

‘결국 이렇게 되는군.’

표결 시작을 알리는 사무총장의 선언이 멀게만 느껴진다.

지금 백한성 대통령의 귓가에는 사흘 전 최민우와 주고받았던 대화만이 또렷하게 되감기 되고 있었다.



‘UN의 결정을 최대한 늦춰야 합니다.’

‘늦추라는 말입니까? 막는 것이 아니라?’

‘예. 막을 수 있다면 더 바랄 것이 없겠지만, 그건 설령 미국과 중국이 돕는다 해도 불가능에 가까울 테니까요.’

‘……시간을 벌겠다는 뜻이군요.’

‘몇 주라도. 아니, 며칠이라도 좋습니다. 할 수 있는 부분까지 최선을 다해 주십시오.’

‘허. 지금 도대체 정확히 무슨 일이 벌어지고 있는 겁니까?’



그리고 침묵 끝에 돌아온 최민우의 대답은 짧았다.



‘전쟁입니다.’



“……령님. 대통령님.”

백한성 대통령은 퍼뜩 상념에서 깨어났다. 비서실장이 걱정과 초조함이 뒤섞인 얼굴로 그를 바라보고 있었다.

“이제 표결하셔야 합니다. 저희가 마지막입니다.”

“아.”

탄식처럼 외마디 신음을 흘린 그는 집무실을 가득 메운 대통령들. 아니, 홀로그램을 바라보았다.

그리고 지금쯤 어디선가 전쟁을 준비하고 있을 최민우와 진태경을 떠올리며, 이 지긋지긋한 회의의 마지막 표를 던졌다.



* * *



때로는 얼굴을 마주하지 않아도, 굳이 말을 많이 하지 않아도 충분한 의사소통이 이루어질 때가 있다.

목소리의 어조. 음의 높낮이만으로도 그 말에 담긴 뜻과 의미를 알 수 있으니까.

그런 의미에서 최민우는, 백한성 대통령으로부터 걸려온 전화를 받자마자 모든 전후 사정을 파악할 수 있었다.

- 최선을 다했습니다.

그 한 마디가 가져온 침묵은 길었고, 두 사람 사이에 남아 있던 대화는 공허했다.

짧은 통화를 끝마친 최민우는 걸음을 옮겼다. 각종 서류와 모니터로 가득 차 있는 방을 향해.

자신이 온 것도 눈치채지 못할 만큼 무언가에 열중해 있는 한 사람을 향해.

그리고 문득 입을 열었다.

“UN이…… 세계 헌터 연맹 재설립을 승인했습니다.”

돌아온 대답은 짧았다.

“씨벌.”
```

## Final English reading copy

```markdown
# Chapter 768

Marie Antoinette Syndrome.

The name originated from the story that Queen Marie Antoinette’s hair suddenly turned completely white several days before her execution during the French Revolution in the eighteenth century.

Although the exact nature and cause of this strange phenomenon had never been determined, the President of Korea, Baek Hanseong, was certain that its cause was extreme stress.

After all, his current situation was much the same.

*Fuck.*

The profanity he had kept under control ever since his highly publicized debut in politics swirled around inside his mouth.

The sharp-eyed secretary who had been with him since his days as a member of the National Assembly gestured for him to cover his mouth, but President Baek Hanseong did not care.

The entire room was packed with foreigners.

Naturally, none of them were proficient enough in Korean to infer the pronunciation and meaning from the shape of his mouth alone. And they certainly were not free enough to spend their time watching his lips.

It was only natural.

With the rare spectacle of presidents from various countries abandoning all dignity and pointing fingers at one another, why would anyone bother watching his mouth?

“You call that an argument? Of course we have to reestablish the World Hunter Federation!”

“I’m not saying we should never establish it! I’m saying we should put it on hold for now. Don’t you know what ‘on hold’ means?”

“Did you just speak informally to me? Are you insane?”

“You’re the insane one. What are we going to do about the Federation’s overwhelming authority? This isn’t something we can approve half-assedly in a few days without even properly reviewing the revisions!”

“You fucking… What’s your country’s GDP?”

Shouts rang back and forth through the translation devices, accompanied by faces flushed bright red.

For President Baek Hanseong, who held a perfect three-for-three record in the brawls that were a famous feature of Korea’s National Assembly, it was an oddly heartwarming sight.

But after several days of the same situation, he felt as though his head were about to explode.

*What are they, children?*

Of course, it was not always like this.

Sometimes sharp words were exchanged and an uncomfortable atmosphere formed in accordance with international affairs, but the UN General Assembly was supposed to be a place where nations demonstrated their dignity and their leaders showed their character.

However, as the situation spiraled toward the worst possible outcome and the presidents were crushed beneath immense stress and pressure from all sides, they had no choice but to throw off the masks they had been wearing and reveal their true faces.

“We’re all about to die! What do you think will happen if we put off establishing the Federation even now?”

“Exactly! Saudi Arabia strongly supports the establishment of the World Hunter Federation…”

“The Middle East should know when to bow out. You’ve sold more than enough oil, and now you’ve even exported terrorists to the entire world. What more do you want?”

“What?”

At the words of the Russian president, who was old beyond measure, a middle-aged man wearing a turban bulged his eyes.

“How dare you, you dictator!”

“A dictator? That’s rich coming from a king. At least I was elected through fair elections and voting. I wasn’t born into royalty and handed this position like someone else.”

“Ah, are you talking about that fair election where the voter turnout reached 140 percent in the last presidential election?”

“Well, these things happen from time to time. And it’s already in the past.”

More than twenty years ago, Vladimir Furin had become the Russian president for life through the astonishing voter turnout that had surpassed the country’s entire population.

His eyes gleaming, he looked around the room.

Although he had already passed the age of one hundred long ago, he had maintained his health through cutting-edge medical technology and magical potions. He continued in a powerful voice.

“The important thing is that I—and Russia—oppose the establishment of the World Hunter Federation.”

“You…!”

“Let’s be frank. It’s not that I believe the World Hunter Federation is unnecessary. I’m concerned about who will take that position.”

Tap. Tap.

His wrinkled fingers drummed against the table.

The force of the gesture came through the hologram intact, and the representatives of the pro-Federation camp, who had been about to lash out, fell silent for a moment.

“When the establishment of the World Hunter Federation was first discussed, I supported it because I trusted Sky. From the time I met him personally, he seemed like a man with little interest in power.”

“And the circumstances were at their worst as well.”

At the words of the President of the United States, Doramp Junior, Furin nodded.

“Yes, they were. Back then, that damned Asmodeus was sweeping across the entire world.”

“The situation is still serious, but it is not as bad as it was then. I hope everyone will consider that the World Hunter Federation possesses far too much authority for us to make such a hasty decision.”

The Cold War between Russia and the United States had already been over for more than a century. It would have been impossible to say that the deep resentment accumulated over such a long time had completely disappeared, but at least in this room, the two presidents were in agreement.

And that was very welcome news to President Baek Hanseong, who had been the first to argue that the Federation’s establishment should be put on hold.

Especially with the help of another ally who had already promised to stand with Korea.

“Our Zhonghua People’s Republic likewise wishes to express our deep concern once again.”

Chairman Xiao Yang looked at President Baek Hanseong and continued.

“As President Baek of Korea has repeatedly stated, the establishment of the World Hunter Federation must be discussed with great care.”

“Er, Japan also agrees with Kankoku’s opinion…”

“Thank you both.”

*What the hell is that bastard going to say this time?*

President Baek Hanseong hurriedly cut off Prime Minister Koizumi before he could dump shit all over the discussion. He leaned toward the microphone fitted with a translation device.

“As I have already said several times, the World Hunter Federation is an issue that must be handled carefully. Deciding the matter after only three days would be far too hasty—”

“Only three days? Hasty?”

The President of France cut in with a derisive laugh.

“Are you unaware of what has happened outside during those three days?”

“That…”

“I don’t know what the situation is like in Korea, but France has already suffered five large-scale riots. Insane doomsday cultists have poured into the streets screaming, and all business and production have already ground to a near halt.”

“…Please, just listen to me for a moment.”

“If you’re going to repeat the same thing we’ve already heard for three straight days, I must respectfully decline. Half of the Louvre Museum has burned down. What more do you possibly have to say?”

President Baek Hanseong was rendered speechless. Without realizing it, he rubbed his throbbing temples.

*That damned bastard.*

Everyone knew that the French president had risen to his current position with the support of the Odin Guild.

But the reason Baek could not easily refute him was that everything he had said was true.

*Michael Silbert.*

One word from a hero with tremendous public support had set fire to the powder keg of a world filled with anxiety and fear.

Half the world’s population had watched him in real time as he announced the coming of a second Great Cataclysm, and the flames had spread into reality in less than a day.

Demonstrators of a scale bordering on a riot.

The people who had poured into the streets, seized by rage and fear, had very little patience left. It was only natural that flames soon began to rise throughout the cities.

The police? The military?

Their calls, made while fully armed and demanding that the demonstrators disperse immediately, could not reach the ears of people who had already lost half their reason.

If that was the situation in France, one of the ten most advanced countries in the world, the state of every other country was obvious.

“What the people want now is a result. A result that will reassure them. A result that will guarantee the lives of themselves and their families.”

“If the reestablishment of the World Hunter Federation fails… our country is finished. At the very least, the presidential palace will burn, and I won’t come out of it intact.”

“We have no choice but to support it wholeheartedly. The movements of our military factions are already deeply suspicious.”

“You’re insane. You’re opposing it in this situation? Are you watching a fire across the river because you think it’s someone else’s problem?”

The spotlight was bright.

But everything around it was dark.

A small number of developed nations lived amid civilization more advanced than ever before. But out of the 185 countries belonging to the UN, how many could truly enjoy all of that civilization?

Even after Demon King Asmodeus had been defeated, hunger and civil war had not disappeared. More than a few nations were clutching the deep wounds left by the Great Cataclysm while struggling to keep their governments intact.

And for those caught in such circumstances, this incident was not merely a powder keg exploding.

It was a nuclear detonation.

A nuclear detonation that would soon swallow the entire country.

If things continued like this, it was obvious that enraged citizens and military factions—not monsters—would burn down the presidential palaces.

“We can’t delay any longer!”

“Let’s vote!”

“We do not trust the Security Council or the permanent members! We demand a full vote!”

It was not just one or two people.

As shouts erupted simultaneously from every corner of the room, President Baek Hanseong realized that the long meeting was finally drawing to a close.

*This… can’t be stopped anymore.*

Of course, the UN Security Council still possessed immense authority.

The United States, the United Kingdom, France, Russia, and China—the victors of the Second World War.

With Korea, which had joined after the Great Cataclysm, there were six permanent member states in total. And if the United Kingdom, which had chosen neutrality on this matter, and France, which had chosen to support it, were excluded, four permanent members were standing with the opposition camp that was effectively calling for a delay.

But even the veto power held by the permanent members had clear limits now that the UN had been reorganized.

*So this is how it ends.*

The secretary-general’s declaration announcing the start of the vote seemed distant.

At that moment, the only thing ringing clearly in President Baek Hanseong’s ears was the conversation he had exchanged with Choi Minwoo three days earlier.

“UN decisions must be delayed as long as possible.”

“You mean delayed? Not stopped?”

“Yes. If we could stop them, there would be nothing more I’d ask for. But even if the United States and China helped us, that would be nearly impossible.”

“…You mean we need to buy time.”

“Even a few weeks. No, even a few days would be enough. Please do everything you can until we reach the limit of what is possible.”

“Hah. What exactly is happening right now?”

And Choi Minwoo’s answer, which had come after a long silence, had been short.

“It’s war.”

“…Mr. President. Mr. President.”

President Baek Hanseong abruptly came to himself. The chief secretary was looking at him with a face filled with equal parts concern and impatience.

“You have to cast your vote now. We’re the last ones.”

“Ah.”

After letting out a short groan that sounded almost like a sigh, President Baek Hanseong looked at the presidents filling the office.

No—the holograms.

Then, thinking of Choi Minwoo and Jin Taekyung, who were probably preparing for war somewhere by now, he cast the final vote of this miserable meeting.

* * *

Sometimes, communication was possible without facing one another or even saying very much.

The tone of a voice. Its rise and fall.

That alone could convey the meaning and significance contained in the words.

In that sense, Choi Minwoo understood everything the moment he answered the call from President Baek Hanseong.

“I did everything I could.”

The silence that followed those words was long, and the conversation remaining between the two men was empty.

After ending the short call, Choi Minwoo began to walk.

Toward a room filled with documents and monitors.

Toward a person so absorbed in something that he had not even noticed Choi’s arrival.

Then, suddenly, Choi opened his mouth.

“The UN… approved the reestablishment of the World Hunter Federation.”

The answer was short.

“Fuuuck.”
```
