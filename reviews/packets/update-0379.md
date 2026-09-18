<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0379.txt",
      "sha256": "9ede64f7ec4876ce13f9000aa10c43e1f0849bc2f842b87812931335504058b6",
      "bytes": 13984
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b96def6f1986a428b697f6a6e081ca72ec70aa9a25b6cc6d5447ac80cc7bcc66",
      "bytes": 3011
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "be3c24737395b8320d5582f95590f3ec17d77d0ecf24f6c76a1a0240b8668ea6",
      "bytes": 131330
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9ea3739a3da9bd6838453862c146d6e54b656807276c570ed465ef130a8d8731",
      "bytes": 533
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d63ca3fd77c6da12db9999ec518c87a471838963ac3cfa82ad410ce67252e92f",
      "bytes": 101472
    }
  ],
  "estimated_tokens": 9131
}
-->

# Durable State Update — Chapter 379

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 379. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 379. Profile updates may replace only one
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
  "chapter": 379,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 379,
    "continuity_sources": [379],
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; Mungyeong captured the Third Fiend in the hidden cavern, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is Level 120 and at the Supreme Peak realm, has manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened, while Dong Feng's dantian and martial arts were destroyed while shielding him.",
    "Mungyeong is the Divine Physician and former Slaughter Saint, has sworn never to kill again, and intends to live as a physician; Dong Feng is his Disciple.",
    "Cheongpung remains a Supreme Peak master with Mimi and is Mimi's temporary guardian.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation; the Lord of Heaven's nature and the Western Heaven Demon Lord's ultimate fate remain unresolved.",
    "The Myriad-Poison Ring is bound to Jin Taekyung alongside White Flame and the Fire Dragon Armor.",
    "Aehyang is manipulating the Sichuan City Lord under the direction of an unidentified person.",
    "Jin Taekyung has returned to the modern world and is aboard a private jet bound for Chengdu International Airport.",
    "Chengdu International Airport is under attack by monsters, and Jin suspects the Lich responsible for the recent monster wave has reached the area.",
    "More than ten Wyverns pursued the jet, but Jin killed their leader and two others with a spear charged with flame Force, causing the survivors to flee."
  ],
  "continuity_sources": [
    378
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "Will Mungyeong remain outside the coming war, or will the crisis force him to intervene?"
  ],
  "safe_through": 378,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, and 화룡갑 as Fire Dragon Armor.",
    "Render 강기(劍罡) as Force or Aura Blade by context, and retain Barrier, Breath, Air Breath, and bangzi consistently."
  ],
  "version": 1
}
```

## Exact glossary matches

| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 오크 | **Orc** | Monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 오성홍기 | **Five-Starred Red Flag** | China's national flag. |
| 중화인민공화국 | **People's Republic of China** | Formal country name shouted by the Chinese Hunters. |
| 인민해방군 | **People's Liberation Army** | Chinese military deployed to seal off the catastrophe area. |
| 청두 | **Chengdu** | Administrative capital of Sichuan Province and destination airport city. |
| 오성 | **Oseong** | One half of the paired Joseon-era names used in Taekyung's joke. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 377
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

## Korean source

```text
＃379화



드드드득!

거대한 울림과 지면을 통해 전해지는 진동.

지평선을 바라본 스무 살의 청년. 샤오 쉔(Shao Shen)은 도무지 지금의 상황을 믿을 수 없었다.

‘수천 킬로 밖에 있어야 할 몬스터들이 어떻게……!’

이것은 샤오 쉔 혼자만이 떠올린 의문이 아니었다.

천여 명의 공안 무력부 소속의 헌터와 치안 유지를 위해 파견된 오천 명의 중국 인민 해방군. 청두 국제공항에 주둔해 있던 모두가 같은 의문을 떠올렸고, 눈앞에 닥쳐 온 현실에 경악했다.

- 취이익!

- 그워어어!

하급 몬스터인 고블린, 오크부터 트롤, 오우거와 라이칸슬로프 같은 상위 몬스터까지.

지평선을 가득 메운 몬스터 대군이 괴성과 함께 돌진하고 있었다.

1km의 거리가 시시각각 빠르게 좁혀지는 광경에 비명 같은 외침이 터져 나왔다.

“각 제대 별로 대열 갖춰! 집합! 집하압-!”

“쏴, 쏴라! 쏘란 말이다!”

타다다당! 꽈앙!

황급히 대열을 갖춘 인민해방군이 상관의 명령에 따라 화력을 퍼부었지만, 효과는 미비하기 짝이 없었다.

예상치 못한 몬스터 대군의 습격.

아무 능력도 없는 일반인에 불과한 군인들은 공포로 몸이 굳었고, 그들이 발사한 화기는 고작해야 하급 몬스터들에게만 통하는 수준이었다.

“몬스터들이, 몬스터들이 너무 많습니다!”

“파일럿!”

“어서 전투기를 띄워라! 놈들의 머리 위로 폭격을……!”

다급한 지휘관들의 외침은, 다음 순간 하늘 위에서 울려 퍼진 흉포한 괴성에 파묻혔다.

- 캬우우우우!

“저, 저건!”

“와이번! 와이번이다!”

석양을 등지고 날아오는 거대한 동체.

창공의 공포라 불리는 와이번을 선두로 수십 마리의 그리폰(Griffon), 가고일(Gargoyle)이 뒤따른다.

수 미터의 날개를 비스듬히 꺾으며 하강한 A급 몬스터들이 아직 미처 이륙하지 못한 전투기들을 덮쳤다.

콰드드득! 콰광!

위력적인 날갯짓에 수 톤의 쇳덩이가 들썩였고, 마력이 실린 발톱에 전투기의 기체가 종잇장처럼 찢겨 나갔다.

폭발과 함께 엄청난 힘으로 튕겨 나간 금속 파편이 황급히 뛰어가던 파일럿들을 덮쳤다.

퍼버벙! 콰직!

비명조차 남기지 못한 즉사.

정신을 차린 지휘관의 명령에 따라 총기가 불을 뿜었지만, 강력한 마력을 머금은 피부와 가죽은 수백, 수천 발의 탄환으로도 생채기만 내는 것이 고작이었다.

- 키키키킷.

무력한 인간을 비웃는 몬스터의 웃음소리에, 사람들은 전신의 털이 곤두서는 듯한 충격과 공포를 느꼈다.

“이, 이럴 수가.”

지상과 상공을 가득 메운 몬스터 대군. 화기조차 제대로 통하지 않는 놈들은 그야말로 괴물이었다.

“괴, 괴물…….”

“나, 난 살아야겠어. 이런 곳에서 개죽음당하기는 싫다고!”

죽음에 대한 공포는 그 어떤 전염병보다 빠르게 퍼져 나갔다.

인민 해방군이 하나둘씩 뒷걸음질 치던 그때, 오히려 앞을 향해 나아가는 한 사람이 있었다.

“물러서지 마라!”

아직 앳된 기가 가시지 않은 청년, 샤오 쉔이 타오르는 눈빛으로 외쳤다.

그가 착용한 갑옷의 가슴팍에는 중화인민공화국의 국기인 오성홍기(五星紅旗)가 새겨져 있었다.

“우리가 누구인가!”

젊은 청년의 물음에 도망치려던 이들이 발걸음을 멈췄다.

샤오 쉔은 수백 미터 밖에서 돌격해 오는 몬스터 군단을 노려보았다. 깊게 눌러쓴 투구 사이로 다시 한번 천둥 같은 목소리가 터져 나왔다.

“우리가 누구인가!”

피가 끓어오르는 듯한 외침.

모두의 시선 속에 샤오 쉔은 창날을 곧추세웠다.

“우리는 중화의 후예이고, 인민 해방군과 공안 무력부(公安武力部)의 형제들이다!”

하늘을 찌를 듯 높이 솟구친 창날에서 석양빛을 닮은 오라가 솟구쳤다.

츠츠츠츠!

“가자! 저 괴물들을 모조리 쓸어 버리자!”

“와아아아아!”

귀가 먹먹해지는 거대한 함성이 지축을 뒤흔들었다.

샤오 쉔을 필두로, 공안 무력부 소속의 헌터들이 각자의 무기를 손에 쥔 채 몬스터 대군을 향해 맹호처럼 짓쳐 들었다.

“물러서지 마라! 중화의 힘을 보여 줘라!”

“으아아아!”

- 구워어어어!

- 아우우우!

죽음을 각오한 결의가 담긴 인간의 외침과 몬스터들의 괴성이 뒤섞인다. 한 덩어리가 된 두 집단이 서로를 향해 얽혀들었다.

콰과과과광!

하늘과 땅을 울리는 격돌. 그리고 사방에서 빗발치는 죽음.

“크아아악!”

- 쿠에엑!

푸푸푹! 퍼걱!!

지상 곳곳에서 비명과 굉음이 울려 퍼졌다.

오라가 서린 A급 헌터의 검신이 라이칸스로프의 목을 갈랐고, 오우거가 휘두른 쇠몽둥이에 서너 명의 헌터들이 피곤죽이 되어 날아간다.

힘을 합쳐 몬스터 하나를 쓰러트리고 다음 적을 향해 무기를 휘두르려던 두 헌터의 머리 위에 거대한 그림자가 드리웠다.

- 키이이잇!

서걱!

급강하한 그리폰의 발톱이 헌터들의 육신을 갑옷과 함께 갈기갈기 찢었다.

다음 사냥감을 찾아 헤매는 그리폰을 향해 커다란 불의 구(球)가 날아왔다.

“파이어 볼(Fire Ball)!”

퍼버벙!

매캐한 연기와 함께 상공을 유영하던 그리폰의 동체가 휘청였다. 지상에서 호시탐탐 때를 노리고 있던 원거리 부대는 그 틈을 놓치지 않았다.

“지금!”

펑! 퍼버버벅!

가지각색의 마법과 마나를 한껏 머금은 화살이 그리폰을 꿰뚫었다.

단말마와 함께 추락하는 그리폰의 모습에 비행 몬스터들이 흉포한 괴성을 토해 냈다.

- 캬우우우우!

원거리 부대를 향해 내리꽂히는 비행 몬스터들을 가로막은 것은, 납과 철로 이루어진 현대식 무기였다.

“일제 사격, 실시!”

타타타타탕! 콰앙!

무수히 많은 소총과 중화기. 수십여 대의 전차가 일시에 불을 토해냈다.

비록 몬스터들의 마력과 상극이라 할 수 있는 마나(Mana)의 힘에 비할 바는 아니지만, 일거에 화력을 집중시키니 비행 몬스터들도 주춤할 수밖에 없었다.

- 키잇!

“통한다!”

“다른 곳은 소용없다! 눈을 노려!”

날 때부터 마력을 머금은 몬스터들의 피륙은 대부분의 물리력을 가뿐히 무시한다. 그러나 단 한 곳, 눈만은 예외였다.

얕은 피막에 싸여 있는 안구는 중화기를 동원한다면 충분히 피해를 입힐 수 있는 수준.

멈칫거리는 몬스터들의 모습에, 모든 광경을 지켜보고 있던 사단장이 신나게 지휘봉을 휘둘렀다.

“더! 더 퍼부어라! 저 괴물들이 꼼짝도 못 하게…….”

콰아아아아!

음성은 이어지지 못했다.

그린 와이번이 쏘아 보낸 포이즌 브레스(Poison Breath)가 반경 백여 미터를 뒤덮었고, 사단장을 포함한 참모 지휘부는 강력한 산성 독을 뒤집어쓴 채 녹아내렸다.

“사, 사단장님!”

“지휘부가……!”

눈 깜짝할 사이에 수백의 병사와 고급 지휘관을 잃은 인민 해방군은 패닉 상태에 빠졌다.

장교와 부사관, 병사. 가릴 것 없이 모두가 경악에 찬 외침과 함께 눈 앞에 펼쳐진 끔찍한 광경을 바라봤다.

“이럴 수가…….”

“이, 이건 아니야. 이럴 수는 없어! 이런 건 내 임무가 아니라고!”

누군가의 비명은 모두의 심정을 대변하는 것이었다.

만일을 대비해 전력을 끌고 오긴 했지만, 그들의 주 임무는 곧 청두 국제공항에 도착할 외국의 헌터들과 합류, 호위하며 상부의 명령에 따라 움직이는 것이었다.

수천 킬로미터 밖에 있을 몬스터 군단이 쳐들어올 거라는 내용은 어디에서도 들은 바 없었다.

“이게 도대체…….”

“죽는다. 우리 모두 죽을 거야.”

잠시 잊었던 공포감이 인민 해방군의 머리 위에 내려앉았다.

그들은 전장의 선두에서 싸우고 있는 공안 무력부의 헌터들이 아니라, 현대식 화기를 든 평범한 일반인에 불과했으니까.

그리고 불길한 짐작은 곧 현실이 되었다. 그들이 생각했던 것보다 더한 악몽으로.

- 옴. 느. 하. 소. 유.

뚝뚝 끊어지는 목소리. 수신이 불안정한 라디오의 노이즈를 닮은 스산한 소음이 전장에 울려 퍼진다.

어디선가 몰려온 검은 안개가 사람들의 머리 위를 뒤덮었다.

- 옌. 위. 가. 지. 케!

그때였다. 끔찍한 변화가 일어난 것은.

쏴아아아악!

먹구름처럼 어두운 마력이 피와 시체를 타고 거미줄처럼 뻗어 나갔다.

싸늘하게 식어 가는 시신에 새로운 힘과 영혼을 불어넣고, 사슬로 묶어 종속시킨다.

투둑, 투두두둑.

새로운 생명을 얻고 죽음의 웅덩이에서 서서히 몸을 일으키는 백골(白骨)의 군단.

무수한 망자들을 보이지 않는 사슬로 엮어 종으로 삼은 ‘그 존재들’은 만족스럽게 웃었다.

- 킥, 키키킥.

- 그극. 키히히.



* * *



- 그르르륵.

끓어오르는 소리와 함께 사내가 몸을 일으킨다.

오성홍기가 새겨진 갑옷과 거대한 도끼를 든 그는 샤오 쉔이 기억하는 A급 헌터의 모습 그대로였다.

‘……야오위 씨.’

그러나 샤오 쉔은 사내의 이름을 소리 내어 부를 수 없었고, 부르지도 못했다.

눈앞의 그가, 더이상 자신이 알던 사람이 아니라는 사실을 알기 때문이다.

‘아, 아아.’

만약 십여 분 전 그가 목이 잘리는 광경을 목격하지 않았다면, 지금 이 순간 자신의 잘려 나간 목을 옆구리에 낀 채 일어나지 않았다면 샤오 쉔은 그를 동료이자 친구로 생각했을 것이다.

하지만 이제 야오위는 존재하지 않는다. 샤오 쉔의 입술 사이에서 그의 새로운 이름이 흘러나왔다.

“듀라한(Dullahan)…….”

목 없는 기사. 듀라한.

샤오 쉔은 상위 언데드 몬스터로 거듭난 동료의 모습에 입술을 깨물었다. 뜨거운 무언가가 볼을 타고 흘러내렸다.

“미안합니다. 정말로.”

- 그어어어!

괴성과 함께 달려드는 듀라한을 향해, 샤오 쉔은 바람처럼 쏘아졌다.

과거 두 사람은 종종 이렇게 대련을 벌이고는 했다. 단순한 호승심으로 시작한 대련은 매일마다 계속되었고, 대련이 끝나면 야오위의 투정을 받아 주어야 했다.



‘어린놈이 예의가 없어요, 예의가. 한 번 져 주면 덧나냐?’

‘하하. 밥이나 먹으러 가죠. 대련에 진 사람이 계산하기로 했으니까, 오늘도 야오위 씨가 사겠네요.’

‘집에 돈도 많은 놈이 밝히기는. 내가 언젠가 네 녀석한테 밥 얻어먹고 만다.’



하지만 그런 일은 과거에도, 앞으로도 없을 것이다. 승자는 늘 샤오 쉔이었다.

‘잘 가요. 그동안 고마웠습니다.’

후웅! 서걱!

휘둘러진 도끼는 허공을 갈랐고, 샤오 쉔의 창날에서 솟구친 오러는 듀라한의 상반신을 갈랐다.

허리춤으로부터 그어진 선. 목 없는 기사의 신형이 천천히 허물어진다.

쿵, 털썩.

쓰러진 듀라한, 아니 야오위의 얼굴을 물끄러미 내려다보던 샤오 쉔의 눈동자가 뜨겁게 달아올랐다.

“감히, 감히 이런 짓을…….”

반나절 전만 해도 함께 웃고 떠들던 친구와 동료들이 언데드 몬스터가 되었다.

공안 무력부의 헌터들은 군기가 엄정하기로 이름 높지만 피 한 방울 없는 냉혈한들은 아니었다.

죽을 각오로 전투에 임하던 헌터들은 처음으로 인정(人情)이라는 두려움에 직면했다.

“정신 차려! 나 류인친이야! 류인친!”

“혀, 형……!”

- 크르르륵!

퍼걱! 콰과광!

사방에서 비명과 죽음이 빗발쳤다. 절반에 가까운 피해를 입은 공안 무력부와 달리, 오히려 숫자를 불린 몬스터 군단은 끊임없이 밀려들었다.

‘이곳에서, 이렇게 죽는 건가?’

샤오 쉔은 난생처음으로 죽음을 떠올렸다. 늘 밝고 쾌활하던 그가 이렇게 생각할 만큼 상황은 절망적이었다.

‘위험 신호를 받지 못했으니 아마도 통신은 불통, 지원도 없을 테니…… 정말 끝장이구나.’

서걱!

달려드는 언데드 몬스터를 연달아 베어 넘긴 샤오 쉔은 허탈하게 웃으며 하늘을 바라봤다.

노을빛이 퍽 아름답다. 곧 해가 지고 어둠이 찾아오면, 이런 광경도 두 번 다시 보지 못할 것이다.

‘다행이야. 마지막으로 보는 하늘치고는 썩 괜찮…….’

어?

샤오 쉔은 생각을 잇지 못하고 눈을 깜빡였다.

하늘 위, 엄청나게 거대한 무언가가 빠른 속도로 전장을 향해 가까워지고 있었다.

‘비행기?’

콰아아아아아!

불길이 타오르는 거대한 기체. 그리고 드넓은 창공에 울려퍼지는 누군가의 외침.

“야아! 몬스터어!”

“……?”

- ……?

지금 헛것을 들은 건가.

샤오 쉔뿐만 아니라 전장의 모두가 하늘을 올려다보았다.

광기마저 느껴지는 누군가의 목소리가 천둥처럼 울려 퍼졌다.

“박는다!”

박아? 뭘?

샤오 쉔은 곧 그 말의 뜻을 깨달을 수 있었다.

쿠구구구궁!

비행기의 거대한 동체가, 그대로 전장을 휩쓸었다.
```

## Final English reading copy

```markdown
# Chapter 379

Rumble, rumble, rumble!

A tremendous roar and vibrations transmitted through the ground.

The twenty-year-old man staring toward the horizon, Shao Shen, could not believe what was happening.

*They’re supposed to be thousands of kilometers away. How are the monsters…?*

This was not a question Shao Shen alone had asked himself.

More than a thousand Hunters from the Public Security Armed Forces Department and five thousand members of the Chinese People’s Liberation Army dispatched to maintain public order were stationed at Chengdu International Airport. Every one of them had wondered the same thing, and all of them were stunned by the reality bearing down on them.

—Screeech!

—Graaaar!

From low-level monsters such as goblins and Orcs to higher-tier monsters like Trolls, ogres, and Lycanthropes…

An army of monsters filled the horizon, charging forward with hideous shrieks.

As the distance of one kilometer rapidly closed by the second, cries like screams broke out.

“Form up by platoon! Assemble! Assemble—!”

“Fire! Fire!”

Rat-a-tat-tat! Boom!

The People’s Liberation Army hurriedly formed ranks and unleashed their firepower at their commanders’ orders, but the effect was utterly negligible.

An unexpected army of monsters had attacked.

The soldiers, ordinary people without any abilities, were paralyzed with fear. The weapons they fired were effective only against low-level monsters at best.

“There are too many monsters! There are too many!”

“Pilots!”

“Get the fighter jets into the air! Bomb them from above—!”

The frantic shouts of the commanders were drowned out the next moment by a vicious roar that echoed through the sky.

—Kyaaaao-o-o!

“W-What is that?”

“Wyvern! It’s a Wyvern!”

A gigantic body flew in with the setting sun behind it.

A Wyvern, known as the terror of the skies, led the way, followed by dozens of Griffons and Gargoyles.

The A-rank monsters angled their several-meter-long wings and dove upon the fighter jets that had not yet managed to take off.

Crunch! Boom!

The tons of metal lurched beneath their powerful wingbeats, while the aircraft hulls were torn apart like sheets of paper by claws imbued with mana.

Metal fragments blasted away with tremendous force alongside the explosions, crashing into the pilots who were running frantically toward their planes.

Boom! Crunch!

They died instantly, without even leaving behind a scream.

The firearms roared at the commanders’ orders once they regained their senses, but the monsters’ skin and hides, saturated with powerful mana, could do no more than suffer scratches beneath hundreds or thousands of bullets.

—Kikikik.

At the monsters’ laughter mocking the helpless humans, everyone felt a shock of terror that made the hair on their entire bodies stand on end.

“H-How can this be?”

An army of monsters filled both the ground and the sky. The creatures were monsters in every sense of the word, and even firearms barely affected them.

“M-Monsters…”

“I-I have to live. I don’t want to die like a dog in a place like this!”

The fear of death spread faster than any epidemic.

And while the members of the People’s Liberation Army were slowly backing away, one person was instead advancing toward the front.

“Don’t retreat!”

Shao Shen, a young man who had not yet lost all traces of his youth, shouted with blazing eyes.

The Five-Starred Red Flag, the national flag of the People’s Republic of China, was embroidered across the chest of his armor.

“Who are we?”

At the young man’s question, those who had been trying to flee stopped in their tracks.

Shao Shen glared at the army of monsters charging from several hundred meters away. His voice thundered out once more from beneath his tightly pulled-down helmet.

“Who are we?”

His shout made their blood boil.

With every eye upon him, Shao Shen raised the tip of his spear.

“We are the descendants of Zhonghua, and we are brothers in the People’s Liberation Army and the Public Security Armed Forces Department!”

An aura resembling the light of the setting sun rose from the spearhead, which had been thrust high enough to pierce the heavens.

Hissss!

“Let’s go! Let’s wipe out every last one of those monsters!”

“Waaaaaaah!”

A tremendous roar that numbed the ears shook the earth.

Led by Shao Shen, the Hunters of the Public Security Armed Forces Department gripped their weapons and charged toward the army of monsters like ravenous tigers.

“Don’t retreat! Show them the strength of Zhonghua!”

“Uaaaaah!”

—Graaaar!

—Awooooo!

Human cries filled with the resolve to face death mingled with the monsters’ shrieks. The two groups collided and became entangled in one mass.

Kwagwagwagwang!

A clash that shook the sky and earth. Death rained down from every direction.

“Gyaaaah!”

—Kweeeek!

Squish! Crack!

Screams and thunderous noises rang out from every part of the battlefield.

An A-rank Hunter’s aura-coated blade sliced through a Lycanthrope’s neck, while the iron club swung by an ogre turned three or four Hunters into bloody pulp and sent them flying.

Two Hunters combined their strength to bring down a monster, then raised their weapons toward the next enemy. A gigantic shadow fell over their heads.

—Kiiiiiit!

Slice!

The claws of a Griffon diving straight down tore the Hunters’ bodies apart along with their armor.

A large ball of fire flew toward the Griffon as it searched for its next prey.

“Fire Ball!”

Boom!

The Griffon’s body, gliding through the sky, lurched amid the acrid smoke. The ranged units on the ground, waiting for the perfect opportunity, did not let the opening pass.

“Now!”

Bang! Boom-boom-boom!

All manner of spells and arrows brimming with mana pierced the Griffon.

As the Griffon plummeted with a dying shriek, the flying monsters let loose ferocious cries.

—Kyaaaao-o-o!

Modern weapons made of lead and iron blocked the flying monsters as they plunged toward the ranged units.

“Concentrated fire, commence!”

Rat-a-tat-tat-tat! Boom!

Countless rifles and heavy weapons, along with dozens of tanks, belched fire all at once.

Though modern weapons could not compare to mana—the natural counter to the monsters’ magical power—concentrating their firepower all at once forced even the flying monsters to hesitate.

—Kiiit!

“It works!”

“It’s useless anywhere else! Aim for their eyes!”

The flesh of monsters, which had been saturated with mana since birth, easily ignored most physical force. But there was one exception: their eyes.

Their eyeballs, covered by a thin membrane, could be damaged sufficiently if heavy weapons were brought to bear.

At the sight of the monsters hesitating, the divisional commander, who had been watching the entire scene, excitedly waved his command baton.

“More! Pour it on! Don’t let those monsters move—”

Rooooar!

His voice never continued.

The Poison Breath fired by a Green Wyvern blanketed an area over a hundred meters in radius, and the divisional commander and his command staff were drenched in the powerful acidic poison and melted away.

“C-Commander!”

“The command staff…!”

The People’s Liberation Army lost hundreds of soldiers and high-ranking officers in the blink of an eye and fell into a state of panic.

Officers, noncommissioned officers, and soldiers alike stared at the horrific scene unfolding before their eyes, crying out in shock.

“This can’t be happening…”

“N-No. This isn’t right. It can’t be! This isn’t my mission!”

Someone’s scream spoke for everyone’s feelings.

They had brought their forces in preparation for an emergency, but their primary mission was to join and escort the foreign Hunters who would soon arrive at Chengdu International Airport, then act according to their superiors’ orders.

They had never heard a single word about an army of monsters that was supposed to be thousands of kilometers away invading them.

“What the hell is this…?”

“We’re going to die. We’re all going to die.”

The fear they had briefly forgotten settled over the heads of the People’s Liberation Army.

They were not the Hunters from the Public Security Armed Forces Department fighting at the front of the battlefield. They were nothing more than ordinary people carrying modern firearms.

And their ominous suspicion soon became reality.

A nightmare worse than anything they had imagined.

—Om. Neu. Ha. So. Yu.

A voice broken into disconnected syllables. An eerie noise resembling the static of a radio with an unstable signal echoed across the battlefield.

Black fog that had gathered from somewhere spread over the people’s heads.

—Yen. Wi. Ga. Ji. Ke!

That was when the horrific change occurred.

Swoosh!

Dark mana, black as storm clouds, spread like a web through the blood and corpses.

It breathed new power and souls into the corpses growing cold, binding them in chains and subjugating them.

Thud. Thud-thud-thud.

An army of skeletons gained new life and slowly rose from pools of death.

*Those beings* had woven countless dead together with invisible chains and made them their slaves. They laughed with satisfaction.

—Kik, kikikik.

—Grrk. Kihihih.

* * *

—Grrrrrk.

With a bubbling sound, a man rose to his feet.

He wore armor emblazoned with the Five-Starred Red Flag and carried a massive ax. He looked exactly like the A-rank Hunter Shao Shen remembered.

*…Mr. Yao Wei.*

But Shao Shen could not call the man’s name aloud. He could not bring himself to.

Because he knew that the person standing before him was no longer the man he had known.

*Ah… ahhh.*

If he had not witnessed the man’s head being severed only ten minutes earlier—if he had not seen him rise at this very moment with his own severed head tucked beneath his arm—Shao Shen would have thought of him as a colleague and friend.

But Yao Wei no longer existed.

A new name slipped between Shao Shen’s lips.

“Dullahan…”

A headless knight. A Dullahan.

Shao Shen bit his lip at the sight of his former colleague transformed into a high-level undead monster. Something hot ran down his cheek.

“I’m sorry. I truly am.”

—Graaaar!

As the Dullahan charged with a shriek, Shao Shen shot forward like the wind.

In the past, the two of them had often sparred like this. What began as simple competitive pride continued every day, and whenever the sparring ended, Shao Shen had to put up with Yao Wei’s complaints.

*You little punk, where are your manners? Would it kill you to let me win once?*

*Ha-ha. Let’s go get something to eat. The loser was supposed to pay, so I guess you’re buying again today, Mr. Yao Wei.*

*You’ve got plenty of money at home, and you’re still so greedy. One day, I’ll make you buy me a meal.*

But that had never happened before, and it never would.

Shao Shen had always been the winner.

*Goodbye. Thank you for everything.*

Whoosh! Slice!

The ax swung through empty air, while the aura surging from Shao Shen’s spearhead cleaved through the Dullahan’s upper body.

A line was drawn from the waist upward. The headless knight’s body slowly collapsed.

Thud. Crash.

Shao Shen stared blankly down at the face of the fallen Dullahan—or rather, Yao Wei—and his eyes burned.

“How dare you… How dare you do this…”

Only half a day ago, his friends and colleagues had been laughing and chatting alongside him. Now they had become undead monsters.

The Hunters of the Public Security Armed Forces Department were famous for their strict discipline, but they were not cold-blooded people without a drop of blood in their veins.

The Hunters who had entered battle prepared to die now faced a new kind of fear for the first time: their attachment to one another.

“Get a grip! It’s me, Liu Yinqin! Liu Yinqin!”

“Hyung…!”

—Grrrrrk!

Crack! Boom!

Screams and death rained down from every direction. Unlike the Public Security Armed Forces Department, which had suffered losses approaching half its strength, the army of monsters had actually increased its numbers and continued pouring forward without end.

*Am I going to die here, like this?*

For the first time in his life, Shao Shen thought of death. The situation was desperate enough to make even someone as bright and cheerful as him think that way.

*We never received a warning signal, so communications are probably down. There won’t be any reinforcements either… This really is the end.*

Slice!

After cutting down one undead monster after another as they charged him, Shao Shen laughed hollowly and looked up at the sky.

The sunset was quite beautiful. Once the sun went down and darkness arrived, he would never see a sight like this again.

*At least the last sky I see is pretty decent…*

Huh?

Shao Shen blinked, unable to continue his thought.

Something enormous was approaching the battlefield at tremendous speed high above.

*An airplane?*

Roooooar!

A gigantic aircraft wreathed in flames. And someone’s shout echoing across the vast sky.

“Hey! Monsters!”

“…”

—…?

*Am I hearing things?*

Everyone on the battlefield, not only Shao Shen, looked up at the sky.

Someone’s voice, carrying an almost palpable madness, rang out like thunder.

“I’m going to ram it!”

Ram what?

Shao Shen soon understood what those words meant.

Rumble, rumble, rumble!

The airplane’s enormous fuselage swept straight across the battlefield.
```
