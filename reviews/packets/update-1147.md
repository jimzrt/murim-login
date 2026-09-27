<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1147.txt",
      "sha256": "a860137d87d99d3dc2b8e195501d88c27db2a1e570d575b45398a0d33313e7c6",
      "bytes": 11461
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7510dd5439f09e88e1be0f70399cd1f20d3f0ad494b37a3c635618cfb276c994",
      "bytes": 1659
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "590e227f6652008e661a5c9624697025c1d16f377a5ff81370b8d975e672de8e",
      "bytes": 246053
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "268dfca04eaed14c41559626c61d48a70039b0f0a264014e66ca8d3ab91a3693",
      "bytes": 1672
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "dd0974cf6878370d94f5350a4780ff06b5d115fcee1abeb7ec731360fe23718e",
      "bytes": 623
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "bc30ed5d8baf6a79a9ceff36b51db6b62dfbfab2a4af5023c9556dd5a72e1248",
      "bytes": 703
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c82f263de10dd0958ded0f894f7dba84829301622e9b030e0155b6ec412754d7",
      "bytes": 291579
    }
  ],
  "estimated_tokens": 8542
}
-->

# Durable State Update — Chapter 1147

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1147. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1147. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1147,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1147,
    "continuity_sources": [1147],
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
    "Taekyung’s consciousness is in the realm of immortals while his body sleeps in Murim; he promised Jeok Cheongang he would return.",
    "Jeok Cheongang remains beside Taekyung and intends to protect him on the march to Tianshan.",
    "The coalition army of more than two hundred thousand is crossing the Taklamakan Desert toward Tianshan.",
    "The Grand Mage has been reborn through the Lord of Heaven’s grace and felt a wave; the Lord says the heavens have opened again, as green light rises over jade.",
    "Choi Minwoo commands Hunters sheltering underground in the desert; thousands of enemies are approaching, and he has chosen to lead the group into battle.",
    "The Skeleton King is with Choi Minwoo’s group, whose Hunters are ready to follow his command."
  ],
  "continuity_sources": [
    1145,
    1146
  ],
  "open_questions": [
    "What caused the wave that the Grand Mage felt and the Lord of Heaven acknowledged?",
    "What does the Lord of Heaven mean when he says the heavens have opened again?",
    "What danger awaits the coalition army at Tianshan?",
    "Who are the thousands of enemies approaching Choi Minwoo’s shelter, and what are they pursuing?",
    "Who speaks the unexpected line, “Dad’s not sleeping”?"
  ],
  "safe_through": 1146,
  "temporary_decisions": [
    "Render 仙界 as “realm of immortals.”",
    "Render 塔克拉玛干 as “Taklamakan Desert.”",
    "Render 汗血寶馬 as “sweat-blood horse.”",
    "Render 時辰 as “shichen.”",
    "Render 스켈레톤 킹 as “Skeleton King” and 방공호 as “bomb shelter.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 절정     | **Peak**          |
| 절정고수                | **Peak master** / **Peak martial artist** |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 만티코어 | **Manticore** | A-Rank Gate monster and original raid target. |
| 오크 | **Orc** | Monster species. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 구울 | **Ghoul** | Undead monster species. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 골검 | **Bone Sword** | Sword wielded by the Skeleton Knights. |
| 황하 | **Yellow River** | River along which civilization began. |
| 이족 | **Yi people** | One of Nanman's four great tribes. |
| 리자드 | **Charmeleon** | Game-monster comparison. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 최민우 | 진태경 | trusted allied team leader to younger allied Hunter | Mr. Jin | formal-polite and concerned | Choi warns Jin about the danger of the operation and affirms his deep trust. |
| 진태경 | 최민우 | younger allied Hunter to allied team leader | Team Leader Choi | polite, familiar, and teasing | Jin jokes with Choi while acknowledging and dismissing his concern. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1146
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, and the Son of Heaven has formally enfeoffed him as Prince Shangshan.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1146
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 1146
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader Choi is Jin Taekyung's meticulous intelligence and operations lead, a trusted ally and natural leader capable of guiding the reestablished World Hunter Federation.
- **Personality:** Calm, pragmatic, meticulous, and resolute under pressure.
- **Voice:** Measured, professional, and reassuring without minimizing responsibility.
- **Relationships:** A trusted ally and operational adviser to Jin Taekyung, whom he regards as a model of taking responsibility in a crisis; he is the maternal grandson of Cheon Taemin.

## Korean source

```text
＃1147화



찰나를 쪼개고 쪼갠 그 짧은 순간, 스켈레톤 킹은 생각했다.

‘요새 몸이 허한가.’

그래, 잘못 들은 것이 분명했다.

원래 인간이란 동물은-엄밀히 따지면 그는 인간도 아니고 동물은 더더욱 아니지만- 심신이 약해지면 종종 환청을 듣는 경우가 있다고 하지 않나.

더군다나 지금은 무려 열 배가 넘는 적과 전투를 벌여야 하는 상황.

이렇듯 고양이의 앞발이라도 빌려야 하는 악조건 속에서 환청이 들리는 건 결코 이상한 일이 아니었다.

그놈.

아니, 진태경은 그에게 있어 세상 그 누구보다 믿음직한 존재였으니까.

하지만…….

‘녀석이 깨어났을 리 없지.’

전부 헛된 희망이다.

이 낡고 냄새나는 지하 방공호로 오기까지 수많은 위기가 있었지만, 그럴 때마다 진태경의 눈꺼풀은 미동도 없이 굳게 닫혀 있었다.

어쩌면 이대로 영영 깨어나지 못하는 게 아닌가 하는 걱정이 들 정도로.

‘빌어먹을 인간 같으니라고.’

스켈레톤 킹이 내심 씁쓸하게 읊조린 그때였다.

슈확!

날카로운 파공성과 함께, 잠시 멈춰 있던 시간의 흐름이 급류가 되어 밀려온 것은.

콰아아앙!

공간을 뒤흔드는 강렬한 충격.

허공을 가로지르며 날아든 십여 줄기의 섬광을 상쇄시킨 스켈레톤 킹의 눈빛이 무겁게 가라앉았다.

‘이건.’

틀림없다.

평범한 몬스터와는 궤를 달리하는 속도와 힘.

어느덧 그의 손아귀에서 부르르 떨고 있는 골검(骨劍)이, 저 수천의 괴물들 사이에 ‘그놈들’이 포함되어 있음을 알려주고 있었다.

더는 돌이킬 수 없는 이 전투가, 예상했던 것 이상으로 힘들어지리라는 사실도 함께.

“제기랄, 놈들이다!”

“전원, 수비 대형으로 전환!”

판단도, 실행도 빨랐다.

지금 이 자리에 있는 헌터들은 누구 하나 빠짐없이 뛰어난 실력과 적잖은 실전 경험을 갖춘 베테랑들.

거의 동시에 터져 나온 스켈레톤 킹과 최민우의 고함에, 지휘관을 따라 돌격하던 헌터들은 한 치의 망설임이나 동요도 없이 명령에 따라 움직였다.

정확히는, 누군가의 나지막한 음성이 그들의 발목을 붙잡기 전까지는 그랬다.

“공격 대형 유지.”

“……?”

“……?”

일순간, 수비 대형으로 태세를 전환하던 헌터들이 당황 섞인 눈빛으로 서로를 바라봤다.

첫 번째로는 갑작스럽게 뒤바뀐 명령 때문에.

두 번째로는 이 자리의 유일한 명령권자라 할 수 있는 최민우조차 그들과 비슷한, 아니 더욱 괴상한 표정을 짓고 있어서.

그리고 마지막 세 번째 이유.

‘어디선가 들어 본 목소린데?’

분명히 들어 봤다.

낯설게 느껴지면서도, 귀에 착 하고 달라붙는 듯한 저 음성.

비록 깊게 잠기고 갈라져 있을지언정, 쉬이 사라지지 않은 이 익숙한 느낌.

아마도 그래서였을 것이다.

이미 전투라면 이골이 난 베테랑 헌터들이 동요를 숨기지 못한 것도.

그로 인해 눈앞의 적들에게 치명적인 빈틈을 드러낸 것도.

- 그워어어어어!

거대한 괴성과 함께 파도가 되어 밀려드는 수천의 괴물들.

구울이, 오크가, 리자드맨과 만티코어가 강철도 종잇장처럼 찢어버리는 발톱과 무기를 휘둘렀다.

그리고.

쉬잉.

그 흉험한 괴물들을 향해 나아가는, 눈부신 섬광이 있었다.

퍼어어어엉!

수백, 수천 개의 조각으로 나뉘어 폭발하는 살과 뼈.

동시에 무수한 단말마와 함께 터져 나오는 청록색 핏물들.

삽시간에 사방을 휘감은 짙은 피 안개 속, 그 믿을 수 없는 광경을 목격한 사람들은 그제야 불현듯 깨달았다.

조금 전 들려온 명령이 누구의 것이었는지.

온통 잠기고 갈라진 그 목소리가, 어째서 그토록 익숙하게 느껴졌는지.

“야.”

석상처럼 굳어 버린 스켈레톤 킹의 어깨너머, 어느덧 그가 짊어지고 있던 배낭 속에서 불쑥 얼굴을 내민 청년이 말을 이었다.

“너 일부러 못 들은 척했지.”

“……!”

“……!”



* * *



솔직히, 처음에는 꿈을 꾸고 있는 줄 알았다.

아직 태어나지도 않았던, 엄마 배 속에서 열심히 꼼지락거리고 있던 그 시절의 꿈을.

그도 그럴 것이, 세상 그 어떤 인간이 잠들어 있는 사람을 곱게 접어 통째로 대형 배낭에 쑤셔 박았을 거라고 생각할 수 있겠나.

심지어 그 질기다는 오우거 힘줄로 일본의 어느 영상물에서나 보던 귀갑 묶기를 해놓은 걸 보니, 미쳐도 보통 미친놈이 아니었다.

물론, 그 미친놈이 누구인지는 뻔했지만.

“이 새끼는 취향이 도대체…… 아니다, 나중에 다시 얘기하자.”

“너, 너……!”

귀신이라도 본 듯한 얼굴로 어버버거리는 스켈레톤 킹을 뒤로한 채, 나는 뻐근한 육신에 힘을 불어넣었다.

투두둑.

전신을 속박하고 있던 오우거의 힘줄을 실타래처럼 끊어내고, 그만큼 질긴 가죽으로 만들어진 배낭을 찢고 두 발로 서자 비로소 숨통이 트이는 기분이다.

‘도대체 이 상태로 얼마나 있었던 거지?’

당장이라도 묻고 싶은 질문들이 혀끝에 줄지어 서 있는 상황.

하지만 그럴 만큼 한가한 때가 아니라는 것쯤은, 나 역시 잘 알고 있다.

의식을 되찾은 순간부터 지금까지, 온 사방에 들끓는 악취와 농도 짙은 마력에 속이 메슥거릴 정도였으니.

“팀장님.”

가볍게 고개를 끄덕이는 것으로 인사를 대신하자, 만감이 교차하는 표정으로 나를 바라보던 최 팀장이 참았던 숨을 토해 냈다.

“전원, 공격 대형 갖춰.”

그 순간, 주위의 공기가 들끓었다.

오랜만에 마주한 스켈레톤 킹과 최 팀장. 더불어 여러 인종이 뒤섞인 이백여 명의 헌터가 열기 띤 눈으로 각자의 무기를 곧추세우며 각자의 위치에 섰다.

마치 하나의 화살처럼.

그리고 이 화살이 나아가는 방향은, 이미 정해져 있다.

콰드드득, 탁!

처음 나아갔을 때와 같이, 수십여 마리의 몬스터를 관통하며 되돌아온 백염(白炎)이 손아귀 안에서 부르르 몸을 떨었다.

마치, 앞으로 펼쳐질 일을 직감하듯이.

“가자.”

그 한 마디가 전부였다.

더할 것도, 뺄 것도 없었다.

생각이 소리가 되고, 소리가 입술 밖으로 새어 나온 그 순간 나는 이미 적들을 향해 쇄도하고 있었으니까.

팟.

단 한 걸음.

이십여 미터의 거리를 단숨에 좁힌 나는 망설임 없이 백염을 내리그었다.

화아아악!

어느덧 창날에 깃든 군청색의 화염 앞에 공간이 일그러진다.

끔찍하리만치 강한 열기가 괴물들을 집어삼키고, 용암 지대처럼 달궈진 지면 틈새로 크고 작은 불기둥이 솟구쳤다.

콰아아앙!

폭발과 굉음. 동시에 곳곳에서 터져 나오는 비명.

하지만 그 거대한 충격파와 혼란 속에서도 나는 아랑곳하지 않았다.

아니, 정확히는 나를 비롯한 아군 모두가 그랬다.

쉬쉬쉬쉭!

흩날리는 불씨와 형체조차 제대로 남기지 못한 살 조각들.

그 모든 것들을 뒤로한 채 바람처럼 돌격한 이백여 명의 헌터는 말 그대로 적들을 찢어발겼다.

나조차도 미처 예상치 못한, 실로 놀라운 무력으로.

쉬이이잉!

찰나의 순간, 무수한 섬광이 동공을 휘황하게 물들인다.

그리고 그와 동시에 대물 저격 소총으로도 관통할 수 없다는 오우거의 가죽이, 만티코어의 꼬리가 두부처럼 갈라져 사방으로 비산했다.

서걱, 푸화아악!

짙은 피 분수와 함께 산산이 허물어지는 몬스터들의 포위 대형.

그 중심에서 형형하게 빛나고 있는 헌터들의 무기에는, 내가 잘 알고 있는 강력한 힘이 깃들어 있었다.

‘오러(Auror)?’

나도 모르게 눈이 크게 뜨였다.

틀림없다.

오러, 혹은 검기(劍氣)라고도 불리는 것.

현대에서는 A급 헌터의 상징이자, 무림에서는 절정고수의 전유물로 통용되는 그것이 저들의 무기를 타고 흐르고 있었다.

심지어는 열도, 스물도 아닌 이백여 명 전원이.

‘이 정도 숫자의 A급 헌터가 왜 이곳에 모여 있는 거지? 분명 내 마지막 위치는 가장 가까운 아군과 비교해도 천 킬로미터 이상 떨어져 있었을 텐데.’

도대체 그간 무슨 일이 있었던 걸까.

현대에서의 기억을 떠올려 보았지만, 지금의 나로서는 이 상황을 이해하기란 쉽지 않았다.

아니.

당장 눈앞의 현실을 이해하기도 전에 나타난 또 다른 변수가 내 사고를 방해했다.

스아아악.

불현듯 귓가로 들려온, 소름 끼치도록 낮은 파공성.

동시에 뇌보다 먼저 반응한 몸이 움직이고, 그에 따라 잠시 멈춰있던 백염의 창날이 내리그어졌다.

서걱, 콰아아앙!

모든 것이 찰나였다.

내가 초승달 형태로 날아든 마력의 덩어리를 베어 낸 것도.

그 끈적하고 차가운 기운의 집약체가 좌우의 몬스터들을 집어삼킨 것도.

그리고.

철벅.

청록색 피 웅덩이를 밟으며 모습을 드러낸, 일단의 무리가 내 시야에 들어온 것도.

“……뭐지?”

본능적으로 불쑥 튀어나온 물음에, 어느새 양옆으로 다가온 최 팀장과 스켈레톤 킹이 대답했다.

“놈들이군요.”

“조심해라. 인간. 네가 알고 있던 몬스터들이랑은 궤가 달라.”

나는 대답 대신 불청객들을 바라보았다.

숫자는 일곱.

외형은…… 인간과 닮았다.

그나마 이족보행을 하는 덕분에 인간형 몬스터라고 불리는 리자드맨조차 비교할 수 없을 만큼.

하지만 결코 인간은 아니었다.

비단 이 미터를 훌쩍 웃도는 신장과 터질 듯한 근육 때문만은 아니다.

공장에서 찍어 낸 것처럼 한 치의 오차도 없이 똑같은 키와 체격을 지니고 있었기 때문만도 아니다.

‘이건, 도대체 무슨 기운이지?’

인간의 것이라 하기에는 너무 짙고, 몬스터의 것이라 하기에는 너무나도 순수한 마력(魔力).

스켈레톤 킹의 말이 맞았다.

놈들은 하나하나가 네임드 몬스터에 비견될 수 있을 만큼 강한 동시에, 지금껏 내가 마주한 그 어떤 몬스터와도 비교할 수 없는 순도 깊은 마력을 지니고 있었다.

마치, 조금의 결점도 없는 유전자를 갖고 태어난 생명처럼.

하지만…….

“그래, 확실히 다르긴 하네.”

조금 전 스켈레톤 킹이 했던 말이, 전부 옳았던 것은 아니다.

저벅.

궤가 다른 것은 놈들뿐만이 아니었으니까.

조심해야 할 대상이 누구인지도.

서걱.

이 자리의 그 누구도 보지도, 느끼지도 못한 그 순간 움직인 나는 창날을 타고 전해지는 감촉을 느끼며 마음속으로 속삭였다.

이제 남은 숫자는, 여섯.
```

## Final English reading copy

```markdown
# Chapter 1147

In that brief moment, split into a thousand smaller moments, the Skeleton King thought:

*Have I been feeling a little weak lately?*

Yes. He must have heard wrong.

They said that humans—strictly speaking, he wasn’t human, and certainly not an animal—sometimes heard things that weren’t there when their bodies and minds were weak.

Besides, he was about to fight enemies who outnumbered them by more than ten to one.

With the odds so bad he’d take help from a cat if he could get it, hearing things wasn’t strange at all.

That guy—

No, Jin Taekyung was the most reliable person in the world to him.

But…

*There’s no way he’s woken up.*

It was all wishful thinking.

They’d faced countless dangers on the way to this old, musty underground bomb shelter, but every time, Jin Taekyung’s eyelids had stayed firmly shut without so much as a twitch.

The Skeleton King had even begun to worry that he might never wake up at all.

*That damn human.*

As the Skeleton King thought bitterly to himself, it happened.

Whoosh!

With a sharp whistle, the flow of time—which had briefly stopped—came rushing back like a flood.

KABOOM!

A powerful impact shook the space around them.

The Skeleton King’s eyes grew heavy as he canceled out a dozen or so streaks of light flying through the air.

*This is…*

There was no mistaking it.

Speed and strength on a level entirely different from ordinary monsters.

The Bone Sword trembling in his grasp told him that *those guys* were among the thousands of monsters.

It also told him this battle, now past the point of no return, would be even harder than expected.

“Shit, it’s them!”

“Everyone, switch to a defensive formation!”

They were quick to judge, and quick to act.

Every Hunter here was a skilled veteran with plenty of combat experience.

At the almost simultaneous shouts from the Skeleton King and Choi Minwoo, the Hunters charging behind their commander moved at once, without the slightest hesitation or sign of panic.

Or they did—right up until a low voice stopped them in their tracks.

“Maintain the attack formation.”

“……?”

“……?”

The Hunters, midway through switching to a defensive formation, looked at one another in confusion.

First, because the order had suddenly changed.

Second, because Choi Minwoo—the only one there with the authority to give orders—looked just as strange as they did. Stranger, even.

And third—

*I’ve heard that voice somewhere before.*

He definitely had.

It sounded unfamiliar, yet somehow it stuck with him the moment he heard it.

Though low and hoarse, it carried a feeling that wouldn’t fade.

Perhaps that was why the veteran Hunters, all of them battle-hardened, couldn’t hide their dismay.

And why they left a fatal opening for the enemies right in front of them.

—Grrrrrrrr!

Thousands of monsters surged toward them like a wave, roaring.

Ghouls, Orcs, Lizardmen, and Manticores swung claws and weapons that could tear through steel like paper.

And then—

Whoosh.

A dazzling streak of light shot toward the fearsome monsters.

BOOM!

Flesh and bone exploded into hundreds, then thousands of pieces.

At the same time, countless dying screams burst out alongside sprays of blue-green blood.

In the thick mist of blood that wrapped around them in an instant, those who witnessed the unbelievable scene suddenly understood.

Who had given the order they’d just heard.

Why that low, hoarse voice had felt so familiar.

“Hey.”

Over the Skeleton King’s shoulder, rigid as a statue, a young man suddenly poked his head out of the backpack he’d been carrying.

“You were pretending not to hear me on purpose, weren’t you?”

“……!”

“……!”

* * *

Honestly, at first I thought I was dreaming.

Dreaming of a time before I was even born, when I was busy kicking around in Mom’s belly.

I mean, what kind of person would neatly fold up someone who was asleep and shove them into a huge backpack?

And they’d used those famously tough ogre tendons to tie me up in a turtle-shell pattern like something out of a certain kind of Japanese video. Whoever did this wasn’t just crazy.

Of course, I knew exactly who that lunatic was.

“This guy’s tastes are seriously… No, let’s talk about that later.”

“You, you…!”

Leaving the Skeleton King behind as he stammered, his face like he’d seen a ghost, I put strength back into my stiff body.

Crack, crack.

I snapped the ogre tendons binding me from head to toe like strands of thread, tore through the backpack made of equally tough hide, and stood on my own two feet. Only then could I finally breathe freely.

*How long was I like that?*

Questions lined up at the tip of my tongue, each one demanding an answer.

But I knew it wasn’t the time to ask.

From the moment I regained consciousness until now, the stench boiling all around me and the thick magical power had been enough to make me nauseous.

“Team Leader.”

I gave a slight nod in greeting. Team Leader Choi, looking like he was overwhelmed by a dozen different emotions, finally let out the breath he’d been holding.

“Everyone, form up for an attack.”

At once, the air around us began to boil.

The Skeleton King and Team Leader Choi, whom I hadn’t seen in ages. Along with them, more than two hundred Hunters of various races raised their weapons, eyes alight, and took their places.

Like a single arrow.

And the direction it would fly was already decided.

CRUNCH, clack!

Just as when it first charged out, White Flame returned after piercing through dozens of monsters, trembling in my grasp.

As if it sensed what was about to come.

“Let’s go.”

That was all I said.

Nothing more, nothing less.

The thought became a sound, the sound slipped past my lips—and in that instant, I was already charging at the enemies.

Whoosh.

One step.

I closed the twenty-meter gap in an instant and brought White Flame down without hesitation.

Fwoosh!

Space warped before the deep-blue flames now burning along the spearhead.

Heat so intense it was horrifying swallowed the monsters, and pillars of fire erupted from cracks in the ground, heated like a field of lava.

KABOOM!

Explosions and thunderous noise. Screams burst out from all around.

But I paid no attention to the massive shock wave or the chaos.

No—more accurately, none of my allies did.

Whoosh, whoosh, whoosh!

Flying sparks and pieces of flesh too mangled to make out.

Leaving them behind, more than two hundred Hunters charged like the wind and tore through the enemy ranks.

With a level of force even I hadn’t expected.

Whoooooosh!

In a split second, countless streaks of light dazzled my eyes.

And at the same time, ogre hide—said to be impenetrable even to an anti-materiel sniper rifle—and Manticore tails split apart like tofu, scattering in every direction.

Slash, splatter!

The monsters’ encirclement crumbled amid fountains of dark blood.

The Hunters’ weapons shone fiercely at its center, charged with a power I knew well.

*Auror?*

My eyes widened despite myself.

There was no mistaking it.

Auror, also known as Sword Energy.

A hallmark of A-rank Hunters in the modern world, and the exclusive domain of Peak masters in Murim, it flowed through their weapons.

Not just ten or twenty of them. Every one of the two hundred or so Hunters.

*Why are there this many A-rank Hunters gathered here? The last place I remember being was more than a thousand kilometers from even the nearest ally.*

What on earth had happened while I was gone?

I tried to recall what I knew of the modern world, but it was hard to make sense of the situation.

No.

Before I could even begin to understand the reality in front of me, another unexpected factor got in the way.

Ssssh.

A chillingly low whistle suddenly reached my ears.

My body reacted before my brain. White Flame, which had paused for only an instant, swung down.

Slash, KABOOM!

Everything happened in a flash.

I cut through a crescent-shaped mass of magical power as it flew toward me.

The sticky, cold force at its core swallowed the monsters to either side.

And then—

Splash.

A group appeared in my sight, stepping through a puddle of blue-green blood.

“……What are they?”

Team Leader Choi and the Skeleton King, who had moved up beside me, answered the question that had slipped out on instinct.

“It’s them.”

“Be careful, human. They’re nothing like the monsters you know.”

I looked at the uninvited guests instead of answering.

There were seven of them.

Their appearance was… similar to humans.

More so than even Lizardmen, who at least walked on two legs and could be called humanoid monsters.

But they weren’t human. Not even close.

It wasn’t just their height, well over two meters, or their bulging muscles.

It wasn’t even that they were all exactly alike, with identical height and builds, as though they’d come off the same production line.

*What is that energy?*

Magical power too dense to be human, yet far too pure to be a monster’s.

The Skeleton King had been right.

Each of them was as strong as a named monster, and their magical power was purer than that of any monster I’d ever encountered.

Like beings born with genes entirely free of flaws.

But…

“Yeah. They’re definitely different.”

What the Skeleton King had said a moment ago wasn’t entirely right.

Step.

They weren’t the only ones on a different level.

And they’d picked the wrong person to warn.

Slash.

I moved in that instant—when not a single person there could see or sense me—and felt the touch of the spearhead as it passed through.

*Six left.*
```
