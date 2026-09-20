<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0567.txt",
      "sha256": "5d2bd1206aaafa5ee3c7a53a837f6d5b5d939fde45c3fa255dab515b2b65a533",
      "bytes": 14176
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a56e1d5a80dcec63943b9956b80be9a5966e9580382811af46667be5c8b7b0b7",
      "bytes": 5052
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7db1061caff09b1d328319581319914a6ea3ee3665e14d699a6e8785d0d9d09b",
      "bytes": 179504
    },
    {
      "path": "characters/Cheonwoo.md",
      "sha256": "7c0e133bb3744d6d1854b096a158bca4c74382bef78ce5f345a55a8716bca9c1",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "223b65a48d9ddb02599ea9b51d9c2ac974a504f5cf5e530f5b052f0c1f883101",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "7ed509cb1f62964fa54cb2a07c91ee09806405048a6908d2eeb07f4728f6fa24",
      "bytes": 898
    },
    {
      "path": "characters/Go Se-won.md",
      "sha256": "a3af046b73aeb194ce501b7cfe923fe5521d8dadd604aee7be08ead90436a2d1",
      "bytes": 635
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "3252d88481fc6e83b624f5d01218e33c828038cd6ff118d08460b962f928a3a9",
      "bytes": 1182
    },
    {
      "path": "characters/Song Cheonwoo.md",
      "sha256": "ac258ca458e555a8b51e2064177aa8568b42a1005f9ba5a286edfb762770fb46",
      "bytes": 852
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "2549357664002b327adc27a63a6d15f769de4e65144e22fec07d955e3317cfc4",
      "bytes": 714
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "43b40b6713298f4152b190b5a370c4b864f8359ce56dc7f85d659b1d01acc7a3",
      "bytes": 174315
    }
  ],
  "estimated_tokens": 11548
}
-->

# Durable State Update — Chapter 567

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 567. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 567. Profile updates may replace only one
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
  "chapter": 567,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 567,
    "continuity_sources": [567],
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
    "Magic Johnson's chip contains more than twenty videos and attached materials showing simultaneous Gate and monster crises across Europe, the Middle East, West Africa, Southeast Asia, and elsewhere; worldwide mana levels are up seven percent year over year.",
    "The videos show strengthened monsters increasingly ignoring normal type advantages, with many under-defended Gates causing major casualties before suppression.",
    "Taekyung suspects this may mark the beginning of a second Great Cataclysm and plans to accelerate the project he has been developing since Murim to prevent Korea from becoming a hellish peninsula.",
    "Team Leader Choi says the crisis has exceeded the limit of national concealment and that delaying disclosure would only increase public confusion.",
    "Choi's immediate priority is reinforcing Gate defenses, despite the resulting reduction in Peace Guild's raid personnel and ability to use all its Gates.",
    "Choi is working with Song Cheonwoo, a powerful Ares insider seeking a final political comeback, against Go Jun's control of Ares Guild; Go Jun has ordered Song's extended family killed.",
    "Song Cheonwoo knows where Choi's maternal grandfather Cheon Taemin is located, while Cheon Taemin remains hidden from the world.",
    "Taekyung is a Supreme Peak master, publicly recognized as S-rank-level while retaining an A-rank license, leads the Fire Dragon Pavilion's first Nanman mission, and is Peace Guild's wealthy modern-world patron.",
    "The Fire Dragon Pavilion's six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is Can't Go to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong.",
    "Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants, while the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains."
  ],
  "continuity_sources": [
    566,
    565
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Where is Cheon Taemin, why has he remained hidden, and what will happen after Song Cheonwoo's faction moves against Go Jun?"
  ],
  "safe_through": 566,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 모하비 사막 as Mojave Desert, 애리조나주 as Arizona, 대의 as greater cause, 순수혈통 as pureblood, 국부 as Founding Father, 위저드(Wizard) 길드 as Wizard Guild, 조셉 바이든 as Joseph Biden, 펠릭스 왕자 as Prince Felix, 곽한구 as Gwak Hangu, 역곡 as Yeokgok, 오크의 황무지 as Orc Wasteland, 오크 로드 as Orc Lord, 국회의사당 as National Assembly, 고세원 as Go Se-won, 경호팀장 as Head of Security, A구역 as Section A, 신성불가침 as sacrosanct, 바티칸 as Vatican, 영구 임대 as permanent lease, 혈안 as bloodshot, 매직 존슨 as Magic Johnson, 썩코춘 as Sseokkochoon, 길드 하우스 as Guild House, 자이언트 맨티스 as Giant Mantis, 파이어 레인 as Fire Rain, 파트라슈 as Patrache, 송천우 as Song Cheonwoo, 유럽 총괄 지사장 as head of the European regional branch, 조손 as grandparent and grandchild, and 외조부님 and 외할아버지 as maternal grandfather."
  ],
  "version": 1
}
```

## Exact glossary matches

| 최민우    | **Choi Minwoo**   |
| 이정룡    | **Lee Jungryong** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 초식     | **form**                                         | Numbered technique movement                           |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 고세원 | **Go Se-won** | Ares Guild Head of Security and Team Leader. |
| 송천우 | **Song Cheonwoo** | Ares Guild Director, former third-ranked Korean Hunter, and longtime European regional branch director. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 팀원 | 석고준 | subordinate security-team member to security-team leader | Team Leader | fearful formal-polite | The team member repeatedly addresses Go Jun as 팀장님 while reporting the strange object. |
| 석고준 | 고세원 | Ares Vice Guild Master to Head of Security | you | curt and informal | Go Jun tells Go Se-won that he is later than usual when Se-won enters the wrecked office. |
| 고세원 | 석고준 | subordinate_to_Vice_Guild_Master | Vice Guild Master | formal-deferential | Uses 부길드장님 while trying to stop Go Jun from watching the broadcast. |

## Listed compact profiles

### Cheonwoo.md

# Cheonwoo (천우)

- **Safe through:** Chapter 566
- **Aliases:** None
- **Role:** One of the five current Five Gates of Shanxi scions and a First Rate martial artist present at Honghwa Inn.
- **Personality:** Pampered and contemptuous toward Cheongpung's group as part of the five scions' collective mockery.
- **Voice:** Mocking in the group's exchange; no distinct individual speech is established.
- **Relationships:** Associates with Seongryong, Myeonghwa, Sohye, and Jintae as a group of current Five Gates scions.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 566
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 566
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death and regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away.

### Go Se-won.md

# Go Se-won (고세원)

- **Safe through:** Chapter 566
- **Aliases:** Head of Security
- **Role:** Go Se-won is Ares Guild's Head of Security and a Team Leader with privileged access to restricted Section A.
- **Personality:** Composed and confident in public, he is mildly uncomfortable with Ares Guild's increasingly severe discipline but obeys its policy.
- **Voice:** Calm and deferential toward superiors, but blunt and decisive when issuing orders.
- **Relationships:** Go Se-won reports to Vice Guild Master Go Jun and commands Ares Guild security personnel.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 566
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Song Cheonwoo.md

# Song Cheonwoo (송천우)

- **Safe through:** Chapter 566
- **Aliases:** Director Song
- **Role:** Ares Guild Director and former A-rank Hunter who reached third place among Korean rankers, briefly headed the Hunter training center, and led Ares Guild's European regional branch for twenty years; he now leads an internal faction capable of threatening Go Jun.
- **Personality:** Highly ambitious, honor-obsessed, politically calculating, and determined to use his final opportunity to reclaim influence before retirement.
- **Voice:** Not established.
- **Relationships:** Song Cheonwoo followed Cheon Taemin since before Team Leader Choi was born, was Lee Jungryong's former friend and rival, was exiled to Europe after Lee's victory, and is now aligned with Choi against Go Jun.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 562
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Cheon Taemin's only living blood relative and is positioning himself to take control of the Ares Guild after Lee Jungryong's death.
- **Personality:** Strategic, candid, controlled, and possessive of the power and influence he intends to inherit.
- **Voice:** Dry, formal, and direct, with calm candor and carefully chosen metaphors.
- **Relationships:** Maternal grandson and only living blood relative of Cheon Taemin; was kept out of public knowledge by Lee Jungryong and now seeks to acquire the Ares Guild intact.

## Korean source

```text
＃567화



“이 늙은이가 노망이 났나…….”

몇 번째인지 모르겠다. 저 붉은 눈을 마주하는 것이.

이제는 불길함을 넘어 오싹하기까지 한 석고준의 눈빛에, 고세원은 자신도 모르게 마른침을 삼켰다.

하지만 그는 경호팀장이다.

폭주하는 석고준을 잠시나마 멈추게 할 수 있는 유일한 브레이크였고, 장고(長考) 끝에 악수(惡手)를 두려는 상관의 선택을 만류할 의무가 있었다.

“부길드장님.”

석고준의 눈동자가 그를 향했다. 등골이 서늘해지는 듯한 감각에, 고세원은 가까스로 목소리를 끄집어냈다.

“지금 하신 말씀…… 진심이십니까?”

석고준이 눈살을 찌푸렸다.

“당연히 아니지. 고 팀장은 내가 그 정도로 병신처럼 보이나?”

“아.”

설마 하는 마음으로 대답을 기다리던 고세원은 내심 안도의 한숨을 내쉬었다.

하긴, 생각해 보면 말도 안 되는 소리다.

최근 석고준의 성격이 급격히 난폭해진 것은 사실이지만, 송천우의 집안 식구들까지 모조리 죽이라는 명령을 내릴 리는 없…….

“죽이진 말고, 붙잡아 와.”

“예?”

“못 들었나?”

그럴 리가.

고세원은 10m 밖에 있는 모기 날갯짓 소리도 들을 수 있는 A급 헌터다.

그럼에도 다시 한번 묻는 것은, 차라리 안 듣는 것만 못한 말을 들었기 때문이다.

“다시 한번 말씀해 주시겠습니까.”

쾅! 우직!

불과 며칠 전 교체된 테이블이 다시 한번 박살 났다. 석고준의 두 눈동자에서 불길이 솟구쳤다.

“잡아 오라고. 송천우가 매일같이 물고 빤다는 손주 새끼건, 유럽 실버타운에서 만난 백인 할머니건 간에. 그 늙은이 명줄을 쥐고 흔들 수 있는 거라면 뭐든!”

고함이 쩌렁쩌렁 울렸다. 목에 핏대를 세우며 외친 석고준의 목소리가 착 가라앉았다.

“그러니까, 고 팀장. 당장 애들 풀어서 잡아와.”

“……!”

“왜. 이번에도 못 들었나?”

두 번은 없다. 더 이상 물러설 곳이 없음을 깨달은 고세원이 작게 고개를 숙였다.

“아닙니다. 제대로 들었습니다.”

“그럼 바로 움직이면 되겠네. 아, 그 늙은이 집안 식구들이 어디 산다고 했지?”

“런던 외곽 지역입니다. 성을 개조해서 지은 대저택에 일가(一家)가 모여 살죠.”

그야말로 유럽 귀족과도 같은 삶.

일찍이 내부 권력 싸움에서 패배한 송천우가 이런 삶을 살 수 있었던 것은, 이정룡의 묵인과 지원이 있었기 때문이었다.

친구로서의 옛정? 관용? 이정룡에게는 전부 양배추만큼이나 쓸모없는 단어다.

그것은 단지 상대를 몇 수 아래로 내려다보는 자만이 보일 수 있는 오만함이었고, 그 오만함이야말로 압도적인 힘을 지닌 강자의 여유였다.

‘그분은 유일했던 정적(政敵)을 완전히 손아귀에 쥐고 통제했는데, 그분의 뒤를 이은 후계자는 가족들을 납치할 생각부터 하는군.’

타고난 기질. 즉 그릇의 차이다.

순간 머릿속에 떠오른 생각을 빠르게 밀어낸 고세원이 말을 이었다.

“자식 내외와 손주들을 합해서 열세 명 정도인데. 손주 중 몇 명은 헬기나 텔레포트 마법진을 이용하여 통학 중입니다. 물론 실시간으로 위치를 보고받고 있고요.”

“손 썼어? 언제부터?”

“입국 직후입니다. 당시에 보고드렸지만 부길드장님께서 워낙 바쁘신 것 같아, 우선 제 선에서 조치해 뒀습니다.”

“일 잘하네, 우리 고 팀장. 결혼한 후로 감 잃은 줄 알았는데.”

“……감사합니다.”

칭찬과 힐난이 동시에 서린 한마디. 다시금 고개를 숙이는 고세원을 내려다보던 석고준이 문득 서늘한 목소리로 중얼거렸다.

“그나저나 참 은혜도 모르는 늙은이군. 지금까지 자리 보전시켜 준 것만으로 감지덕지했어야지. 이런 식으로 뒤통수를 쳐?”

원래대로라면 새해가 밝기 전 은퇴했어야 할 송천우다.

하지만 중국에서 발생한 몬스터 웨이브와 이정룡의 죽음은 늙은 사자가 마지막까지 버리지 못한 야망에 불씨를 지폈고, 냄새를 맡은 하이에나들은 슬그머니 늙은 사자의 뒤에 줄을 섰다.

대대적인 세대 교체를 앞둔 원로 세대의 중진들.

바로 그들이 하이에나 무리다.

“빌어먹을 노친네들 같으니.”

자리에서 벌떡 일어나 주위를 서성이던 석고준이 불쑥 입을 열었다.

“그놈은?”

그놈.

이름 한 글자 나오지 않은 누군가에 대한 지칭이었지만, 고세원은 즉각 알아들었다.

사실 현재 상황에서 가장 우려되는 것은, 하이에나 무리를 이끄는 늙은 사자가 아니다.

아레스 길드의 높은 울타리 밖, 초원을 어슬렁거리며 기회를 노리는 젊은 숫사자다.

“최민우는 평화 길드로 복귀했습니다.”

“송천우 그 늙은이와 만난 건 확실한 건가?”

고세원이 즉각 대답했다.

“만남 자체도 워낙 은밀했고 고위 환영 마법으로 위장했지만, 확실합니다.”

“홍 이사 그 인간은 어때. 믿을 만해?”

홍 이사는 송천우와 함께 명예퇴직을 앞두고 있던 원로 세대의 한 사람이자, 오늘의 만남을 전해 준 기특한 정보원이다.

고세원이 고개를 끄덕였다.

“예. 상황 판단이 빠르더군요.”

“그 양반이 예전부터 눈치는 귀신이었지. 그래도 방심은 하지 마. 송천우와는 삼십 년 넘게 알고 지낸 사이다.”

“그렇지 않아도 눈치채지 못하는 선에서, 일거수일투족을 감시 중입니다.”

배신의 배신이다. 모두가 저마다의 목적을 이루기 위해 발버둥 치고 있었고, 그중 홍 이사는 얼마 남지 않은 여생의 안락과 생존을 택했을 뿐이다.

“경호팀은?”

“삼십 명 전원, 상시 대기 중입니다.”

경호팀은 아레스 길드 내에서도 특별 선별한 정예였다.

한 사람 한 사람이 A급 헌터로 이루어져 있어 실력은 말할 것도 없고 충성심도 뛰어났다.

갑작스럽게 모시는 주인이 바뀌긴 했지만, 살인 정도는 눈 하나 깜짝하지 않고 해결할 머슴들이다.

‘그리고 나도 마찬가지지.’

고세원은 내심 중얼거렸다.

이정룡의 밑에 있으면서 온갖 더러운 일에 손을 담갔던 그다.

가끔은 그런 자신의 모습에 환멸이 나기도 했지만, 지금까지는 그럭저럭 견딜 만했다.

덕분에 남들은 평생 꿈도 꿀 수 없는 재산을 모았고, 마흔이 넘은 나이에 예쁘고 사랑스러운 지금의 아내를 만나 늦장가도 들었으니까.

하지만…….

‘너무 오랫동안 일했나.’

허기를 잊은 자의 위선인지, 지금껏 억누르고 있던 환멸 때문인지는 모르겠다.

어쩌면 이제 막 걸음마를 시작한 아들과 얼마 전 둘째를 임신한 아내 때문일 수도 있다.

‘송천우. 그 양반 막내 손자가 딱 우리 상호 나이였지, 아마.’

부하들에게 아직 말도 못 하는 어린애를 납치하라는 지시를 전달할 생각에 벌써부터 기분이 묘했다.

‘아니, 납치로 끝나면 다행이겠지.’

근 한두 달 사이, 석고준은 사람이 달라졌다.

극도로 난폭해진 그가 이후에 무슨 일을 벌일지는 아무도 모른다.

그토록 수단과 방법을 가리지 않던 이정룡조차 아이는 건드리지 않았는데…….

“고 팀장.”

생각 도중 들려온 상관의 부름에 고세원의 허리가 꼿꼿이 펴졌다.

“예, 부길드장님.”

“경호팀 준비시켜. 무슨 뜻인지는 알겠지?”

조금 전과 다른 부드러운 목소리에 머리카락이 곤두선다. 잠깐의 침묵 끝에, 고세원의 입술이 열렸다.

“예.”

“최대한 빨리 결과를 받아 봤으면 좋겠는데. 너무 큰 바람인가?”

이미 고세원의 대답은 정해져 있었다.

자신 역시 어차피 결국 같은 똥통 속의 똥일 뿐이다. 한 번 진흙탕에 발을 담근 이상. 돌아가기에는 너무 늦었다.

“아닙니다. 늦어도 내일까지는 좋은 소식을 가져오겠습니다.”

“좋아. 나가 봐.”

대화는 그것으로 끝났다.

굳은 다리를 움직여 집무실을 벗어난 고세원은 귓가에 손을 가져갔다.

삑. 미세한 기계음과 함께 잠시 꺼놨던 통신기에 불빛이 들어왔다.

“현재 인원 보고.”

짤막한 한마디가 끝나기 무섭게, 통신기 너머로 칼 같은 음성이 들려왔다.

- 1팀 전원 대기 중. 이상 무.

- 2팀 전원 대기 중. 이상 무.

- 3팀 전원 대기 중. 이상 무.

세 개 팀을 합쳐 총합 서른. 최고만 모인다는 아레스 길드 내에서도 고르고 고른 인재들이다.

경호팀장답게 압도적인 실력을 지닌 고세원도 이들 중 다섯 이상이 뭉치면 쉽게 승리를 장담할 수 없을 정도이니, 상대가 아무리 철저히 방비해 뒀다 해도 막을 수 없을 것이다.

“부길드장님 명령이다. 한 시간 뒤. 모든 준비를 끝마치고 집결 장소로 이동. 최종 목적지는…….”

순간 멈칫한 고세원이 가라앉은 목소리로 입을 열었다.

“영국, 런던이다.”

이번 여행에는 여권이 필요 없다.

고도의 환영 마법과 특수 분장으로 얼굴과 이름, 심지어는 지문까지 감춘 그들은 정확히 한 시간 뒤에 장거리 텔레포트 마법진 앞에 집결했다.

그리고 휘황한 빛무리를 향해 걸어 들어갔다.

화아아악!



* * *



다음 날 아침, 석고준은 자신의 경호팀장으로부터 기대하던 대답을 들을 수 있었다.

“성공입니다. 경호팀 총원 삼십 명 중 사망자 둘을 제외한…….”

“송천우의 가족들은?”

“……모두 무사히 생포했습니다. 기존 경호 전력으로 위장한 1, 2팀이 남아 저택을 점거하고 감시 중입니다.”

“잘했어. 역시 고 팀장이야.”

“팀원들의 희생이 컸습니다. 최대한 이점을 살려 기습했습니다만, 예상외로 저택의 경비가 삼엄했던 탓에 사망자가 둘이나…….”

“괜찮아. 뒤처리는 문제없이 했겠지?”

짧은 침묵 끝에, 굳게 닫혀 있던 고세원의 입술이 열렸다.

“예. 통신망도 장악했고, 현혹 마법으로 모든 암어와 보고 체계를 알아냈으니 저쪽에서 연락이 오더라도 크게 의심하지 못할 겁니다.”

“예상 유지 기간은?”

“최대 나흘입니다.”

“그 정도면 일을 마무리 짓기에는 충분하지. 송천우, 그 늙은이한테 연락 넣어. 곧 있으면 설날인데, 오랜만에 얼굴이나 보자고.”

곧 마주하게 될 늙은 배반자의 표정을 상상하며 소리 내어 웃던 석고준은 문득 고개를 들었다.

“아, 그리고. 고 팀장.”

뜻을 알 수 없는 묘한 눈빛으로 상관을 응시하던 고세원이 재빨리 안색을 고쳤다.

“예, 부길드장님.”

“미안하군. 워낙 기분 좋은 소식을 들어서 깜빡 잊고 있었어.”

“아.”

“고 팀장도 알다시피 내가 요즘 정신이 없어서. 이해하지?”

“아닙니다!”

조금 전보다 힘찬 대답이 흘러나왔다.

그럼 그렇지. 아무리 사람이 변했어도 이럴 리는 없지.

내심 중얼거린 고세원은 기대하던 말이 나오길 기다렸지만, 뒤이어 들려온 석고준의 한 마디에 우뚝 굳어 버렸다.

“항상 고생이 많다. 이건 따로 넣어 둬.”

“……!”

스윽.

말과 함께 테이블 위에 올려진 새하얀 봉투.

사안이 사안이었던 만큼 적잖은 금액이 적힌 수표가 들어 있을 것이 분명하다. 그간의 경험으로 미루어 보자면 아마도 최소 백억 이상.

하지만 고세원이 바란 것은 금일봉이 든 봉투가 아니었다.

그러나…….

“감사합니다. 부길드장님.”

봉투를 공손히 받아 든 고세원이 허리를 깊이 숙였다.

먼지 하나 없이 반질반질한 대리석 표면에 비친 어떤 사내를 응시하는 그의 눈빛은, 어느덧 깊게 가라앉아 있었다.



* * *



무공은 수많은 동작으로 이루어져 있다.

찌르고, 베고. 때리거나 후려친다.

이와 같은 동작이 연결된다면 비로소 초식(招式)이라 부를 수 있다.

쉭, 파앙!

허공을 향해 내지른 일권(一拳). 압축된 공기가 터지고 머리카락이 흩날린다.

나는 보이지 않는 가상의 상대를 향해 초식을 이어 나갔다.

쉬쉬쉭! 스악!

지금껏 직접 보고, 체득한 깨달음이 초식에 스며든다. 자연스럽게 연계되며 쉴 새 없이 이어진다.

초식의 연결. 바로 투로(鬪路)다.

퍼버버벙!

손날. 팔꿈치. 어깨. 신체의 모든 부위가 회전하고 비틀리며 사방을 때렸다.

무공을 배우며 다시 한번 깨달은 것이 있다면, 무기라는 단어는 비단 날붙이에만 통용되는 것이 아니라는 사실이다.

‘적을 상처입힐 수 있는 모든 것이 무기.’

그렇기에 단련은 중요하다. 손가락 하나만으로도 목을 부러트릴 수 있고, 녹슨 조각칼로도 바위를 가를 수 있다.

후웅. 쾅!

번개처럼 내리꽂힌 발뒤꿈치가 지면을 강타한다. 단단한 외피를 지닌 A급 몬스터라 해도 즉시 두개골이 부서졌을 일격이다.

하지만 지금 이 공간에 쓰러트려야 할 적은 없다.

백여 명, 혹은 백여 마리에 달하는 적들의 시체는 내가 그려 낸 상상 속의 허상일 뿐이니까.

“후우…….”

작게 숨을 내뱉은 그 순간.

짝짝짝.

등 뒤에서 누군가의 힘찬 박수 소리가 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 567

“Has this old man gone senile…?”

Go Se-won had lost count of how many times he had met those red eyes.

The look in Go Jun’s eyes had gone beyond ominous and become downright chilling. Go Se-won swallowed dryly without realizing it.

But he was the Head of Security.

He was the only brake capable of stopping Go Jun’s rampage, even if only for a moment, and it was his duty to dissuade his superior from making a disastrous move after such long deliberation.

“Vice Guild Master.”

Go Jun’s gaze turned toward him. A chill ran down Go Se-won’s spine, but he managed to force out his voice.

“What you just said…… Were you serious?”

Go Jun frowned.

“Of course not. Do I look that much like an idiot to you, Team Leader Go?”

“Oh.”

Go Se-won had waited for the answer with a sinking feeling, so he let out a quiet sigh of relief.

Come to think of it, that would have been absurd.

It was true that Go Jun’s personality had grown violently harsher of late, but there was no way he would order every member of Song Cheonwoo’s family killed……

“Don’t kill them. Bring them here.”

“Excuse me?”

“Didn’t you hear me?”

Of course he had.

Go Se-won was an A-rank Hunter who could hear the flutter of a mosquito’s wings from ten meters away.

The reason he asked again was that he had heard something he would almost rather not have heard.

“Would you repeat that, please?”

*Bang! Crack!*

The table that had been replaced only a few days earlier was smashed to pieces once again. Flames rose in Go Jun’s eyes.

“Bring them here. I don’t care if it’s the grandchild Song Cheonwoo dotes on every day or some white grandmother he met at a retirement community in Europe. If it can be used to get that old man by the throat, bring me anything!”

His shout rang through the room. The veins in his neck stood out as he yelled, but then his voice suddenly sank low.

“So, Team Leader Go. Send the men out and bring them here immediately.”

“……!”

“What? Didn’t you hear me this time either?”

There would not be a third warning.

Realizing that there was nowhere left to retreat, Go Se-won lowered his head slightly.

“No, sir. I heard you clearly.”

“Then get moving. Ah, where did you say that old man’s family lived?”

“On the outskirts of London. The entire family lives together in a huge mansion built by renovating a castle.”

They lived a life worthy of European nobility.

Song Cheonwoo had been able to live that way because of Lee Jungryong’s tacit approval and support, despite having lost the internal power struggle long ago.

Old affection between friends? Mercy? To Lee Jungryong, those were words as useless as cabbage.

It had merely been the arrogance visible only in someone who looked down on another person by several moves, and that arrogance was the leisure of a strong man possessing overwhelming power.

*That man completely controlled his only political rival in the palm of his hand. But the successor who came after him is already thinking about kidnapping the rival’s family.*

Innate temperament.

In other words, the difference in the size of their vessels.

Go Se-won quickly pushed the thought from his mind and continued.

“There are about thirteen of them, counting his children, their spouses, and his grandchildren. Some of the grandchildren commute to school by helicopter or through Teleportation magic circles. Of course, we receive their locations in real time.”

“You made a move? When?”

“Immediately after Song Cheonwoo entered the country. I reported it at the time, but you seemed extremely busy, so I took care of it on my own authority first.”

“You’re good at your job, Team Leader Go. I thought you’d lost your touch after getting married.”

“……Thank you.”

The single remark contained both praise and criticism. As Go Jun looked down at Go Se-won, who bowed his head again, he suddenly muttered in a chilling voice.

“Come to think of it, what an ungrateful old man. He should have been grateful that I let him keep his position all this time. How dare he stab me in the back like this?”

Song Cheonwoo should have retired before the new year arrived.

But the Monster Wave in China and Lee Jungryong’s death had fanned the embers of ambition the old lion had been unable to abandon until the end, and the hyenas that caught its scent had quietly lined up behind him.

The influential members of the elder generation, just before a sweeping change of generations.

They were the pack of hyenas.

“Damn old bastards.”

Go Jun abruptly rose from his seat and began pacing around the room.

“What about him?”

*Him.*

It was a reference to someone whose name had not been spoken even once, but Go Se-won immediately understood.

In truth, the greatest concern in the current situation was not the old lion leading the pack of hyenas.

It was the young male lion prowling the grassland outside Ares Guild’s tall fences, waiting for an opportunity.

“Choi Minwoo has returned to Peace Guild.”

“Are you certain he met with that old man, Song Cheonwoo?”

Go Se-won answered immediately.

“The meeting itself was extremely secretive, and they disguised it with advanced illusion magic, but yes. We’re certain.”

“What about Director Hong? Is he trustworthy?”

Director Hong was one of the elder-generation figures who had been approaching honorary retirement alongside Song Cheonwoo. He was also the useful informant who had passed along word of today’s meeting.

Go Se-won nodded.

“Yes. He judges situations quickly.”

“That man has always been uncannily perceptive. Still, don’t let your guard down. He’s known Song Cheonwoo for more than thirty years.”

“We’re monitoring his every move without crossing the line where he would notice.”

It was betrayal layered on betrayal. Everyone was struggling to achieve their own goals, and Director Hong had simply chosen comfort and survival for the small amount of life he had left.

“What about the security team?”

“All thirty members are on constant standby.”

The security team consisted of elite personnel specially selected from within Ares Guild.

Every one of them was an A-rank Hunter. Their ability went without saying, and their loyalty was exceptional as well.

Their master had suddenly changed, but they were servants who could solve something like murder without batting an eye.

*And I’m no different.*

Go Se-won muttered inwardly.

He had gotten his hands dirty with all kinds of filthy work while serving under Lee Jungryong.

Sometimes he felt disgusted by the person he had become, but until now, he had been able to endure it more or less.

Thanks to it, he had amassed wealth that other people could never dream of in their entire lives. And in his forties, he had met his beautiful, loving wife and married late.

But……

*Have I been doing this for too long?*

He did not know whether it was the hypocrisy of someone who had forgotten hunger or the disgust he had suppressed all this time.

Perhaps it was because of his son, who had only recently begun taking his first steps, and his wife, who had become pregnant with their second child not long ago.

*Song Cheonwoo. His youngest grandson was about the same age as our Sangho, wasn’t he?*

The thought of passing along orders to his men to abduct a child who was too young even to speak properly made him feel strange already.

*No. It would be fortunate if it ended with kidnapping.*

Go Jun had changed over the past month or two.

No one knew what the man would do next now that he had become so violently ruthless.

Even Lee Jungryong, who had never cared what means he used, had never laid a hand on children……

“Team Leader Go.”

At the sound of his superior calling him, Go Se-won’s back straightened.

“Yes, Vice Guild Master.”

“Prepare the security team. You understand what I mean, don’t you?”

His voice was gentler than before, and Go Se-won’s hair stood on end. After a brief silence, his lips parted.

“Yes.”

“I’d like to see the results as soon as possible. Is that too much to ask?”

Go Se-won already knew what his answer would be.

In the end, he was just another piece of shit in the same shit pit. Once he had stepped into the mud, it was too late to turn back.

“No. I’ll bring you good news by tomorrow at the latest.”

“Good. You may go.”

The conversation ended there.

Go Se-won moved his stiff legs and left the office, then raised a hand to his ear.

*Beep.*

A faint mechanical sound rang out, and the communicator he had turned off for a while lit up.

“Report the current personnel.”

As soon as the brief command ended, a sharp voice came through the communicator.

—Team One standing by in full. No abnormalities.

—Team Two standing by in full. No abnormalities.

—Team Three standing by in full. No abnormalities.

The three teams had thirty members in total. Even within Ares Guild, where only the best were gathered, they had been chosen from among the best of the best.

Go Se-won possessed overwhelming skill befitting the Head of Security, but even he could not easily guarantee victory if five or more of these men joined forces. No matter how thoroughly the target had prepared, there was no way to stop them.

“It’s the Vice Guild Master’s order. One hour from now, finish all preparations and move to the assembly point. The final destination is……”

Go Se-won paused, then spoke in a low voice.

“The United Kingdom. London.”

This trip did not require passports.

With advanced illusion magic and special makeup concealing their faces, names, and even fingerprints, they assembled in front of a long-distance Teleportation magic circle exactly one hour later.

Then they walked into the dazzling mass of light.

*Whooosh!*

* * *

The following morning, Go Jun heard the answer he had been waiting for from his Head of Security.

“It was a success. Of the thirty members of the security team, excluding the two fatalities……”

“What about Song Cheonwoo’s family?”

“……They were all captured alive. Teams One and Two remained behind, disguised as the existing security personnel, and have occupied the mansion. They’re keeping watch.”

“Well done. I knew I could count on you, Team Leader Go.”

“The team members paid a heavy price. We exploited every advantage we had and launched a surprise attack, but the mansion was guarded more heavily than expected, and two men were killed…”

“It’s fine. You handled the cleanup without any problems, right?”

After a short silence, Go Se-won’s tightly closed lips opened.

“Yes. We’ve seized their communications network, and we used enchantment magic to learn all their passwords and reporting procedures. Even if their people contact us, they’re unlikely to suspect anything.”

“How long do you expect it to hold?”

“Up to four days.”

“That’s enough time to finish the job. Contact that old man, Song Cheonwoo. Tell him the Lunar New Year is coming soon and that we should meet face-to-face after all this time.”

Imagining the expression on the face of the old traitor he would soon meet, Go Jun laughed aloud. Then he suddenly looked up.

“Oh, and Team Leader Go.”

Go Se-won, who had been staring at his superior with an inscrutable look, quickly composed his expression.

“Yes, Vice Guild Master.”

“Sorry. I heard such good news that I forgot.”

“Oh.”

“As you know, I’ve been out of sorts lately. You understand, don’t you?”

“Of course not!”

The answer came out with more force than before.

*That’s right. No matter how much a person changes, he wouldn’t do something like this.*

Go Se-won muttered inwardly and waited for the words he had been hoping to hear. But at Go Jun’s next remark, he froze in place.

“You’re always working hard. Put this aside for yourself.”

“……!”

*Swish.*

A spotless white envelope was placed on the table.

Considering the nature of the matter, it obviously contained a check for a substantial sum. Judging from his experience, it was probably at least ten billion won.

But the envelope Go Se-won wanted was not one containing a bonus.

And yet……

“Thank you, Vice Guild Master.”

Go Se-won accepted the envelope politely and bowed deeply.

By then, his gaze had grown deep and unreadable as he stared at the man reflected in the spotless, gleaming marble.

* * *

Martial arts consist of countless movements.

Thrusting and cutting. Striking and smashing.

When movements like these are linked together, they can finally be called a form.

*Whoosh. Boom!*

I punched into empty space. Compressed air exploded, and my hair fluttered.

I continued performing forms against an invisible opponent I had imagined before me.

*Whoosh-whoosh-whoosh! Slash!*

The insights I had directly witnessed and absorbed until now flowed into each form. They linked together naturally and continued without pause.

The connection between forms.

That was a combat sequence.

*Boom-boom-boom!*

The edge of my hand. My elbow. My shoulder. Every part of my body rotated and twisted as I struck in every direction.

If learning martial arts had taught me one thing all over again, it was that the word *weapon* did not apply only to sharpened blades.

*Anything that can wound an enemy is a weapon.*

That was why training mattered. A person could break someone’s neck with a single finger, or cut through a rock with a rusty carving knife.

*Whoom. Boom!*

My heel came down like lightning and slammed into the ground. Even an A-rank monster with a hard outer shell would have had its skull crushed instantly by that strike.

But there were no enemies to bring down in this space.

The corpses of a hundred or so human enemies—or perhaps a hundred or so monsters—were nothing more than phantoms I had conjured in my imagination.

“Hoo……”

At the moment I quietly exhaled—

*Clap, clap, clap.*

A vigorous round of applause rang out from behind me.
```
