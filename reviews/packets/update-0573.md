<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0573.txt",
      "sha256": "3b1fef54306933b69c0cb4f291fa01e6018347a7b74dd6d3f76d8f514e9b4548",
      "bytes": 12770
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "397b45dfbe858958a83a6b84871c1993a40aec7bfb9270c2532e2dc510f5cab6",
      "bytes": 4171
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "190d7ff85990b85fd5adad0584f486fc89b16e0889ba889f2a7b12d100c6ef40",
      "bytes": 180890
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8ee5ccdf280dc76affc1916ae52e4932dc3e459b47c9d9b9b7f3cc7cd0efde8f",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c82461dfe17ccd7f239caa4269eb7d4bc610e12fe2d53a38693367bba4bab815",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "772f92bb9b39617d272e0019a62c56c8067cbf832b1a9c1c391b9bf83b0c9db4",
      "bytes": 177134
    }
  ],
  "estimated_tokens": 9422
}
-->

# Durable State Update — Chapter 573

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 573. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 573. Profile updates may replace only one
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
  "chapter": 573,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 573,
    "continuity_sources": [573],
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
    "The Busan Monster Wave is led by an intelligent Kraken that was transformed by absorbing magic power from a gift supplied by Dongseok on behalf of “that person.”",
    "The Kraken killed Dongseok, opened a rift into the surface world, led nearly a thousand Mermen and Sirens ashore, and severed Gwangan Bridge while attacking civilians.",
    "Taekyung has engaged the Kraken, cut several tentacles with White Flame and Force carrying Scorching Yang Qi, and is continuing an unresolved close-quarters battle near the collapsed bridge.",
    "Dongseok’s objective and the identity of “that person” remain unknown.",
    "The worldwide Gate and monster crisis may mark the beginning of a second Great Cataclysm; rising magic power readings are strengthening monsters, Mutated Gates now appear roughly every three days, and Hunter shortages are worsening.",
    "Team Leader Choi says the crisis has exceeded the limit of national concealment and is prioritizing Gate defenses despite reducing Peace Guild’s raid capacity; she is working with Song Cheonwoo against Go Jun’s control of Ares Guild while Song knows where Cheon Taemin is hidden.",
    "Taekyung is a Supreme Peak master publicly recognized as S-rank-level while retaining an A-rank license, leads the Fire Dragon Pavilion’s first Nanman mission, and is Peace Guild’s wealthy modern-world patron.",
    "The six-member Fire Dragon Pavilion mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is Can’t Go to Nanman.",
    "Mungyeong ended Taekyung’s direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong.",
    "Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants, while the mechanism behind Jang Sam’s transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon’s remains.",
    "Go Jun has become increasingly ruthless, controls Ares Guild’s legacy, has seized Song Cheonwoo’s children as leverage, and appears to be arranging Song’s quiet elimination; Go Se-won commands Ares Guild’s thirty-member A-rank security team while remaining obedient despite growing moral conflict."
  ],
  "continuity_sources": [
    572,
    571
  ],
  "open_questions": [
    "What is the identity of “that person,” how is that figure connected to the Lord of Heaven and Dark Heaven, and how can Dark Heaven or its agents open rifts and Gates?",
    "What will Taekyung’s party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam’s mutant form, whether Dark Heaven’s mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What caused the Haeundae Gate’s transformation, what is the object entrusted to Lee Dongseok, and what does his mission require?",
    "What will result from Taekyung’s unresolved Kraken battle, Jeok Cheongang’s duel with Nangong Cheon, Ju Hwaran and Sama Pyo’s broken engagement, Go Jun’s plan for Song Cheonwoo’s children, and Taekyung’s unfinished training project?"
  ],
  "safe_through": 572,
  "temporary_decisions": [
    "Render 크라켄 as Kraken and 그것 as the thing; identify the creature as the Kraken only when the narration does so.",
    "Render 마력 as magic power, 머맨 as Merman, 세이렌 as Siren, and retain Monster Wave.",
    "Render 광안대교 as Gwangan Bridge and 현수교 as suspension bridge.",
    "Render 동석 씨 as Mr. Dongseok, 김 팀아 as Team Leader Kim, and 그분 as that person.",
    "Retain White Flame, Force, Scorching Yang Qi, Stepping on Empty Air, dry rations, Guangxi, Mount Daebyeol, Ten-Thousand-Li Journey, Going Merry, Busan, Haeundae, Pocheon, Gyeonggi Province, and Siren’s Black River."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 대한민국 | **Korea** | Country reference. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 크라켄 | **Kraken** | Sea monster leading the Monster Wave; newly identified in this chapter. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 570
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 570
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃573화



모든 것에는 순서와 단계가 있는 법.

당연하게도 이는 변이 게이트에도 적용되는 부분이었다.

마력 수치가 일정 수준을 돌파하면, 위험을 알리는 경보음과 함께 인근에 있는 모든 사람에게 대피령이 떨어진다.

그러나 평범했던 C급 게이트가 변이 게이트를 넘어 몬스터 웨이브(Monster Wave)에 이르기까지 걸린 시간은 불과 수십 초 남짓.

전례 없는 아득한 수치에 해당 게이트 관리소에서는 측정 오류를 의심할 수밖에 없었다.

1분도 채 되지 않은 짧은 고민은 공간을 찢고 현세에 강림한 크라켄이 가장 먼저 게이트 관리소를 박살 내며 끝났다.

쾅!

그리고 재앙의 불길은 삽시간에 사방으로 번졌다.

크라켄은 검은 바다의 공포인 동시에 강력한 힘을 지닌 왕. 그런 왕의 휘하에는 흉폭하고 충성스러운 군사들이 있었다.

- 시시시싯!

쉴 새 없이 움직이는 지느러미와 뻐끔거리는 아가미.

기묘한 울음소리를 흘리는 머맨(Merman)의 등장에, 차량과 인파로 북적이던 사거리가 일순 침묵에 잠겼다.

“저게 뭐…….”

누군가의 의문 어린 목소리는 끝까지 이어지지 못했다.

쉬익, 뻑!

그야말로 찰나에 벌어진 일이었다.

따개비가 달라붙은 삼지창은 인간의 몸을 꿰뚫고 그대로 날아가, 신호 대기 중이던 차량마저 관통했다.

쾅!

폭발음과 함께 사방으로 튀는 차량 파편.

사람들이 멍하니 그 비현실적인 광경을 바라보고 있을 때, 사거리 곳곳에 설치한 경보기와 각자의 스마트폰으로 위험 신호가 전달되었다.

위이이이이잉!

띠링. 삐비빅. 우우웅.

침묵을 깨트리는 소음.

화염에 휩싸인 차량과 우뚝 서 있는 머맨을 번갈아 바라보던 사람들은 그제야 자신들의 코앞에 닥친 위험을 깨달았다.

“모, 몬스터!”

“몬스터 웨이브다!”

“꺄아아아아악!”

비명과 함께 거리를 오가던 수많은 인파가 삽시간에 흩어졌다.

몬스터에게서 조금이라도 멀어지기 위해, 살아남기 위해 발버둥 치는 그들의 머릿속에는 이미 규칙과 법 따위는 존재하지 않았다.

“씨발, 비켜!”

“자, 잠깐……!”

우당탕! 우직!

“크아아악!”

사람이 사람을 넘어트리고, 신호를 무시하고 쏜살같이 튀어 나간 차량이 횡단보도를 가로지르던 행인을 덮쳤다.

빠아아앙, 쿵!

“컥!”

대격변 이후 세계에서 가장 높은 인구 밀도를 갖게 된 대한민국.

그중에서도 제2의 도시라 불리는 부산의 사거리는 삽시간에 혼란과 공포의 구렁텅이로 빠져들었다.

하지만 어디에나 예외는 있는 법이다.

쉬쉬쉭!

수많은 인파가 만들어 낸 물살을 거슬러 오르는 존재들.

비록 숫자는 네 명에 불과했지만, 침착한 눈빛과 빛살 같은 움직임은 그들이 숙달된 헌터라는 증거였다.

“세 시 방향으로!”

“오케이. 한 번에?”

“앞에 있는 놈부터 자릅시다.”

“놈들이 흩어지지 않게!”

처음 보는 얼굴이지만 짧게 주고받는 말 몇 마디면 충분하다.

그들 모두는 적게는 일 년에서 길게는 십 년 동안 몬스터와 싸워 왔고, 지금 같은 상황에서 자신들이 해야 할 일이 무엇인지 정확히 알고 있었다.

‘여기서 막지 못한다면…… 끝장이다.’

‘어떻게든 발을 묶어야 해.’

다행히 사거리에 나타난 머맨들의 숫자는 적은 편이었다. 십여 마리 남짓.

비록 자신들도 그다지 높은 등급의 헌터는 아니었지만, 저 정도 숫자라면 어떻게든 시간을 끌며 버틸 수 있을 것 같았다.

“포위 대형, 펼쳐!”

그러나 힘찬 외침과 함께 십여 마리의 머맨을 향해 쏘아지던 그들은, 다음 순간 깊은 절망감에 휩싸여 발걸음을 멈췄다.

쿵. 쿵쿵. 쿵쿵쿵!

- 시싯!

- 시시시시싯!

아스팔트 도로가 부르르 몸을 떨었다. 진동의 근원지는 육중한 체구로 돌격하는 수백 마리의 머맨이었다.

선봉대가 아닌, 진짜 본대가 도착한 것이다.

어쩌면 이 어마어마한 숫자의 머맨들도 일부에 불과할지도 몰랐다.

“……아.”

끝장이다.

모두의 머릿속에 떠오른 생각이었다.

십여 마리의 머맨을 상대하는 것조차 목숨을 걸어야 하는데, 중하급 헌터 네 명으로 저 많은 숫자를 감당하는 것은 불가능에 가까웠다.

아니, 상급 헌터들의 지원이 없는 한 불가능하다.

“지, 지원을 기다리면서 버티는 건…….”

“버텨?”

간절하기까지 한 누군가의 말에, 중년 헌터가 씹어뱉듯이 중얼거렸다.

“난도질당해 죽는 게 천 배는 빠르겠지.”

“……빌어먹을.”

전신이 물먹은 솜처럼 무겁다. 맞서 싸워야 하지만 도저히 엄두가 나지 않았다.

그들 역시 가족이 있고, 살고자 하는 욕구가 있는 사람이었다. 당장이라도 뒷걸음질 치려는 발을 붙잡을 수 있는 건 헌터로서의 사명감과 의지 때문이다.

하지만 이제 그 시간도, 얼마 남지 않았다.

- 아아, 아아아아!

도대체 언제 나타난 걸까.

높게 솟은 빌딩 위, 진주 왕관을 쓰고 출렁이는 긴 머리카락으로 나신을 가린 새하얀 미녀가 부르는 노랫소리가 사방으로 퍼져 나갔다.

세이렌(Siren).

아름다운 음색으로 듣는 이를 홀리고 파멸로 이끄는 마녀. 검은 바다의 여왕.

숫자는 불과 하나였으나, 그 강렬하고도 아련한 음색 넓은 사거리를 점령하기에 충분했다.

비명을 내지르며 정신없이 도망치던 사람들이 허공에 천사처럼 떠올라 있는 반인반조(半人半鳥)의 몬스터를 보고 황홀한 표정을 지으며 멈춰 선다.

헌터들은 그 마력에 저항하기 위해 이를 악물었지만, 상황은 나아지지 않았다.

툭, 투둑.

악문 잇새 사이로 흐른 피가 턱을 타고 떨어진다.

계속해서 귓가를 파고드는 노랫소리에 무기를 쥔 손아귀에 힘이 빠져나가고, 시시각각 가까워져 오는 수백 마리의 머맨들이 흐릿하게 보였다.

“제기……랄.”

코앞에 닥친 죽음이 보였다. 그들은 물론이고 천 명에 달하는 민간인들도 죽음을 피할 수는 없다.

그리고 오늘의 학살극은 끝없이 이어질 것이다.

상급 헌터들이 지원을 온다 해도 수백만에 달하는 부산 시민 모두를 보호할 수는 없을 테니까.

‘니미, 이렇게 뒈질 줄은 몰랐는데.’

늦었다. 이미 불가항력이다.

모든 것을 체념한 중년 헌터가 흐릿해진 눈동자로 세이렌을 바라보던 그때였다.

- 아아, 아아아……!

쐐애애액, 퍼걱!

강렬한 파공성과 함께, 노랫소리가 뚝 끊겼다.

바다처럼 검푸른 핏물이 터져 나오고 힘차게 퍼득이던 날개가 꺾인다.

천사처럼 우아하게 허공을 유영하던 반인반조의 몬스터는 아스팔트 도로 위로 추락했다.

후우웅, 쿵!

“아?”

- 시싯?

매혹의 마력이 담긴 노랫소리가 끊기자 정신이 돌아왔다.

살아남은 인간들, 그리고 여왕의 죽음을 눈앞에서 목격한 머맨들은 얼빠진 얼굴로 추락한 세이렌을 바라보았다.

부릅뜬 채 굳어 버린 눈동자. 추락의 충격으로 벗겨진 진주 왕관과 머리카락이 펼쳐지며 드러난 가슴 사이에는 길고 뾰족한 무언가가 튀어나와 있었다.

이건…….

“뼈?”

중년 헌터의 입술 사이로 의문 어린 음성이 흘러나온 그 순간.

쏴아아아악!

기묘한 소음과 함께 모두의 머리 위로 그늘이 드리워졌다. 그리고 고개를 들어 하늘을 바라본 사람들은 볼 수 있었다.

까마득한 상공 위를 뒤덮은 거대하고도 새하얀 무언가를. 그 중심에 우뚝 선 한 남자를.

“이 몸. 강림.”

거만하면서도 힘이 넘치는 목소리가 모두의 귓가를 파고든다.

금빛 머리카락이 언뜻 사람들의 눈에 비친 그때, 정체불명의 남자가 수백의 머맨들을 가리키며 말을 이었다.

“너희. 뒈짐.”

- ……!

수백여 마리의 머맨이 눈동자를 부릅뜬 동시에, 사거리에 그늘을 드리운 새하얀 무언가가 번쩍 빛났다.

파파파파팟!

뼈. 그건 뼈였다. 창날보다 날카롭고 화살만큼 빠른 그것은 삽시간에 지상을 뒤덮었다.

쐐애애액! 퍼버버벅!

일시에 쏘아진 수천 개의 뼛조각이 비늘을 부수고 지느러미를 찢었다.

몇 개의 뼛조각을 간신히 창으로 쳐 낸 머맨도 곧장 날아드는 또 다른 뼛조각에 의해 벌집이 되어 쓰러졌다.

푸푸푸푹!

허공으로부터 쏟아지는 뼈의 폭우(暴雨)는 오직 몬스터만을 위한 것이었다.

그 무시무시한 광경 속에서 우뚝 굳은 인간들은, 잘 정돈된 아스팔트 도로가 삽시간에 몬스터의 피로 물드는 것을 지켜보았다.

털썩, 털썩, 쿵!

불과 십여 초. 이백에 달하는 머맨 중 절반에 달하는 숫자가 삽시간에 쓰러졌다.

아니, 녹아내렸다.

이 예상치 못한 상황에 지휘관 격인 머맨 하나가 다급한 기성을 토해 냈다.

- 시싯, 시시시시싯!

- 시. 시싯!

머맨은 반인반어(半人半漁)답게 상당한 지능을 갖춘 몬스터.

지휘관의 명령에 따라 일사불란하게 등에 찬 거대 가리비 방패로 벽을 쌓는 놈들의 모습에, 정체불명의 남자. 스켈레톤 킹이 혀를 찼다.

“이런 무엄한 놈들을 보았나. 감히 이 몸에게 저항하다니.”

하지만 그렇다 해도 결과는 달라지지 않는다.

스켈레톤 킹의 권능은 머맨 따위가 범접할 수 없는 영역에 있었으니.

“왕에게 거스른 죗값을 단단히 치르도록 해 주…… 응?”

드드득, 쿠쿵!

이상함을 느낀 스켈레톤 킹은 문득 고개를 틀었다.

저 멀리, 개미 떼처럼 바글바글 몰려오고 있는 머맨이 가면 너머 그의 금빛 눈동자에 담겼다.

“……이놈들 보게.”

언뜻 봐도 오백 마리가 넘어가는 숫자.

그리고 스켈레톤 킹은 놈들이 더더욱 무엄하게 느껴짐과 동시에, 잠시 잊고 있던 사실을 깨달았다.

‘아, 언데드.’

아무리 다급하다지만 부산 사거리에서 언데드 군단을 일으켜 세울 수는 없는 법이다.

심지어 천 명에 달하는 인간들이 두 눈을 말똥말똥하게 뜬 채 자신을 지켜보고 있을 때는 더욱 그렇다.

“어라. 이게 아닌데.”

떨떠름하게 중얼거린 스켈레톤 킹은 문득 분노가 솟구쳤다.

자신에게 제약을 걸어 둔 어느 간악한 인간의 얼굴이 눈앞을 스친 탓이었다.

‘이런 빌어먹을 인간을 보았나. 나한테 이런 개고생을 시켜?’

놈이 일부러 가장 많은 몬스터가 몰린 지역을 맡겼다고 생각하니 가슴뼈가 뒤틀리는 기분이었다.

그리고 까마득한 상공 위, 조금 전 진태경이 향했던 그 방향을 향해 홱 고개를 돌린 스켈레톤 킹은 볼 수 있었다.

후우우우웅!

그워어어어어!

쾅! 콰과과과광!

먼 거리에서도 똑똑하게 보이는 무언가의 거대한 촉수와 폭발음.

그 광경을 말없이 응시하던 스켈레톤 킹은 지상에 옹기종기 모여 있는 머맨 무리를 향해 다시금 시선을 던졌다.

“……다시 보니 걸그룹 같구나.”

흉측한 머맨이 예뻐 보이기는 또 처음이었다.



* * *



후우우웅, 퍼엉!

포탄이 터지는 소리와 함께 바닷물이 솟구친다.

하지만 그 공세는 처음과는 달리 한참 약했고, 날아드는 공격의 범위는 확연히 줄어들었다.

아무래도 가장 큰 이유는, 서른 개에 달하는 다리가 아홉 개로 줄어들었기 때문인지도 모른다.

서걱!

아니, 이제 여덟 개다.

- 그워어어어어!

“옳게 된 문어로구나.”

울부짖는 크라켄을 향해, 나는 힘차게 신형을 쏘았다.

날아드는 다리를 피하고, 허공을 밟으며 날아오른 내 발아래에 거대한 한 쌍의 눈이 있었다.

이제는 끝내야 할 때다.

화륵.

창날을 휘감은 불꽃이 가파르게 회전한다. 나는 모든 공력을 힘을 실어, 놈의 눈동자를 향해 창을 내리꽂았다.

화룡신창 삼 초식. 타코야끼.
```

## Final English reading copy

```markdown
# Chapter 573

Everything has an order and a progression.

Naturally, the same applied to Mutated Gates.

When a magic power reading broke through a certain threshold, an alarm sounded to warn of danger, and an evacuation order was issued to everyone nearby.

However, the time it took an ordinary Grade C Gate to transform into a Mutated Gate and then reach the Monster Wave stage was only a few dozen seconds.

The reading was so far beyond anything ever recorded that the Gate management office had no choice but to suspect a measurement error.

Their brief deliberation lasted less than a minute before ending with the Kraken tearing through space and descending upon the present world, smashing the Gate management office first.

*Boom!*

And the flames of disaster spread in every direction in an instant.

The Kraken was the terror of the black sea and a king who possessed immense power. And beneath such a king were savage, loyal soldiers.

—Ssssss!

Fins moved without pause, and gills opened and closed.

At the appearance of a Merman emitting strange cries, the intersection, which had been crowded with vehicles and people, fell silent in an instant.

“What the……”

Someone’s bewildered question never reached its end.

*Whoosh—crack!*

It happened in the blink of an eye.

A barnacle-covered trident pierced through a human body and continued flying, punching straight through even a vehicle waiting at the light.

*Boom!*

Vehicle fragments flew in every direction with the sound of an explosion.

As people stared blankly at the unreal scene, danger signals were transmitted through the alarms installed around the intersection and everyone’s smartphones.

*Weeeeeeeeng!*

*Ding. Beep-beep. Bzzzz.*

Noise shattered the silence.

The people looked back and forth between the vehicle engulfed in flames and the Merman standing upright. Only then did they realize the danger right in front of them.

“M-Monster!”

“It’s a Monster Wave!”

“Aaaaaaaah!”

With screams, the countless people moving through the streets scattered in an instant.

Desperate to put even a little distance between themselves and the monsters—to survive—they no longer had room in their minds for rules or laws.

“Fuck, move!”

“W-wait……!”

*Crash! Crack!*

“Graaagh!”

People knocked one another down, and a vehicle that shot forward without regard for the traffic light plowed into a pedestrian crossing the crosswalk.

*Hooooonk! Thud!*

“Ghk!”

Korea had become the most densely populated country in the world after the Great Cataclysm.

And the intersection in Busan, known as the country’s second city, plunged into a pit of chaos and terror in an instant.

But there were always exceptions.

*Whoosh-whoosh-whoosh!*

Several figures pushed against the current created by the fleeing crowd.

There were only four of them, but their calm gazes and lightning-fast movements were proof that they were seasoned Hunters.

“Three o’clock!”

“Okay. All at once?”

“Let’s cut down the ones in front.”

“Don’t let them scatter!”

They had never seen one another before, but a few brief exchanges were enough.

All of them had fought monsters for at least a year and as long as ten, and they knew exactly what they had to do in a situation like this.

*If we can’t stop them here…… we’re finished.*

*We have to tie them down somehow.*

Fortunately, the number of Mermen that had appeared at the intersection was relatively small. Only around a dozen.

They were not particularly high-rank Hunters themselves, but they thought they could somehow hold out and buy time against that many.

“Spread out into an encirclement!”

However, just as they shouted and charged toward the dozen Mermen, they stopped in their tracks, overcome by deep despair.

*Thud. Thud-thud. Thud-thud-thud!*

—Ssssit!

—Ssssss!

The asphalt road trembled.

The source of the vibration was hundreds of Mermen charging forward with massive bodies.

The main force had arrived—not the vanguard.

Perhaps even this tremendous number of Mermen was only a fraction of the whole.

“……Ah.”

*We’re finished.*

The same thought came to everyone’s mind.

Even facing a dozen Mermen required risking their lives. For four low-to-mid-rank Hunters to deal with that many was practically impossible.

No. It was impossible without support from high-rank Hunters.

“W-we can hold out while waiting for reinforcements……”

“Hold out?”

A middle-aged Hunter muttered through clenched teeth in response to someone’s almost desperate suggestion.

“Getting hacked to death would be a thousand times faster.”

“……Damn it.”

His entire body felt as heavy as cotton soaked in water. He had to fight, but he could not bring himself to do it.

They had families too. They were people who wanted to live.

The only thing keeping their feet from stepping backward was their sense of duty and resolve as Hunters.

But they would not be able to hold themselves back much longer.

—Aah, aaaaaah!

When had she appeared?

From atop a tall building, the song of a pure-white beauty spread in every direction. A pearl crown rested on her head, and long, flowing hair covered her naked body.

A Siren.

A witch who bewitched those who heard her beautiful voice and led them to ruin. The queen of the black sea.

There was only one of her, but her intense yet wistful voice was enough to conquer the wide intersection.

The people who had been screaming and fleeing in confusion stopped when they saw the half-human, half-bird monster floating in the air like an angel, their faces filled with rapture.

The Hunters gritted their teeth as they resisted her magic, but the situation did not improve.

*Drip. Drip.*

Blood that had flowed between their clenched teeth ran down their chins.

The song continued drilling into their ears. Strength drained from the hands gripping their weapons, and the hundreds of Mermen drawing closer by the moment grew hazy before their eyes.

“Goddamn it……”

Death was right in front of them.

The Hunters—and the nearly thousand civilians—could not escape it.

And today’s massacre would continue without end.

Even if high-rank Hunters came to support them, they could never protect all the millions of Busan’s citizens.

*Fuck. I didn’t think I’d die like this.*

It was too late. It could no longer be helped.

The middle-aged Hunter had given up on everything and was staring at the Siren through blurred eyes when it happened.

—Aah, aaaaaah……!

*Fwooooosh—crack!*

With a powerful shriek of displaced air, the song abruptly stopped.

Dark blue blood like the sea burst outward, and the wings that had been beating powerfully snapped.

The half-human, half-bird monster that had been gliding gracefully through the air like an angel fell onto the asphalt.

*Whoooosh—thud!*

“Huh?”

—Ssssit?

The moment the song filled with bewitching magic power stopped, their minds cleared.

The surviving humans and the Mermen who had witnessed their queen’s death stared blankly at the fallen Siren.

Her eyes were wide open and frozen in place. Her pearl crown had been knocked off by the impact, and her hair had spread apart, revealing something long and pointed jutting out between her breasts.

What was this……?

“Bone?”

The middle-aged Hunter had barely voiced his bewilderment when—

*Whooooooosh!*

A strange noise rang out, and a shadow fell over everyone’s heads.

Those who looked up at the sky saw it.

Something enormous and pure white covering the distant heavens.

And a man standing at its center.

“This body. Descends.”

The arrogant yet powerful voice pierced everyone’s ears.

When golden hair flashed briefly in their vision, the unidentified man pointed toward the hundreds of Mermen and continued speaking.

“You. Die.”

—……!

The hundreds of Mermen opened their eyes wide.

At the same time, the enormous white thing casting a shadow over the intersection flashed with light.

*Papapapapat!*

Bone.

That was what it was.

Sharper than spearheads and as fast as arrows, the bones covered the ground in an instant.

*Fwooooosh! Thud-thud-thud-thud!*

Thousands of bones shot down at once, crushing scales and tearing through fins.

A Merman that barely managed to knock away several bone fragments with its spear was immediately turned into a pincushion by another fragment that came flying at it, then collapsed.

*Thud-thud-thud!*

The rain of bones pouring down from the sky was meant for monsters alone.

Amid that horrifying spectacle, the humans stood frozen as they watched the neatly paved asphalt road become stained with monster blood in an instant.

*Thump. Thump. Crash!*

Only a dozen seconds passed.

Nearly half of the two hundred Mermen collapsed in an instant.

No.

They melted.

One Merman who seemed to be a commander let out an urgent cry at the unexpected situation.

—Ssssit, ssssssit!

—Sss. Ssssit!

Mermen were monsters with considerable intelligence, as befitted half-human, half-fish creatures.

At their commander’s order, they moved in perfect formation and built a wall with the enormous scallop shells strapped to their backs.

The unidentified man—the Skeleton King—clicked his tongue.

“What insolent wretches. How dare you resist this body?”

But even so, the outcome did not change.

The Skeleton King’s power existed in a realm that Mermen could never approach.

“I shall make you pay dearly for the crime of defying a king…… Hm?”

*Rrrrk. Boom!*

Sensing something strange, the Skeleton King abruptly turned his head.

Far away, the swarm of Mermen pouring toward him like a colony of ants filled his golden eyes behind the mask.

“……Would you look at these bastards.”

There were more than five hundred at a glance.

And as the Skeleton King found them increasingly insolent, he remembered a fact he had momentarily forgotten.

*Ah. Undead.*

No matter how urgent the situation was, he could not raise an undead army in the middle of a Busan intersection.

Especially not while nearly a thousand humans were watching him with their eyes wide open.

“Oh. This isn’t right.”

After muttering awkwardly, the Skeleton King suddenly felt anger rising within him.

The face of the wicked human who had placed a restriction on him flashed before his eyes.

*That fucking bastard. How dare he put me through all this shit?*

The thought that the bastard had deliberately assigned him the area where the most monsters had gathered made his breastbone feel twisted.

Then the Skeleton King abruptly turned his head toward the distant sky, in the direction Jin Taekyung had headed moments earlier.

He saw it.

*Whoooooosh!*

*Gwooooooar!*

*Boom! Krrrrr-boom!*

Even from this distance, the enormous tentacles were clearly visible and the explosions clearly audible.

The Skeleton King silently watched the scene, then turned his gaze back toward the cluster of Mermen gathered below.

“……Now that I look again, they resemble a girl group.”

It was the first time the hideous Mermen had ever looked beautiful.

* * *

*Whoooosh—boom!*

Seawater surged upward with the sound of an exploding shell.

But unlike the beginning, the attack was much weaker, and the range of the incoming strikes had clearly diminished.

The biggest reason was probably that the Kraken’s nearly thirty tentacles had been reduced to nine.

*Slash!*

No.

Now it had eight.

—Gwooooooar!

“Now that’s a proper octopus.”

I shot forward with all my strength toward the roaring Kraken.

I dodged an incoming tentacle and stepped on empty air to leap higher. Beneath my feet was a gigantic pair of eyes.

It was time to finish this.

*Fwoosh.*

The flames coiling around the spearhead spun sharply.

I poured all my internal energy into it and drove the spear down toward the creature’s eye.

Fire Dragon Divine Spear, Third Form: Takoyaki.
```
