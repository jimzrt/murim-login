<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0398.txt",
      "sha256": "1b40d2262ba3c2a3556703fc2637d662d885fe251f0e66548c4efbcf9b5d235c",
      "bytes": 13288
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "43a6ed1c25ae4f00886db98731d89e921187a32c395a611caa70dda65fc1b2c8",
      "bytes": 2088
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "89060d8deb1aecc1feaa715fa00524cd58dd7dfd97dcd08d1c5d706e79dfeaef",
      "bytes": 135344
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f9a0778f23de477cced4c88caa479d7f8af392738a5970db49cea90cd7a6a950",
      "bytes": 533
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "10a6d7232f48ad57713e4e0059699102c273655f1965f1daecb7cda5c79525b1",
      "bytes": 735
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3f3d53c9f53f220dbda108e609c119e345c65d28105f2ac04217767fdb302d09",
      "bytes": 116340
    }
  ],
  "estimated_tokens": 9012
}
-->

# Durable State Update — Chapter 398

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 398. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 398. Profile updates may replace only one
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
  "chapter": 398,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 398,
    "continuity_sources": [398],
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
    "The black knight serves an unnamed lord whose commands bind him completely and commands the Death Knights and the wider undead army.",
    "The black knight recognizes the attacked city as connected to memories of a child, light, and an unknown hand, but does not know his own origin.",
    "The Arch Lich's forces have used communications interference and coordinated surprise attacks to overwhelm the human defenses.",
    "Choi Minwoo and Shao Shen led 325 Hunters in a final stand after ordering other surviving forces to retreat.",
    "The black knight possesses an infant shoe, feels unexplained emotional and physical pain, and is beginning to resist his usual obedience.",
    "The black knight has two human survivors brought before him as potential servants.",
    "Jin Taekyung has reached the hospital rooftop alive and is confronting the black knight.",
    "Lei Fei remains missing with his unit, and Wei Fenghu still wants Jin to bring him back if found."
  ],
  "continuity_sources": [
    397,
    396
  ],
  "open_questions": [
    "What is the black knight's identity and origin, and what is the significance of the child and shoe connected to his memories?",
    "Who is the lord served by the black knight, and what is the Arch Lich's larger objective?",
    "What will happen in Jin Taekyung's confrontation with the black knight?",
    "Did Choi Minwoo, Shao Shen, and the 325 Hunters survive their final stand?",
    "What happened to Lei Fei and the Second Fiend assigned to the Qingcheng attack?"
  ],
  "safe_through": 397,
  "temporary_decisions": [
    "Render 파이 첸 as Faye Chen and 매직 존슨 as Magic Johnson.",
    "Render 전하 as His Highness for Prince Felix, including Jin's sarcastic use of the title.",
    "Preserve Magic Johnson's casual, flirtatious banter and Jin's dry, blunt resistance.",
    "Preserve Jin's profane humor and Choi Minwoo's blunt battlefield profanity.",
    "Render Death Knight as the capitalized Monster type and black knight as its lower-case leader title."
  ],
  "version": 1
}
```

## Exact glossary matches

| 화산파    | **Huashan**                      |
| 남궁세가   | **Nangong Family**               |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 화산     | **Huashan**            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 듀라한 | **Dullahan** | Headless undead monster form taken by Yao Wei. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 공안무력부 | **Public Security Armed Forces Department** | Chinese security organization ordered to assemble during the attack. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 396
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 395
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and Faye Chen, and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃398화



텔레포트를 시도하기 전, 문득 머릿속에 떠오른 생각이 있었다.

‘내 지난 2년을 백분율로 따진다면 얼마나 될까.’

어느 F급 헌터가 길드에서 잘린 날, 터덜터덜 언덕길을 오르다가 분리수거장에 버려진 구형 캡슐을 발견할 확률.

바로 그 구형 캡슐이 또 다른 세상으로 가는 연결 통로일 확률.

남궁세가도, 화산파 적전제자도 아닌 변방 무가의 삼공자로 제2의 인생을 시작할 확률.

그렇게 한 번의 전쟁, 두 번의 혈사와 셀 수도 없는 사선(死線)을 넘나들며 지금까지 살아남을 확률…….

그 모든 것을 종합해 본 결과, 단 하나의 결론이 나왔다.

“역시, 10%면 충분해.”

나는 나직한 중얼거림과 함께 손을 뻗었다.

허공섭물(虛空攝物).

삼 갑자의 공력이 최 팀장과 샤오 쉔을 끌어당긴다. 데스나이트와 몬스터들이 나서려 했지만, 우두머리가 손을 들자 멈추었다.

나는 놈들에게 신경 쓰지 않고 두 사람의 상태를 살폈다. 가느다란 숨결과 금방이라도 끊어질 것처럼 위태로운 기운.

만약 텔레포트가 아니라 제트기를 탔다면, 나는 영영 늦어 버렸을지도 모르겠다.

“1%여도 시도했을 거야. 난 이렇게 허무하게 죽을 놈이 아니거든.”

물론 만일을 대비해 들어 놓은 보험도 있었다. 이 보험을 이렇게 빨리, 이런 상황에서 쓰게 될 줄은 몰랐지만.

‘인벤토리 오픈. 소환.’

몬스터들의 시선 따위, 신경 쓰지 않는다.

즉시 인벤토리에서 필요한 물건을 꺼내는 내 모습을 본 우두머리가 고저 없는 목소리로 묻는다.

- 아공간이군. 마법을 익혔나.

아가리 닥쳐.

혀끝에 맴도는 말을 삼켰다. 평소였으면 상당히 힘들었겠지만, 지금의 나에게 그건 그리 어려운 일이 아니었다.

아무에게도 방해받고 싶지 않다. 적어도 지금만큼은.

퐁.

마법으로 밀봉된 마개를 벗기자 은은한 향기가 흘러나왔다. 투명한 유리병 안에는 우윳빛 색깔을 띤 액체가 출렁였다.

최상급 포션.

숨만 붙어 있다면 그 어떤 부상도 치료한다는 기적의 물약.

적어도 현재의 나는 이 100ml 남짓한 소량의 액체가 가진 희소성과 가치에는 아무런 관심도 없다.

그저 최상급 포션을 소유했던 우헤이싱의 엄청난 재력과 놈의 멍청함에 감사를 표하며, 죽은 듯 누워 있는 환자의 입술 사이로 포션을 흘려보낼 뿐이다.

‘조금만 참아라, 쉔.’

첫 번째 순서는 최 팀장이다. 함께 지낸 시간도 그렇지만, 지금까지의 정이 아니었더라도 그를 먼저 택했을 것이다. 그만큼 최 팀장의 부상은 심각했다.

‘이건…….’

어깻죽지부터 뜯겨 나간 왼팔. 뭔가가 씹어 삼킨 것처럼 너덜거리는 오른쪽 발목과 깔끔하게 절단된 왼쪽 다리. 그 밖에도 갈비뼈가 일곱 대나 나가고, 척추가 부러졌다.

그리고…… 기형적으로 꺾인 오른손에는 아직도 검 자루가 쥐어져 있다.

어떤 상황에서도 놓치지 않기 위해 단단히 고정한 가죽끈은 피에 흠뻑 젖어 있었다.

“…….”

나는 묵묵히 가죽끈을 풀었다. 뼈마디가 으스러진 그의 오른손에서 검을 빼내어 옆에 놔두었다.

마음속으로 던지는 핀잔 한마디도 잊지 않았다.

‘왜 그러셨습니까? 이건 살아 있는 게 기적이라고요.’

그리고 곧 진짜 기적이 시작되었다.

신중히 유리병을 기울여 정확히 절반을 섭취시켰을 때, 무언가 타들어 가는 소리와 함께 최 팀장의 전신을 뒤덮은 상처들이 회복되기 시작한 것이다.

치익, 치이이익-

뼈는 자라나고, 끊어진 근육은 이어졌으며 장기와 살은 아물었다.

재생(再生)의 대명사라 할 수 있는 트롤보다도 빠른 회복 속도. 마치 시간을 되돌린 것처럼 회복된 최 팀장의 얼굴에 비로소 혈색이 돌기 시작했다.

‘기운도 안정되었고. 이 정도면 충분해.’

내게는 더할 나위 없이 만족스러운 결과였다. 이 광경을 지켜보던 다른 누군가에게는 아니었겠지만.

- 겁 없는 인간이여.

- 당장 멈추어라.

- 그들은 강대하신 우리의 로드께.

- 종속되어야 할 운명을 부여받았다.

나는 우두머리를 대신해 앞으로 나선 두 기의 데스나이트를 말없이 바라보았다.

칠흑 같은 전신 갑주를 걸친 놈들은 언뜻 보면 쌍둥이 같았다. 키도 비슷하고 목소리도 구분하기 어려웠다.

다만 한 가지 확연히 눈에 띄는 차이점은, 허리에 찬 무기가 다르다는 것이다.

‘하나는 메이스(Mace). 다른 한 놈은 검.’

그것으로 이미 답은 나왔다. 문제를 풀었으니 답은 나중에 적어도 된다. 지금은 남은 문제를 해결해야 할 때다.

“너도 고생 많았다, 쉔.”

최 팀장만큼은 아니지만, 역시 심각한 중상을 입은 샤오 쉔에게 절반쯤 남은 포션을 흘려보내려던 그 순간이었다.

- 하찮은 인간이여.

- 마지막 경고다.

- 그 두 인간을 내려놓고, 물러나 자비를 구하라.

- 그럼 로드께서, 널 종으로 거두어 주실 것이다.

“종?”

- 그렇다.

감정이 느껴지지 않는 고저 없는 목소리와 함께, 데스나이트 중 하나가 나를 향해 발을 내디뎠다. 걸음마다 허리에 고정된 검집이 흔들린다.

덜그럭, 덜그럭, 덜그럭.

한 걸음. 두 걸음. 세 걸음.

내게 다가오는 놈에게는 어떤 망설임도 엿볼 수 없었다.

어림잡아도 수천에 달하는 몬스터와 우두머리가 지켜보는 앞이다.

데스나이트는 감정이 없는 언데드 몬스터라는 게 믿기지 않을 만큼, 자신감에 찬 어조로 말했다.

- 너는 실로 크고 빛나는 영혼을 가진 자. 우리의 일원이 되어라.

크고 빛나는 영혼이라…….

나는 고개도 들지 않고 포션을 계속해서 흘려보냈다.

마지막으로 보이는 몇 방울을 샤오 쉔의 입에 털어 넣은 후, 유리병의 마개를 닫아 인벤토리에 보관했다.

치익, 치이이익.

회복을 알리는 신호.

기다리고 있던 반가운 소리에 허리를 폈다. 데스나이트를 바라보며 아까부터 하고 싶었던 말을 건넸다.

“왼쪽 다리.”

- 음?

“최 팀장님 왼쪽 다리. 무릎 아래 한 뼘부터 텅 비어 있더라. 아주 깔끔하게. 샤오 쉔. 저 어린 녀석은 오른팔이었고.”

- 인간. 무슨 말이 하고 싶은 것인가.

“무슨 말이 하고 싶긴.”

나는 놈을 향해 희미하게 웃어 보였다.

“멀쩡하게 붙어 있던 팔다리 잘랐으면, 그만한 각오는 해야 했다는 거지.”

그리고 다음 순간.

찰나를 반으로 쪼개고 쪼갠 시간 속에서, 어느새 놈은 내 코앞까지 도착해 있었다.

아니, 그 반대다.

놈이 온 것이 아니라, 내가 갔다.

“어디 그 잘난 솜씨 좀 보자.”

- ……!

모든 것이 한순간에 일어났다. 데스나이트는 검을 뽑으려 했고, 나는 왼손을 뻗어 놈의 손등을 지그시 눌렀다.

그리고 그것은 시작인 동시에 끝이었다.

스릉, 철컥!

묵빛 검신이 채 뽑히기도 전에 검집으로 돌아갔을 때는, 내 일권(一拳)이 놈의 가슴을 관통한 후였으니까.

퍼걱!

삼 갑자의 열양지기가 실린 멸염신권(滅炎神拳)은 언데드의 체내에 남아 있던 한 줌의 핏물마저 증발시켰고, 이미 오래전에 죽은 육신을 장작 삼아 타올랐다.

화륵, 콰아아아!

꺼지지 않는 불길에 휩싸인 데스나이트는 손을 휘적거리며 동족들을 향해 돌아섰다.

거침없이 걸어왔던 그 길을 비틀비틀 걷다가 이내 잿가루가 되어 허물어졌다.

- ……!

- ……!

수천 마리의 몬스터가 모여 있음에도 음소거 버튼을 누른 것처럼 조용하다.

나는 인벤토리에 넣어 둔 백염(白炎)을 꺼내 들고 천천히 걸음을 옮겼다.

철벅, 철벅.

시선이 닿고, 발이 밟는 곳마다 시체와 핏물이 가득했다.

셀 수도 없이 많은 소총이 발에 챘고 비뚤어진 방탄을 눌러쓴 군인은 이미 생명이 빠져나간 눈동자로 허공을 올려다보았다.

그나마 저 군인은 시체라도 보존했다.

가장 치열한 격전지로 짐작되는 곳에는 공안무력부 헌터로 짐작되는 이들이 온전치 못한 모습으로 숨이 끊어져 있었다.

샤오 쉔이 이끄는 1연대와 함께한 지 어언 일주일. 시신 중에는 낯익은 얼굴도 여럿이었다.

‘많이 죽었구나. 정말로 많이.’

오늘, 이 자리에서만 족히 삼천에 달하는 인간이 죽음을 맞이했다.

다섯 개 전선을 모두 합한다면, 이번 몬스터 웨이브로 희생당한 민간인들까지 더한다면 그 희생자는 얼마나 될까.

푹!

이름 모를 헌터의 창을 빌려 지면 깊숙이 박아넣었다. 창대 끝에 단단히 묶어 둔 최 팀장의 가죽끈이 바람을 타고 휘날린다.

그 너머로 수천 마리에 달하는 몬스터 군단과 ‘놈’이 있었다.



[Lv.135 데스나이트 로드]



데스나이트 로드라. 이름 한 번 거창하다. 거창한 이름에 어울릴 만한 힘을 지닌 몬스터이기도 하고.

‘경우는 다르지만, 저런 놈이 하나 더 있긴 하지.’

나는 역대 최장 시간 침묵을 지키고 있는 녀석을 불렀다.

“부탁 하나만 하자.”

못 들은 척할 줄 알았는데, 잠시 망설이던 스켈레톤 워로드가 대답했다.

- ……부탁? 설마 함께 싸워 달라는 건 아니겠지?

“그럴 리가.”

기대한 적도 없고, 기대하지도 않는다. 내가 녀석에게 할 부탁은 싸우는 게 아니라 누군가를 지키는 것이다.

“뒤에 두 사람을 지켜. 무슨 수를 써서라도.”

현재 스켈레톤 워로드는 내 허락하에 틈틈이 사기(死氣)를 흡수함으로써 힘의 성장을 이룬 상태.

애당초 네임드 몬스터인 만큼 어지간한 A급 몬스터 몇 마리쯤은 홀로 감당할 수 있을 것이다.

“전투가 끝나면 무슨 소원이든 들어주지.”

- 그렇다면야 못 할 건 없지만. 도대체 언제까지 지켜야 하는 건가?

“그야 당연히…….”

나는 백염을 들어 데스나이트 로드를 겨누었다.

“저 새끼들이 모두 죽을 때까지지.”

- 이런 미친……!

“늦었다.”

인벤토리에서 스켈레톤 워로드의 해골을 꺼내 등 뒤로 던졌다.

뿌드득, 뚜둑.

녀석이 황급히 신체를 재생시키는 사이, 나는 창대에 묶여 휘날리는 가죽끈을 쓰다듬었다.

그는, 그들은 어떤 기분이었을까.

죽음을 향해 돌격하며 어떤 생각을 품었을까. 감히 짐작할 수 없다.

지금의 내가 확신할 수 있는 것은, 단 한 가지뿐이다.

“이 창을 넘어오는 새끼들은, 다 뒈질 줄 알아라.”

단전에 웅크리고 있던 화룡이 고개를 들었다.



* * *



콰드드드득!

살과 뼈가 으스러지며 사방으로 튀었다.

오우거의 팔다리가 사방으로 날아가고 트롤은 재생할 틈도 없이 꺼지지 않는 불길에 휩싸였다.

퍼벙! 서걱!

송곳니를 들이대던 라이칸스로프의 머리통이 터져 나간다.

악취 나는 뇌수를 뒤집어쓰며 달려오는 듀라한은 단 일격에 몸뚱이가 양단되었고, 새로운 주인을 찾은 할버드는 엄청난 힘을 받고 날아가 와이번의 날개를 찢었다.

콰지지직!

- 캬우우우우!

투두두둑!

허공에서 흩뿌려지는 피의 소나기.

동시에 소나기를 뚫고 날아드는 푸른 불꽃의 궤적.

후우우우웅! 서걱!

한바탕 피 보라가 일었다. 불꽃이 허공을 수놓을 때마다, 수십의 몬스터가 쓰러지고 수백의 몬스터가 뒷걸음질 쳤다.

그리고 수천의 몬스터는…… 어느 순간 압도당하기 시작했다.

고작 단 한 사람의 인간을, 그가 한 자루의 창으로 나눈 사선(死線)을 두려워하고 있었다.

- 로, 로드.

어느 순간에도 흔들림이 없던 데스나이트의 고저 없는 목소리에는 이제 떨림과 굴곡이란 것이 생겼다.

수하의 간곡한 부름이 뜻하는 바가 무엇인지, 검은 기사 역시 모르는 바가 아니었다.

- 길을 터라.

깊이 눌러쓴 투구 사이, 붉은 안광이 일렁였다.

막강한 마력을 흘리며 나아가는 그는 끊임없이 떠오르는 기이한 단어와 장면들을 무시하려 애썼다.

그 어떤 것도 창조주이자 영원한 군주보다 우선 될 수는 없기에.

- 듣고 있느냐, 나의 종아.

환청처럼 울려 퍼진 군주의 목소리에, 검은 기사는 나직이 대답했다.

- 예. 군주시여.

그는 마지막까지 인식하지 못했다.

지금 자신의 손이, 갑옷 틈새 어딘가를 더듬고 있다는 사실을.
```

## Final English reading copy

```markdown
# Chapter 398

Before attempting teleportation, a thought suddenly occurred to me.

*If I calculated the past two years as a percentage, what would it be?*

What were the odds that an F-rank Hunter, trudging up a hill after getting fired from his Guild, would find an old capsule discarded at a recycling station?

What were the odds that the old capsule would be a passage connecting to another world?

What were the odds that I would begin a second life as the Third Young Master of a frontier martial family, rather than as a member of the Nangong Family or the direct Disciple of Huashan?

And after crossing one war, two massacres, and more death lines than I could count, what were the odds that I would still be alive now…?

After considering all of that, only one conclusion emerged.

“Ten percent is enough after all.”

With that quiet mutter, I reached out.

Seizing an Object Through Empty Space.

Three jiazi of internal energy pulled Team Leader Choi and Shao Shen toward me. The Death Knights and monsters tried to move, but stopped when their leader raised a hand.

Ignoring them, I checked the two men’s condition. Their breaths were faint, and their qi was so precarious it seemed ready to vanish at any moment.

If I had taken a jet instead of teleporting, I might have been too late forever.

“I would have tried even with a one-percent chance. I’m not someone who’s going to die this pointlessly.”

Of course, I had insurance prepared in case something like this happened. I never expected to use that insurance so soon, or in a situation like this.

*Open Inventory. Summon.*

I paid no attention to the monsters watching me.

The leader watched me immediately take the necessary item from my Inventory, then asked in a flat voice,

—An extradimensional space. Have you learned magic?

*Shut your fucking trap.*

I swallowed the words hovering at the tip of my tongue. Normally, that would have been quite difficult, but it was not so hard for me now.

I did not want anyone to interfere with me. At least not right now.

Pop.

When I removed the magically sealed stopper, a faint fragrance escaped. A milky liquid sloshed inside the transparent glass bottle.

A top-grade potion.

A miraculous medicine said to heal any injury as long as the patient was still breathing.

At least right now, I had no interest in the rarity or value of this small amount of liquid—barely a hundred milliliters.

I simply felt grateful for Wu Heixing’s immense wealth and stupidity as I let the top-grade potion trickle between the lips of the patient lying there as if dead.

*Bear with it a little, Shen.*

Team Leader Choi came first. Not only because of the time we had spent together, but even if we had shared no bond until now, I would still have chosen him first.

That was how serious Team Leader Choi’s injuries were.

*This is…*

His left arm had been torn away from the shoulder. His right ankle was mangled as if something had chewed and swallowed it, while his left leg had been cleanly amputated. Seven ribs were broken, and his spine was fractured.

And…

His right hand was still twisted at an unnatural angle, yet it continued to grip the hilt of his sword.

The leather strap he had fastened tightly so he would never lose hold of it was soaked through with blood.

“……”

I silently undid the strap. I pulled the sword from his right hand, whose bones had been crushed, and set it beside him.

I did not forget to offer him a reproach in my heart.

*Why did you do this? It’s a miracle you’re still alive.*

And then a genuine miracle began.

When I carefully tilted the bottle and administered exactly half of it, a sound like something burning filled the air, and the wounds covering Team Leader Choi’s entire body began to heal.

Hissssss, hissssss—

His bones grew back, severed muscles reconnected, and his organs and flesh closed together.

His recovery was even faster than a Troll’s, the very embodiment of regeneration. As Team Leader Choi’s body recovered as if time were being reversed, color finally returned to his face.

*His qi is stable, too. This is enough.*

The result was more than satisfactory to me.

It was not satisfactory to someone else watching the scene.

—Fearless human.

—Stop immediately.

—They have been given the destiny—

—of becoming subservient to our mighty Lord.

I silently looked at the two Death Knights who stepped forward in place of their leader.

Their bodies were covered in pitch-black armor, and at a glance they looked like twins. They were similar in height, and their voices were difficult to distinguish.

There was only one obvious difference between them: the weapons hanging at their waists were different.

*One has a mace. The other has a sword.*

That was already enough to provide an answer. I had solved the question, so I could write down the answer later. Right now, it was time to solve the remaining problem.

“You’ve had a rough time too, Shen.”

Shao Shen was not as severely injured as Team Leader Choi, but he had still suffered serious wounds. I was just about to pour the remaining half of the potion into his mouth when—

—Wretched human.

—This is your final warning.

—Put down those two humans, withdraw, and beg for mercy.

—Then our Lord will take you in as a servant.

“A servant?”

—That is correct.

Along with the emotionless, flat voice, one of the Death Knights stepped toward me. The scabbard fixed to his waist swayed with every step.

Clank. Clank. Clank.

One step. Two steps. Three steps.

There was not even a hint of hesitation in the creature approaching me.

Thousands of monsters and their leader were watching.

The Death Knight spoke in a confident tone so strong that it was hard to believe he was an undead monster without emotions.

—You possess a truly great and radiant soul. Become one of us.

A great and radiant soul…

Without even raising my head, I continued pouring in the potion.

After emptying the last few drops into Shao Shen’s mouth, I closed the bottle and put it back in my Inventory.

Hissssss, hissssss.

A signal that recovery had begun.

I straightened up at the welcome sound I had been waiting for. Looking at the Death Knight, I said what I had wanted to say for some time.

“His left leg.”

—Hm?

“Team Leader Choi’s left leg. It was empty from a handspan below the knee. Completely clean. Shao Shen—the young one’s was his right arm.”

—Human. What are you trying to say?

“What am I trying to say?”

I gave him a faint smile.

“If you cut off limbs that were perfectly attached, you should be prepared for the consequences.”

And then, in the next moment—

Time was split in half, then split again within that divided instant, and before I knew it, the creature had arrived right in front of my nose.

No.

It was the opposite.

It had not come to me.

I had gone to it.

“Let’s see that vaunted skill of yours.”

—……!

Everything happened in an instant. The Death Knight tried to draw his sword, and I reached out with my left hand and pressed down firmly on the back of his hand.

That was both the beginning and the end.

Shing. Click!

The dark-gray blade had barely begun to emerge before it slid back into its scabbard—but by then, my fist had already punched through the creature’s chest.

Crunch!

The Flame-Extinguishing Divine Fist, charged with the Scorching Yang Qi of three jiazi, vaporized even the fistful of blood remaining inside the undead monster and blazed up using its long-dead body as kindling.

Whoosh! KRAAAASH!

Engulfed in inextinguishable flames, the Death Knight waved its hands and turned toward its kin.

It staggered along the path it had walked so confidently, then collapsed into ash.

—……!

—……!

Even with thousands of monsters gathered together, the silence was absolute, as if someone had pressed a mute button.

I took White Flame from my Inventory and began walking slowly.

Splash. Splash.

Everywhere my gaze fell, and everywhere my feet stepped, there were corpses and blood.

Countless rifles kept catching against my feet, while a soldier wearing a crooked helmet stared up at the sky with eyes from which life had already departed.

At least that soldier’s corpse was still intact.

In what appeared to have been the fiercest battlefield, people who seemed to be Hunters from the Public Security Armed Forces Department lay dead in mangled conditions.

I had spent a full week with the 1st Regiment led by Shao Shen. Among the corpses were many familiar faces.

*So many people died. So many.*

At least three thousand humans had died here today alone.

If all five fronts were combined, and the civilians killed in this monster wave were included, how many victims would there be?

Thud!

I borrowed the spear of an unknown Hunter and drove it deep into the ground. The leather strap belonging to Team Leader Choi, tied securely to the end of the shaft, fluttered in the wind.

Beyond it stood an army of thousands of monsters—and *him.*

> **System**
>
> Lv. 135 Death Knight Lord

Death Knight Lord. What an imposing name.

It was also a monster with enough power to match that grand name.

*The circumstances are different, but there is another one like him.*

I called out to the one who had maintained the longest silence in history.

“Let me ask you for one favor.”

I thought he might pretend not to hear me, but after a brief hesitation, the Skeleton Warlord answered.

—……A favor? You’re not asking me to fight alongside you, are you?

“Of course not.”

I had never expected that, nor did I expect it now. The favor I wanted to ask had nothing to do with fighting.

It was about protecting someone.

“Protect the two people behind me. No matter what it takes.”

With my permission, the Skeleton Warlord had been absorbing death qi whenever there was an opportunity, and had consequently grown stronger.

As a Named Monster, it should have been able to handle several ordinary A-rank monsters by itself.

“When the battle is over, I’ll grant you any wish.”

—In that case, there’s nothing I can’t do. But how long am I supposed to protect them?

“That should be obvious…”

I raised White Flame and aimed it at the Death Knight Lord.

“Until every last one of those bastards is dead.”

—You insane—

“You’re too late.”

I pulled the Skeleton Warlord’s skull from my Inventory and threw it behind me.

Crack. Pop.

While it hurriedly regenerated its body, I stroked the leather strap fluttering from the spear shaft.

How had he—how had they—felt?

What had they been thinking as they charged toward death? I could not even begin to guess.

There was only one thing I could be certain of now.

“Any bastard who comes past this spear is going to fucking die.”

The fire dragon coiled within my dantian raised its head.

* * *

CRUNCH!

Flesh and bone shattered and flew in every direction.

An ogre’s limbs were sent flying, while a Troll was engulfed in inextinguishable flames before it had a chance to regenerate.

Boom! Slash!

The head of a Lycanthrope that had bared its fangs exploded.

A Dullahan came charging at me, covered in foul-smelling brain matter, only to be cleaved in two with a single blow. The halberd, having found a new master, flew away with tremendous force and tore through a Wyvern’s wing.

CRACKLE!

—Kyaaaaaaa!

Thud-thud-thud!

A rain of blood scattered through the air.

At the same time, a streak of blue flame came flying through the rain.

Whoooooosh! Slash!

A storm of blood erupted. Whenever the flames embroidered the air, dozens of monsters fell and hundreds of monsters stepped backward.

And the thousands of monsters…

At some point, they began to be overwhelmed.

They were afraid of the death line carved by a single human with a single spear.

—L-Lord.

The flat voice of the Death Knight, which had never wavered, now contained tremors and inflection.

The black knight knew perfectly well what his subordinate’s desperate call meant.

—Make way.

Between the slits of the deeply lowered helmet, red eyes flickered.

As he advanced, leaking immense magical power, he tried to ignore the strange words and scenes that kept surfacing in his mind.

Nothing could take precedence over his creator, his eternal lord.

—Are you listening, my servant?

At the voice of his lord echoing like a hallucination, the black knight quietly replied,

—Yes, my lord.

He failed to realize it until the very end.

That his hand was groping somewhere between the plates of his armor.
```
