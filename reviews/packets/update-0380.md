<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0380.txt",
      "sha256": "77da415e27450ded443c430202a192f958531844d76c60353282e71a7901a05a",
      "bytes": 14411
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b296738d3385de6acca8408c1e8970897af8c40aba39f9cac80cc384aad6172f",
      "bytes": 3025
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "90a9c5eb7e6e8c29c0114047d5de31b94c6f17a90ebc2ecd65178e94a0607956",
      "bytes": 132181
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9c2f7d5f711423b9569c86d2600137711533cdb792952f2a0b366e0a4dda687b",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "30e488ae346569c69cbe67f37a168984efa56156dc4d4fb2ed48edbc02631973",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a1c490fe043bc36b4dcbc168a96848b49835d4c89aafb9eb079ad619b835b499",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "931ac56f7d8341bcdc308d8fd1a1241ac96755772e85cdf2d6e6bdcd88a7e7f6",
      "bytes": 101645
    }
  ],
  "estimated_tokens": 10049
}
-->

# Durable State Update — Chapter 380

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 380. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 380. Profile updates may replace only one
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
  "chapter": 380,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 380,
    "continuity_sources": [380],
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
    "Chengdu International Airport is under attack by an unexpectedly large monster army that includes ground monsters and flying monsters.",
    "The Chinese People’s Liberation Army and Public Security Armed Forces Department Hunters are defending the airport, but the defenders have suffered losses approaching half their strength while the monster army continues to grow.",
    "Shao Shen is a young Hunter of the Public Security Armed Forces Department who rallied the defenders and fights with a spear imbued with aura.",
    "Black necromantic magic has raised the battlefield dead as chained undead, including the former A-rank Hunter Yao Wei as a Dullahan.",
    "A gigantic burning aircraft has entered the airport battlefield and swept across it; its identity and the consequences remain unresolved.",
    "Jin Taekyung is Level 120 at the Supreme Peak realm, has manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jin Taekyung remains aboard a private jet approaching Chengdu International Airport as the battle unfolds.",
    "The Myriad-Poison Ring is bound to Jin Taekyung alongside White Flame and the Fire Dragon Armor.",
    "Mungyeong is the Divine Physician and former Slaughter Saint, has sworn never to kill again, and intends to live as a physician; Dong Feng is his Disciple.",
    "Cheongpung remains a Supreme Peak master with Mimi and is Mimi’s temporary guardian.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord’s body and escaped after One Annihilation; their nature and ultimate fate remain unresolved.",
    "Aehyang is manipulating the Sichuan City Lord under the direction of an unidentified person."
  ],
  "continuity_sources": [
    379
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "Will Mungyeong remain outside the coming war, or will the crisis force him to intervene?"
  ],
  "safe_through": 379,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, and 화룡갑 as Fire Dragon Armor.",
    "Render 듀라한 as Dullahan, 공안 무력부 as Public Security Armed Forces Department, 중화 as Zhonghua, and 포이즌 브레스 as Poison Breath."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 살기     | **killing intent**                               |                                                       |
| 대주     | **Squad Leader** / **Commander**             |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 퀘스트              | **Quest**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 구울 | **Ghoul** | Undead monster species. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 배리어 | **Barrier** | Team Leader Choi's protective spell. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 듀라한 | **Dullahan** | Headless undead monster form taken by Yao Wei. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 379
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 378
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 378
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃380화



샤오 쉔은 처음으로 깨달았다.

콰아아아아!

두 날개가 불에 휩싸인 채 지상으로 돌진하는 비행기를 목격한다면, 종(種)을 넘어선 공포에 사로잡힌다는 것을.

- 으어어어어!

그토록 흉포하다는 오우거가, 트롤이 비명을 내질렀고.

- 구워어어어!

언데드 몬스터 중에서도 가장 느려터졌다는 구울(Ghoul)도 발바닥에 땀이 나도록 뛰었다.

- 취이이익!

「어, 어어, 어어어…….」

비명이라도 지를 수 있는 몬스터들은 양반이었다.

샤오 쉔을 비롯한 대부분은 석상처럼 굳은 채 지상을 향해 돌진하는 비행기를 바라볼 수밖에 없었다.

‘도망쳐야 하는데…….’

발이, 손이 움직이지 않는다.

무엇보다 전장의 한가운데에 포위되어 있던 샤오 쉔과 공안 무력부의 헌터들에게는 도망칠 기회조차 주어지지 않았다.

‘이대로 끝장인가?’

모두의 머릿속에 같은 생각이 떠오른 그 순간.

쿠구구구구궁!

귀가 먹먹해지는 굉음과 함께, 비행기의 거대한 동체가 전장을 휩쓸었다.

그리고 그 경천동지할 충돌은 개미 떼처럼 흩어지던 몬스터 군단의 최후방으로부터 시작되었다.

콰지지지직! 우두둑!

수십 톤의 무게를 지닌 거대한 강철의 덩어리는 앞을 막아서는 모든 것을 부수고 터트렸다.

몬스터들의 녹색 핏물이 분수처럼 뿜어졌고 크고 작은 사지가 사방으로 솟구친다.

‘이, 이게 도대체…….’

몬스터들의 물리 방어력이 아무리 뛰어나다지만, 그것도 정도가 있는 법. 몬스터 믹서기로 변모한 비행기를 멈출 수 있는 것은 아무것도 없었다.

- 구워……!

- 키이이익!

콰드드드득!

섬뜩한 파육음에 몬스터들의 비명이 파묻힌다. 지금껏 본 적도, 들은 적도 없는 아비규환(阿鼻叫喚).

상상치도 못한 광경을 넋 놓고 바라보던 샤오 쉔과 헌터들의 귓가에, 광기에 찬 누군가의 외침이 파고들었다.

“몬스터! 박는다! 죽인다!”

“……!”

이런 와중에도 똑똑히 들리는 모국의 언어에 공안 무력부의 헌터들은 지원군이라는 세 글자를 떠올렸고, 샤오 쉔은 경악했다.

‘엄청난 강자!’

목소리에 실린 강대한 마나(Mana). 필시 S급 헌터가 틀림없었다.

“가 버렷! 비행기이이잇!”

“…….”

그것도 살짝 미친 S급 헌터가 확실하다.

섬나라 놈들이 세계 2차 대전 때나 쓰던 방법을 가져오다니. 아군이 죽을 것까지는 생각 못 했단 말인가.

‘중앙 군사 위원회에서 파견된 것 같은데…… 우리나라에 저런 S급 헌터가 있었나?’

문득 든 의문. 그러나 이제 샤오 쉔과는 그다지 상관없는 일이 될 것이다.

몬스터들을 갈아 버리며 전장의 절반을 가로지른 거대한 강철 덩어리가 그와 헌터들을 향해 돌진하고 있었으니까.

- 취, 취익!

「도망쳐!」

살기 위한 몸부림에 적아(敵我)의 구분은 없었다.

샤오 쉔은 코앞에 인간이 있는 것도 잊은 채 몸을 부딪혀 오는 몬스터를 향해 단검을 내질렀다.

푸푹!

- 크르륵.

숨이 끊긴 몬스터의 육체가 샤오 쉔을 향해 허물어진다.

사방에서 밀려드는 몬스터들로 인해 한 걸음도 움직일 수 없는 상황. 샤오 쉔은 자신을 덮쳐 오는 육중한 무게를 느끼며 외쳤다.

「전투는 끝나지 않았다! 마지막까지 싸워라!」

맞다. 아직 전투는 끝나지 않았다. 헌터는 숨이 끊기는 마지막 순간까지 몬스터를 죽여야 하는 존재다.

샤오 쉔의 외침을 들은 헌터들이 이를 악물고 무기를 휘둘렀다.

‘이걸로 됐어.’

번개 같은 솜씨로 도망치는 오우거의 뒤통수에 단검을 박아 넣은 샤오 쉔은 크게 심호흡했다.

어느새 이십여 미터 앞까지 들이닥친 비행기의 거체가 보였다.

처음보다 속도가 훨씬 줄긴 했지만, 옴짝달싹하지 못하는 상황에서 저것을 피하기란 요원해 보였다.

‘미련은 없다.’

자랑스러운 중화의 헌터로 인민을 위해 싸우다가 죽는다면, 그것으로 족했다.

샤오 쉔이 사방에서 빗발치는 비명을 들으며 눈을 감은 그 순간이었다.

“읏차.”

콰드드드득! 촤아악!

핏물로 짐작되는 끈적한 액체를 뒤집어쓴 샤오 쉔은 생각했다.

‘……읏차?’

보통은 으악, 아닌가?

단말마치고는 기묘한 소리에 샤오 쉔은 슬그머니 눈꺼풀을 들어 올렸다.

그리고 마침내 볼 수 있었다. 몇 걸음 앞에서 우뚝 멈춘 비행기와 두런두런 이야기를 나누고 있는 두 사내를.

“자, 도착했습니다. 혹시 폭발할지도 모르니까 사람들 데리고 얼른 내리세요.”

“……진태경 씨. 전부 다 기절했습니다.”

“그래요? 나약하네.”

“……배리어 마법이 아니었으면 죽었을 겁니다.”

“그럼 최 팀장님이 옮겨 주세요. 아, 맞다. 아까 우리한테 빵즈라고 했던 그 새끼도 살았어요?”

“예. 그, 살아는 있긴 한데.”

“그럼 그 새끼 잘 지켜 주세요. 나중에 돌아갈 때 두고두고 갈굴 거니까.”

“……노력해 보죠.”

샤오 쉔은 도무지 이 상황을 이해할 수 없었다.

누가, 언제, 어디서, 무엇을, 어떻게. 왜. 이건 육하원칙으로도 정리할 수 없을 만큼 괴상한 광경이었다.

‘비행기는 갑자기 어떻게 멈춘 거고, 저 사람들은 뭐지? 중앙 군사 위원회에서 보낸 헌터가 아니었단 말인가?’

심지어 두 사람은 다른 언어로 이야기를 나누고 있었다.

둘 중 귀공자처럼 멀끔하게 생긴 사내의 말은 알아들을 수 없었지만, 어느 나라의 언어인지는 안다.

오랜 시간 동안 이웃한 옆 나라, 바로 한국이다.

‘잠깐. 한국인이라면……!’

샤오 쉔은 핏물로 끈적이는 눈가를 황급히 비볐다. 그제야 한 사람을 알아볼 수 있었다.

남들보다 머리 하나는 큰 근육질의 청년.

TV에서나 보던 그가, 자신의 우상이 눈앞에 있었다.

「호, 혹시 한국에서 오신 진 선생님 되십니까?」

“엥?”

청년, 진태경이 샤오 쉔을 보며 고개를 갸웃거렸다.

“저 선생님 아닌데요.”

「그럼 시벌좌…….」

“……시벌. 뭐여.”

맞구나!

샤오 쉔은 전신을 감싸는 안도감과 희망에 몸을 부르르 떨었다.



* * *



‘도대체 중국인이 시벌좌를 어떻게 아는 거지.’

나에 관한 기사가 잠깐 외신에서 떠들썩하긴 했는데, 시벌좌라는 별명까지 알려져 있을 줄은 몰랐다.

오대양 육대주를 떨어 울리는 시벌좌라니.

미국에 가게 되면 떡대 끝내주는 양키 형님들이 맥주병을 들고 다가와 알은척을 할지도 모르겠다.

‘헤이, 유. 씨뻘쫘?’

아임 파인 땡큐다. 시벌. 도대체 어느 정신 나간 놈들이 이따위 별명을 지은 거야.

그나저나…….

“개판이네.”

주위를 둘러본 내 짤막한 감상평이다.

기절한 승무원들을 굴비처럼 엮은 최 팀장과 인벤토리 안에 처박아 둔 스켈레톤 워로드가 대답했다.

“끔찍한 광경입니다.”

- 간악한 인간이여, 본 사령관은 이곳이 마음에 드는구나. 익숙하고도 정겨운 기분이다.

“…….”

죽음, 그 자체라고 할 수 있는 네임드 언데드 몬스터가 흡족해할 정도니 두말해 봐야 입 아픈 수준이다.

“오자마자 실전 투입이라니.”

내 푸념에 응답하는 것처럼, 시스템 알림이 울렸다.

띠링.



- 돌발 퀘스트, [예상치 못한 습격]이 생성되었습니다.



이래서 돈을 많이 준다고 했던 건가. 나는 내심 혀를 차며 입을 열었다.

“최 팀장님, 우선 민간인들부터 보호하고 그 후에는 알아서 싸우세요. 너무 무리하지는 마시고.”

“예. 안 그래도 그럴 생각입니다.”

최 팀장은 똑똑한 사람이다. 진가심법을 익히면서 예전과는 비교할 수 없을 만큼 강해졌지만, 결코 과시하려 하지 않을 것이다.

“그리고 거기 계신 젊은 분.”

「예, 옛. 진 선생님.」

선생님은 무슨. 나는 빠릿빠릿하게 대답하는 젊은 청년을 위아래로 훑었다.

얼굴은 어리지만 척 봐도 헌터다. 그것도 A급 정도로 보이는 강자. 마치 공장에서 찍어 낸 것처럼 똑같은 갑옷을 입은 주위의 헌터들과는 달리, 어깨에는 붉은 휘장도 달려 있었다.

“보니까 직급깨나 있어 보이시는데, 부하들 잘 간수해요. 한 사람이라도 더 살리자고.”

「예, 예?」

“이제부터 시작이니까.”

나는 대답과 동시에 주먹을 뻗었다.

콰아아앙!

줄기줄기 쏟아진 열양지기(熱陽之氣)가 멍하니 서 있던 몬스터들을 향해 쏘아진다.

후끈한 열기가 한바탕 휩쓴 곳에는 수십여 구의 몬스터 사체만이 남았다.

“뭘 그렇게 쳐다보고 있냐. 누가 정지 버튼이라도 눌렀어?”

“……!”

- ……!

내 한 마디를 신호로.

전장을 짓누르고 있던 침묵이 산산 조각나며 깨어졌다.

- 쿠워어어어!

「주, 죽여라! 몬스터 놈들을 막아!」

인간과 몬스터, 몬스터와 인간.

죽고 죽이는 전투가 시작된다. 나는 지면 깊숙이 박혀 있는 백염을 뽑아 휘둘렀다.

스걱!

물 반, 고기 반이 아니라 사방이 몬스터로 득실거리는 상황.

창날에서 뻗어 나간 반월의 강기가 한데 뭉친 몬스터 무리를 스쳤다.

띠링.



- [Lv.15 언데드 고블린]를 처치했습니다!

- [Lv.78 언데드 라이칸스로프]를 처치했습니다!

- [Lv.93 듀라한]을 처치했습니다!

- [Lv.30 스켈레톤]을 처치했습니다!

.

.

.

- 레벨의 격차가 큽니다. 미비한 경험치를 획득했습니다!



몬스터 처치와 경험치 획득을 알리는 시스템 알림이 끊임없이 울려 퍼진다.

평소였다면 한 귀로 흘려듣거나 무시했을 알림.

그러나 이번만큼은 중요한 힌트가 되어 주었다.

“이놈들 이거 설마…….”

- 아아, 맞다. 간악한 인간이여! 이토록 강한 언데드 군단이라니!

환희에 가득 찬 스켈레톤 워로드의 외침은 내 짐작을 확신으로 바꿔 주기에 충분했다.

‘어쩐지, 뭔가 이상하더라니.’

안 그래도 놈들에게서 생기(生氣)가 느껴지지 않아 의아하던 차였다.

아직 살아 있는 몬스터의 숫자도 상당했지만, 거의 절반 이상의 몬스터가 언데드 상태였다. 모두 합하면 이천 마리에 달하는 대군이다.

“그리고 언데드 몬스터는…….”

스켈레톤 워로드가 잔뜩 신이 나서 외쳤다.

- 아름답고! 멋있고! 용맹하다!

퍼걱!

다섯 마리의 몬스터를 베어 버린 내가 중얼거렸다.

“방금 저놈처럼 소멸하고 싶냐? 아름답고, 멋있고, 용맹하게?”

- ……실언을 했군. 사과한다. 간악한 인간이여.

잠시 자신의 처지를 망각했던 스켈레톤 워로드가 황급히 덧붙였다.

- 잠깐. 그렇다면 누군가의 조종을 받는 것이 틀림없다!

내 생각도 마찬가지다.

다만 한 가지 확신이 서지 않는 것은…….

“리치(Lich). 그놈이 직접 나선 걸까?”

- 으음. 지난번에 네가 보여 준 그 홀로그램 영상이라는 것에 나오는 그 리치를 말하는 것이라면, 아마 아닐 거다.

스켈레톤 워로드의 대답을 들으며 반걸음을 내디뎠다.

쾅!

거대한 쇠몽둥이가 어깨를 아슬아슬하게 지나쳐 지면을 부순다. 아직 생기가 느껴지는, 평범한 오우거다.

- 구워어어!

“어, 구워 줄게.”

퍼벙!

화염신장을 가슴에 얻어맞은 오우거의 칠공에서 검녹색의 핏물이 터져 나왔다.

허물어지는 거체를 지나치며 백염을 비스듬히 내리그었다.

쉬이이이익! 서걱!

공간이 잘려 나가고 그 사이에 있던 몬스터들의 몸뚱어리가 조각 난다.

핏물과 체액을 뒤집어쓴 채로 날 멍하니 바라보는 중국인 헌터를 뒤로하며, 주먹을 말아쥐었다.

고오오옹.

초고온의 열기가 주먹을 향해 내달리고, 이내 전방을 향해 쏘아졌다.

꽈앙!

멸염신권(滅炎神拳).

거대한 불의 기둥이 몬스터들을 집어삼켰다.

살이 타들어 가는 고약한 냄새와 함께 용케 살아남은 놈들이 고통에 찬 괴성을 내지른다.

몬스터도, 헌터도 순간 싸우는 것을 잊을 정도의 파괴력.

스켈레톤 워로드가 더듬거리는 목소리로 말했다.

- 가, 간악한 인간이여. 더욱 더 괴물이 되었구나.

“괴물한테 괴물 소리 들으니까 기분 묘한데. 그나저나 리치가 아니면 도대체 어떤 놈이 이 난리를 피우는 건데?”

- 그야 본 사령관도 모르지. 하지만 한 가지는 장담할 수 있다.

“장담? 뭘?”

- 놈의 언데드 통제는 이 몸에 비해 한 수 아래라는 것. 으하하! 군단이여! 본 사령관은 너희가 그립구나!

“…….”

이 자식을 죽여, 살려.

고민하던 나는 문득 뇌리를 스치는 어떤 생각에 우뚝 멈췄다.

“야, 방금 뭐라고?”

- 으하하핫! 본 사령관의 위엄을 느꼈는가. 간악한 인간이여!

“소멸할래, 말할래.”

- ……말하겠다. 그런데 뭘 묻는 거지?

“언데드 통제 어쩌구 했던 거.”

- 그거야 당연하지 않나. 본 사령관은 스켈레톤 워로드다. 놈들에 비교하면 당연히…… 어?

짧은 침묵.

나와 같은 생각을 했음이 틀림없다. 마른침을 꿀꺽 삼킨 나는 넌지시 말을 꺼냈다.

“해 봐. 그거.”

- …….

“할래, 소멸할래.”

스켈레톤 워로드가 입을 열었다.

- 자, 자라나라 해골해골…….

그 순간, 치열한 전투를 벌이던 언데드 몬스터들의 신형이 우뚝 멈췄다.

‘……이게 되네.’
```

## Final English reading copy

```markdown
# Chapter 380

Shao Shen realized it for the first time.

Roooooar!

If you witnessed an airplane diving toward the ground with both wings engulfed in flames, you would be seized by a terror that transcended species.

—Graaaar!

The supposedly fearsome ogres screamed, and the Trolls shrieked.

—Gweeeaaah!

Even the notoriously sluggish Ghouls ran so fast that sweat broke out on the soles of their feet.

—Squeeeeee!

“Uh, uh, uhhh…”

The monsters that could scream were the lucky ones.

Shao Shen and most of the others could do nothing but stare at the airplane hurtling toward the ground, frozen like stone statues.

*I have to run…*

His feet and hands would not move.

More importantly, Shao Shen and the Hunters of the Public Security Armed Forces Department were surrounded in the middle of the battlefield. They were not even given the chance to escape.

*Is this really the end?*

The same thought crossed everyone’s mind at that moment.

Rumble, rumble, rumble!

With a deafening roar, the airplane’s enormous fuselage swept across the battlefield.

And that earth-shaking collision began at the rear of the monster army, which had been scattering like a swarm of ants.

Crunch! Crack!

The massive steel hulk, weighing dozens of tons, crushed and burst apart everything in its path.

Green monster blood sprayed like fountains, while limbs of every size flew in all directions.

*W-What is this…?*

No matter how powerful the monsters’ physical defenses were, there were limits. Nothing could stop the airplane after it had transformed into a monster blender.

—Graaaar…!

—Kiiiiek!

Krrrunch!

The monsters’ screams were buried beneath the grisly sounds of flesh being torn apart. It was a scene of carnage beyond anything they had ever seen or heard.

As Shao Shen and the Hunters stared blankly at the unimaginable sight, someone’s frenzied shout pierced their ears.

“Monsters! Ram them! Kill them!”

“……!”

The unmistakable language of their homeland reached them even in the midst of all this chaos. The Hunters of the Public Security Armed Forces Department had one word flash through their minds: *reinforcements.*

Shao Shen was stunned.

*An incredible powerhouse!*

The powerful mana carried in that voice. The person was unquestionably an S-rank Hunter.

“Go for it! Airplane!”

“……”

And definitely a slightly insane S-rank Hunter.

*To think he’d resort to a tactic those island bastards used back in World War II. Did he not consider that his own allies might die?*

*He seems to have been sent by the Central Military Commission… But did our country have an S-rank Hunter like that?*

The question suddenly occurred to Shao Shen. But it was about to become irrelevant to him.

The gigantic steel hulk that had ground its way across half the battlefield was now charging straight toward him and the Hunters.

—K-Kiiit!

“Run!”

There was no distinction between friend and foe in the struggle to survive.

Shao Shen forgot the humans right in front of him and drove his dagger into a monster barreling toward him.

Schunk!

—Grrrk.

The monster’s lifeless body collapsed toward Shao Shen.

Unable to move even one step because monsters were surging in from every direction, Shao Shen felt the crushing weight descending upon him and shouted.

“The battle isn’t over! Fight until the very end!”

He was right. The battle was not over yet. A Hunter was someone who had to kill monsters until the final moment, until their own breath ran out.

The Hunters who heard Shao Shen’s shout gritted their teeth and swung their weapons.

*This will do.*

With lightning-fast skill, Shao Shen drove his dagger into the back of a fleeing ogre’s head, then drew a deep breath.

The airplane’s massive body had already reached a point less than twenty meters away.

Its speed had decreased considerably from before, but with everyone trapped in place, avoiding it seemed impossible.

*I have no regrets.*

If he died fighting for the people as a proud Hunter of Zhonghua, that was enough.

Shao Shen closed his eyes as screams rained down from every direction.

“Heave-ho.”

Krrrunch! Splat!

Drenched in a sticky liquid that he assumed was blood, Shao Shen thought:

*…“Whew”?*

Wasn’t it usually more of an “Aaaah”?

The strange sound was an odd choice for a dying cry, so Shao Shen slowly raised his eyelids.

And at last, he saw it.

A few steps away, the airplane had come to a complete stop. Two men were standing beside it, chatting casually.

“All right, we’ve arrived. It might explode, so get everyone off quickly.”

“……Mr. Jin Taekyung. They’re all unconscious.”

“Really? How weak.”

“……They would have died if not for the Barrier magic.”

“Then carry them out, Team Leader Choi. Oh, right. Is that bastard who called us chinks earlier alive, too?”

“Yes. He’s… alive, at least.”

“Then keep a close eye on that bastard. I’m going to give him hell for it when we head back.”

“……I’ll do my best.”

Shao Shen could not make sense of the situation at all.

Who, when, where, what, how, and why. It was such a bizarre sight that even the six fundamental questions could not organize it.

*How did the airplane suddenly stop, and who are those people? Were they not Hunters sent by the Central Military Commission?*

The two men were even speaking in a different language.

Shao Shen could not understand the words of the clean-cut man who looked like a young master, but he knew what country the language belonged to.

Korea, their longtime neighbor.

*Wait. If he’s Korean…!*

Shao Shen hurriedly wiped the blood from around his eyes. Only then did he recognize one of the men.

A muscular young man who stood a full head taller than everyone else.

The man Shao Shen had only ever seen on television—his idol—was standing right in front of him.

“C-Could you possibly be Mr. Jin from Korea?”

“Huh?”

The young man, Jin Taekyung, tilted his head as he looked at Shao Shen.

“I’m not a teacher.”

“Then… Lord Fuck…”

“…Fuck. What?”

*It really is him!*

Relief and hope coursed through Shao Shen’s entire body, making him tremble.

* * *

*How on earth does a Chinese person know about Lord Fuck?*

Articles about me had caused a brief stir in the foreign media, but I never expected my nickname to spread this far.

*Lord Fuck, making the five oceans and six continents tremble.*

If I ever went to the United States, some huge Yankee bros might approach me with beer bottles and act like they knew me.

*Hey, you. Lord Fuck?*

*I’m fine, thanks. Fuck. What kind of deranged bastards came up with a nickname like this?*

Anyway…

“What a mess.”

That was my brief assessment as I looked around.

Team Leader Choi, who had tied up the unconscious flight attendants like a string of dried fish, and the Skeleton Warlord, who I had shoved into my Inventory, answered me.

“It is a horrifying sight.”

—You wicked human. This commander finds this place quite pleasing. It feels familiar and even nostalgic.

“……”

The fact that a named undead monster—something that could be called death itself—was pleased by the sight said it all.

“We get thrown into actual combat the moment we arrive.”

As if responding to my complaint, the System notification rang.

Ding.

> **System**
>
> —An unexpected Quest, **Unexpected Attack**, has been generated.

*Was this why they said they were paying so much?*

I clicked my tongue and spoke.

“Team Leader Choi, protect the civilians first. After that, fight as you see fit. Don’t push yourself too hard.”

“Yes. That was already my intention.”

Team Leader Choi was a clever man. Learning the Jin Family’s Cultivation Technique had made him incomparably stronger than before, but he would never try to show off.

“And you there, young man.”

“Yes, y-yes, Mr. Jin.”

*Mr. Jin? What am I, a schoolteacher?*

I looked the young man who had answered so quickly up and down.

His face was young, but he was obviously a Hunter. A powerful one, too—probably around A-rank. Unlike the surrounding Hunters, who all wore identical armor as if they had been stamped out in a factory, he also had a red insignia on his shoulder.

“You look like you hold a pretty significant rank, so take good care of your men. Let’s save even one more person.”

“Y-Yes?”

“This is only the beginning.”

As I answered, I thrust out my fist.

Boom!

Streams of Scorching Yang Qi shot toward the monsters standing blankly in place.

When the searing heat swept through the area, only dozens of monster corpses remained.

“Why are you all staring? Did someone hit the pause button?”

“……!”

—……!

At my single remark, the silence pressing down on the battlefield shattered.

—Graaaar!

“K-Kill them! Stop the monsters!”

Humans and monsters. Monsters and humans.

A battle of killing and being killed began. I pulled White Flame from where it was deeply embedded in the ground and swung it.

Shing!

This wasn’t half water and half fish. Monsters filled every direction.

A crescent of Force extending from the spearhead brushed against a tightly packed cluster of monsters.

Ding.

> **System**
>
> —Defeated **Lv. 15 Undead Goblin**!
>
> —Defeated **Lv. 78 Undead Lycanthrope**!
>
> —Defeated **Lv. 93 Dullahan**!
>
> —Defeated **Lv. 30 Skeleton**!
>
> —…
>
> —…
>
> —There is a large Level gap. You gained negligible EXP!

System notifications announcing monster kills and EXP gains rang out without pause.

Under normal circumstances, I would have let such notifications go in one ear and out the other, or simply ignored them.

But this time, they provided an important clue.

“These things couldn’t possibly be…”

—Ah, that’s right. Wicked human! Such a powerful undead army!

The Skeleton Warlord’s delighted shout was enough to turn my suspicion into certainty.

*No wonder something felt strange.*

I had already been puzzled by the fact that I could not sense any life force from them.

There were still quite a few living monsters, but more than half of them were undead. Altogether, they formed a massive army numbering nearly two thousand.

“And undead monsters are…”

The Skeleton Warlord shouted, brimming with excitement.

—Beautiful! Magnificent! Heroic!

Thwack!

I cut down five monsters and muttered.

“Do you want to be annihilated like that thing just now? Beautiful, magnificent, and heroic?”

—……I misspoke. I apologize, wicked human.

The Skeleton Warlord, who had briefly forgotten its current situation, hurriedly added:

—Wait. If that is the case, then they must be under someone’s control!

I thought so, too.

There was only one thing I was not certain about.

“The Lich. Did that bastard personally come here?”

—Hmm. If you mean the Lich in that holographic video you showed me last time, then probably not.

As I listened to the Skeleton Warlord’s answer, I took half a step forward.

Boom!

A massive iron club passed dangerously close to my shoulder and smashed into the ground. It was an ordinary ogre, still carrying the vitality of a living creature.

—Graaaar!

“Sure. I’ll grill you.”

Boom!

The ogre struck in the chest by the Flame Divine Palm spurted dark green blood from all seven orifices.

I passed the collapsing bulk and brought White Flame down at an angle.

Shiiiiing! Slice!

Space itself was cut apart, and the bodies of the monsters caught within it were chopped to pieces.

Leaving behind the Chinese Hunter who stared blankly at me while covered in blood and bodily fluids, I clenched my fist.

Whoooom.

Extreme heat raced into my fist, then shot forward.

Boom!

Flame-Extinguishing Divine Fist.

A massive pillar of fire swallowed the monsters.

Alongside the foul stench of burning flesh, the few monsters that had somehow survived shrieked in pain.

The destructive power was enough to make both monsters and Hunters forget to fight for a moment.

The Skeleton Warlord spoke in a faltering voice.

—W-Wicked human. You have become even more of a monster.

“It feels strange hearing that from a monster. Anyway, if it wasn’t the Lich, then what kind of bastard is causing all this?”

—How should this commander know? But I can guarantee you one thing.

“Guarantee what?”

—His control over the undead is a notch below mine. Wahaha! Legion! This commander has missed you!

“……”

*Should I kill this bastard or let him live?*

As I pondered the question, a thought suddenly flashed through my mind, and I stopped dead.

“Hey. What did you just say?”

—Wahahaha! Have you finally felt the majesty of this commander, wicked human?

“Disappear or talk.”

—……I will talk. But what are you asking about?

“That bit about controlling the undead.”

—Isn’t that obvious? This commander is a Skeleton Warlord. Compared to them, of course I’m… Huh?

A brief silence followed.

The Skeleton Warlord must have reached the same conclusion I had. I swallowed dryly before bringing it up casually.

“Try it. Do that.”

—…….

“Do it, or disappear.”

The Skeleton Warlord opened its mouth.

—Grow, grow, skeletons, skeletons…

At that moment, the undead monsters in the middle of their fierce battle suddenly froze in place.

*…It works.*
```
