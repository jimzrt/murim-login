<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0381.txt",
      "sha256": "72b34dc3a00ee4cf069f91194c3af311d1130c076cc35a6d9f69dc13f13df4a1",
      "bytes": 15670
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "451a30813cfae7bf0e67ac923c07bdc463b9a55fdef5b2e1d5a8d51e8da3ac5d",
      "bytes": 2920
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "90a9c5eb7e6e8c29c0114047d5de31b94c6f17a90ebc2ecd65178e94a0607956",
      "bytes": 132181
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "934ff7616b95a5b96893793313039637655ebf7b223bca38202204710526b2b3",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2383c8d1bd721253ba625974699fa76ba36548327a9df7ee781ffa4cda34ff96",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d862f780d968bbc757ff9937db8857f9bdc2ef61e50241bf3838d2293330c7e6",
      "bytes": 102060
    }
  ],
  "estimated_tokens": 10486
}
-->

# Durable State Update — Chapter 381

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 381. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 381. Profile updates may replace only one
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
  "chapter": 381,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 381,
    "continuity_sources": [381],
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
    "Chengdu International Airport is under attack by an unexpectedly large monster army that includes living and undead monsters.",
    "The Chinese People’s Liberation Army and Public Security Armed Forces Department Hunters are defending the airport, but the defenders have suffered losses approaching half their strength.",
    "Jin Taekyung and Team Leader Choi have arrived at Chengdu International Airport, where Jin halted their aircraft in the middle of the monster army.",
    "More than half of the nearly two-thousand-monster army are undead and appear to be controlled by an unidentified external force.",
    "The Skeleton Warlord can control the undead army, and its command has caused the undead monsters to freeze in place.",
    "Shao Shen is a young Hunter of the Public Security Armed Forces Department who rallied the defenders and recognizes Jin Taekyung as Lord Fuck.",
    "Jin Taekyung is Level 120 at the Supreme Peak realm, has manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "The Myriad-Poison Ring remains bound to Jin Taekyung alongside White Flame and the Fire Dragon Armor.",
    "The System has generated the unexpected Quest Unexpected Attack.",
    "Mungyeong is the Divine Physician and former Slaughter Saint, has sworn never to kill again, and intends to live as a physician; Dong Feng is his Disciple.",
    "Cheongpung remains a Supreme Peak master with Mimi and is Mimi’s temporary guardian.",
    "Aehyang is manipulating the Sichuan City Lord under the direction of an unidentified person."
  ],
  "continuity_sources": [
    380
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "Who is controlling the Chengdu undead army, and what will result from the Skeleton Warlord seizing control of it?"
  ],
  "safe_through": 380,
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
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 오크 | **Orc** | Monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 네크로맨서 | **necromancer** | Alternate description of the black wizard ruling the Gate. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 워로드몬 | **Warlordmon** | Taekyung's mocking nickname for the Skeleton Warlord. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 그리폰 | **Griffon** | Flying monster species attacking the airport. |
| 듀라한 | **Dullahan** | Headless undead monster form taken by Yao Wei. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 워로드몬 | captor_to_captured_monster | Warlordmon | mocking-commanding | Taekyung uses the childish nickname while ordering the Skeleton Warlord to perform tricks. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 380
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 380
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃381화



솨아아아.

보이지 않는다. 그러나 느껴진다. 나를 중심으로, 아니 인벤토리라는 아공간에 존재하는 스켈레톤 워로드로부터 흘러나온 끈적한 기운이 사방으로 뻗어 나가는 것이.

변화는 순식간에 일어났다.

- 키릭?

- 구워?

흉포하기 그지없던 몬스터들의 움직임이 우뚝 멈췄다.

오크, 트롤, 고블린, 라이칸스로프와 몬스터 백과사전에서나 보던 온갖 종류의 몬스터와 전사한 헌터들까지.

놈들의 공통점은 단 하나, 이미 한 번 죽어 언데드로 부활했다는 점이었다.

꿀꺽.

마른침을 삼킨 내가 중얼거렸다.

“이게 되네.”

- 와, 이게 진짜 되네.

“……?”

- ……?

아니, 지금 뭐라고?

순간 뇌정지가 온 나는 작게 속삭였다.

“무슨 개뼈다귀 같은 소리야. 당연히 되니까 한 거 아니었어?”

스켈레톤 워로드가 우물쭈물 대답했다.

- 그게 사실…… 본 사령관도 이렇게 쉽게 될 줄 몰랐다.

“네 통제력이 훨씬 높다면서?”

- 아, 그건 홧김에 그냥 해 본 말인데.

“뭐?”

- 가만히 있기에는 자존심이 상해서…….

“…….”

이거 완전 미친놈 아냐.

어이가 없었지만, 그것과는 별개로 결과는 확실했다.

반경 수십 미터에 존재하던 언데드 몬스터들이 일시에 움직임을 멈추자 주위에서 벌어지던 치열한 전투도 잠시 소강상태에 빠진 것이다.

「모, 몬스터들이 움직임을 멈췄다!」

「이게 도대체 무슨 상황이지?」

「방심하지마! 아직 움직이는 놈들이 있다!」

누군가의 외침대로, 방심하기에는 아직 일렀다.

스켈레톤 워로드의 통제에 들어온 것은 근처의 일부 언데드 몬스터일 뿐, 멀리 떨어져 있거나 언데드 상태가 아닌 일반 몬스터의 경우는 예외였으니까.

- 우워어어어!

- 취이익!

“흐아아압!”

카가가강! 푸푹!

갑작스러운 동족의 변화에 어리둥절하던 것도 잠시, 통제가 되지 않는 몬스터들이 재차 날뛰기 시작하자 다시금 전투가 시작되었다.

머릿수에서부터 비교가 되지 않는 싸움. 그러나 지금 이 순간부터는 달라질 것이다.

나는 한껏 숨죽인 목소리로 외쳤다.

“가라, 워로드몬!”

발끈한 워로드몬, 아니 스켈레톤 워로드가 외쳤다.

- 간악한 인간이여! 본 사령관을 그렇게 부르지 말라!

“그럼 소멸하고 싶어서 환장한 워로드몬?”

- ……빌어먹을.

숨도 못 쉬는 해골 주제에 한숨을 푹 내쉬더니 이내 마법의 주문을 외운다.

- 싸워라, 해골해골.

저놈도 해골해골에 재미가 들린 게 틀림없다. 별 우습지도 않은 주문이었지만 효과는 확실했다.

- 구워?

스켈레톤 워로드의 명령에, 멍하니 풀려 있던 언데드 몬스터들의 눈동자에 흉포함이 서린다. 그리고 다음 순간.

콰직!

언데드 오우거의 쇠몽둥이가 어느 트롤의 머리통을 부수는 것을 시작으로, 새로운 주인을 섬기게 된 언데드 몬스터들이 동족을 향해 달려들었다.

- 쿠워어어어!

- 취, 취릭?

빠각! 서걱! 푸푸푹!

등 뒤에서 벌어진 예상치 못한 아군의 기습. 중국 헌터들을 포위하고 있던 몬스터 군단의 한 축이 속절없이 허물어졌다.

- 취이이익!

「뭐, 뭐야!」

「갑자기 저놈들이 왜……?」

당황한 것은 동족에게 배신당한 몬스터들 뿐만이 아니었다.

갑작스러운 상황에 얼떨떨해하는 중국 헌터들. 나는 그들의 선두에서 줄곧 종횡무진 창을 휘두르던 청년 헌터를 향해 외쳤다.

“샤오 쉔!”

「지, 진 선생님?」

동그래진 눈동자가 나를 바라봤다.

「어, 어떻게 제 이름을?」

방금 [기감]으로 레벨 창을 확인해서 알게 된 거지만, 지금은 그게 중요한 게 아니다.

“뭐 합니까! 적극 공세로 전환하지 않고.”

「그런데 이 상황은 도대체…….」

“지금 그게 그렇게 궁금해요? 언데드 몬스터 하나 붙잡고 육하원칙에 따라 왜 우리를 돕는지 설명을 듣고 싶어?”

「아, 아닙니다!」

“그럼 이제 어떻게 해야 될까?”

정신이 번쩍 든 샤오 쉔이 창을 번쩍 치켜들었다.

「공격 대형! 공안 무력부 전원, 지금부터 언데드 몬스터들을 제외한 나머지를 친다!」

「옛!」

훌륭한 판단의 표본이로군.

하나가 된 외침과 함께 궁지에 몰려 있던 오백여 명의 헌터들의 기세가 바뀌었다.

「죽여!」

「동지들의 원한를 갚아라!」

쉬쉬쉬쉭, 서걱!

- 아우우우!

막 오크의 목을 잘라낸 헌터를 향해 달려드는 라이칸스로프.

누런 송곳니로 목줄기를 물어뜯으려는 놈의 아가리를 거대한 주먹이 후려쳤다.

콰직!

- 그워어어어!

라이칸스로프의 두개골을 박살 낸 오우거가 흉포한 함성을 내질렀다. 그런 오우거의 머리 위로 급강하한 그리폰의 날카로운 발톱이 번쩍 빛을 발했다.

- 끼이이이익!

날카로운 괴성. A급 몬스터의 마력이 실린 발톱이 오우거의 안구를 할퀴려던 그 순간.

「아이스 볼!」

「라이트닝 볼트!」

대기하고 있던 원거리 헌터들의 마법에, 감전된 그리폰이 허공에서 몸을 부르르 떨었다.

바로 그때, 트롤의 어깨를 밟고 솟구친 한 인영이 그리폰을 향해 무기를 휘둘렀다.

“독일 최고의 무기 공방으로 손꼽히는 J사에서 특별 제작한……!”

서걱!

군더더기 없이 깔끔한 일격이 그리폰의 머리를 가른다.

우아하게 착지한 최 팀장이 피 한 방울 묻지 않은 투명한 검신을 바라보며 흡족하게 웃었다.

“경매가 52억에 낙찰받은 롱소드. 역시 제값을 하는군.”

“…….”

병신 같은데 멋있어. 멋있긴 한데 병신 같아.

그 광경을 지켜보던 스켈레톤 워로드가 떨떠름한 목소리로 물었다.

- 간악한 인간이여, 저 인간이 네 상관이라고 했나?

“아니, 그. 길드 내부 직책상으로 따지면 그렇긴 한데…….”

- 인간치고는 제법 똑똑해 보였는데, 별 괴상한 인간을 다 보겠군. 과연 네 녀석의 상관답다.

“혓바닥 잘못 놀려서 소멸하고 싶은 스켈레톤 워로드 손?”

짧게 침묵한 스켈레톤 워로드는 주문을 외는 것으로 대답을 대신했다.

- 자라나라, 해골해골!

서당 개 삼 년이면 풍월을 읊는다고, 이제는 시키지 않아도 알아서 잘한다.

투둑, 투두두둑.

최 팀장에게 죽은 그리폰이, 헌터와 언데드의 합공에 의해 쓰러진 몬스터들이 새로운 생명을 얻으며 죽은 육신을 일으켜 세운다.

그 숫자가 무려 이백. 처음 시도했던 것에 비해 범위도 더욱 넓어졌는지, 저 멀리에 있는 언데드 몬스터들도 스켈레톤 워로드의 통제에 들어와 아군을 공격하기 시작했다.

“와. 너 이 정도였냐?”

- 와. 본 사령관이 이 정도였나?

“…….”

- ……사실 이 정도까지는 아니었다. 하지만 어째서인지는 몰라도, 이곳에 오니 엄청난 마력이 솟구치는구나!

“어, 그래.”

나는 이 괴상한 네임드 몬스터를 이해하기를 포기했다.

하긴 결과만 좋으면 됐지, 지금 당장은 따져 봤자 머리만 아플 것 같다.

- 많은, 더 많은 군단을 내게 다오!

인벤토리에 넣어 둔 터라 보이지는 않지만, 뼈 밖에 안 남은 두개골을 부르르 떨고 있을 것이 분명했다.

나는 한숨을 내쉬며 창을 말아쥐었다.

“안 그래도 그럴 생각이야.”

- 방법이 있나?

“있지.”

더 많은 언데드를 늘리는 방법? 간단하다.

“싹 다 죽이면 돼.”

- 크하하하! 너는 실로 간악하고도 무식한 인간이로구나!

건방진 녀석. 하지만 이번만큼의 놈의 말에 일부분 동의할 수밖에 없다.

머릿속에 울려 퍼지는 스켈레톤 워로드의 광소를 들으며, 나는 걸음을 내디뎠다.

‘염화일로(炎火一路)’

화아아악!

발걸음을 따라, 불꽃의 길이 열렸다.



* * *



새카만 로브와 해골이 주렁주렁 매달린 지팡이. 동공이 있어야 할 그곳은 텅 비어 있었고 몸에는 아직 썩지 않은 살점이 붙어 있었다.

악몽에나 나올 법한 모습을 한 세 존재는 서로를 향해 의념(疑念)을 전달했다.

- 문제가 생겼군.

- 언데드 몬스터들이 통제를 벗어나고 있다. 인간을 도와 군단을 공격하고 있어.

- 어째서?

통제를 벗어나게 한 방법을 묻는 것이 아니다. 그들 세 존재는 이미 그 물음에 대한 답을 알고 있었으니까.

- 상위 언데드다. 우리보다 강력한.

모든 몬스터는 우열이 있지만, 그중에서도 특히 언데드는 철저한 힘의 지배를 받는다.

지금처럼 통제력을 빼앗겼다면 그것은 필시 상위의 존재가 벌인 소행이었다.

- 하지만…….

- 어떻게 그럴 수 있지?

세 존재 중 그 물음에 답할 수 있는 자는 아무도 없었다.

도대체 어찌 자신들보다 강력한 존재가 이곳에 있으며, 언데드의 통제권을 빼앗아 인간을 돕는단 말인가.

- 설마 ‘그분’께서?

- 말도 안 되는 소리. 그분께서 우리를 보내며 내리신 명령을 잊었는가?

- 인간을 죽여라. 더 많은 언데드와 군단을 만들어 더, 더 많은 인간을 죽여라.

명령을 다시금 떠올린 세 존재는 작은 혼란에 빠졌다.

그분, 아크 리치(Arch Lich)가 아니라면 그 누가 자신들의 통제력을 뛰어넘을 수 있단 말인가.

- 인간들 중 네크로맨서가 있었나?

- 아무것도 느끼지 못했다.

- 인간은 죽음을 배척하고 혐오하지. 그럴 리 없어. 설령 있더라도 우리에 비할 바는 아니다.

의념에서 숨길 수 없는 적의(敵意)가 느껴지는 까닭은, 그들 역시 한때 인간의 배척과 멸시를 한 몸에 받았던 네크로맨서였기 때문이었다.

하지만 그것은 이미 아득한 과거이며 또 다른 차원에서 있었던 일.

죽음이라는 망망대해를 표류하던 그들은 아크 리치라는 뱃사공을 만났고, 새로운 힘을 얻어 그토록 염원하던 리치(Lich)로 발돋움하려 하고 있었다.

그러나…….

- 아쉽군.

- 변화가 완전히 끝났더라면. 이 땅에 더 많은 죽음이 있었다면.

- 그럼 통제력을 빼앗기는 일 역시 없었겠지.

세 존재는 안타까움을 금치 못했다.

살아생전 위대한 네크로맨서였던 그들은 아직 완전한 리치로 거듭나지 못한 상태였다.

죽은 마법사의 몸을 빌려 새롭게 태어나기는 했으나, 일주일이라는 시간은 리치로 변화하기 위한 사기(死氣)를 흡수하기에는 너무나도 짧았다.

- 그렇기에 그분께서 우리 셋을 보낸 것인데.

- 이 일이 실패로 돌아간다면 실망하실 거다.

- 우리에게 주신 힘을 도로 빼앗으실지도 몰라.

그건 세 존재가 가장 두려워하는 일이었다.

아크 리치의 신임을 얻기 위해서라면 어떻게든 이 난관을 헤쳐나가야 했다. 설령 극심한 힘을 소모하더라도.

- 어쩔 수 없지.

- 힘을 합치자는 말인가?

- 그렇다. 우리 셋이 힘을 합친다면, 정체를 알 수 없는 상위 언데드도 더는 통제력을 빼앗을 수 없을 것이다.

- 으음. 좋다.

- 동의하는가?

- 동의한다.

아크 리치의 총애를 얻기 위해 경쟁하던 세 존재는 마침내 합의점을 찾았다.

그들은 망설임 없이 사령의 주문을 외우기 시작했다.

- 바렌시아. 마드릿.

- 바이엘른. 뮌헨.

- 스토흐. 시리.

세 존재로부터 흘러나온 죽음의 기운이 대기를 타고 뻗어 나갔다.

푸른 잔디가 까맣게 물들고, 범위에 들어와 있던 인민 해방군 소속의 병사들이 목을 움켜쥐고 쓰러졌다.

“컥!”

“크허억!”

쏴아아악.

단말마와 함께 숨이 끊긴 인간들의 몸에서 흘러나온 사기는 몬스터들의 전신에 스며들었다.

- 캬우우우우!

- 그워어어!

흉포한 외침에 실린 강력한 마력에 주위의 공기가 요동쳤다. 그 힘은 일반적인 몬스터와는 비교도 할 수 없을 정도였다.

강화된 통제력과 휘하 몬스터들의 힘을 느낀 세 존재는 그제야 주문을 멈추었다.

- 키키키키킥.

- 성공이다.

- 엄청난 힘을 소비하긴 했지만…… 이 정도면 차고 넘치는 수준이지.

세 존재가 더욱 강력해진 자신들의 군단을 바라보며 만족스럽게 웃던 그때.

꽈앙!

저 멀리, 굉음과 함께 몬스터의 사지가 날아올랐다.

세 존재는 솟구치는 불꽃을 바라보며 대화를 나누었다.

- 화염 마법사가 있나 보군. 제법인데?

- 그래 봤자 인간이다. 스켈레톤 메이지들을 대거 투입하도록 하지.

- 좋은 생각이야.

그리고 잠시 후, 다시금 솟구치는 화염에 세 존재는 서로를 바라보았다.

- 방금. 뭐였지?

- 통제력이 끊겼다. 빼앗긴 건 아니야.

- 소멸시켰다고? 제법이군.

- 그런데 정말 마법사가 맞나? 움직임이 너무 빠른 것 같은데…….

- 음. 오우거 부대를 투입 시키자.

- 오우거 받고, 듀라한 더.

- 듀라한까지? 그럼 우리들의 호위는 누가 맡지?

- 그의 말이 맞다. 듀라한은 너무 과해. 강화된 오우거로 충분하다.

- 그렇긴 하지.

그리고 삼 분 후.

세 존재의 두개골 위로는 심각한 공기가 어렸다.

- 끊겼다.

- 또?

- 그러게 듀라한 보내자니까.

- 저거 도대체 뭐지. 마법사 아닌 것 같은데.

- 아, 일단 듀라한부터 보내자고!

- 그, 그러도록 하지.

호위부대로 삼은 듀라한 이십여 마리가 우르르 사라지는 모습을 보며, 세 존재는 슬그머니 또 다른 합의점을 찾기 시작했다.

- 음. 그런 일이 벌어지지는 않겠지만 혹시…….

- 나도 비슷한 생각을 했다.

- 데스나이트(Death Knight)…… 만들까?

- 이미 너무 많은 힘을 소비했는데 데스나이트까지? 재료도 마땅치 않고, 시간도 오래 걸릴 텐데.

- 급한 대로 가장 쓸 만한 놈을 골라서 만들면 된다. 우리 셋이 힘을 합친다면 가능해.

- 그, 그럼 시도는 해 볼까.

그러나 세 존재의 데스나이트 제작 계획은 채 십 분도 지나지 않아 산산조각 나고 말았다.

화륵, 콰아아앙!

뼈밖에 남지 않은 몸으로도 느낄 수 있는 초고온의 열기.

“시벌 놈들. 더럽게 많네.”

콰드드득!

겁화(劫火)에 휩싸인 창을 휘두르며 몬스터 군단을 박살 내는 존재를 목격한 세 존재는 황급히 주문을 외웠다.

느릿느릿하던 목소리는 랩처럼 빨라져 있었다.

- 옴느하소유!

- 옌위가지케!

그러나 주문이 완성되기도 전에, 화염 마법사인지 전사인지 분간이 되지 않는 젊은 인간은 그들의 코앞에 도착해 있었다.

“어, 반갑다.”

- 오, 옴느하소유!

- 예, 옌위가지케!

청년, 진태경이 삐딱하게 고개를 꺾었다.

“안녕하세요. 연예가중계? 병신들인가.”
```

## Final English reading copy

```markdown
# Chapter 381

Whoooosh.

I couldn’t see it. But I could feel it.

Centered around me—or rather, flowing out from the Skeleton Warlord in the subspace known as my Inventory—a sticky energy spread in every direction.

The change happened in an instant.

—Kirik?

—Gwoo?

The movements of the monsters, who had been nothing short of ferocious, abruptly stopped.

Orcs, Trolls, goblins, Lycanthropes, every kind of monster I had only ever seen in monster encyclopedias, and even the fallen Hunters.

They had only one thing in common: they had already died once and been resurrected as undead.

Gulp.

I swallowed dryly and muttered.

“It works.”

—Wow. It really works.

“……?”

—……?

*Wait. What did he just say?*

My brain froze for a moment before I whispered,

“What kind of dog-bone bullshit is that? Didn’t you try it because you knew it would work?”

The Skeleton Warlord answered hesitantly.

—The truth is… This commander did not know it would work so easily.

“You said your control was much stronger.”

—Ah, that? I just said it in the heat of the moment.

“What?”

—I was too proud to just sit around doing nothing…

“…….”

*Isn’t this guy completely insane?*

I was dumbfounded, but regardless of that, the result was undeniable.

The undead monsters within a radius of several dozen meters had all stopped moving at once, and the fierce battle raging around us had temporarily fallen into a lull.

「T-The monsters have stopped moving!」

「What in the world is going on?」

「Don’t let your guard down! Some of them are still moving!」

Just as someone shouted, it was still too early to relax.

Only some of the nearby undead monsters had come under the Skeleton Warlord’s control. The ones farther away, along with the ordinary monsters that were not undead, were exceptions.

—Gwoooooar!

—Chiiik!

“Haaah!”

Clang! Stab!

The uncontrolled monsters were only briefly bewildered by the sudden change in their own kind before they began rampaging again, and the battle resumed.

It was a fight where the two sides could not even be compared in terms of numbers.

But from this moment onward, that would change.

I shouted in a hushed voice.

“Go, Warlordmon!”

The Warlordmon—no, the Skeleton Warlord—shouted back in outrage.

—Wicked human! Do not call this commander that!

“Then how about Warlordmon who’s desperate to be annihilated?”

—……Damn it.

Despite being a skeleton that couldn’t even breathe, he let out a deep sigh before chanting a spell.

—Fight, Skeleton Skeleton.

That guy had definitely started enjoying the whole Skeleton Skeleton thing. It was hardly an impressive incantation, but its effect was undeniable.

—Gwoo?

At the Skeleton Warlord’s command, ferocity filled the eyes of the undead monsters that had been standing blankly. Then, in the next moment—

Crunch!

An undead ogre’s iron club crushed a Troll’s skull.

That was the beginning.

The undead monsters who had gained a new master charged at their own kind.

—Gwoooooar!

—Ch, chirik?

Crack! Slice! Stab-stab-stab!

An unexpected ambush from behind.

One flank of the monster army surrounding the Chinese Hunters collapsed helplessly.

—Chiiiiiik!

「W-What the hell!」

「Why are those monsters suddenly…?」

The monsters betrayed by their own kind were not the only ones thrown into confusion.

The Chinese Hunters were also bewildered by the sudden turn of events.

I shouted toward the young Hunter who had been cutting through the battlefield with his spear from the front of the formation.

“Shao Shen!”

「M-Mr. Jin?」

His round eyes looked toward me.

「H-How do you know my name?」

I had just checked his Level with Qi Sense, but that was not important right now.

“What are you doing? Why aren’t you switching to an all-out offensive?”

「But what is going on here…?」

“Are you really curious about that right now? Do you want to grab an undead monster and make it explain why it’s helping us using the five Ws and one H?”

「N-No, sir!」

“Then what should you do now?”

Shao Shen’s eyes cleared, and he raised his spear high.

「Attack formation! Everyone in the Public Security Armed Forces Department, from this moment on, attack everything except the undead monsters!」

「Yes, sir!」

*That was an excellent decision.*

Along with their unified shout, the momentum of the roughly five hundred Hunters who had been driven into a corner changed.

「Kill them!」

「Avenge our fallen comrades!」

Shish-shish-shishik! Slice!

—Awooooo!

A Lycanthrope charged toward a Hunter who had just cut down an Orc.

The creature opened its jaws, yellow fangs aimed at the Hunter’s throat, but a massive fist slammed into its mouth.

Crunch!

—Gwoooooar!

The ogre that had crushed the Lycanthrope’s skull let out a savage roar.

Above the ogre’s head, a Griffon dove sharply. Its razor-sharp claws flashed.

—Kiiiieeeek!

Just as the A-rank monster’s mana-infused claws were about to rake across the ogre’s eyes—

「Ice Ball!」

「Lightning Bolt!」

The waiting ranged Hunters unleashed their magic, and the electrocuted Griffon shuddered in midair.

At that very moment, a figure sprang upward after stepping on a Troll’s shoulder and swung a weapon at the Griffon.

“Specially made by J Company, widely considered one of Germany’s finest weapon workshops—!”

Slice!

The clean, effortless strike split the Griffon’s head in two.

Team Leader Choi landed gracefully and smiled with satisfaction as he looked at the transparent sword blade, which did not have a single drop of blood on it.

“A longsword I won at auction for 5.2 billion won. It certainly earns its price.”

“…….”

*It looks stupid, but it’s cool.*

*It’s cool, but it looks stupid.*

The Skeleton Warlord, who had been watching the scene, asked in a dubious voice,

—Wicked human, you said that man was your superior?

“No, well. Technically speaking, in terms of Guild positions, he is, but…”

—He looked rather clever for a human, but I have never seen such a strange human. He truly is a fitting superior for you.

“Who wants to be annihilated because he couldn’t keep his mouth shut?”

After a brief silence, the Skeleton Warlord answered by chanting another spell.

—Grow, Skeleton Skeleton!

They say even a dog at a village school can recite poetry after three years. Now he could do it without being told.

Crack. Crack-crack-crack.

The Griffon killed by Team Leader Choi, along with the monsters brought down by the combined attacks of the Hunters and undead, gained new life and rose from their dead bodies.

There were two hundred of them.

It seemed the range was also wider than during the first attempt. Even the undead monsters in the distance had come under the Skeleton Warlord’s control and begun attacking their former allies.

“Wow. You were capable of this?”

—Wow. Was this commander capable of this?

“…….”

—……Actually, this commander was not capable of quite this much. But for some reason, an enormous amount of mana is surging through me now that I am here!

“Sure. Great.”

I gave up on trying to understand this bizarre named monster.

As long as the result was good, that was all that mattered. Trying to figure it out right now would only give me a headache.

—Give me more. More legions!

I couldn’t see him because he was inside my Inventory, but I was certain his bony skull was trembling with excitement.

I sighed and tightened my grip on the spear.

“I was planning to.”

—Do you have a way?

“I do.”

The method for increasing the number of undead was simple.

“Kill them all.”

—Kahaha! You truly are a wicked and ignorant human!

The bastard was being cheeky, but this time, I had no choice but to agree with part of what he said.

Listening to the Skeleton Warlord’s laughter echo through my mind, I stepped forward.

*Flamefire Path.*

Whoooosh!

A path of flame opened with every step.

* * *

Black robes. A staff with skulls dangling from it.

The places where their pupils should have been were empty, and patches of flesh that had yet to rot still clung to their bodies.

The three beings, who looked as though they had stepped out of a nightmare, conveyed their thoughts to one another.

—There is a problem.

—The undead monsters are slipping out of our control. They are helping the humans and attacking the legion.

—Why?

They were not asking how their control had been broken. The three beings already knew the answer to that question.

—A higher undead. One more powerful than us.

All monsters had a hierarchy, but undead were ruled by power more absolutely than any other species.

If control had been stolen from them like this, it was undoubtedly the work of a higher existence.

—But…

—How is that possible?

None of the three beings could answer.

How could an existence more powerful than them be here, seize control of the undead, and help the humans?

—Could it be that person?

—That is absurd. Have you forgotten the command that person gave us when sending us here?

—Kill the humans. Create more undead and an army, and kill more, more humans.

The three beings recalled the command and fell into a state of confusion.

If that person—the Arch Lich—was not responsible, then who could possibly surpass their control?

—Was there a necromancer among the humans?

—I sensed nothing.

—Humans reject and despise death. That is impossible. Even if there were one, they would be nothing compared to us.

The reason unmistakable hostility could be felt in their thoughts was that they, too, had once been necromancers who had suffered human rejection and contempt.

But that had happened in the distant past, in another dimension.

Drifting across the boundless ocean of death, they had met a boatman named the Arch Lich. After gaining new power, they were finally on the verge of becoming the Liches they had longed to be.

But…

—What a shame.

—If only our transformation had been completed. If only there had been more death in this land.

—Then we would not have lost control, either.

The three beings could not hide their regret.

They had been great necromancers while alive, but they had not yet fully transformed into Liches.

They had been reborn using the bodies of dead mages, but one week was far too short to absorb enough death energy to complete their transformation into Liches.

—That is why that person sent the three of us.

—If this mission fails, that person will be disappointed.

—That person might even take back the power they gave us.

That was what the three beings feared most.

They had to overcome this crisis somehow if they wanted to earn the Arch Lich’s favor.

Even if it meant exhausting a tremendous amount of power.

—There is no other choice.

—Are you suggesting that we combine our strength?

—Yes. If the three of us combine our strength, even an unidentified higher undead will no longer be able to steal control from us.

—Hmm. Fine.

—Do you agree?

—I agree.

The three beings, who had been competing to earn the Arch Lich’s favor, finally reached an agreement.

Without hesitation, they began chanting a spell of necromancy.

—Valencia. Madrid.

—Bayern. Munich.

—Stoke. City.

The energy of death flowing from the three beings spread through the air.

The green grass turned black, and the soldiers of the People’s Liberation Army within its range clutched their throats and collapsed.

“Ghk!”

“Guhhh!”

Whoooosh.

The death energy flowing from the bodies of the humans whose lives had been cut short seeped into the monsters’ entire bodies.

—Kyaaaaaaah!

—Gwoooooar!

The air trembled from the powerful mana carried in their savage cries. Their strength was beyond comparison with that of ordinary monsters.

Only after sensing their strengthened control and the power of the monsters under their command did the three beings stop chanting.

—Kikikikik.

—Success.

—We did consume an enormous amount of power… but this is more than enough.

Just as the three beings were smiling in satisfaction at their now more powerful army—

Boom!

Far away, a monster’s limbs flew through the air with a thunderous explosion.

The three beings looked toward the rising flames and exchanged thoughts.

—There appears to be a flame mage. Not bad.

—He is still only human. Deploy a large number of Skeleton Mages.

—Good idea.

A short while later, more flames rose into the distance, and the three beings looked at one another.

—What was that just now?

—Our control was severed. It was not stolen.

—Did he annihilate them? Impressive.

—But is he really a mage? His movements seem far too fast…

—Let us deploy the ogre unit.

—I’ll see your ogres and raise you Dullahans.

—Dullahans, too? Then who will protect us?

—He is right. Dullahans would be excessive. Strengthened ogres will be enough.

—That is true.

Three minutes later, a grim atmosphere hung over the three beings’ skulls.

—It broke.

—Again?

—I told you we should send Dullahans.

—What is that thing? It does not seem to be a mage.

—J-Just send the Dullahans first!

—Th-Then we shall do so.

The three beings watched as more than twenty Dullahans, chosen as their escort force, rushed away. Then they quietly began searching for another point of agreement.

—Hmm. It is unlikely that such a thing will happen, but just in case…

—I had a similar thought.

—Should we create a Death Knight?

—We have already consumed too much power. A Death Knight, too? We do not have suitable materials, and it would take a long time.

—In an emergency, we can choose the most useful one and make it. If the three of us combine our strength, it will be possible.

—Th-Then should we try?

But the three beings’ plan to create a Death Knight was smashed to pieces less than ten minutes later.

Whoosh! Boom!

Even with nothing but bones left on their bodies, they could feel the heat of the searing flames.

“Fucking bastards. There’s a shitload of them.”

Crunch!

The three beings witnessed an existence tearing through the monster army with a spear engulfed in hellfire and hurriedly began chanting spells.

Their slow, dragging voices had become as fast as rap.

—Omnehasoyu!

—Yenwigajike!

But before the chant was complete, the young human who could not be identified as either a flame mage or a warrior had already arrived right in front of them.

“Oh, nice to meet you.”

—O-Omnehasoyu!

—Y-Yes, Yenwigajike!

The young man, Jin Taekyung, tilted his head to one side.

“Hello. *Entertainment Weekly*? Are you idiots?”[^1]

[^1]: The garbled incantations sound like the Korean phrase *annyeonghaseyo, Yeonye-ga Junggye* (“Hello, *Entertainment Weekly*”), using the title of a long-running Korean entertainment-news program.
```
