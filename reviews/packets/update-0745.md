<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0745.txt",
      "sha256": "d9a48323d96adfa11778cf9ee5017f70985584cbb9aeebb6c171d46e4812a56a",
      "bytes": 13776
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ff9edb363823965f660e8c6ff6b551194c3e3472a5a81e83df0d6c0c85e652b3",
      "bytes": 2510
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1b107b0174ca91cc940eb768ed87f0404acc28e96440c44ff26c2ae7758c63a3",
      "bytes": 215136
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3c691b32f7f4e892c38814c64f0737814158e0a9e892275175892dce518a7e1a",
      "bytes": 553
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "340268bc6b1d3116782f9446ca28496d4b9f58ec8e2f964d4d1d8e5e7901b3e4",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "936357991f1db5039d9a1d2aea70404c394046d1784a7b7a07bb03d2d4bbc013",
      "bytes": 228554
    }
  ],
  "estimated_tokens": 8950
}
-->

# Durable State Update — Chapter 745

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 745. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 745. Profile updates may replace only one
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
  "chapter": 745,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 745,
    "continuity_sources": [745],
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
    "The retired Grand Mage Siegfried Wassmann, one of only three Grand Mages in the world and Switzerland's greatest Hunter, was found dead in his sealed hideout.",
    "Siegfried's corpse was unnaturally dried out without wounds, rot, or odor, suggesting that something drained his life force through an unknown form of magic.",
    "Michael Silbert remains the strongest suspect because he knows that Cheon Taemin is unconscious and may know about A Area, but the source of his knowledge is unknown.",
    "The Prophet remains a second major suspect connected to the terrorist campaign, and even the Pentagon has not located him.",
    "Jin has forcibly accepted the Supreme Peak Quest Unknown Death, whose mission is to discover the truth behind Siegfried's death; its Reward and Failure are unknown.",
    "Mana levels are rising sharply, and mutation Gate phenomena continue occurring dozens of times daily while the distribution of magical power has amplified again.",
    "Michael has gained an unexplained increase in power through a painful transformation and now possesses overwhelming strength.",
    "Michael and Huginn are bribing media outlets and sustaining malicious coverage intended to weaken Jin's public support.",
    "Magic Johnson has received stolen research materials from Siegfried's laboratory and is investigating them for clues.",
    "Huginn has completed an undisclosed operation whose consequences are expected to begin within three days.",
    "An enormous ancient monster has awakened in the deep sea after having been believed gone for a very long time."
  ],
  "continuity_sources": [
    744
  ],
  "open_questions": [
    "Who killed Siegfried Wassmann, by what magic, and why?",
    "How did Michael Silbert learn about A Area and Cheon Taemin's condition, and did he order Siegfried's death?",
    "What connection, if any, does The Prophet or the terrorist network have to Siegfried's death?",
    "What is Huginn's undisclosed operation, and can its consequences actually bring Jin down?",
    "What is the identity, purpose, and origin of the ancient monster that awakened in the deep sea?"
  ],
  "safe_through": 744,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 스켈레톤 킹 as Skeleton King.",
    "Render A구역 as A Area.",
    "Render 마력 as magical power, distinct from mana.",
    "Render 지크프리트 바스만 as Siegfried Wassmann and 실베르트 as Silbert."
  ],
  "version": 1
}
```

## Exact glossary matches

| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 알라 | **Allah** | Deity invoked by the Middle Eastern terrorist groups' rhetoric. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 모세 | **Moses** | Figurative comparison for Chuck Hagel carrying a cigar instead of a staff. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 도쿄 | **Tokyo** | City visible behind Huginn's departing ship. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 743
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 744
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of a hidden Middle Eastern terrorist organization whose ten warriors carried out the day's coordinated attacks.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered as a sacred figure by the followers.

## Korean source

```text
＃745화



사막의 밤은 싸늘하다.

작열하던 햇빛과 아지랑이가 사라진 자리에는, 영하의 기온과 유독 커다랗게 뜬 달만이 남아 있을 뿐이다.

자그마치 60도에 달하는 일교차.

그러나 초승달 모양의 모래 언덕을 오르는 누군가의 발걸음은, 혹한의 추위조차 막아설 수 없었다.

스륵.

높은 경사를 오르고 있음에도 마치 미끄러지는 듯 나아가는 걸음걸이.

실크로 만들어진 얇은 로브의 끝자락이 모래알을 스치다, 이내 한 자리에 멈춰 섰다.

“이곳이군.”

고저 없는 목소리가 울려 퍼진 그 순간, 아무것도 없는 허공이 일렁였다.

슥.

미세한 소리와 함께 모래 언덕 위에 내려앉은 십여 개의 인영(人影).

하나같이 검은 복면과 터번으로 얼굴을 가린 그들은 공손히 한쪽 무릎을 꿇으며 속삭였다.

“인샬라. 이 땅에 다시 임하신 위대한 선지자를 뵙나이다.”

그들의 앞에 홀로 우뚝 서 있는 한 사람, 선지자의 로브가 가볍게 흔들렸다.

“인샬라. 언제쯤 너희가 스스로 모습을 드러낼까 궁금했었다.”

처음부터 모든 것을 꿰뚫고 있었음을 의미하는 선지자의 한 마디에, 복면 위로 드러난 십여 쌍의 눈동자가 흔들렸다.

“선지자시여…….”

“안다. 너희가 나를 위하고 있음을. 그러니 내 명령을 거스르면서까지 뒤를 따랐겠지.”

“불복한 죄를 물으신다면 기꺼이 죽음으로 값을 치르겠나이다. 하지만 저희, 하샤신(Hasasin)은 어떤 상황에서도 당신을 곁을 떠나지 않을 것입니다.”

하샤신. 혹은 어쌔신.

13세기 무렵 적들에 의해 본거지를 함락당한 뒤, 단순한 종교 분파로써 명맥을 이어 오다 대격변을 기점으로 부활한 이 유서 깊은 암살 집단은 결코 자신들의 뜻을 굽히지 않았다.

“서방의 이단자들은 교활한 동시에 강한 힘을 지니고 있습니다. 만약 선지자께서 놈들의 눈에 띄시기라도 한다면…….”

“알-니자르. 누구보다 충성스러우나, 어리석고 근심 많은 자여.”

“……!”

“나를 보아라.”

흠칫 몸을 떤 하샤신의 수장이 조심스럽게 고개를 들었다.

위대하기 그지없는 자신의 선지자가 별 무리가 흩뿌려진 밤하늘을 등진 채 그를 내려다보고 있었다.

이상하리만치 어두운 로브 사이, 신비롭게 빛나는 안광(眼光)과 함께.

“아직도 모르겠느냐.”

선지자가 하늘을 향해 양팔을 뻗었다.

우우웅.

거대한 기운이 로브 자락을 밀어 내며 부풀어 올랐다. 바람이 멎고 공기가 진동했다.

저도 모르게 숨을 삼킨 하샤신들의 시선이 선지자의 손을 따라 움직인 다음 순간.

솨아아악.

그들은 볼 수 있었다. 하늘에서 시작되어 반경 수백여 미터를 둥글게 감싼 투명한 막(膜)을.

그리고 그것은 어떤 과학의 산물로도, 심지어는 마법으로도 간파할 수 없는 보호막인 동시에 적들의 시선으로부터 그들의 모습을 감추는 가림막이었다.

“내가 너희를 지키는 한, 저들은 우리의 그림자조차 발견할 수 없을 것이다.”

“……!”

“……!”

극한의 훈련을 견뎌 낸 하샤신들조차 이 순간만큼은 격동하는 감정을 감출 수 없었다.

자신들의 선지자가 이토록 놀라운 능력을 가졌다는 것에 한 번. 또 하찮은 종복에 불과한 그들을 ‘우리’라 칭해 주었다는 것에서 다시 한번.

“인샬라……!”

“선지자시여!”

감격과 기쁨에 가득 찬 부르짖음이 고요한 사막을 울린다. 그러나 오늘 선지자가 보여 줄 기적은 그것으로 끝이 아니었다.

스륵,

풍성하고 긴 로브의 옷소매가 펄럭인 그때, 그들이 서 있던 초승달 모양의 모래 언덕이 흔들렸다.

아니, 갈라졌다.

파스스슥!

그것은 실로 경이로운 광경이었다.

지금으로부터 아득한 과거. 모세가 홍해(紅海)를 갈라 히브리인들을 이끌었다면, 천년이 넘는 세월을 넘어 나타난 새로운 선지자는 거대한 사해(沙海)의 일부를 반으로 나누었다.

그리고 그 무수한 모래알 속에 숨겨져 있던 것은, 마치 신이 내린 선물처럼 달빛을 받아 반짝였다.

“세상에…….”

“선지자시여. 저것들이 대관절 무엇입니까?”

하지만 선지자는 하샤신들의 물음에 답하는 대신, 말없이 손을 뻗었다.

철컹. 철컹. 철컹!

보이지 않는 기운에 의해 폭발하듯 터져 나가는 자물쇠들.

마침내 수십여 개의 철궤(鐵櫃)에 담겨 있던 내용물을 확인한 하샤신의 수장이 눈을 부릅떴다.

“이, 이건.”

어둠으로도 가릴 수 없는 환한 빛.

지금껏 본 적 없는 수많은 금괴와 은괴. 거기에 더해 각종 마법이 부여된 무기가 흩뿌리는 광채가 그의 동공을 어지럽힌다.

그러나 그를 가장 경악하게 만든 것은 따로 있었다.

“마정석……!”

신음처럼 흘러나온 외침은 사실이었다.

마정석.

그것도 상급에서 최상급이 분명한 마정석이 무려 수백 개에 이른다. 더군다나 그중에서는 유독 크고, 거대한 기운을 뿜어내는 것들도 있었다.

스아아아아.

하샤신을 이끄는 우두머리이기 이전에, S급 헌터의 경지에 이른 그조차 쉽사리 접근할 수 없는 강력한 기운.

“흡.”

순간 자신도 모르게 헛숨을 삼킨 하샤신 수장의 귓가에, 특유의 고저 없는 목소리가 닿았다.

“S급 마정석이다. 본래의 힘을 고스란히 간직한.”

“서, 선지자시여.”

“물러서라. 너희가 감당할 수 있는 힘이 아니니.”

나직한 경고와 함께 정제되지 않은 S급 마정석들이 두둥실 떠올랐다.

살아 있는 생물체처럼 움직여 선지자의 로브로 빨려 들어간 그것의 개수는 무려 열 개.

그 광경을 바라보는 하샤신 수장의 시선이 파르르 떨렸다.

‘선지자께서는 도대체 어떻게 저것들을…….’

선지자가 상식을 벗어날 만큼 극히 뛰어난 능력을 지녔다는 것은 이미 알고 있던 바.

그러나 대격변 당시부터 지금까지, 공식적으로 인류 역사에 등장한 S급 몬스터는 백여 마리에 불과하다.

매우 드물게 극소수의 A급 몬스터가 S급 마정석을 품고 있는 경우도 있었지만, 그건 말 그대로 이례적인 일이었고 당장 수많은 게이트가 존재하는 중동 지역에서도 S급 마정석의 출현은 한두 번이 고작이었다.

한데 바로 그 S급 마정석이 자그마치 열 개나 모여 있다.

그것도 본래의 마력을 고스란히 간직한 채로.

‘엄청난 양이다. 믿을 수 없을 만큼.’

선지자에게 무한한 신뢰를 보내는 그지만, 이번만큼은 묻지 않을 수 없었다.

고개를 돌린 그 순간. 로브 사이로 은은한 빛을 흘리는 안광을 마주하기 전까지는.

“묻겠다. 지금 네 앞에 서 있는 이가 누구라고 생각하느냐.”

“……!”

이미 모든 것을 꿰뚫어 본 듯한 그 시선에, 하샤신의 수장은 번개를 맞은 듯한 충격을 느끼며 무릎을 꿇었다.

감히 자신 따위가 선지자께서 하시는 일에 의문을 품다니.

이는 있을 수도 없고, 있어서도 안 되는 일이었다.

“위대하신 선지자시여. 부디 이 죄 많은 종을 용서하소서!”

순식간에 얼어붙은 공기. 하샤신들은 각자의 무기를 매만지며 선지자의 입이 열리길 기다렸다.

만약 그가 명령을 내린다면, 그들은 일말의 망설임도 없이 자신들의 수장을 제거할 준비가 되어 있었다.

그는 신의 말씀을 전하는 예언가요, 모두를 이끄는 선지자니까.

선지자 무함마드의 죽음 이후, 이슬람 세계는 천년이 넘는 세월 동안 반목하며 싸웠고 사막의 모래알은 피로 얼룩졌다.

세월이 흐름에 따라 극소수의 누군가는 막대한 부와 권세를 누렸으나, 석유로 쌓아 올린 대도시에서 우선시되는 것은 알라의 말씀이 아닌 배교자들의 자본주의뿐.

이제는 서로를 향해 칼날을 겨누던 알라의 자손들을 하나의 뿌리로 모으고, 서방세계에서조차 탄압받는 동포들을 구해야 할 때였다.

위대하신 신의 이름으로.

지금으로부터 수십여 년 전, 신을 대신하여 자신들에게 찾아온 선지자의 이름으로.

그리고 보이지 않는 칼날이 서서히 적막을 베어 내던 그때, 굳게 닫혀 있던 한 사람의 입이 열렸다.

“알 니자르.”

나이도, 심지어는 성별도 구분할 수 없는 목소리.

그 부름에 하샤신의 수장은 숨을 삼켰다. 그의 전신은 이미 식은땀으로 흥건하게 젖어 있었다.

“선지자시여.”

“네게 마지막으로 당부하마. 아직은 성숙하지 못한, 그렇기에 더욱 마음이 가는 신의 아들아.”

“……!”

“인샬라. 이 모든 것은 신께서 내게 주신 오랜 인내와 안배의 결과이니, 너희는 절대 의심하지 말지어다. 알겠느냐?”

“명심. 명심하겠습니다.”

투둑.

식은땀과 눈물이 뒤섞인 액체가 모래알을 적셨다.

감격과 안도로 몸을 떠는 하샤신의 수장을 자애롭게 응시하던 선지자가 말을 이었다.

“이제 다시 때가 되었다. 준비하고 있던 네 형제들에게 일러라.”

그 한 마디에 모두의 눈이 번쩍 뜨였다.

이미 그들 사이에서는 ‘알라의 심판’이라 불리는 그날로부터 어언 열흘에 가까운 시간이 흐른 지금.

선지자를 따르는 모두가 다음으로 찾아올 심판의 날을 목이 빠지게 기다리고 있었다.

“선지자시여. 그 말씀은…….”

“신께서 원하신다. 내부를 좀 먹는 배교자들과 서방의 이단자들에게 신의 철퇴를 내려라.”

복면 위로 드러난 눈동자들이 광신(狂信)과 환희로 번들거렸다.

선지자는 별 무리가 흩뿌려진 하늘을 바라보며 뇌까렸다.

“마지막까지, 얼마 남지 않았다.”

누군가는 재앙을 원하고, 누군가는 재앙을 막기 위해 애쓰며, 또 다른 누군가는 그 이상의 무언가를 원한다.

지금 이 순간에도, 그들은 각자의 목적을 향해 달려가고 있었다.



* * *



스기하라 교이쿠는 오랫동안 화물업에 종사한 인부(人夫)다.

도쿄에서 평생을 살아온 토박이였고, 동시에 젊은 적부터 해운(海運)업에 몸담은 잔뼈 굵은 인부이기도 했다.

간혹 육체노동을 하는 그를 무시하는 사람들도 있었지만, 별 상관은 없었다.

세상 모두가 헌터나 변호사, 의사와 같은 직업을 가질 수는 없는 법이고 자신 역시 이 세상에 꼭 필요한 존재였으니까.

하지만 근래에는 영 기분이 좋지 않았다.

아니, 기분이 좋을 수가 없었다.

‘칙쇼. 빌어먹을 몬스터 놈들.’

불과 열흘 전, 도쿄에서 발생한 몬스터 웨이브에 많은 사람들이 죽고 다쳤다.

도쿄 토박이인 그가 내심 자랑스럽게 생각했던 도쿄 타워가 처참하게 무너졌고, 삼십 년간 단골이던 치킨집도 그 여파에 휘말려 사라졌다.

‘사장이 조센징인 건 마음에 안 들었지만, 그래도 치킨 하나는 끝내줬었는데.’

퇴근 후 한국표 치맥을 즐길 수 없다는 사실이 교이쿠를 슬프게 만들었지만, 그것과는 별개로 그는 오늘도 직장에 출근했다.

“교이쿠 상. 오셨어요?”

“여어.”

동료 인부들과 간단한 인사를 주고받고 곧바로 현장 투입. 그가 근무하는 도쿄만(灣)은 이미 화물선으로 인산인해였다.

“어디부터 시작하면 되지?”

“이미 작업 시작했어요. 같이 가시죠.”

스기하라 교이쿠는 선박에 화물을 적재하며 동료들과 이런저런 이야기를 나누었다.

근래 들어 도쿄의 마력 분포도가 특히 급증하고 있다는 소식, 명문 정치가 출신인 현 총리가 또 미친 소리를 했다는 뉴스.

그리고 쓰나미에 관한 이야기 등등.

“쓰나미?”

“예. 도쿄에 서서히 가까워지고 있다더라고요. 규모가 엄청나대요.”

“흠.”

“걱정마세요. 정부에서도 금방 가라앉을 거라고 했으니까.”

“뭐, 그렇겠지.”

약간 우려가 되긴 했지만, 딱 거기까지였다.

쓰나미라고 해 봤자 결국 도쿄에까지 미치지는 않는다.

특히 도쿄만은 말 그대로 육지로 바다가 들어간 만(灣)의 형태이기도 하고, 마법을 이용한 방어 시스템도 철저히 구축되어 있었다.

‘오늘 작업이 마무리되면, 새로운 한국 치킨집을 찾아볼까.’

교이쿠는 시답지 않은 생각을 떠올리며 허리를 폈다. 그리고 동시에 석상처럼 굳었다.

“어?”

저게 뭘까.

처음으로 뇌리를 스친 생각. 그리고 다음 순간. 조금 전 들었던 한 가지 소식이 머릿속에 울려 퍼졌다.

‘쓰나미.’

멍하니 입을 벌린 그의 시선이 항구 밖의 바다를 향했다.

지금껏 본 적 없는 거대한 파도가, 햇빛을 가릴 듯이 높이 솟구친 채 달려오고 있었다.

고오오오오옹.

듣는 것만으로도 얼어붙는, 알 수 없는 무언가의 울음소리와 함께.
```

## Final English reading copy

```markdown
# Chapter 745

The desert night was bitterly cold.

Where the scorching sunlight and shimmering heat had vanished, nothing remained but subzero temperatures and an unusually enormous moon.

A daily temperature swing of no less than sixty degrees.

But even the frigid cold could not stop the footsteps of someone climbing a crescent-shaped dune.

*Sssrrk.*

Despite ascending a steep slope, the figure moved as though gliding across the sand.

The hem of a thin silk robe brushed against the grains before coming to a stop.

“This is the place.”

The moment that flat voice rang out, the empty air rippled.

*Ffft.*

With the faintest sound, a dozen or so figures descended onto the dune.

Every one of them had their face concealed by a black mask and turban. They politely dropped to one knee and whispered,

“Inshallah. We pay our respects to the great Prophet who has returned to this land.”

Standing alone before them, the Prophet’s robe fluttered lightly.

“Inshallah. I wondered when you would finally reveal yourselves.”

Those words made it clear that The Prophet had seen through everything from the beginning. The dozen pairs of eyes visible above the masks trembled.

“Prophet…”

“I know. I know that you act for my sake. That is why you followed me even while defying my orders.”

“If you would punish us for our disobedience, we would gladly pay for it with our lives. But we, the Hasasin, will never leave your side, no matter the circumstances.”

The Hasasin. Or the Assassins.

After their stronghold was conquered by their enemies around the thirteenth century, this venerable order of assassins had survived as nothing more than a religious sect. Then, with the Great Cataclysm, they had risen again.

And they had never once bent their will.

“The Western heretics are both cunning and powerful. If you were to be discovered by them…”

“Al-Nizar. More loyal than anyone, yet foolish and full of worry.”

“…”

“Look at me.”

The leader of the Hasasin flinched and cautiously raised his head.

The great Prophet stood against a sky scattered with stars, gazing down at him.

A mysterious light shone from the eyes framed by the strangely dark folds of the robe.

“Do you still not understand?”

The Prophet stretched both arms toward the sky.

*Vwoooom.*

An immense force swelled, pushing out the edges of The Prophet’s robe. The wind died, and the air vibrated.

The Hasasin swallowed unconsciously. Their gazes followed the Prophet’s hands, and in the next moment—

*Shhhhhhhk.*

They saw it.

Beginning in the sky and curving around an area several hundred meters in radius, a transparent membrane had formed.

It was both a protective barrier that no product of science—not even Magic—could see through and a screen that concealed them from their enemies’ eyes.

“As long as I protect you, they will not discover even our shadows.”

“…”

“…”

Even the Hasasin, who had endured extreme training, could not hide their surging emotions at that moment.

First, because their Prophet possessed such astonishing abilities.

And again, because The Prophet had called even lowly servants like them “us.”

“Inshallah…!”

“Prophet!”

Their cries of joy and emotion echoed through the quiet desert.

But that was not the end of the miracle the Prophet would show them today.

*Sssrrk.*

As the long, voluminous sleeve of The Prophet’s robe fluttered, the crescent-shaped dune beneath their feet began to shake.

No—it split apart.

*Crk-crk-crk!*

It was a truly miraculous sight.

In the distant past, if Moses had parted the Red Sea and led the Hebrews across, then this new Prophet, appearing after more than a thousand years, had divided part of a vast sea of sand in two.

And what had been hidden beneath the countless grains of sand glittered in the moonlight like a gift from God.

“My God…”

“Prophet. What in the world are those?”

But instead of answering the Hasasin’s questions, the Prophet silently extended a hand.

*Clank. Clank. Clank!*

Locks burst apart as though exploding under the force of invisible energy.

At last, the leader of the Hasasin saw the contents of the dozens of iron chests and opened his eyes wide.

“T-this is…”

A bright light that even the darkness could not conceal.

Countless gold and silver bars unlike anything he had ever seen. On top of that, the radiance of weapons imbued with various forms of Magic dazzled his pupils.

But something else shocked him more than anything.

“Magic Gems…!”

The cry that escaped him like a groan was the truth.

Magic Gems.

And not just any Magic Gems—there were hundreds of them, clearly ranging from high-grade to top-grade. Some among them were especially large and radiated an immense force.

*Fwoooosh.*

Even he, a leader of the Hasasin who had reached the realm of an S-rank Hunter, could not easily approach that powerful energy.

“Hk.”

The leader of the Hasasin involuntarily sucked in a startled breath. Then the Prophet’s familiar, toneless voice reached his ears.

“They are S-rank Magic Gems. They retain all their original power.”

“P-Prophet…”

“Stand back. This is power you cannot handle.”

With that quiet warning, the unrefined S-rank Magic Gems rose into the air.

They moved like living creatures before being drawn into the Prophet’s robe.

There were ten of them.

The leader of the Hasasin’s gaze trembled as he watched.

*How in the world does the Prophet possess those…?*

He had already known that the Prophet’s abilities were extraordinary beyond common sense.

But from the time of the Great Cataclysm until now, only a little over a hundred S-rank monsters had officially appeared in human history.

On extremely rare occasions, a tiny number of A-rank monsters had possessed S-rank Magic Gems. But those instances were exactly what they were—exceptional cases. Even in the Middle East, where countless Gates existed, S-rank Magic Gems had appeared only once or twice.

And yet ten S-rank Magic Gems had gathered here.

All of them retaining their original magical power.

*It’s an incredible amount. Unbelievable.*

Despite his boundless faith in The Prophet, this time he could not help but ask—or so he thought.

The moment he turned his head, he met the faint glow of The Prophet’s eyes between the folds of the robe.

“I will ask you. Who do you think the person standing before you is?”

“…”

That gaze seemed to have already seen through everything.

The leader of the Hasasin felt as though he had been struck by lightning and dropped to his knees.

How dare someone like him question what the Prophet was doing?

It was something that could not happen—and must never happen.

“Great Prophet, please forgive this sinful servant!”

The air froze in an instant.

The Hasasin touched the weapons at their sides and waited for the Prophet to speak.

If The Prophet gave the order, they were prepared to eliminate their own leader without a moment’s hesitation.

Because The Prophet was a prophet who conveyed God’s word and the one who led them all.

After the death of the Prophet Muhammad, the Islamic world had fought and feuded for more than a thousand years, and the sands of the desert had been stained with blood.

As the years passed, a tiny few enjoyed immense wealth and power. But in the great cities built on oil, what took priority was not the word of Allah, but the capitalism of the apostates.

Now was the time to gather Allah’s children, who had once turned blades against one another, beneath a single root—and to save their brothers persecuted even in the Western world.

In the name of the great God.

In the name of the Prophet who had come to them decades ago in God’s place.

And just as an invisible blade slowly cut through the silence, one tightly closed mouth finally opened.

“Al-Nizar.”

It was a voice that revealed neither age nor even gender.

At the call, the leader of the Hasasin swallowed. His entire body was already soaked in cold sweat.

“Prophet.”

“I will give you one final warning, son of God. You are still immature—and that is precisely why I care for you all the more.”

“…”

“Inshallah. All of this is the result of the long patience and providence God has granted me. You must never doubt it. Do you understand?”

“I will remember. I will remember it well.”

*Drip.*

A liquid mixed with cold sweat and tears dampened the grains of sand.

The Prophet gazed benevolently at the trembling leader of the Hasasin, whose body shook with emotion and relief, and continued.

“The time has come again. Tell your brothers who have been preparing.”

At those words, everyone’s eyes flashed open.

Nearly ten days had passed since the day they called “Allah’s Judgment.”

Everyone who followed the Prophet had been waiting impatiently for the next day of judgment.

“Prophet. Do you mean…”

“God wills it. Bring down God’s hammer upon the apostates gnawing away at us from within and the Western heretics.”

The eyes visible above the masks gleamed with fanaticism and exultation.

The Prophet gazed up at the star-scattered sky and muttered,

“There isn’t much time left until the end.”

Some wanted catastrophe. Some struggled to prevent it. And still others wanted something beyond it.

Even now, they were all rushing toward their own purposes.

* * *

Sugihara Gyoiku was a laborer who had worked in cargo shipping for a long time.

He was a lifelong Tokyo native and, at the same time, a seasoned laborer who had entered the maritime transport industry when he was young.

Some people occasionally looked down on him for doing manual labor, but he did not particularly care.

Not everyone in the world could become a Hunter, lawyer, or doctor. And he, too, was a necessary part of this world.

But lately, he had been in a terrible mood.

No—there was no way he could feel good.

*Chikushō. Those damn monsters.*

Just ten days earlier, a monster wave in Tokyo had killed and injured many people.

Tokyo Tower, which he had secretly been proud of as a Tokyo native, had collapsed horribly. The chicken restaurant he had frequented for thirty years had also vanished in the aftermath.

*I didn’t like that the owner was a Chosenjin,[^1] but the chicken was incredible.*

The fact that he could no longer enjoy Korean-style chicken and beer after work made Gyoiku sad. But setting that aside, he went to work again today.

“Gyoiku-san. You’re here?”

“Yo.”

After exchanging brief greetings with his fellow laborers, he went straight to the work site.

Tokyo Bay, where he worked, was already packed with cargo ships.

“Where should we start?”

“They’ve already started. Come on.”

Sugihara Gyoiku loaded cargo onto the ships while chatting with his coworkers about this and that.

News that Tokyo’s magical-power distribution had been rising particularly sharply lately. Reports that the current prime minister, who came from a prestigious political family, had said something insane again.

And talk about the tsunami, among other things.

“A tsunami?”

“Yes. Apparently, it’s gradually getting closer to Tokyo. They say it’s enormous.”

“Hmm.”

“Don’t worry. The government said it would die down soon.”

“Well, I suppose.”

He was a little worried, but that was all.

Even if it was a tsunami, it would not reach Tokyo in the end.

Tokyo Bay, in particular, was literally a bay where the sea extended into the land, and its magical defense systems had also been thoroughly established.

*When I finish work today, maybe I’ll look for a new Korean chicken place.*

Gyoiku straightened his back, thinking about something pointless.

And at the same time, he froze like a stone statue.

“Huh?”

*What is that?*

That was the first thought that flashed through his mind.

Then, in the next moment, something he had heard just a little while ago rang through his head.

*The tsunami.*

Gyoiku stared blankly, mouth open, toward the sea beyond the harbor.

A colossal wave unlike anything he had ever seen was racing toward him, rising so high that it seemed capable of blocking out the sunlight.

*Goooooong.*

Along with the cry of some unknown thing—a sound that froze him merely by hearing it.

[^1]: A Japanese ethnic slur for Koreans.
```
