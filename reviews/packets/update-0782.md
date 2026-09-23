<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0782.txt",
      "sha256": "f08ae51015fb23894f9b26c80e017804b86f12eb2dac5d9da384e2a725a8f73e",
      "bytes": 12619
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "536aec57a2424f5ac15386d35eba2734d66279fa2b11e995dd639c530efc8108",
      "bytes": 1008
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "47349c578ce3a378dc53173dec4002c0828b8095d08eadab83cdfaafdabfc433",
      "bytes": 223666
    },
    {
      "path": "characters/Michael.md",
      "sha256": "5ca9dca77889558090e99465c83fcbd360cb8dfaac47329eb995fcc67947eea5",
      "bytes": 887
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "b3e87a7e75172278d553047f899874f4a8fbfcacef8125a62587fca2cbfe2dae",
      "bytes": 693
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "302a52e41f2bff1ce437d4c5472677761047d3a5c5a63b6eebc90be858388339",
      "bytes": 243088
    }
  ],
  "estimated_tokens": 8160
}
-->

# Durable State Update — Chapter 782

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 782. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 782. Profile updates may replace only one
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
  "chapter": 782,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 782,
    "continuity_sources": [782],
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
    "Michael Silbert has absorbed magical power and integrated it with mana, becoming something neither human nor monster.",
    "Michael says Cheon Taemin is the only person he fears; Taemin remains in a coma and is absent.",
    "Michael threatens to expose the private secrets of his former supporters; nearly half of the Hunters at the World Hunter Federation gathering lower their weapons and side with him.",
    "Jin’s allies launch a prepared attack on Michael’s defecting supporters at the National Assembly.",
    "Jin and Michael have begun a direct clash; Jin’s fire dragon has surged from his dantian."
  ],
  "continuity_sources": [
    781,
    780
  ],
  "open_questions": [
    "Who will prevail in the fighting at the National Assembly?",
    "What will Michael do if his supporters’ secrets are exposed or his power is challenged?"
  ],
  "safe_through": 781,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 열화문    | **Fire Gate Clan**               |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 마정석     | **Magic Gem**         |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 골검 | **Bone Sword** | Sword wielded by the Skeleton Knights. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 781
- **Aliases:** None
- **Role:** Michael Silbert is Odin Guild Master and a public hero positioning himself to lead the World Hunter Federation, secretly able to absorb monsters’ magical power while concealing it alongside mana.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 773
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃782화



꽈아아아앙!

굉음을 이기지 못한 귓가가 먹먹해진다.

그러나 이명(耳鳴)보다 앞서 찾아온 것은, 짧은 순간 맞닿은 두 손을 타고 전해진 어마어마한 충격파였다.

퍼엉!

마치 거인의 손바닥이 전신을 후려치는 듯한 느낌.

그 항거할 수 없는 거대한 힘에 의해 뒤로 튕겨 나간 내가 허공에서 신형을 비틀기가 무섭게, 칼날과도 같은 잿빛 기운이 코앞으로 들이닥쳤다.

서걱!

아주 미세한, 그야말로 한 끗 차이.

번개처럼 고개를 돌린 내 코끝을 스쳐 지나간 그것은 지면을 두부처럼 갈랐고, 나는 부드럽게 그 위로 내려앉았다.

그리고 잿빛 기운을 전신에 두른 채 걸어오는 한 사람을 응시했다.

아니, 이제는 인간의 울타리를 벗어난 무언가를.

“미카엘 실베르트.”

내 부름에 놈이 웃었다. 움푹 파인 보조개에 드리운 음영(陰影)이 유난히도 짙게 느껴지는 것은 결코 단순한 착각이 아니다.

콰직. 콰지직.

한 걸음, 한 걸음 내딛는 발걸음을 따라 지면이 으스러진다.

미카엘 실베르트로부터 흘러나오는 기운이 얼마나 압도적이었는지, 비교적 가까운 곳에서 전투를 치르던 이들조차 헛숨을 삼키며 최대한 거리를 벌릴 정도였다.

하지만…… 나는 아니다.

물러설 수도 없고, 물러설 생각도 없다.

오늘 이 자리에 오기 전 결심했듯이, 그저 맞서 싸울 뿐이다.

여유롭게 다가오는 저 괴물을 막기 위해. 수십억에 달하는 인류를 다시 한번 불구덩이에 밀어 넣지 않기 위해.

나는 힘주어 걸음을 내디뎠다.

쉭.

단 한 걸음.

전신을 스치는 바람과 함께 공간이 접혔다. 동시에 머릿속에서 완성된 두 개의 키워드가 명령어로 발현(發現)했다.

‘인벤토리 오픈, 소환.’

아무도 볼 수 없는 곳에 감추어 두었던 한 자루의 창이 손아귀에 감긴다.

어느덧 느려진 세상 속, 창날을 타고 솟구친 청백색의 화염이 어둠이 출렁이는 회색빛 눈동자를 물들이며 내리그어졌다.

미카엘 실베르트.

저 괴물의 정수리를 향해.

화아아악!

열기가 집중된 반경 수 미터의 모든 수분이 증발한다.

닿는 것만으로도 불타오를 것 같은 공기 속에서 크게 뜨인 놈의 눈동자가 보였다.

이 자리의 누구도 예상치 못했던 일격 앞에서도, 여전히 올라가 있는 입꼬리도 함께.

그리고 그 순간.

빛살처럼 쳐올린 한 자루의 검이, 놈의 정수리를 향해 떨어져 내리던 백염(白炎)의 창날을 후려쳤다.

콰앙!

마치 하늘이 쪼개지는 듯한 굉음이 울려 퍼졌다.

그그극, 한 치의 양보도 없이 허공에서 맞물린 창날과 검신 너머로 낮은 웃음소리가 흘러나왔다.

“역시. 줄곧 그 창이 안 보인다 했지.”

“……!”

“그래서, 자네가 준비한 깜짝 마술은 다 끝났나?”

까드득.

혼탁한 오라에 휩싸인 검신이 화염을 머금은 창날을 조금씩 밀어낸다.

인간이라고는 믿기지 않는 엄청난 힘과 끝을 모르고 샘솟는 미증유(未曾有)의 기운이, 이내 일거에 폭발하듯 터져 나왔다.

콰아아아!

그리고 그 거대한 힘을 정면에서 맞닥트린 순간, 나는 새삼 확실하게 깨달았다.

시스템 덕분에 한계를 아득히 초월한 신체 능력도, 무림의 그 누구도 경시하지 못하는 삼 갑자의 공력으로도 놈의 기운을 완전히 억누를 수 없다는 것을.

‘만약 이 힘의 여파가 주위로 미친다면…….’

뒷일은 굳이 깊게 생각하지 않아도 알 수 있었다.

적어도 수십 명은 죽는다는 것을. 그리고 그중 절반은 이런 자리에서 죽어서는 안 될 영웅들이라는 것을.

결국 내게 남아 있는 선택지는 하나뿐이었다.

‘상쇄(相殺).’

뇌리에 떠오른 한 단어와 함께, 나는 반발력에 의해 위로 쳐든 백염을 미련 없이 놓으며 양손을 떨쳤다.

화륵, 퍼어엉!

오른손으로는 멸염신권. 왼손으로는 화염신장.

일권(一拳)과 일장(一掌).

열화문이라는 뿌리에서 갈라져 나온 두 개의 가지가, 그 끝에서 피워 올린 두 줄기의 불꽃이 혼탁한 오라와 부딪혔다.

콰드드득!

어마어마한 반발력과 함께 욱신거리는 통증이 전신으로 전해지고, 밀려 나가는 발끝을 따라 밭고랑처럼 뒤집힌 지면이 흉한 내부를 드러낸다.

하지만 나는 오직 눈앞의 기운에만 집중했다. 양손에 깃든 화염을 혼탁한 오라 안으로 끊임없이 흘려보냈다.

집어삼키는 대신 갉아먹으며.

막아서는 대신 흐트러트리며.

그리고 마침내 눈에 띄게 줄어든 그 파괴적인 기운의 집합체를, 온 힘을 다해 비틀어 등 뒤로 내던졌다.

후우우웅, 꽈앙!

찢어지는 듯한 굉음과 진동이 국회의사당을 뒤흔들었다.

순간 중심을 잃고 비틀거리는 배신자 중 한 사람의 가슴에 골검(骨劍)을 박아 넣은 스켈레톤 킹이 외쳤다.

“조심!”

그건 적절한 조언이었지만, 반 박자 늦은 조언이기도 했다.

나는 이미 눈앞까지 들이닥친 미카엘 실베르트와 마주하고 있었으니까.

슈확!

혼탁한 빛을 머금은 오라가 목덜미를 스쳤다.

마치 섬광과도 같은 찌르기를 피해 내며 놈의 안으로 파고든 나는 망설임 없이 일권을 뻗었다.

퍼엉!

오라에 겹겹이 휩싸인 손으로 멸염신권을 막아 낸 미카엘 실베르트가 무릎을 차올렸다.

아니, 차올리려 하던 그 순간 돌연 나를 밀쳐 내며 물러났다.

쉭! 퍼걱!

허공에서 맹렬하게 내리꽂힌 은빛 섬광이 조금 전 놈이 서 있던 그 자리를 정확히 관통한다.

묵묵히 백염을 뽑아 드는 나를 바라보던 놈이 부드럽게 웃었다.

“그래, 너무 쉬우면 재미없지.”

재미라, 재미.

비명과 핏물이 어지럽게 뒤섞이고 있는 주위를 둘러보자 나도 모르게 헛웃음이 새어 나왔다.

“미친 새끼. 아무리 생각해 봐도 넌 다시 인간 되긴 글렀다.”

“설령 인간이 아니라 한들, 뭐가 문제란 말인가?”

“뭐?”

“이미 오늘과 같은 불균형은 과거에도 몇 번이나 겪었다. 마력 수치가 강해지면 강해질수록 마나와의 균형이 어긋났고, 마정석에서 흡수한 마력을 통제하지 못한 적도 있었어. 하지만 그럴 때마다 내가 어떤 생각을 떠올렸는지 알고 있나?”

미카엘 실베르트는 내 대답을 기다리지 않았다.

한 공간에서 수백 명의 헌터들이 처참한 내전을 벌이고 있음에도, 그 광경을 바라보는 놈의 표정은 한없이 편안했다.

“마왕(魔王).”

“……!”

“누군가가 끝끝내 나를 방해한다면. 그로 인해 인간으로서 정점에 설 수 없다면…… 아스모데우스의 뒤를 이은 새로운 마왕이 되는 것도 나쁘지는 않겠구나. 그리 생각했지.”

할 말을 잊은 채 미카엘 실베르트를 바라보던 나는, 문득 앞서 했던 말을 정정해야 할 필요성을 느꼈다.

“……이거 다시 보니 그냥 미친 새끼가 아니라, 아주 제대로 미친 새끼였네.”

“지금 당장은 뭐라 부르든 상관없다. 어차피 해가 저물 때쯤이면 모든 것이 결정 날 테니까. 자네와 저 친구들의 생사도, 세상에 알려질 내 진정한 이름도.”

미카엘 실베르트라는 이름은 이미 온 세상이 다 안다.

하지만 지금 들은 ‘진정한 이름’의 의미는 그것이 아니다.

이 전투의 결과에 따라 놈은 세계 헌터 연맹의 맹주가 될 수도 있고, 새로운 마왕으로 거듭날 수도 있었다.

물론, 내게 있어 그것은 미카엘 실베르트 혼자만의 생각일 뿐이었다.

“병신. 너 같은 거머리 주제에 뭘 한다고.”

“거머리?”

“그래, 이 거머리 새끼야.”

서서히 굳어 가는 놈의 얼굴을 보자 실소가 터져 나왔다.

“맑은 연못에 살던 이무기가 승천하지, 시궁창에서 꿈틀거리던 굼벵이가 용 되는 거 봤냐? 너 같은 새끼가 아무리 강해져 봤자 어차피 본질은 그대로야. 기껏해야 모기 아니면 거머리지.”

“……!”

“그깟 힘에 취해서 마정석에 빨대까지 꽂은 모기. 놔둬 봤자 사람 피만 빨아먹는 백해무익한 거머리. 그게 바로 너라고. 이 한심한 새끼야.”

한심한 새끼.

그 말은 나 자신에게 하는 말이기도 했다.

한때는 정말 모든 걸 포기하고 물러나는 생각도 했었으니까.

저 같잖은 야망의 종점이 단지 세계 헌터 연맹을 손에 넣는 것뿐이라면, 단지 정점에 서는 것만이 유일한 목표라면…… 더 이상 아무런 재앙도 일어나지 않을 거라는 생각을 했으니까.

나는 고통스러웠다.

모두가 바라마지 않는 힘과 능력이 있음에도 처참히 무너지는 도시를, 그 안에서 죽어 가는 무수한 사람들을 구하지 못해서.

마치 지금 벌어지는 이 끔찍한 재앙들이 내가 미카엘 실베르트와 맞섰기 때문인 것 같아서.

그렇기에 잠시나마 고민할 수밖에 없었다.

‘아니, 두려웠던 거지.’

그래. 인정하자.

나는 무수한 죽음이 내리깔린 이 길을 계속 달리는 것이 두려웠다.

미카엘 실베르트의 뒤를 쫓으면 쫓을수록, 더욱 많은 피와 시체가 발에 밟힐 것 같아 무서웠다.

차라리 놈의 손아귀에 세상을 쥐여 준다면, 이제 제 것이 되어버린 세상을 지키기 위해서라도 선지자를 비롯한 모든 재앙을 멈출 거라 생각했다.

하지만…… 이제는 알겠다.

그리고 아무도 모르게 마음속으로 홀로 걸었던 그 어둡고 길었던 터널을 빠져나오자, 그토록 바라던 빛이 있었다.

아니, 답이 있었다.

그 모든 것은 내 나약함으로부터 비롯된 헛된 바람이었고, 미카엘 실베르트는 결승선을 통과해도 뛰는 것을 멈추지 않을 괴물이라는 것을.

바로 그런 이유로, 나는 인간으로서 놈을 죽여야 한다는 것을.

“아무리 생각해 봐도, 너 같은 거머리 새끼들은 역시 밟아서 터트리는 게 답이야. 안 그래?”

“……!”

“지금부턴 아가리 닫아. 산소도 아깝다.”

나는 미카엘 실베르트를 향해 창날을 겨누었다.

더는 본래의 색을 찾아볼 수 없을 만큼 까맣게 물들어 버린 눈동자, 동시에 끝도 없는 거대한 기운이 놈의 전신을 휘감으며 회오리쳤다.

콰아아아.

올올히 피어오르는 기운에 닿은 모든 것들이 부서지고 갈라진다.

부드럽고 여유가 넘치던 놈의 목소리가 이 세상 것이 아닌 것처럼 울려 퍼졌다.

- 네 시체는 오늘 이 자리에 묻힌다. 세상에 알려지지 않을 모든 진실과 함께.

그 말에, 나는 문득 고개를 들어 곳곳에 설치된 카메라들을 바라보았다.

절반은 파괴되었지만, 절반은 여전히 제 역할을 수행 중이었다.

진실이라.

대충 짐작은 했다. 그토록 주목받기 좋아하는 미카엘 실베르트가 어째서 인생에서 가장 빛나는 순간을 전 세계에 생중계하지 않는지.

그리고 언제나 그림자처럼 곁을 따라다니던 그 빌어먹을 애완 까마귀는 지금 어디에 있으며, 이런 소란 속에서도 왜 바깥은 여전히 잠잠한지.

하지만 지금 이 순간, 내가 놈에게 해 줄 수 있는 대답은 한마디뿐이다.

“아가리 닫으랬지. 이 씨벌 놈아.”

- 놈……!

콰드드드득!

마치 망망대해 속 파도처럼 휘몰아치는 놈의 기파(氣波)를 향해 달려나가며, 나는 문득 생각했다.

내가 지닌 삼 갑자의 공력마저 턱없이 부족하게 느껴질 만큼 거대한 저 기운이, 왜 두렵게 느껴지지 않는지.

마정석을 흡수하여 나와 비견될 만큼 강한 신체 능력과 마르지 않는 마력을 갖게 된 미카엘 실베르트가 어째서 작게만 느껴지는지.

그리고 창날을 뻗으며, 답을 찾았다.

‘헌터(Hunter)니까.’

사냥꾼은, 사냥감을 두려워하지 않는다.

쉬이이잉!
```

## Final English reading copy

```markdown
# Chapter 782

*Kwaaaang!*

My ears went numb beneath the deafening crash.

But before the ringing came, an enormous shock wave traveled through our hands, which had touched for only an instant.

*Boom!*

It felt as if a giant’s palm had smacked my entire body.

The irresistible force sent me flying backward. I twisted in midair, and a blade of gray energy came rushing toward my face.

*Shhk!*

A hair’s breadth. That was all.

I snapped my head aside, and the gray energy skimmed past the tip of my nose, cleaving the ground like soft tofu. I landed lightly on the spot it had cut through.

Then I watched one man walk toward me, his entire body wrapped in gray energy.

No—something that had crossed beyond the bounds of humanity.

“Michael Silbert.”

He smiled at the sound of my voice. The shadow in his deep-set dimples seemed especially dark. That wasn’t just my imagination.

*Crack. Crack.*

The ground crumbled beneath each step he took.

The energy pouring from Michael Silbert was so overwhelming that even those fighting nearby choked on their breath and retreated as far as they could.

But not me.

I couldn’t back down. And I had no intention of doing so.

Just as I’d decided before coming here, all I could do was fight back.

To stop that leisurely approaching monster. To keep him from hurling billions of people into the flames all over again.

I stepped forward, putting my weight into it.

*Whoosh.*

One step.

The wind brushed past my body, and space folded. At the same time, two keywords completed themselves in my mind and became commands.

*Inventory open. Summon.*

A spear I’d hidden where no one could see it wrapped itself in my hand.

The world had slowed. Blue-white flames surged up along the spearhead, painting the gray eyes where darkness rippled as I brought it down.

Michael Silbert.

Straight for the crown of that monster’s head.

*Fwoosh!*

Every trace of moisture within several meters evaporated beneath the concentrated heat.

Through air hot enough to catch fire at a touch, I saw his eyes fly wide.

And the corners of his mouth were still turned up, even in the face of an attack no one here could have expected.

Then—

A sword shot upward like a streak of light and smashed into the White Flame spearhead falling toward his crown.

*Kwaang!*

A deafening crash rang out, as if the sky itself had split open.

*Grrrrk.*

The spearhead and sword blade locked together in midair, neither giving an inch. Beyond them came a low laugh.

“So that’s it. I wondered why I’d never seen that spear.”

“……!”

“So, are you done with the surprise magic trick you prepared?”

*Grit.*

The sword, wrapped in a murky aura, slowly pushed back the flame-wreathed spearhead.

A strength impossible to believe belonged to a human, and an unprecedented power that seemed to well up without end, burst forth all at once.

*Kwaaaah!*

The moment I faced that immense power head-on, I realized with absolute certainty:

Even the physical abilities I’d pushed far beyond their limits thanks to the System, even my three jiazi of internal energy—a level no one in Murim could afford to underestimate—weren’t enough to fully suppress him.

*If the fallout from this power reaches the people around us…*

I didn’t need to think hard about what would happen.

At least dozens would die. And half of them would be heroes who shouldn’t die here.

In the end, I had only one option left.

*Neutralize it.*

With that word flashing through my mind, I let go of the White Flame, which had been flung upward by the force of the clash, and threw out both hands without hesitation.

*Flicker. Boom!*

The Flame-Extinguishing Divine Fist with my right hand. The Flame Divine Palm with my left.

One fist and one palm.

Two branches from the same root—the Fire Gate Clan—sent two streams of flame surging into the murky aura.

*Grrrrk!*

The tremendous recoil sent throbbing pain through my body. The ground turned over beneath my sliding toes, revealing its ugly innards in long furrows.

But I focused only on the energy in front of me. I kept pouring the flames from both hands into the murky aura.

Not swallowing it—gnawing it away.

Not stopping it—throwing it out of balance.

At last, the mass of destructive energy had visibly shrunk. I twisted it with all my strength and hurled it behind me.

*Whoooosh—Kwaang!*

A tearing crash and tremor shook the National Assembly building.

The Skeleton King had just plunged his Bone Sword into the chest of one of the traitors, who’d staggered off balance. He shouted,

“Watch out!”

It was good advice, but half a beat too late.

Michael Silbert was already right in front of me.

*Shwack!*

An aura filled with murky light grazed the back of my neck.

I dodged his lightning-fast thrust and closed in, driving my fist at him without hesitation.

*Boom!*

Michael Silbert blocked my Flame-Extinguishing Divine Fist with a hand wrapped in layer upon layer of aura, then raised his knee.

No—he was about to raise it, but suddenly shoved me away and retreated.

*Whoosh! Thwack!*

A silver streak plunged viciously from the air, piercing exactly the spot where he’d stood a moment ago.

Watching me silently draw the White Flame, he smiled softly.

“Sure. If it were too easy, it wouldn’t be any fun.”

Fun. That was what he called it.

I looked around at the screams and blood splashing everywhere. A bitter laugh escaped me before I knew it.

“You crazy bastard. No matter how I look at it, you’re never going to be human again.”

“Even if I’m not human, what of it?”

“What?”

“I’ve experienced imbalances like this several times before. The stronger my magical power grew, the more it fell out of balance with my mana. There were even times I couldn’t control the magical power I absorbed from Magic Gems. But do you know what I thought of every time that happened?”

Michael Silbert didn’t wait for an answer.

Hundreds of Hunters were fighting a horrific civil war in the same room, but his expression was utterly at ease as he watched.

“Demon King.”

“……!”

“If someone kept getting in my way. If I couldn’t reach the pinnacle as a human because of them… I thought it wouldn’t be so bad to succeed Asmodeus as the new Demon King.”

I stared at Michael Silbert, at a loss for words. Then I realized I had to correct what I’d said earlier.

“……Now that I think about it, you’re not just crazy. You’re completely out of your fucking mind.”

“Call me whatever you like for now. By the time the sun sets, everything will be decided. Whether you and your friends live or die, and the name the world will know as my true one.”

The whole world already knew the name Michael Silbert.

But the “true name” he’d just mentioned meant something else.

Depending on how this fight turned out, he might become the Alliance Leader of the World Hunter Federation—or become a new Demon King.

Of course, to me, that was just something Michael Silbert had decided for himself.

“Idiot. What’s a leech like you going to do?”

“A leech?”

“Yeah, you leeching bastard.”

His face slowly stiffened. I let out a scornful laugh.

“An imugi that lives in a clear pond ascends to heaven. Ever seen a grub wriggling in a sewer turn into a dragon? No matter how strong you get, your nature stays the same. At best, you’re a mosquito or a leech.”

“……!”

“A mosquito drunk on power, with its straw stuck in a Magic Gem. A useless leech that does nothing but suck people’s blood. That’s what you are, you pathetic bastard.”

*Pathetic bastard.*

Those words were for me, too.

There’d been a time when I’d seriously considered giving up on everything and backing away.

If the end of that laughable ambition of his was just taking control of the World Hunter Federation, if his only goal was to stand at the top… then maybe no more disasters would happen.

I was in pain.

I had power and abilities that everyone wanted, yet I couldn’t save the cities crumbling into ruins or the countless people dying inside them.

It felt as if I were the one causing this terrible disaster by standing against Michael Silbert.

That was why, for a little while, I couldn’t help but wonder.

*No. I was afraid.*

Fine. I’d admit it.

I was afraid to keep running along this path, paved with countless deaths.

The closer I chased Michael Silbert, the more blood and bodies I feared I’d trample underfoot.

I thought that if I simply handed him the world, he’d stop The Prophet and every other disaster, if only to protect what had become his.

But… now I understood.

When I finally came out of the dark, endless tunnel I’d walked alone inside my heart, where no one else could see, there was the light I’d wanted so badly.

No. There was an answer.

All of it had come from my own weakness. My foolish hope was wrong, and Michael Silbert was a monster who wouldn’t stop running even after he crossed the finish line.

That was why I had to kill him as a human being.

“No matter how I look at it, the answer is still to stomp on leeches like you until they burst. Don’t you think?”

“……!”

“From now on, shut your mouth. You’re wasting oxygen.”

I leveled my spear at Michael Silbert.

His eyes had turned so black there was no trace of their original color. At the same time, an immense, seemingly endless power wrapped around his entire body and began to whirl.

*Kwaaaah.*

Everything the strands of power touched broke and split apart.

His voice, once gentle and unhurried, rang out as if it belonged to something from another world.

“Your corpse will be buried here today, along with every truth that will never come to light.”

At his words, I looked up at the cameras installed all around us.

Half had been destroyed, but the rest were still doing their job.

The truth, huh?

I could more or less guess. Why wasn’t Michael Silbert, who loved attention so much, broadcasting the brightest moment of his life to the whole world?

And where was that damned pet crow that always followed him like a shadow? Why was everything outside still so quiet despite all this chaos?

But at this moment, there was only one thing I could say to him.

“I said shut your mouth, you fucking bastard.”

“You…!”

*Grrrrrrk!*

As I charged toward his energy, surging like waves across a boundless sea, I suddenly wondered why that immense power—enough to make even my three jiazi of internal energy feel hopelessly inadequate—didn’t frighten me.

Why Michael Silbert, who’d absorbed a Magic Gem and gained physical abilities comparable to mine and a seemingly inexhaustible supply of magical power, seemed so small.

And as I thrust out the spearhead, I found the answer.

*Because I’m a Hunter.*

Hunters aren’t afraid of their prey.

*Whoooosh!*
```
