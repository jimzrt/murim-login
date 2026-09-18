<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0396.txt",
      "sha256": "fd8143f43d1b43f7594e173e12bcbe623b1a889cc38bf368443e15e6a3582cf7",
      "bytes": 14012
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c6c83341a5508f5e1b167701f6146c7659a2c1a740475a03e0d0227737595a46",
      "bytes": 2947
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e0bafef3495a98388b0f1c94b13c9f6bdb6ffb80e4cff9c31e840f7fa0e37511",
      "bytes": 134883
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "90537352c7a8021e514a015db871cbfe0f70ed84c36a2d1098d7ea46dfc38cce",
      "bytes": 533
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "df12091e19f3000cca155fda03264fc66d7ca800e4dffceca85941a0b48f4c16",
      "bytes": 631
    },
    {
      "path": "characters/Wei Fenghu.md",
      "sha256": "0a4e557f7c354dd4d957288cbd16e29ab2cd68d9037a5733e759dc023d55db08",
      "bytes": 555
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4c188737fdd677970672bba1c872a310d751e102789240cc4ddb36e9e62cad46",
      "bytes": 115630
    }
  ],
  "estimated_tokens": 9452
}
-->

# Durable State Update — Chapter 396

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 396. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 396. Profile updates may replace only one
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
  "chapter": 396,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 396,
    "continuity_sources": [396],
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
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "Jin has crossed the wall into true mastery and can use overwhelming physical force without internal energy when he restrains himself.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "The Arch Lich's power and magical interference have weakened substantially since the previous night, though communications remain unreliable.",
    "The Arch Lich can teleport missiles with extraordinary speed and precision, making aerial fire support unsafe and forcing the armies toward a ground battle.",
    "Monster armies have resumed their advance, with fighting reported on every front.",
    "Death Knights have appeared on the northern and western fronts, and Jin suspects the western-front black knight may also have appeared in the north.",
    "Lee Jungryong claims Ares Guild has a record of nine victories and one defeat, while Jin suspects the northern defeat was intentional because Ares withdrew intact despite heavy casualties.",
    "Sichuan Province remains under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, and a large undead army.",
    "Lei Fei remains missing with his unit, and Wei Fenghu has asked Jin to bring him back if he is found.",
    "Wu Heixing remains hostile toward Jin and Faye Chen and is planning action against Jin after recalling his conversation with Lee Jungryong.",
    "Magic Johnson commands the southern front, has a strongly flirtatious interest in Team Leader Choi, and can now use teleportation despite the Arch Lich's interference."
  ],
  "continuity_sources": [
    395,
    394
  ],
  "open_questions": [
    "Who is the Arch Lich's true king, who is the black knight, and why did the undead armies withdraw before resuming their advance?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is Wu Heixing planning after recalling his conversation with Lee Jungryong?",
    "Did the black knight appear among the Death Knights on the northern front, and what is its objective?"
  ],
  "safe_through": 395,
  "temporary_decisions": [
    "Render 파이 첸 as Faye Chen and 매직 존슨 as Magic Johnson.",
    "Render 전하 as His Highness for Prince Felix, including Jin's sarcastic use of the title.",
    "Preserve Magic Johnson's casual, flirtatious banter and Jin's dry, blunt resistance.",
    "Preserve Jin's profane and irreverent humor when he challenges authority figures.",
    "Render Death Knight as the capitalized Monster type and black knight as its lower-case leader title."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 최민우    | **Choi Minwoo**   |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 탱커      | **tank**              |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 웨이펑후 | **Wei Fenghu** | Minister of National Defense under China's Central Military Commission. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 오크 | **Orc** | Monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 골렘 | **Golem** | Magical rock-based monster classification. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 가고일 | **Gargoyle** | Flying monster species accompanying the Wyverns. |
| 듀라한 | **Dullahan** | Headless undead monster form taken by Yao Wei. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 395
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 392
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader in the Public Security Armed Forces Department who mediates between Jin and Shao Shen's enraged subordinates.
- **Personality:** Practical, emotionally aware, and attentive to the political consequences of violent decisions.
- **Voice:** Low, calm, and pragmatic, framing emotional choices through their consequences.
- **Relationships:** He supports Jin's intervention and works with Shao Shen's regiment during the aftermath of the massacre.

### Wei Fenghu.md

# Wei Fenghu (웨이펑후)

- **Safe through:** Chapter 395
- **Aliases:** None
- **Role:** Wei Fenghu is the Minister of National Defense under China's Central Military Commission and a four-star general.
- **Personality:** Courteous, reserved, and authoritative.
- **Voice:** Formal and measured, addressing Jin as Mr. Jin.
- **Relationships:** Wei Fenghu is Lei Fei’s maternal uncle who raised him as his own son, and he has asked Jin Taekyung to bring Lei Fei back if he is found.

## Korean source

```text
＃396화



검은 기사는 고개를 들어 하늘을 올려다보았다.

구름 한 점 없이 푸르른 창공. 그러나 이미 빛을 잃은 검은 기사의 눈에는 어둡고 탁한 잿빛으로 보일 뿐이었다.

‘어둡구나.’

문득 떠오른 생각에 검은 기사는 기분이 이상해졌다. 어둡다니. 도대체 어둠이 무엇을 뜻한단 말인가.

처음부터 그는 검은 기사였다. 어둠에서 태어난 존재는 어둠이라는 의미를 모른다.

‘하지만 이건. 뭐지?’

빛과 햇살. 맑게 웃는 아이. 자신의 머리를 쓰다듬는 누군가의 손길…….

연달아 뇌리를 스치는 여러 단어와 알 수 없는 장면들이 그를 혼란스럽게 만들었다.

다음 순간 들려온 수하의 부름이 아니었다면, 검은 기사는 한참을 그렇게 서 있었을 것이다.

- 로드.

- 부디.

전신을 감싼 칠흑 같은 갑주. 머리 전체를 덮은 투구 사이로 녹색 안광이 일렁인다.

해골마에서 내려 한쪽 무릎을 꿇은 두 기의 데스나이트가 고저 없는 목소리로 말을 이었다.

- 명령을.

- 내려 주십시오.

아.

검은 기사는 잠시 잊고 있던 사실을 떠올렸다. 그것은 그가 모시는 군주가 내린 명령이었다.

- 가라. 사방으로 진격하여 모든 것을 짓밟고 죽여라. 시체의 산과 피의 바다를 내게 바쳐라.

군주의 명령은 절대적이다. 그에게 영혼까지 종속된 검은 기사는 충실히 명령을 따랐다.

휘하에 놓인 열 기의 데스나이트를 다섯 군단의 사령관으로 삼고, 스스로 한 군단의 선봉장이 되어 이곳에 왔다.

‘그런데 왜 하필 이곳일까.’

검은 기사는 저 멀리 보이는 작은 도시를 바라보았다.

기억에 있는 장소다. ‘아이’라는 낯선 단어를 불현듯 떠올린 곳이었고, 정체 모를 거대한 힘을 느낀 곳이기도 했다.

하지만 도대체 어떤 이유로 자신이 이곳으로 향했는지, 검은 기사는 알지 못했다.

- 로드?

- 로드?

수하들을 가만히 내려다보던 검은 기사는 마침내 명했다.

- 진격하라.

- 명을.

- 받듭니다.

기다리던 대답을 들은 데스나이트가 해골마에 올라 거대한 창을 번쩍 치켜들었다.

창날에서 솟구친 칠흑색의 마기(魔氣)에 너른 평야를 빽빽하게 메운 몬스터들이 괴성을 내질렀다.

- 끽. 끼기기긱.

- 그어어어어!

죽은 지 얼마 되지 않아 아직 살점이 붙어 있는 스켈레톤부터 소형 몬스터인 고블린, 오크. 트롤과 오우거 등의 대형 몬스터까지.

그 숫자가 어림잡아 수만을 헤아렸고 상공에는 가고일과 와이번 무리가 거대한 그림자를 드리웠다.

- 집결.

- 하라.

이어지는 지시에 이백여 기의 듀라한(Dullahan)이 정렬했다. 한 손에는 자신의 잘려 나간 머리를, 다른 한 손에는 무기를 든 그들은 백골로 이루어진 짐승 위에 올라 흉광을 번뜩였다.

- 돌격.

- 준비.

두 기의 데스나이트가 군단의 꼭짓점이 되었다. 하늘을 찌를 듯이 높이 솟구친 창날이 천천히 내려가 도시를 겨누었다.

인간들의 도시. 그러나 이제 곧 언데드의 도시이자 죽음의 땅이 될 곳이다.

「공안무력부는 집결하라!」

「씨, 씨발! 몬스터들이다! 놈들이 나타났다!」

「당장 경보를 울리고 사령부에 보고해!」

위이이이잉!

불어오는 바람을 타고 인간들의 외침과 비상을 알리는 소리가 울려 퍼졌다.

그러나 이미 명령은 떨어졌다. 진격을 시작한 언데드 군단을 멈출 수 있는 건 아무것도 없었다.

쿵, 쿵, 쿵.

칼같이 짜인 오와 열.

데스나이트와 듀라한을 필두로 빠른 기동력을 갖춘 라이칸스로프 등이 최전방에 섰고 오우거와 트롤, 골렘과 같은 대형 몬스터가 거대한 벽이 되어 이동했다.

활과 마법을 다루는 몬스터는 최후방으로 이동한 지 오래.

일반 몬스터들에게는 없는 규율과 대형을 생각해 낸 것 역시 검은 기사였다.

‘나는 도대체 어디서 이런 것을 배웠던가.’

다시금 떠오른 의문을 뒤로하고 검은 기사는 입을 열었다.

- 따르라.

주인의 뜻에 따라, 그가 탄 해골마가 걸음을 옮기기 시작한다.

다그닥, 다그닥.

백골로 이루어진 말발굽이 새싹을 짓밟았다. 드넓은 곡창(穀倉)을 뒤덮은 언데드 군단이 자신들의 사령관을 따라 천천히 진격한다.

거대한 진동이 지축을 울리고, 느린 물결처럼 나아가던 군단은 이내 백골의 파도가 되어 평야를 휩쓸었다.

두두두두두두!

- 그아아아아아!

수만의 몬스터가 토해 내는 거대한 함성.

도시를 향해 밀려드는 몬스터들의 선두에, 한 줄기 빛이 되어 쏘아지는 검은 기사가 있었다.

「저놈이 우두머리다!」

「원거리 부대! 준비!」

「탱커들은 동요하지 마라! 전차 부대는 헌터들과 함께 놈을 요격해라!」

탱커, 전차, 헌터.

검은 기사는 인간들의 외침을 들을 수 있었고, 놀랍게도 정확히 이해했다.

심지어는 그 뒤에 나올 명령까지도.

「집중 사격 개시!」

타다다다당!

퍼버버버벙!

쉬쉬쉬쉬쉭!

화려하다. 불꽃이, 얼음이, 섬광이 도시 곳곳에서 솟구친다.

더러는 곡선을 그리며 내리꽂혔고, 더러는 일직선에 가까운 궤적으로 검은 기사와 그의 뒤를 따르는 언데드 기사단을 노렸다.

- 아아.

잿빛으로 물든 세상에서도 그것들이 뿜어내는 빛은 매혹적이었고 친숙했다. 검은 기사는 왠지 모를 울렁임을 느끼며 손을 뻗었다.

스르릉.

등에 매여 있던 대검이 뽑혀 나온다.

발사된 포탄과 마법, 화살이 그에게 닿기도 전, 칠흑빛을 띤 검신이 허공을 종횡(縱橫)으로 긋고 베었다.

콰아아아아!

마력의 바람이 휘몰아친다. 공간이 갈라진다. 휘황찬란한 마나를 머금은 마법이 촛불처럼 꺼지고 화살은 산산이 부서졌다.

빛이 어둠에 잡아먹히는 광경을, 도시에 있던 모두는 똑똑히 지켜보았다.

최민우와 샤오 쉔의 뇌리에 한 가지 생각이 스쳐 지나갔다.

‘이건…….’

‘막을 수 없다.’

확신에 가까운 깨달음. 그리고 다음 순간 공간을 뛰어넘어 헌터들을 향해 들이닥친 칠흑빛 섬광.

콰아아아앙!

하늘이 쪼개지는 듯한 굉음이 울려 퍼졌다.

수십 개의 타워 실드가 박살 나고 피 보라가 터져 나온다. 일검(一劍)을 휘둘러 세 명의 A급 헌터와 스무 명의 B급 헌터를 베어 버린 검은 기사는 붉은 안광으로 얼어붙은 인간들을 바라보았다.

깊숙이 눌러쓴 투구 아래로, 스산한 망자의 목소리가 흘러나왔다.

- 악사르. 가로쉬.

모두 죽여라.

전날 이곳에서 죽어 갔던 이들이 마지막으로 들었던 마계의 언어.

그리고…… 검은 기사가 자신의 뒤를 따른 군단을 향해 내린 명령.

- 명을.

- 받듭니다.

검은 기사의 좌우로 모습을 드러낸 두 기의 데스나이트, 이어 들이닥친 일백의 듀라한이 예리한 송곳이 되어 인(人)의 장벽을 꿰뚫었다.

콰드드드득!



* * *



‘기습이라고?’

각 전선에서 올라온 긴급 보고. 웨이펑후가 어떻게 된 일이냐며 호통을 쳤지만, 돌아온 건 각 전선과 통신이 완전히 두절되었다는 소식이었다.

「완전 두절이라니! 어젯밤부터는 불안정하긴 해도 연결은 되지 않았나!」

통신 장교가 식은땀을 흘리며 대답했다.

「그, 그게…… 어떤 이유에서인지 통신 방해가 더욱 강해졌습니다. 막 도착한 긴급 보고도 약 30분 전의 것으로 확인되었습니다.」

“……!”

뭐? 삼십 분?

저 말이 사실이라면 회의 진행 도중 습격이 이루어졌다는 뜻이다.

그마저도 통신 방해에 헤매다가 겨우 도착한 소식이니, 30분이 아니라 한 시간일 수도 있다.

매직 존슨의 얼굴이 딱딱하게 굳은 얼굴로 중얼거렸다.

「그럴 리가. 분명 내가 가기 전만 해도 그 정도는…….」

문득 도시를 떠나기 전, 매직 존슨이 했던 말이 뇌리를 스쳤다.



‘아크 리치. 놈의 힘이 아주 조금씩 줄어들고 있어. 특히 어젯밤을 기점으로 방해 요소가 상당 부분 사라지게 되었지.’



틀렸다.

인근에 미치는 아크 리치의 힘이 약화 된 것이 아니라, 놈이 그렇게 보이게끔 만든 것이다.

티 내지 않고 조금씩. 그러다가 군단을 물림으로써 마치 자신의 힘이 미치는 범위가 대폭 줄어든 것처럼. 우리가 조금이라도 더 안심할 수 있게끔.

‘이건…….’

철저한 함정이다.

아크 리치가 S급 헌터들의 부재를 어떻게 알아차렸는지는 모른다. 중요한 것은 놈이 그 짧은 틈을 포착하여 몬스터 군단을 진격시켰다는 것이다.

전날에 목격했던 참혹한 도륙이 전선 곳곳에서 벌어진다고 생각하니, 처음 텔레포트를 겪었을 때보다 더한 울렁거림이 찾아왔다.

하지만 이번에는 구역질 대신 매직 존슨을 붙잡고 말했다.

“텔레포트.”

「뭐?」

“텔레포트요. 어서!”

나는 매직 존슨이 당장이라도 마법을 써 줄 줄 알았다. 그러나 다음 순간 들려온 그의 대답은 내가 생각했던 것이 아니었다.

「진. 제트기를 타고 가.」

“네? 제트기라니 갑자기 그게 무슨……. 그럼 너무 늦어요.”

「지금은 곤란해.」

“어째서입니까? 아까 우리가 있던 병원 옥상 좌표, 알고 있잖아요.”

매직 존슨이 고개를 저었다.

「좌표가 문제가 아니야. 이대로 텔레포트를 시도한다면…… 우리 둘 다 죽을 수도 있어.」

“……!”

다급함에 잠시 잊고 있었다. 아크 리치의 마법 방해에 대해서. 이런 함정을 판 놈이 친절하게 텔레포트를 시도하게 둘 리 없다.

매직 존슨이 가라앉은 목소리로 말을 이었다.

「십 분. 길어야 이십 분이야. 제트기를 타, 진.」

“……그사이에 많은 사람이 죽을 겁니다.”

「그래. 하지만 텔레포트를 하는 과정에서 네가 개죽음을 당한다면, 더 많은 사상자가 나오겠지.」

S급 헌터는 전세를 뒤엎을 수 있는 전략 병기다.

늦더라도 도착만 한다면 일부를 살릴 수 있겠지만, 텔레포트 과정에서 사고라도 난다면 나와 지원군을 잃은 수많은 사람은 함께 돌아올 수 없는 강을 건너게 될 것이다.

지금 매직 존슨은 나를 걱정하는 동시에 그 점을 지적하고 있었다.

「용감하지만, 어리석은 짓이야.」

“…….”

「곧 제트기가 이륙 준비를 끝마칠 거야. 이럴 시간 없어.」

대회의실의 한 면을 차지한 방탄 유리창 밖으로 이륙장을 가로질러 기체에 탑승하는 파일럿들이 보인다.

어느새 대회의실을 빠져나간 다른 S급 헌터들의 뒷모습도.

말없이 그 광경을 바라보던 내가 불쑥 입을 열었다.

“가능하다고 하셨죠?”

「뭐?」

“아까 봤던 홀로그램 영상에서처럼, 미사일을 텔레포트 시키는 거요.”

매직 존슨이 눈을 커다랗게 떴다.

「진, 너 설마?」

“존슨까지 위험을 감수하러 갈 필요는 없잖아요. 저 혼자면 충분해요.”

「맙소사. 너 미쳤어? 그렇게 말했는데도 못 알아듣다니!」

“충분히 알아들었어요. 그만한 각오도 되어 있고.”

「너…….」

뭐라 말할 것처럼 입술을 달싹이던 그가 돌연 탁자를 내리쳤다. 쾅! 힘이 실린 주먹에 고급 원목이 박살 난다.

「제기랄! 이런 개 같은 일이!」

쉴 새 없이 욕설을 중얼거리는 매직 존슨을 보며 나는 피식 웃었다.

그의 반응이 무엇을 뜻하는지, 이미 알고 있기 때문이었다.

“승낙한다는 의미로 받아들여도 되죠?”

「그래. 이 건방진 꼬마 녀석아.」

그가 충혈된 눈으로 나를 바라본다.

욕이라도 퍼부을 것 같은 분위기.

매직 존슨은 지금 진심으로 분노하고, 한편으로는 슬퍼하는 중이었다.

「이봐, 진. 나는…….」

“압니다. 당신에게도 지켜야 할 사람들이 있다는 거. 이런 부탁을 해서 미안해요.”

「……빌어먹을. 병원 옥상으로 보내주면 되냐?」

“네. 충분해요.”

스아아아.

이를 악문 매직 존슨이 두툼한 손바닥으로 내 가슴을 짚었다.

신중에 신중을 기하는 듯, 처음의 텔레포트와는 달리 그의 마나는 천천히 내 몸을 감싸기 시작했다.

「10%. 그게 네 생존 확률이야. 90%의 확률로 죽을 수도 있어.」

10%라…….

나는 고개를 들어 창밖의 하늘을 올려다보았다.

구름 한 점 없이 푸르른 창공. 저 하늘 위, 아득한 우주 어딘가에 무림이 있을까. 그들이 날 기다리고 있을까.

그 순간, 문득 떠오른 생각에 입꼬리가 올라간다.

“괜찮네요. 10% 정도면.”

「뭐?」

휘황찬란한 빛무리가 뿜어져 나왔다. 나는 전신을 감싸는 온기를 느끼며 말을 이었다.

“아마도, 차원을 넘을 확률보다는 천 배 정도 높을 테니까.”

「……!」

지금쯤 매직 존슨은 어떤 표정을 짓고 있을까.

궁금했지만, 안타깝게도 그의 얼굴은 이제 보이지 않았다. 시야를 가리는 눈부신 섬광과 함께, 나를 일그러지는 공간 너머로 빨아들이는 거칠고 강한 힘이 있었다.

쏴아아악!
```

## Final English reading copy

```markdown
# Chapter 396

The black knight raised his head and looked up at the sky.

A clear blue expanse without a single cloud. But to the black knight’s eyes, which had already lost their light, it appeared only as a dark, murky gray.

*How dark.*

The thought that suddenly occurred to him left the black knight feeling strange. Dark? What did darkness even mean?

He had been a black knight from the beginning. A being born from darkness does not know what darkness means.

*But this… What is it?*

Light and sunlight. A child laughing brightly. Someone’s hand stroking his head…

Several words and inexplicable scenes flashed through his mind in succession, leaving him confused.

If not for the call from one of his subordinates a moment later, the black knight would have stood there for a long time.

—Lord.

—Please.

Black armor as dark as night covered his entire body. Green lights flickered between the slits of the helmet covering his head.

Two Death Knights dismounted from their skeletal warhorses and knelt on one knee. Their voices were flat as they continued.

—Give us—

—your orders.

Ah.

The black knight recalled something he had briefly forgotten. It was the command given by the lord he served.

—Go. Advance in all directions, trample everything, and kill them all. Offer me mountains of corpses and seas of blood.

His lord’s commands were absolute. With even his soul bound to that lord, the black knight faithfully obeyed.

He had appointed the ten Death Knights under his command to lead five legions, then personally taken command of one legion’s vanguard and come here.

*But why this place, of all places?*

The black knight gazed at the small city in the distance.

It was a place he remembered. A place where the unfamiliar word *child* had suddenly come to mind, and where he had sensed an enormous power whose nature he could not identify.

But the black knight did not know why he had come here.

—Lord?

—Lord?

After silently looking down at his subordinates, the black knight finally gave his command.

—Advance.

—Your command.

—We obey.

Hearing the answer they had been waiting for, the Death Knights mounted their skeletal warhorses and raised their enormous spears high.

Demonic qi surged from the spearheads, and the monsters packed across the broad plain let out shrill howls.

—Kik. Kikikikik.

—Graaaargh!

From Skeletons that had died only recently and still had flesh clinging to their bones, to small monsters like goblins and Orcs, and large monsters such as Trolls and ogres…

Their numbers reached tens of thousands by a rough estimate. In the sky, groups of Gargoyles and Wyverns cast enormous shadows over the land.

—Rally.

—Do it.

At the next command, roughly two hundred Dullahans formed ranks. Holding their severed heads in one hand and weapons in the other, they rode atop beasts made of white bones, their eyes gleaming with ferocity.

—Prepare.

—for the charge.

The two Death Knights formed the tip of the legion. Their spearheads rose high enough to pierce the sky, then slowly descended until they pointed toward the city.

A city of humans. But soon, it would become a city of the undead—a land of death.

—Public Security Armed Forces Department, assemble!

—F-fuck! Monsters! They’ve appeared!

—Sound the alarm immediately and report to command!

Wheeeeeeng!

The cries of the humans and the sound announcing the emergency carried on the wind.

But the order had already been given. Nothing could stop the undead legion now that it had begun its advance.

Boom. Boom. Boom.

Ranks and files arranged with military precision.

Death Knights and Dullahans led the way, with fast-moving Lycanthropes and other monsters at the very front. Large monsters such as ogres, Trolls, and Golems advanced like a gigantic wall.

Monsters capable of using bows and magic had long since moved to the rear.

The black knight was also the one who had conceived of the discipline and formations that ordinary monsters lacked.

*Where did I learn something like this?*

Setting the question aside once more, the black knight opened his mouth.

—Follow.

In accordance with their master’s will, the skeletal warhorse he rode began to move.

Clip-clop. Clip-clop.

Hooves made of white bone trampled the new shoots beneath them. The undead legion blanketing the vast breadbasket advanced slowly behind its commander.

The earth shook beneath the enormous vibration. The legion, moving forward like a slow wave, soon became a wave of bones that swept across the plain.

Thudthudthudthudthud!

—Graaaargh!

The enormous roar of tens of thousands of monsters.

At the head of the monsters surging toward the city, the black knight shot forward like a streak of light.

—That one’s the leader!

—Ranged units! Prepare!

—Tanks, stay calm! The armored units will intercept him alongside the Hunters!

Tanks, armored units, Hunters.

The black knight could hear the humans shouting, and astonishingly, he understood them perfectly.

He even understood the command that would come next.

—Begin concentrated fire!

Rat-a-tat-tat-tat!

Boom-boom-boom!

Whoosh-whoosh-whoosh!

It was dazzling. Flames, ice, and flashes of light erupted throughout the city.

Some attacks came crashing down in graceful arcs. Others followed trajectories close to straight lines as they targeted the black knight and the undead knights behind him.

—Ah.

Even in a world dyed gray, the light those attacks emitted was enchanting and familiar. The black knight felt an inexplicable upheaval in his chest as he reached out a hand.

Shrring.

The greatsword strapped to his back slid free.

Before the fired shells, magic, and arrows could even reach him, the pitch-black blade slashed through the air in every direction.

Kraaaash!

A magical wind stormed through the battlefield. Space split apart. The magic containing dazzling mana went out like candle flames, and the arrows shattered into pieces.

Everyone in the city watched clearly as the light was devoured by darkness.

A single thought passed through Choi Minwoo’s and Shao Shen’s minds.

*This is…*

*Impossible to stop.*

An insight approaching certainty.

Then, in the next moment, a pitch-black flash leaped across space and struck the Hunters.

KABOOM!

A thunderous roar rang out, as if the sky itself had been split apart.

Dozens of tower shields shattered, and sprays of blood burst into the air. The black knight, who had cut down three A-rank Hunters and twenty B-rank Hunters with a single sword stroke, stared at the frozen humans through red glowing eyes.

Beneath his deeply lowered helmet, the cold voice of the dead drifted out.

—Aksar. Garosh.

Kill them all.

They were the words of the Demon Realm—the final words heard by those who had died here the previous day.

And…

They were also the order the black knight gave to the legion following behind him.

—Your command.

—We obey.

Two Death Knights appeared to the black knight’s left and right. Then one hundred Dullahans charged in behind them, becoming sharp awls that pierced the human wall.

Kra-d-d-d-d-d!

* * *

*An ambush?*

Emergency reports poured in from every front. Wei Fenghu shouted, demanding to know what had happened, but the answer he received was that communications with every front had been completely severed.

—Completely severed? Even if communications were unstable, weren’t we still connected since last night?

The communications officer answered while sweating coldly.

—W-we don’t know why, but the communications interference has grown even stronger. The emergency report that just arrived was confirmed to be from approximately thirty minutes ago.

“……!”

What? Thirty minutes?

If that was true, it meant the attacks had begun while the meeting was in progress.

And since the report had only barely arrived after struggling through the communications interference, it might not have been thirty minutes. It could have been an hour.

Magic Johnson muttered with his face gone rigid.

—That can’t be. It wasn’t that bad before I left…

Suddenly, the words Magic Johnson had spoken before leaving the city flashed through my mind.

*“Arch Lich. Its power is gradually weakening. In particular, a considerable portion of the interference disappeared after last night.”*

Wrong.

The Arch Lich’s power affecting the surrounding area hadn’t weakened. It had merely made it look that way.

Little by little, without giving anything away. Then, by withdrawing the legion, it had made it seem as if the range of its influence had shrunk dramatically—so that we could let our guard down even a little more.

*This is…*

A thoroughly prepared trap.

I didn’t know how the Arch Lich had realized that the S-rank Hunters were absent. What mattered was that it had seized that brief opening and sent the monster legions forward.

The thought of the horrific slaughter we had witnessed the day before happening across every front made my stomach churn even more violently than it had during my first teleportation.

But this time, instead of throwing up, I grabbed Magic Johnson and said,

“Teleport.”

—What?

“Teleport. Hurry!”

I expected Magic Johnson to use magic immediately. But the answer I heard next was not what I had expected.

—Jin. Take a jet.

“What? A jet? Why are you suddenly talking about that…? We’ll be too late.”

—It’d be too risky right now.

“Why not? You know the coordinates of the hospital rooftop where we were earlier.”

Magic Johnson shook his head.

—The coordinates aren’t the problem. If we try to teleport like this…we could both die.

“……!”

I had momentarily forgotten about the Arch Lich’s magical interference in my desperation. There was no way the one who had laid such a trap would kindly allow us to attempt teleportation.

Magic Johnson continued in a subdued voice.

—Ten minutes. Twenty at most. Take the jet, Jin.

“……A lot of people will die in that time.”

—Yes. But if you get yourself killed for nothing during the teleportation, there’ll be even more casualties.

An S-rank Hunter was a strategic weapon capable of turning the tide of a war.

Even if I arrived late, I might still be able to save some people. But if an accident occurred during teleportation, the countless people who lost me and the reinforcements would cross a river from which there was no return.

Magic Johnson was worried about me, but he was also pointing that out.

—It’s brave, but it’s foolish.

“……”

—The jet will finish preparing for takeoff soon. We don’t have time for this.

Through the bulletproof glass occupying one side of the conference room, I could see the pilots crossing the runway and boarding the aircraft.

I could also see the backs of the other S-rank Hunters, who had already left the conference room.

I watched the scene in silence, then suddenly spoke.

“You said it was possible, right?”

—What?

“Teleporting missiles, like in the hologram footage we saw earlier.”

Magic Johnson’s eyes widened.

—Jin, don’t tell me…

“There’s no need for you to risk yourself too, Johnson. I’m enough on my own.”

—Good God. Are you crazy? I explained it to you, and you still don’t understand!

“I understand perfectly. And I’m prepared to go that far.”

—You…

His lips moved as if he were about to say something, but then he suddenly slammed his fist down on the table.

Bang!

The expensive hardwood shattered beneath the force of his blow.

—Damn it! What the fuck is this!

I let out a quiet laugh as I watched Magic Johnson mutter one curse after another.

I already knew what his reaction meant.

“I can take that as your permission, right?”

—Yes, you insolent little brat.

His bloodshot eyes fixed on me.

He looked as if he might start hurling abuse at me.

Magic Johnson was genuinely furious—and at the same time, he was grieving.

—Listen, Jin. I…

“I know. You have people you need to protect, too. I’m sorry to ask you this.”

—……Damn it. Is sending you to the hospital rooftop enough?

“Yes. That’s enough.”

Swoosh.

Magic Johnson clenched his teeth and placed his thick palm against my chest.

As though taking every possible precaution, his mana began to slowly wrap around my body, unlike the first time he had teleported me.

—Ten percent. That’s your chance of survival. There’s a ninety percent chance you could die.

Ten percent…

I raised my head and looked up at the sky beyond the window.

A clear blue expanse without a single cloud. Was Murim somewhere in the distant universe above that sky? Were they waiting for me?

At that moment, a thought suddenly occurred to me, and the corners of my mouth lifted.

“That’s not bad. Ten percent is enough.”

—What?

A dazzling mass of light burst forth. Feeling warmth envelop my entire body, I continued,

“It’s probably a thousand times higher than the odds of crossing dimensions.”

—……!

I wondered what expression Magic Johnson was wearing by then.

I wanted to know, but unfortunately, I could no longer see his face. Along with the blinding flash blocking my vision came a rough, powerful force that sucked me beyond the distorting space.

Whoooosh!
```
