<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0391.txt",
      "sha256": "d9215c15667272c87d83f4f48f8e8481e65698634dac0073a4d39c57aa28c9ce",
      "bytes": 14274
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c94db364da1e0f957cd6568abec646565f2b7670ba848a5bcc4906b7ab226b2c",
      "bytes": 3733
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b73b7b9e1f62601118b882675d9e4873d65d0bafe2241e087638751eb0bca406",
      "bytes": 134498
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cc8e64956464f0c4386d23b684a19aedb71102aedc2e7e13eb030b9c3e11eb07",
      "bytes": 533
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ab3ece5ecc5c7cae886c3f82e2a67c2a677cdb7b5e24e8816f861b7b97ccb716",
      "bytes": 111746
    }
  ],
  "estimated_tokens": 9351
}
-->

# Durable State Update — Chapter 391

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 391. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 391. Profile updates may replace only one
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
  "chapter": 391,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 391,
    "continuity_sources": [391],
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
    "Jin Taekyung has crossed the wall into true mastery, while Choi Minwoo has become substantially stronger and more refined.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "The Skeleton Warlord cannot raise undead deeper inside the current battlefield because the Arch Lich's control grows stronger there.",
    "Jin's western-front force annihilated more than a thousand monsters in about two hours without a fatality; allied losses were twenty-three severely wounded and thirty lightly wounded.",
    "Public Security Armed Forces Hunters spearhead the western-front advance, while the following military destroys and transports corpses to prevent undead resurrection and rescues civilians.",
    "General Liao commands the 13th Group Army of the Chengdu Military Region, knew that some officers resented cleanup duty, and deployed reserve Hunters into a nearby city while implicated in a military procurement corruption scandal.",
    "Sichuan Province remains under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, magical communications interference, and a large undead army controlled by the Arch Lich.",
    "Wei Fenghu remains China's Minister of National Defense and the Chairman's right-hand man; Lei Fei remains unconfirmed dead or alive after disappearing with his department's Hunters.",
    "United Nations peacekeeping forces and international S-rank Hunters remain engaged on the Sichuan front, with Faye Chen having prevented an east-west breach from spreading.",
    "Wu Heixing remains hostile toward Jin, while Lee Jungryong is seeking an undisclosed discussion with him.",
    "A massive explosion in a nearby city triggered a new Sudden Quest, while Jin remains under the nonrefusable Sudden Quest The Desperate War Situation."
  ],
  "continuity_sources": [
    390,
    389
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen as its influence continues to expand?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What important discussion does Lee Jungryong intend to have with Wu Heixing?"
  ],
  "safe_through": 390,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, 아크 리치 as Arch Lich, 최상급 포션 as Top-Grade Potion, and 상급 포션 as high-grade potion.",
    "Render 짱깨 as chink, 주석 동지 as Chairman Comrade, 전하 as His Highness, 돌발 퀘스트 as Sudden Quest, and 다급해진 전황 as The Desperate War Situation; preserve Jin's vulgar historical and cultural jokes."
  ],
  "version": 1
}
```

## Exact glossary matches

| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 오크 | **Orc** | Monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 389
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

## Korean source

```text
＃391화



후위에 남아 있던 쓰촨성 공안 무력부 2중대장, 장 웨이는 처음부터 이 작전이 꺼림칙했다.

‘군대와 함께 먼저 가서 도시를 점령하라니? 샤오 연대장이 내린 명령과는 다른데.’

장 웨이가 품고 있던 한 줄기 의문이 더욱 커진 것은, 굳이 앞에서 교전 중인 아군을 우회하여 진격했을 때부터였다.

「왕 상교(上校)님. 이 작전, 저희 연대장님께서 동의하신 게 확실합니까?」

장 웨이의 물음에 중년의 고위 장교가 눈살을 찌푸리며 대답했다.

「왜 그런 게 궁금하지?」

「아무리 생각해도 이상해서 말입니다. 분명히 저희 연대장님께서는 후위에서 체력을 비축하며 본부를 호위하라고 하셨는데…….」

「아, 그 꼬마 연대장 말이지.」

샤오 쉔을 향한 고위 장교의 비웃음에 장 웨이가 얼굴을 굳혔다.

「샤오 쉔 연대장은 왕 상교님과 같은 계급입니다. 그것도 곧 소장 진급을 앞두고 계신.」

「세상 물정 모르는 어린 애가 운이 좋았던 게지. A급 헌터로 각성한 것으로도 모자라, 한국 놈이 활약해 준 덕분에 덩달아 이번 진급 명단에도 올랐으니. 이렇게 초고속 승진을 하는 걸 보니까 정계에 괜찮은 꽌시(关系)라도 있는 건가?」

「……나이는 어리지만 그만큼 뛰어난 분입니다. 저희와도 형제처럼 지내실 만큼 신망도 두텁고요.」

고위 장교가 손에 든 지휘봉을 쓸어내렸다.

「헌터들 위아래 없는 거야 본관도 잘 알고 있네. 하지만 지금은 전시 상황이야. 이 명령은 사령관이신 랴오 상장께서 내리신 거고.」

「사령관님께서 직접…… 말씀이십니까?」

「그래. 그러니 명령에 따르기 싫다면 지금이라도 돌아가게. 단, 지금 자네의 행동이 명령 불복종이라는 사실을 알고 있기를 바라지.」

「……!」

「진격 속도를 좀 더 단축하고자 할 뿐이야. 정황상 그럴 리는 없겠지만 몬스터 잔당이 남아 있다면 쓸어 버리고, 위험에 빠진 민간인들을 구출하는 게 전부라고. 알아들었나?」

한참이나 말이 없던 장 웨이는 고개를 끄덕이고 물러났다.

일반적으로 공안 무력부는 군부에 속하지 않은 별개의 단체로 취급받지만, 현재는 전시 상황이었다. 서부 전선 사령관인 랴오 상장의 명령을 거스르는 건 결코 좋은 선택이 아니었다.

「뭐랍니까?」

한껏 목소리를 낮춘 부하의 물음에 장 웨이가 대답했다.

「쉬운 작전이니 닥치고 따라오라는군. 거절하면 명령 불복종이고.」

「그 말을 믿으십니까?」

「전자를 묻는 거라면 당연히 아니지. 하지만 후자는 사실일 거야. 자네는 어떻게 생각하나?」

「당연히 못 믿죠. 왕 상교 저놈, 능력도 없는 주제에 태자당 쪽 꽌시 하나로 여기까지 올라온 놈입니다. 랴오 상장이 기르는 충견이라고 소문이 자자해요.」

「바로 그 랴오 상장의 명령이야. 당장은 구린내가 나더라도 참을 수밖에.」

「……빌어먹을.」

「하지만 왕 상교의 말이 사실일지도 몰라. 인근에 존재하는 대부분의 몬스터는 전부 아군과 교전 중일 테니까. 현재 우리 전력이라면 몬스터 잔당 정도는 충분해.」

장 웨이는 주위를 둘러보았다. 그를 포함한 백 명의 헌터 외에도 이십여 대의 전차와 오백의 보병. 상공에는 전투 헬기 세 대가 시야를 확보하며 나아가는 중이었다.

‘부디 별다른 피해가 없기를.’

장 웨이의 바램이 하늘에 닿았는지, 그가 우려하던 일은 발생하지 않았다.

촉각을 곤두세우며 진입한 쑤이닝시 인근의 작은 소도시는 몬스터에 의해 초토화된 상태였을 뿐, 폐허가 된 도심은 적막하기 그지없었다.

고블린, 오크 따위의 몬스터가 간간이 튀어 나왔지만, 그들에게는 아무런 위협도 되지 못했다.

- 키이이익!

서걱!

가장 선두에서 십여 마리의 몬스터들을 처치한 장 웨이는 약간 이나마 마음이 풀어졌다.

「종도 다른 몬스터가 따로따로 나타나는 걸 보니 무리에서 이탈한 놈들 같군요.」

「예상대로군. 그러게 내가 뭐라고 했나?」

거만하게 대답하는 꼴이 썩 마음에 들지 않았지만, 차라리 이게 낫다.

그렇게 생각하고 잠자코 고개를 끄덕이던 장 웨이는 이어지는 고위 장교의 말에 멈칫하고 말았다.

「병력을 나누라고 하셨습니까?」

「그래. 이런 상황이라면 최대한 빨리 생존자부터 찾아야지.」

「하지만 왕 상교님. 진입한 지 아직 한 시간도 채 되지 않았습니다. 조금 더 중심부로 나아간 후에…….」

「건방진 소리.」

「예?」

「전투 실력은 헌터인 자네들이 나을지 몰라도, 전술은 내가 몇 수 위야. 현재 지휘권은 내게 있으니 그만 입 다물고 명령을 따르라고.」

「……!」

「못 들었나? 그럼 본관이 직접 자네 수하들에게 명령을 내릴까?」

「……제가 하지요.」

「세부 지도는 갖고 있겠지. 그럼 두 시간 후에 중앙 광장에서 보도록 하지.」

장 웨이를 향해 밉살맞게 웃어 보인 장교가 장갑차에 몸을 실으려던 그 순간이었다.

쐐애애액, 펑!

장 웨이는 멍하니 눈을 깜빡였다. 손바닥으로 얼굴을 쓸어내리자 끈적한 핏물이 한가득 묻어 나왔다.

한없이 붉은색을 띤 그것은 분명 인간의 것이었고, 이미 상반신이 흔적도 없이 사라진 장교의 몸뚱어리는 장갑차에서 굴러떨어지고 있었다.

쿵.

숨 막히는 정적. 가장 먼저 정신을 차린 장 웨이가 외쳤다.

「전원 전투 준비-!」

「몬스터! 몬스터가 나타났다!」

「탱커!」

「여, 연대장님께서 전사하셨다!」

그 외침에 가장 먼저 반응한 것은 공안 무력부의 헌터들이었고, 군인들은 한차례 늦게 상황을 파악했다.

그리고 갑작스러운 지휘관의 사망으로 극심에 혼란에 빠진 그들을 기다리고 있던 것은 더욱 처절한 죽음이었다.

쐐애애액!

단 한 번의 파공성.

보이지도 않는 속도로 쏘아진 빛줄기가 오와 열을 맞춘 채 진군 중이던 군인들을 휩쓸었다.

퍼버버벙!

수십의 사람들을 풍선처럼 터트리며 나아간 빛줄기가 마지막으로 꿰뚫은 것은 보병들의 호위를 받으며 이동하던 장갑차였다.

단단한 외피를 뚫고 내부 깊숙이 파고든 빛줄기. 그 광경을 목격한 장 웨이가 벼락처럼 외쳤다.

「모두 피해!」

그러나 그의 외침이 닿기도 전에, 다음 순간 터져 나온 굉음이 모든 것을 집어삼켰다.

꽈아앙!

붉은 섬광, 검은 연기와 함께 터져 나간 장갑차의 파편이 수백, 수천 개의 칼날이 되어 사방을 난자한다.

군인은 물론이고 미처 반응하지 못한 하급 헌터까지. 셀 수도 없는 이들이 짚단처럼 쓰러졌다.

이미 숨이 끊긴 그들의 몸뚱어리는 미동조차 하지 않았다.

「……!」

「이, 이게 도대체…….」

석상처럼 굳어 버린 사람들을 향해 장 웨이가 고함을 내질렀다.

「산개! 모두 산개해라! 전차와 장갑차에서 최대한 멀리 떨어져!」

하지만 난생처음으로 실전을 겪는 병사들의 몸은 굳어 있었고, 아직 모습을 드러내지 않은 상대는 적들의 혼란을 결코 놓치는 법이 없었다.

쐐애애애액!

다시 한번 들려오는 죽음의 소리. 그러나 지금까지와는 달리 쏘아진 빛줄기는 하나가 아니었다.

콰앙! 퍼버버벙!

「크아아아악!」

불꽃이 솟구치고 비명이 넘쳐흐른다.

이십여 대의 장갑차와 전차가 무력화되기까지 걸린 시간은 그야말로 찰나.

상공을 배회하던 세 대의 전투 헬기 역시 수많은 파편으로 화해 지상으로 추락했다.

콰앙! 투두두둑.

시산혈해라고 부를 만한 참혹한 현장에, 장 웨이는 등골을 타고 흐르는 오싹한 기운을 느꼈다.

‘최소 A급 몬스터. 그것도 한둘이 아니다.’

아이러니하게도, 그것이 오늘 장 웨이가 내린 판단 중 가장 정확한 것이었다.

스아아아아.

어두컴컴한 골목과 무너진 건물 사이. 아직도 타오르는 빌딩의 옥상.

검은 안개처럼 나타난 열 개의 형체들은 타오르는 보랏빛 안광으로 살아남은 수백의 인간들을 응시했다.

뼈밖에 남지 않은 전마(戰馬)에 올라탄 형체들을 발견한 장 웨이의 입술 사이로 신음 같은 한 마디가 새어 나왔다.

「……데스나이트(Death Knight).」

한때는 고결했으나 흑마법에 의해 타락한 죽음의 기사들.

리치와 함께 대격변 이후 모습을 감춘 바로 그 데스나이트가 나타났다. 그것도 자그마치 열 기나 되는 숫자.

순간 장 웨이의 머릿속에 가장 먼저 떠오른 단어는 죽음이었다.

‘여기까지인가.’

데스나이트는 A급 몬스터를 벗어난 존재들이다.

아직 백 명의 헌터와 군병력이 남았지만, 장 웨이는 이미 알고 있었다.

놈들이 펼쳐 놓은 그물을 피할 수 없다는 사실을.

하지만…….

「곱게 죽어 줄 생각 따위는 없다.」

그것은 비단 장 웨이만의 생각이 아니었다.

두려움으로 총기조차 제대로 잡지 못하는 군인들과 달리, 공안 무력부의 헌터들은 결의에 찬 눈빛으로 각자의 병장기를 치켜세웠다.

「너희까지 이럴 필요는 없어.」

장 웨이의 나지막한 한마디에, 소대장 중 하나가 퉁명스럽게 대답했다.

「중대장님은 이래도 되고요?」

「미안하다. 너희를 데려오는 게 아니었는데.」

「누가 데려온 게 아니라, 저희가 따라온 겁니다. 중대장님 덕분에 열 번도 넘게 살아남았으니 한 번쯤 이럴 때도 됐죠.」

아무렇지 않게 말하지만, 목소리에 묻어 나오는 떨림마저 감출 수는 없었다.

미동도 하지 않는 열 기의 데스나이트를 바라보며, 장 웨이는 바짝 마른 입술을 핥았다.

「최선을 다해 싸우고, 한 사람이라도 살아남아라. 너희에게 해 줄 말은 그게 전부다.」

대답 대신 우렁찬 함성이 터져 나왔다. 두려움을 몰아낸 헌터들의 눈동자가 샛별처럼 빛났다.

안전하고 풍요로운 삶을 원했다면 다른 길도 있었다.

그러나 그들이 부유한 기업가의 경호원이나, 용병 대신 공안 무력부를 택한 것은 헌터로서의 명예와 책임감 때문이었다.

이건 결코 물러설 수 없는 싸움이다.

「가자! 인민의 아들딸, 중화의 후예들이여!」

온 힘을 다해 부르짖은 장 웨이가 가장 가까운 데스나이트를 향해 쇄도하려던 바로 그 순간.

구구구구궁!

그건 본능에 가까웠다.

거센 진동과 함께 느껴지는 거대한 기운. 살아남은 인간들은 전신의 털이 쭈뼛 곤두서는 공포와 함께 고개를 돌렸다.

여러 눈동자가 향하는 곳에, 폐허가 된 도심지를 천천히 가로지르는 검은 기사가 있었다.

깊게 눌러쓴 투구 아래, 붉은 안광이 번쩍인다. 핏기없는 입술 사이로 죽음의 숨결이 뿜어져 나왔다.

- 사르, 가로쉬.

누구도 알아들을 수 없는 마계의 언어.

그러나 다음 순간, 장 웨이는 곧 그 말이 무엇을 뜻하는지 깨달을 수 있었다.

‘모두 죽여라.’

부릅떠진 장 웨이의 눈동자에, 사방에서 쇄도해 오는 열 기의 데스나이트가 비쳤다.

서걱!

도륙의 시작이었다.



* * *



철벅.

뼈밖에 남지 않은 말발굽이 피 웅덩이를 밟았다.

마지막까지 저항하던 중년의 헌터, 장 웨이의 시신을 물끄러미 내려다보는 검은 기사를 향해 다가온 데스나이트들이 한쪽 무릎을 꿇었다.

- 로드. 다음 명령을.

다음 명령이라.

잠시 말이 없던 검은 기사가 문득 손을 뻗었다.

쉬익, 서걱!

채찍처럼 휘둘러진 흑색 빛줄기가 콘크리트와 철근을 갈랐다.

비스듬히 허물어지는 건물. 드러난 내부 공간에는 한껏 입을 막은 채 웅크려 있는 인간들이 있었다.

「진진. 여보. 괜찮아, 괜찮아…….」

「흑, 흐흐흑!」

「압빠빠?」

인간 수컷과 암컷. 그리고…… 아직 암수 구분이 되지 않을 만큼 한없이 작고 가벼워 보이는 존재.

아마 저걸 아이라고 하던가.

‘아이, 아이?’

이 단어를 어디서 들어 봤던가.

검은 기사는 문득 드는 의문을 뒤로하고 손을 뻗었다. 눈에 보이는 인간은 말살시켜야 한다. 그것이 그가 받은 명령이었다.

하지만.

- ……?

어째서인지 손이 나아가지 않았다.

손가락만 튕겨도 한 줌 핏물로 화해 사라질 나약한 존재들이 분명한데, 마치 보이지 않는 방어막이 인간들을 감싸고 있는 듯했다.

- 너희는. 뭐지?

검은 기사의 음산한 목소리에 부모의 품 안에서 꼬물거리던 아이가 으앙, 하고 소리 내어 울음을 터트린 그때였다.

- 이건.

문득 고개를 들어 저 너머를 바라보던 검은 기사가 말머리를 돌렸다.

갑작스러운 우두머리의 행동에 데스나이트들이 의문을 표했다.

- 로드?

- 돌아간다. 지금. 당장.

- 그럼 인간들은 저희가.

- 돌아간다. 지금. 당장.

그것이 전부였다. 무릎을 꿇어 예를 표한 열 기의 데스나이트는 우두머리의 뒤를 따라 말을 달렸다.

그들의 모습이 안개처럼 사라지기 직전, 검은 기사의 붉은 안광이 기적처럼 살아남은 세 인간에 닿았다가 떨어졌다.

휘이이이잉.

피비린내를 머금은 바람이 시체로 가득한 폐허를 휩쓸었다.
```

## Final English reading copy

```markdown
# Chapter 391

Zhang Wei, commander of the Sichuan Province Public Security Armed Forces Department's 2nd Company, had remained in the rear, and he had felt uneasy about this operation from the very beginning.

*Go ahead with the army and occupy the city? That's different from the orders Colonel Xiao gave me.*

The doubt in Zhang Wei's mind had only grown when they deliberately bypassed their allies engaged in combat up ahead and advanced farther in.

“Colonel Wang, are you certain our regimental commander agreed to this operation?”

A high-ranking, middle-aged officer frowned at Zhang Wei's question.

“Why are you curious about that?”

“No matter how I think about it, something feels wrong. Our regimental commander clearly told us to conserve our strength in the rear and guard headquarters…”

“Ah, you mean that little regimental commander.”

Zhang Wei's expression hardened at the senior officer's mocking tone toward Xiao Shen.

“Regimental Commander Xiao Shen holds the same rank as you, Colonel Wang. And he's about to be promoted to major general.”

“That child knows nothing about the world. He was lucky, that's all. As if awakening as an A-rank Hunter wasn't enough, he even made the promotion list this time thanks to that Korean bastard's exploits. Looking at how quickly he's risen through the ranks, I wonder if he has some decent guanxi[^1] in political circles.”

“He may be young, but he's exceptionally capable. He's highly respected, and he's close enough to us to treat us like brothers.”

The senior officer ran his hand along the command baton he was holding.

“I know perfectly well that Hunters don't recognize ranks. But this is wartime. This order came from General Liao, the commander.”

“From the commander himself…?”

“That's right. So if you don't want to follow the order, go back now. But I hope you understand that what you're doing right now constitutes disobedience.”

“……!”

“We're only trying to shorten our advance time. Given the circumstances, it's unlikely, but if there are any monster stragglers left, we'll wipe them out and rescue any civilians in danger. That's all. Do you understand?”

Zhang Wei remained silent for a long while before nodding and stepping away.

The Public Security Armed Forces Department was generally treated as a separate organization that did not belong to the military. But this was wartime. Defying General Liao, the commander of the western front, was by no means a wise choice.

“What did he say?”

Zhang Wei answered the subordinate who asked in a lowered voice.

“He said to shut up and follow because it's an easy operation. Refusing would be disobedience.”

“Do you believe him?”

“If you're asking whether I believe the first part, of course not. But the second part is probably true. What do you think?”

“Of course I don't believe him. That bastard Colonel Wang has made it this far on nothing but his guanxi with the Crown Prince Party, despite having no ability of his own. Everyone says he's General Liao's obedient dog.”

“It is an order from that very General Liao. Even if it smells rotten, we have no choice but to endure it for now.”

“……Damn it.”

“But Colonel Wang might be telling the truth. Most of the monsters in the surrounding area are probably engaged in combat with our allies. With our current strength, we should be more than capable of handling a few monster stragglers.”

Zhang Wei looked around.

In addition to the hundred Hunters, including himself, there were more than twenty tanks and five hundred infantrymen. Three attack helicopters were advancing overhead, keeping watch on the surroundings.

*Please, let there be no serious casualties.*

Perhaps Zhang Wei's wish had reached the heavens, because what he feared did not happen.

The small city near Suining that they entered with every sense alert had been utterly devastated by monsters, but the ruined downtown was completely silent.

Monsters such as goblins and Orcs occasionally sprang out, but they posed no threat whatsoever.

“Kieeeek!”

Slash!

After killing a dozen or so monsters at the very front, Zhang Wei felt a little less tense.

“The monsters are appearing separately, even by species. They must have broken away from their groups.”

“Just as I expected. What did I tell you?”

The officer's arrogant tone was unpleasant, but this was still preferable.

Thinking that, Zhang Wei silently nodded. Then he stopped short at the senior officer's next words.

“You want us to split up?”

“That's right. In a situation like this, we need to find the survivors as quickly as possible.”

“But, Colonel Wang. We haven't even been inside for an hour yet. We should advance a little farther toward the center first…”

“Don't get insolent.”

“Excuse me?”

“You Hunters may be better at fighting, but I'm several steps ahead of you when it comes to tactics. I have command authority right now, so shut your mouth and follow orders.”

“……!”

“Didn't you hear me? Should I give the order to your men myself?”

“……I'll do it.”

“You have a detailed map, I assume. Then we'll meet at the central square in two hours.”

The officer gave Zhang Wei an unpleasant smile and was just about to climb into an armored vehicle when—

Whoooooosh! Boom!

Zhang Wei blinked blankly.

When he wiped his face with his palm, a large amount of sticky blood came away on it.

It was unmistakably human blood, an endless shade of red, and the body of the officer—whose upper torso had already vanished without a trace—was rolling out of the armored vehicle.

Thud.

A suffocating silence fell.

Zhang Wei was the first to recover.

“Everyone, prepare for battle—!”

“Monster! Monsters have appeared!”

“Tank!”

“The regimental commander has been killed!”

The Hunters of the Public Security Armed Forces Department reacted first to the shouts. The soldiers understood what had happened a beat later.

And waiting for them, already thrown into utter chaos by the sudden death of their commander, was an even more horrific death.

Whoooooosh!

There was only a single sound of something piercing the air.

A beam of light shot forward at an invisible speed and swept through the soldiers advancing in orderly ranks and files.

Boom-boom-boom!

The beam burst dozens of people like balloons as it passed through them. Its final target was the armored vehicle moving under the protection of the infantry.

The beam pierced through the hard outer shell and bored deep into the vehicle's interior.

Zhang Wei witnessed the sight and shouted like a thunderclap.

“Everyone, get clear!”

But before his voice could reach them, the deafening roar that erupted in the next moment swallowed everything.

BOOM!

Along with a red flash and black smoke, fragments of the armored vehicle shot in every direction, becoming hundreds—thousands—of blades that ripped through everything around them.

Soldiers and lower-ranking Hunters who had been unable to react in time alike fell like bundles of straw.

The bodies of those who were already dead did not move at all.

“……!”

“W-what the hell is this…?”

Zhang Wei bellowed at the people frozen like statues.

“Spread out! Everyone, spread out! Get as far away from the tanks and armored vehicles as possible!”

But the bodies of soldiers experiencing actual combat for the first time had gone rigid, and the unseen enemy never failed to take advantage of the enemy's confusion.

Whooooooosh!

The sound of death came again.

But unlike before, there was more than one beam of light.

Boom! Boom-boom-boom!

“Aaaaaagh!”

Flames shot upward, and screams flooded the air.

The more than twenty armored vehicles and tanks were rendered useless in no more than an instant.

The three attack helicopters circling overhead were also reduced to countless fragments and came crashing down to the ground.

Boom! Rattle-rattle-rattle.

In the horrific scene that could only be called a sea of corpses and blood, Zhang Wei felt a chill run down his spine.

*At least A-rank monsters. And there isn't just one or two of them.*

Ironically, it was the most accurate judgment Zhang Wei made that day.

Sssssss.

Between dark alleys and collapsed buildings. On the rooftop of a building that was still burning.

Ten figures that had appeared like black mist stared down at the hundreds of surviving humans with burning violet eyes.

When Zhang Wei spotted the figures mounted on warhorses with nothing but bones left on them, a groan-like word escaped between his lips.

“……Death Knights.”

Knights of death who had once been noble, but had been corrupted by black magic.

The very Death Knights who had vanished along with the Lich after the Great Cataclysm had appeared. There were no fewer than ten of them.

The first word that came to Zhang Wei's mind was *death*.

*Is this where it ends?*

Death Knights were beings that had surpassed A-rank monsters.

A hundred Hunters and a military force still remained, but Zhang Wei already knew.

They could not escape the net the monsters had spread.

But…

“I have no intention of dying quietly.”

Zhang Wei was not the only one who felt that way.

Unlike the soldiers, who were too frightened to even hold their guns properly, the Hunters of the Public Security Armed Forces Department raised their weapons with determined eyes.

“You don't have to go this far.”

One of the platoon commanders answered Zhang Wei's low murmur bluntly.

“And you're allowed to?”

“I'm sorry. I shouldn't have brought you here.”

“No one brought us. We followed you. We've survived more than ten times thanks to you, so it was about time we did this at least once.”

He spoke casually, but he could not hide the trembling in his voice.

Zhang Wei licked his parched lips as he stared at the ten Death Knights standing completely motionless.

“Fight with everything you have, and make sure at least one of you survives. That's all I have to say.”

A booming cheer erupted instead of an answer.

The Hunters' eyes shone like morning stars, having driven away their fear.

If they had wanted a safe and prosperous life, they had other paths available to them.

But they had chosen the Public Security Armed Forces Department instead of becoming bodyguards for wealthy entrepreneurs or working as mercenaries because of their honor and sense of responsibility as Hunters.

This was a fight they could never retreat from.

“Go! Sons and daughters of the people, descendants of Zhonghua!”

Just as Zhang Wei finished shouting with all his strength and was about to charge toward the nearest Death Knight—

Rrrrrumble!

It was almost instinctive.

A massive energy could be felt alongside the violent tremors. The surviving humans turned their heads, terror making every hair on their bodies stand on end.

Where all those eyes turned, a black knight was slowly crossing the ruined downtown.

Red eyes flashed beneath the deeply lowered helmet. The breath of death poured through its bloodless lips.

“—Sar, Garrosh.”

It was a language from the demon realm that no one could understand.

Yet in the next instant, Zhang Wei realized what those words meant.

*Kill them all.*

Reflected in Zhang Wei's widened eyes were the ten Death Knights charging in from every direction.

Slash!

The slaughter had begun.

* * *

Splash.

A horse hoof made of nothing but bone stepped into a pool of blood.

The Death Knights who approached the black knight, who was staring down at the corpse of the middle-aged Hunter Zhang Wei—the last to resist—knelt on one knee.

“—Lord. Your next command.”

His next command.

The black knight was silent for a moment before suddenly extending a hand.

Whoosh! Slash!

A black beam lashed out like a whip and sliced through concrete and rebar.

A building collapsed at an angle. In the exposed space inside, several humans crouched together, desperately covering their mouths.

“Jinjin. Honey. It's okay, it's okay…”

“Sniff… sob…”

“Dadda?”

A human male and female. And…

A being so small and light that it was impossible to distinguish its sex.

*Was that what they called a child?*

*Child. Child?*

Where had he heard that word before?

The black knight pushed the question aside and extended his hand. Every human in sight had to be annihilated. That was the command he had received.

But—

“……?”

For some reason, his hand would not move.

They were undoubtedly weak beings who would turn into a handful of blood and vanish from a mere flick of his finger, yet it was as though an invisible barrier surrounded and protected them.

“What are you?”

At the black knight's eerie voice, the child squirming in its parents' arms suddenly began to wail.

“Waaaaah!”

“This is…”

The black knight abruptly raised his head and looked beyond the ruins, then turned his mount around.

The Death Knights expressed their confusion at their leader's sudden action.

“—Lord?”

“We're going back. Now. At once.”

“Then shall we deal with the humans—”

“We're going back. Now. At once.”

That was all.

The ten Death Knights bowed on one knee in deference before riding after their leader.

Just before their figures vanished like mist, the black knight's red gaze fell upon the three humans who had survived as if by a miracle, then moved away.

Whooooooosh.

Wind carrying the smell of blood swept through the ruin filled with corpses.

[^1]: *Guanxi* refers to influential personal connections and relationships, especially those used within social or political networks.
```
