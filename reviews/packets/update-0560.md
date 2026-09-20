<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0560.txt",
      "sha256": "533ea16550f4f3c15d52783732218172fffb2d8826c51e59902c2a56387bcaaf",
      "bytes": 13522
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5463ad5c2e32bd090f88c49a28da35c221fa817ff3d2e34780a0479d9522d5eb",
      "bytes": 4782
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5eaba5e22911ee46af3a7dd1f504a6fca1d7e7a9bebf347014d58660e5a46d8b",
      "bytes": 177440
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "d073aee3142e875ddc0a16711c73606f382f272b019b3fd057c8363c32dcda24",
      "bytes": 590
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "db461d134e61c5988c1f8f90dc227fe105392035be87ae2b6230b0ccca134dd6",
      "bytes": 793
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "665055234cb13ef7594f09a5991b7dbfe69285542eca69dba1b505c64c5716c2",
      "bytes": 2367
    },
    {
      "path": "characters/Kim Cheol Soo.md",
      "sha256": "26b2906022e9e1b728e571ee9f7274778cae11e6a13ce605ec56e29dd5864f45",
      "bytes": 711
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "2916bd65f94d1634359cefddf3b7f2de10ef95a0fb1bdb98962a00a815d481ee",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1a7c94a9de39573fc1eb198dfeff1d1ea88eda3ff6baae34c2278ebbe5c9dd7f",
      "bytes": 170769
    }
  ],
  "estimated_tokens": 10639
}
-->

# Durable State Update — Chapter 560

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 560. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 560. Profile updates may replace only one
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
  "chapter": 560,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 560,
    "continuity_sources": [560],
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
    "The Fire Dragon Pavilion’s six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can’t Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, leadership of the Fire Dragon Pavilion’s first mission to Nanman, and the Peace Guild’s modern-world patronage.",
    "Mungyeong ended Taekyung’s direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven’s second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam’s transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon’s remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho’s dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi’s mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Lee is being honored as a Great Cataclysm hero, while Taekyung knows the actual deaths were caused by him.",
    "Go Jun is now Ares Guild’s Vice Guild Master and chief mourner for Lee Jungryong, with dozens of A-rank Hunters serving as his new subordinates; he intends to preserve Lee’s legacy and regards Jin Taekyung and Choi Minwoo as its enemies.",
    "Team Leader Choi deliberately revealed his connection to Cheon Taemin as the old hero’s only living blood relative and intends to acquire the Ares Guild with its influence intact before removing Lee’s corruption.",
    "Go Jun possesses a battered necklace recovered from the ruins of the Arch Lich’s former stronghold; it is not Lee Jungryong’s keepsake, but Go Jun bribed an investigation leader to obtain it because he considers it meaningful.",
    "The Peace Guild is piloting a free emergency rescue service for Hunters in the capital region; Mutated Gates are increasing sharply in Korea, while Magic Johnson’s obtained US materials document thirty Mutated Gates and two Monster Waves from the past week."
  ],
  "continuity_sources": [
    559,
    558
  ],
  "open_questions": [
    "What is the Lord of Heaven’s identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung’s party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo’s political engagement end?",
    "What process created Jang Sam’s mutant form, whether Dark Heaven’s mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "How many additional Gate disasters are being concealed, and what is driving the accelerating Mutated Gate and Monster Wave outbreaks?"
  ],
  "safe_through": 559,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can’t Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant’s Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, and 대마도사 as Grand Mage; retain the established renderings for Small Cataclysm, Arch Lich, Skeleton King, Forest of Giants, Cyclops, and Ent.",
    "Render 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, 몬스터 웨이브 as Monster Wave, 모하비 사막 as Mojave Desert, and 애리조나주 as Arizona."
  ],
  "version": 1
}
```

## Exact glossary matches

| 철수     | **Cheol Soo**      |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 임꺽정 | **Im Kkeokjeong** |
| 김철수 | **Kim Cheol Soo** | C-rank junior Hunter in Myeongdong Guild's Security Team. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 국가장 | **national funeral** | State funeral held for Lee Jungryong. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 조셉 | **Joseph** | Hunter named in the recorded Monster Wave footage. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 555
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 555
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's new Vice Guild Master, Lee Jungryong's disciple and former security-team leader, and the chief mourner at Lee's national funeral.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death and regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 559
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild; attacked by three Black Hunters following a solo drinking outing, with both arms severed below the elbows; his wounds were treated with high-ranking healer recovery magic and advanced potions, his arms were reattached, and he regained consciousness after three days; he has chosen to continue as a Hunter and remain with the Peace Guild after recovering; after beginning the Jin Family’s Cultivation Technique, he completed a complete circulation and learned to perform the Small Circulation independently on the first day, adapting unexpectedly quickly; repeated circulation is expected to improve his physical foundations, and resolving his trauma may allow an early return to Guild work
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Kim Cheol Soo.md

# Kim Cheol Soo (김철수)

- **Safe through:** Chapter 389
- **Aliases:** None
- **Role:** C-rank Hunter in Myeongdong Guild's Security Team; a junior employee who has been with the Guild for roughly one month.
- **Personality:** Rigid, conscientious, strongly patriotic, and intensely loyal to Guild regulations and company duty.
- **Voice:** Earnest and formal; objects directly to unauthorized conduct and reacts fervently to praise from a famous Hunter.
- **Relationships:** Junior colleague of an unnamed senior Security Team Hunter; admires Jin Taekyung and is deeply affected when Taekyung says he will recommend him to Park Tae Seop.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 559
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃560화



홀리 쉿. 왓 더 퍽.

알고 있는 영미권 욕을 총동원해도 지금의 좆 같음을 전부 표현할 수 없다.

‘일주일에 서른두 번이라니.’

실로 어마어마한 수치. 심지어 이것조차 매직 존슨이 입수한 정보에 한해서다.

정확한 통계가 얼마나 되는지 모르겠지만, 최소한 서른두 번보다는 많을 것이 분명했다.

‘그래, 어쩌면 당연한 일일지도 모르지.’

미국 국토는 대한민국 면적의 98배, 게이트의 숫자는 근 스무 배에 달한다.

미국은 과거 마왕 아스모데우스의 최우선 타겟이 되어 대격변 내내 엄청난 피해를 입어야 했다.

그러나 아이러니하게도 그런 미국을 다시 최강대국의 자리에 올려놓은 일등 공신은 전쟁이 남기고 간 게이트의 존재였다.

‘유전(油田).’

현대의 게이트는 말 그대로 새롭고, 더욱 풍족해진 형태의 유전이다.

전 세계를 집어삼켰던 재앙이 끝난 지 어느덧 삼십여 년. 몬스터의 부산물은 값비싼 가격에 팔리고 마정석은 친환경적 에너지원이 된 지 오래다.

살아남은 인류는 전쟁으로 황폐해진 폐허 위에 더욱 눈부시고 거대한 문명을 이룩했다.

하지만…….

「파티도 여기까지인 것 같군.」

매직 존슨의 던진 한마디처럼, 승자들의 화려한 파티는 이제 끝났다.

게이트라는 유전에 불이 붙었으니 곧 세계 곳곳에서 폭발이 일어날 것이다. 아니, 이미 일어나고 있었다.

지금은 단지, 보이지 않는 손이 모든 것을 가리고 있을 뿐이다.

“아, 씨바…….”

신음처럼 중얼거린 내가 최 팀장을 향해 물었다.

“설마 국내 상황도 비슷한 건 아니죠?”

내가 던진 질문은, 미국에서 벌어지는 일처럼 내가 모르는 또 다른 사건이 있느냐는 뜻을 품고 있다.

잠시 생각에 잠겼던 최 팀장이 입을 열었다.

“혹시 모를 가능성은 늘 염두에 두고 있습니다만, 제가 알기로는 없습니다.”

“최 팀장님, 이거 확실해야 하는 문제예요.”

“잘 알고 있습니다. 그래서 이참에 다시 한번 자리를 마련해 볼 생각이고요.”

이야기를 듣고 있던 매직 존슨이 물었다.

「자리? 누구랑?」

“어쩌다 보니 인연이 닿게 된 분들입니다. 그분들이 제게 거짓말을 하셨을 리는 없겠지만…… 사람 마음이라는 건 모르는 거니까요.”

「그렇지. 특히 정치인들은.」

매직 존슨이 툭 던진 한마디에, 최 팀장이 조용히 고개를 끄덕였다.

“역시 알고 계셨군요.”

「미스터 리의 영결식 때 워낙 바빠 보였으니까. 최를 찾는 사람이 많던걸.」

나와 최 팀장 역시 이정룡의 국가장에 참석하여 조의를 표했다.

품고 있는 속마음은 달랐지만, 그건 대중에게 보이는 표면적인 이미지 때문만이 아니었다.

“그들도 새로운 그늘을 찾는 거겠지요. 저 역시 바라던 바였고요.”

정계, 재계. 그리고 아레스 길드에 의해 짓눌려 있던 중, 대형 길드의 핵심 인사들은 우리에게 지대한 관심을 보였다.

물론 그중 과반수에 달하는 인원은 가장 먼저 나를 찾아왔지만, 내가 그들에게 해 줄 대답은 처음부터 정해져 있었다.



‘저 같은 헌터 나부랭이 말고, 우리 최 팀장님과 얘기하시죠.’



온갖 거물들이 득실거리는 이정룡의 영결식에 한 자리를 얻었다는 것은, 치열한 투쟁 끝에 이 사회에서 저마다의 승리를 거머쥔 자들이라는 뜻.

그들은 내 말이 의미하는 바를 정확히 알아들었고, 곧장 최 팀장과의 만남을 위해 동분서주했다.

「힘없는 자는 무시받지만, 힘 있는 자들에게는 곳곳에서 손을 내미는 법이지. 세상이 아무리 달라졌어도 그 사실만큼은 변하지 않아.」

매직 존슨의 말은 날카로운 진실이었다.

누구도 찾지 않았던 나와 최 팀장. 아니, 평화 길드는 어느덧 아레스 길드에게 맞설 유일한 대항마로 급부상했다.

대중들은 모르겠지만 이 사회의 위층에 자리한 이들은 누구보다 그 사실을 잘 알고 있다.

지금쯤 정, 재계의 인사들은 두 세력 간의 싸움에서 어떤 이득을 취할 수 있을지, 누구의 그늘로 들어가야 더 시원할지 머리를 굴리고 있을 터였다.

또한 중, 대형 길드의 주인들은 이 기회에 아레스 길드의 과독점 체제를 벗어나고 싶겠지.

그렇게 최 팀장은 새로운 지원군과 그들이 가진 힘을 얻었다.

아레스라는 만찬을 모조리 소화시키기 위한 첫발을 뗀 것이다.

그래서일까. 다음 순간 거스러미 하나 없는 입술 사이로 흘러나온 최 팀장의 목소리에는, 그 어느 때보다 강한 힘이 실려 있었다.

“그들이 내민 손을, 저는 거절하지 않을 겁니다.”

그런 최 팀장을 물끄러미 바라보던 매직 존슨이 불쑥 입을 열었다.

「아무래도…… 사실이었던 모양이군.」

“뭐가 말입니까?”

「그 소문. ‘그’와 최가 연관이 있다는 이야기 말이야.」

“더 이상 감출 이유도 없죠. 맞습니다.”

매직 존슨의 눈동자가 커졌다.

「최가 이렇게 쉽게 시인할 줄은 몰랐는데. 아니면 새롭게 인연이 생긴 다른 사람들에게는 아마 모두 털어놓은 건가?」

“아닙니다. 하지만 그들도, 저도 말은 하지 않았지만 이미 알고 있습니다. 제 몸에 흐르는 피가 누구로부터 이어졌는지.”

피식. 대마도사의 두꺼운 입술 사이로 실소가 흘러 나왔다.

「그래, 그 사실은 누구도 부정할 수 없겠지. 그야말로 21세기에 존재하는 유일한 순수혈통이야.」

현존하는 어떤 귀족(貴族)이나 왕족(王族)도 최 팀장에 비할 수는 없다.

설령 그 콧대 높은 영국의 펠릭스 왕자가 국왕이 된다 해도 마찬가지다.

그의 선조가 해가 지지 않는 거대한 제국을 건설했다면, 천태민은 수십억의 인류가 내일의 해를 볼 수 있게 만든 구세주니까.

「그리고 그에 관해 직접적으로 언급하지 않은 것은 현명하다고 해 두겠네. 과묵하고 스스로를 쉽게 드러내지 않는 사람은 신뢰를 부르는 법이거든.」

“칭찬 감사합니다.”

「감사할 필요 없어. 사실이니까.」

평소 유쾌하고 장난을 즐겨 하던 모습은 이제 찾아볼 수 없다. 매직 존슨이 침착한 목소리로 말을 이었다.

「하지만 최, 부디 명심해. 지금은 어디 있는지 모르는 자네 조부도, 그리고 나도 무엇이 우선인지는 늘 알고 있었어. 더 나은 미래를 위해 목숨을 걸고 싸웠지. 이런 걸 동양에서는 대의(大意)라고 부른다고 하던가?」

“……!”

지금은 아레스 길드보다 코앞에 닥친 사태를 막아야 한다는 것을 에둘러 말하는 매직 존슨의 한마디에, 잠시 침묵하던 최 팀장이 대답했다.

“명심하겠습니다, 미스터 존슨. 하지만 제가 아레스 길드를 노리는 것은, 사적인 이유 때문만이 아닙니다.”

「알아. 최가 어떤 사람인지. 만일을 대비하여 아레스를 약화시키고, 평화 길드 자체의 힘을 키울 생각이겠지. 그 정도 이빨로는 호랑이를 집어삼킬 수는 없는 법이니까.」

최 팀장이 쓰게 웃었다.

“하이에나라……. 부정할 수는 없군요.”

이정룡이라는 구심점이 사라졌어도 아레스는 아레스다.

평화 길드는 내 존재로 인해 전 세계에 이름을 각인시키며 급성장했지만, 수십 년간 아레스 길드가 쌓아 올린 철옹성을 단번에 무너트릴 수는 없었다.

「개인의 영달을 추구하지 않는 선에서 계속 힘을 키우게. 나와 위저드(Wizard) 길드가 돕지. 필요하다면 사적으로 친분이 있는 몇몇 친구도 기꺼이 소개해 줄 수 있고.」

“예, 그럴 생각입니다. 과거의 악연이 아직 끝나지 않았으니까요.”

「그 젊은 친구를 말하는 거로군. 미스터 석.」

매직 존슨이 문득 미간을 좁혔다.

「비록 그를 가까이서 오랫동안 지켜본 것은 아니지만, 그리 친절한 성격이 아니라는 것 정도는 알고 있었지. 그렇지 않나. 진?」

나는 즉각 고개를 끄덕였다.

“좆 같은 새끼죠.”

「성부터 느낌이 와. 발음부터가 Suck이야. 한창 조사 중이던 아크 리치의 근거지에서 진을 습격했을 때부터 영 느낌이 좋지 않았는데…….」

매직 존슨이 심각한 표정으로 말을 이었다.

「그 친구는 잠시 못 본 사이에 더 위험한 냄새를 풍기더군. 진, 자네가 내 바로 앞이었는데 혹시 못 느꼈나?」

“…….”

「진?」

잠시 머뭇거리던 내가 대답했다.

“그, 제가 앞에서 방귀를 뀌긴 했습니다.”

「What rhe Fuck…….」

“아무리 그래도 욕은 좀. 그리고 석고준 그 새끼야 원래 위험한 놈이고요.”

「후우. 그건 그렇지. 하지만 앞으로는 내가 자네 뒤에 있을 때 방귀 뀌는 건 자제해 줘.」

“……예.”

매직 존슨에게 뒤를 맡긴 나도 만만치 않게 불안했었지만, 결국 방귀를 뀐 건 나였으니 뭐라 할 말이 없다.

슬쩍 시선을 회피하며 대답하는 내 모습에, 코를 씰룩거리던 매직 존슨이 입을 열었다.

「좋아. 오늘 이야기는 이 정도면 충분한 것 같군. 다른 사람은 몰라도 나만큼은 두 사람을 굳게 믿고 있다는 것을 알아줬으면 해.」

따뜻한 눈빛으로 나와 최 팀장을 바라보던 그가 멀뚱멀뚱 서 있는 두 사람. 아니, 한 사람과 한 몬스터를 향해 덧붙였다.

「아, 물론 자네들도.」

스켈레톤 킹과 임꺽정이 동시에 대답했다.

“게이바나 데려가지 마라.”

“아, 아이 돈 스피크 잉글리쉬.”

「……아주 든든하군.」

말과는 상반되는 표정으로 중얼거린 매직 존슨이 품에서 작은 유리병을 꺼내 쭉 들이켰다.

유리병의 정체가 소모된 마나를 보충시켜 주는 포션이라는 깨달은 내가 물었다.

“가시게요?”

「이만 돌아가야지. 지금부터는 나도 많이 바빠질 테니까. 요새 보지 못한 친구들에게도 연락을 돌려 봐야겠어.」

“친구분들이라면……?”

「조금 전에 언급했던 친구들이지. 비록 절반 정도는 은퇴했지만, 상당한 도움을 줄 수 있을 거야. 아. 혹시 최가 원한다면 지금 바로 데려가 줄 수 있는데. 어떤가?」

매직 존슨의 뜨거운 눈빛에 주춤한 최 팀장이 빠르게 고개를 저었다.

“괘, 괜찮습니다.”

「아쉽군. 조셉 그 친구가 최에게 관심이 있던데.」

“저도 아쉽지만 다음에…… 잠깐. 지금 조셉이라고 하셨습니까?”

「자네 귀가 잘못되지 않았다면 제대로 들은 게 맞아.」

“그럼 설마. 혹시 미국 전 대통령인 조셉 바이든?”

「맞아. 꽤 오래전에 은퇴했지만 한 달에 한 번 정도는 만나서 술도 마시는 사이지. 그 친구야 워낙 늙은 탓에 거의 못 먹지만.」

“……!”

놀란 것은 최 팀장뿐만이 아니다. 나는 물론이고 임꺽정까지 입을 딱 벌렸다.

“그 조셉 바이든?”

“아, 아이 노우! 아이 노우 조셉 바이든!”

미국 대통령 이름이 차쿰바 오쿰보건 김철수건 별 관심 없지만, 조셉 바이든이라는 이름은 헌터 훈련소에서부터 익히 들었다.

하필 재임 기간에 대격변이 들이닥치는 바람에, 히어로 영화 속 뉴욕 시장보다도 고생을 많이 한 미국 대통령이 아닌가.

‘인맥 클라스 보소.’

미국에서는 조지 워싱턴을 이은 제2의 국부(國父)나 다름없는 사람.

매직 존슨이 대단한 줄은 알았지만, 이 정도로 화려한 인맥을 자랑하는 줄은 몰랐다.

「그렇게 볼 것 없어. 나와는 50년 가까이 알고 지낸 불알친구지만, 대부분은 모르는 개인적인 관계니까.」

“……!”

순간 얼어붙은 최 팀장의 표정에, 매직 존슨이 재빨리 덧붙였다.

「불알이라는 단어는 빼지. 그냥 친구야, 절친.」

“휴우.”

「Shit. 내가 이런 변명까지 해야 하나?」

“미스터 존슨. 한국에는 뿌린 만큼 거둔다는 속담이 있습니다.”

「빌어먹을. 된통 당했군. 그래서, 어떻게 할 거야. 최?」

최 팀장이 망설임 없이 대답했다.

“가시죠. 신세 좀 지겠습니다.”

「좋은 생각이야. 대륙 간 이동이라 멀미는 좀 나겠지만.」

“그깟 멀미가 대수겠습니까.”

덤덤하게 대꾸한 최 팀장은 매직 존슨이 내민 손을 붙잡았다.

가벼운 눈인사와 함께, 막대한 양의 마나가 두 사람의 전신을 빈틈없이 감쌌다.

화아아악!

터져 나온 눈부신 섬광이 두 사람의 신형을 어디론가 날려 버린 바로 그 순간.

우우우웅.

남아 있는 셋. 나와 임꺽정, 그리고 스켈레톤 킹의 스마트폰이 거센 진동을 토해 냈다.
```

## Final English reading copy

```markdown
# Chapter 560

Holy shit. What the fuck.

Even if I brought out every English-language curse I knew, I still couldn’t express how utterly fucked things were.

*Thirty-two times in a single week.*

It was an outrageous number. And even that only covered the information Magic Johnson had managed to obtain.

I had no idea what the exact statistics were, but it was obvious there had been more than thirty-two incidents.

*Yeah. Maybe this was inevitable.*

The United States was ninety-eight times the size of Korea, and it had nearly twenty times as many Gates.

The United States had also been Demon King Asmodeus’s top-priority target in the past, suffering tremendous damage throughout the Great Cataclysm.

But ironically, the thing that had once again elevated the United States to the position of the world’s greatest power was the very existence of the Gates left behind by the war.

*Oil fields.*

Modern Gates were literally new, far more abundant oil fields.

More than thirty years had passed since the disaster that swallowed the entire world. Monster byproducts had long since become expensive commodities, and Magic Gems had become an environmentally friendly energy source.

The surviving human race had built an even more dazzling and enormous civilization atop the ruins left behind by the war.

But…

“The party seems to be over.”

Like Magic Johnson’s offhand remark, the lavish party of the winners was finally coming to an end.

The oil fields called Gates had caught fire. Soon, explosions would erupt all over the world.

No—they were already happening.

For now, an invisible hand was merely covering everything up.

“Ah, fuck…”

I muttered like a groan, then asked Team Leader Choi,

“Domestic conditions aren’t similar, are they?”

My question meant more than what I had said aloud. I was asking whether there were other incidents I didn’t know about, like the ones happening in the United States.

Team Leader Choi, who had been lost in thought for a moment, opened his mouth.

“I always keep unexpected possibilities in mind, but as far as I know, there aren’t any.”

“Team Leader Choi, this is something we need to be certain about.”

“I know. That’s why I’m thinking of arranging another meeting while I have the chance.”

Magic Johnson, who had been listening to us, asked,

“A meeting? With whom?”

“People whose paths happened to cross with mine. I can’t imagine they would have lied to me, but you never know what people are thinking.”

“True. Especially politicians.”

At Magic Johnson’s offhand remark, Team Leader Choi quietly nodded.

“So you knew.”

“Choi looked awfully busy at Mr. Lee’s national funeral. A lot of people were looking for him.”

Team Leader Choi and I had also attended Lee Jungryong’s national funeral to pay our respects.

Our true feelings had been different, but it wasn’t only because of the public image we had to maintain.

“They’re looking for a new shadow to shelter under. I was hoping for the same thing.”

People from the political and business worlds, along with key figures from the mid-sized and large Guilds that had been crushed beneath Ares Guild, had shown tremendous interest in us.

Of course, more than half of them had come looking for me first. But I had known from the beginning what my answer would be.

*Don’t talk to some Hunter nobody like me. Go talk to our Team Leader Choi.*

Earning a place at Lee Jungryong’s national funeral, where every kind of heavyweight had gathered, meant they were people who had claimed their own victories in society after fighting tooth and nail.

They understood exactly what I meant and immediately began scrambling to arrange meetings with Team Leader Choi.

“The powerless are ignored, but people extend their hands in every direction to those with power. No matter how much the world changes, that fact never does.”

Magic Johnson’s words were a sharp truth.

No one had ever sought out me or Team Leader Choi before.

No—the Peace Guild had risen to become the only force capable of standing against Ares Guild.

The public might not know it, but the people sitting at the top of society knew it better than anyone.

By now, political and business leaders were probably racking their brains over how much they could profit from a clash between the two forces, and whose shadow would offer them the most room to breathe.

The owners of the mid-sized and large Guilds probably wanted to use this opportunity to escape Ares Guild’s excessive monopoly as well.

And so Team Leader Choi had gained new allies and the power they possessed.

He had taken his first step toward digesting the entire feast called Ares.

Perhaps that was why, when Team Leader Choi’s voice flowed between his perfectly smooth lips a moment later, it carried more strength than ever.

“I won’t reject the hands they’ve extended.”

Magic Johnson gazed at Team Leader Choi, then suddenly spoke.

“So… it seems the rumor was true.”

“What are you talking about?”

“That rumor. The one saying that Choi is connected to *him*.”

“There’s no reason to hide it anymore. It’s true.”

Magic Johnson’s eyes widened.

“I didn’t expect Choi to admit it so easily. Or have you already told everyone else you’ve newly crossed paths with?”

“No. But they know, and so do I, even though none of us has said it aloud. We know whose blood flows through my veins.”

A quiet laugh escaped between the Grand Mage’s thick lips.

“Right. No one can deny that fact. He’s the only pureblood in existence in the twenty-first century.”

No living noble or royal could compare to Team Leader Choi.

Not even if the arrogant Prince Felix of the United Kingdom became king.

If his ancestor had built a vast empire upon which the sun never set, then Cheon Taemin was the savior who had allowed billions of people to see the sun rise on another day.

“And I’ll say that not mentioning him directly was wise. Quiet people who don’t reveal themselves easily inspire trust.”

“Thank you for the compliment.”

“Don’t thank me. It’s simply a fact.”

The cheerful, playful Magic Johnson of usual was nowhere to be seen. He continued in a calm voice.

“But Choi, keep this in mind. Your grandfather, wherever he may be now, and I have always known what came first. We risked our lives and fought for a better future. Is that what people in the East call a greater cause?”

“...!”

Magic Johnson was indirectly telling him that stopping the crisis looming directly ahead had to take priority over Ares Guild.

After a brief silence, Team Leader Choi answered,

“I’ll keep that in mind, Mr. Johnson. But my reason for targeting Ares Guild isn’t purely personal.”

“I know what kind of person Choi is. You intend to weaken Ares in preparation for the worst while strengthening the Peace Guild itself. You can’t swallow a tiger with teeth like that.”

Team Leader Choi gave a bitter smile.

“A hyena… I can’t deny it.”

Even though the central figure named Lee Jungryong was gone, Ares was still Ares.

The Peace Guild had grown explosively, etching its name into the minds of people around the world because of my existence. But it couldn’t tear down in one blow the impregnable fortress Ares Guild had built over decades.

“Keep increasing your strength without pursuing personal glory. The Wizard Guild and I will help you. If necessary, I can even introduce you to a few friends I know personally.”

“Yes. That’s what I intend to do. The bad blood from the past hasn’t run its course yet.”

“You mean that young fellow. Mr. Seok.”

Magic Johnson suddenly drew his brows together.

“Although I haven’t watched him closely for very long, I know he isn’t a particularly kind person. Isn’t that right, Jin?”

I nodded immediately.

“He’s a fucking asshole.”

“I could tell from his surname. Even the pronunciation sounds like ‘suck.’ I already had a bad feeling about him when he attacked Jin at the Arch Lich’s stronghold, while we were still investigating…”

Magic Johnson continued with a serious expression.

“But that fellow gives off an even more dangerous smell now than he did before. Jin, you were standing right in front of me. Didn’t you notice?”

“…”

“Jin?”

After hesitating for a moment, I answered,

“Well, I did fart in front of you.”

“What the fuck…”

“Even so, there’s no need to swear. And Go Jun was already a dangerous bastard to begin with.”

“Whew. That’s true. But from now on, please refrain from farting when I’m standing behind you.”

“...Yes.”

I had been uneasy about having Magic Johnson at my back too, but I had been the one to fart in the end, so I had nothing to say.

Magic Johnson’s nose twitched as I answered while subtly avoiding his gaze. Then he opened his mouth.

“All right. I think that’s enough for today. I want you two to know that, whatever anyone else may think, I trust you both completely.”

He looked warmly at Team Leader Choi and me before turning to the two people—no, the one person and one monster—standing there blankly and adding,

“Well, of course, you two as well.”

The Skeleton King and Im Kkeokjeong answered at the same time.

“Don’t take us to a gay bar.”

“I-I don’t speak English.”

“...Very reassuring.”

Magic Johnson muttered that with an expression utterly at odds with his words, then pulled a small glass bottle from inside his clothes and drained it in one go.

I realized that the bottle contained a potion for replenishing spent mana and asked,

“Are you leaving?”

“I should head back. I’m going to be quite busy from now on, too. I need to get in touch with some friends I haven’t seen in a while.”

“Your friends?”

“The ones I mentioned earlier. Half of them have retired, but they should still be able to help quite a bit. Oh. If Choi wants, I can take him to meet them right now. What do you say?”

Team Leader Choi hesitated under Magic Johnson’s eager gaze, then quickly shook his head.

“N-No, that’s all right.”

“What a shame. My friend Joseph was interested in meeting Choi.”

“I’m disappointed too, but maybe next time… Wait. Did you say Joseph?”

“Unless your ears have gone bad, you heard me correctly.”

“Then don’t tell me. Could you mean former United States President Joseph Biden?”

“That’s right. He retired a long time ago, but we meet about once a month and have a drink together. Though he’s so old he can barely drink anymore.”

“...!”

Team Leader Choi wasn’t the only one shocked. I gaped as well, and even Im Kkeokjeong’s jaw dropped.

“That Joseph Biden?”

“Ah, I know! I know Joseph Biden!”

I didn’t care whether the name of the American president was Chakumba Okumbo or Kim Cheol Soo, but I had heard the name Joseph Biden many times since my days at the Hunter training camp.

The Great Cataclysm had struck during his time in office, so he had suffered even more than the mayor of New York in a superhero movie.

*Look at the level of his connections.*

In the United States, he was practically the second Founding Father after George Washington.

I had known Magic Johnson was impressive, but I had never realized he could boast connections this extravagant.

“Don’t look at me like that. Joseph and I have been intimate friends for nearly fifty years, but most people don’t know about our personal relationship.”

“...!”

Team Leader Choi froze, and Magic Johnson hurriedly added,

“Forget I said ‘intimate.’ We’re just friends. Best friends.”

“Whew.”

“Shit. Do I really have to make excuses like this?”

“Mr. Johnson, we have a saying in Korea: you reap what you sow.”

“Damn it. I really got what I deserved. So, what are you going to do, Choi?”

Team Leader Choi answered without hesitation.

“Let’s go. I’ll impose on you.”

“Good idea. You might get a little motion sick traveling between continents, though.”

“What’s a little motion sickness compared to this?”

Team Leader Choi answered calmly and took the hand Magic Johnson held out to him.

With a light nod, an enormous amount of mana wrapped tightly around their entire bodies.

*Whoooosh!*

At that exact moment, a blinding flash erupted and sent their figures flying somewhere else.

*Brrrrrrr.*

The smartphones belonging to the three people left behind—Im Kkeokjeong, the Skeleton King, and me—began vibrating violently.
```
