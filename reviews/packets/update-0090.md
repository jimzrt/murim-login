<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0090.txt",
      "sha256": "a9f06b72a7ee2eac434b6bf1cd8d988897cdc365eb9ac4956c5a26585cae9093",
      "bytes": 13646
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8d2af4898ff97f34d1c75b0223fd4ee24fd774da0cc74852ad1ee5ed7c5d12e2",
      "bytes": 2784
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "32808031228f5fd091a75e09ae4051d5afac26707f63b260eb1b40e147922414",
      "bytes": 9119
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ada4a963175a406171b207f58625830e40494272bba2b947c2a73bb7841341fa",
      "bytes": 23901
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "334d95f2ae293161b33046e81394daf7e57f598c975f6b3fcd5174222f1370d5",
      "bytes": 3852
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3d15e3b8de5f08c000f2818c9bb5d688bf4b0147c84ee2edafc8cc59a97c16ff",
      "bytes": 8689
    }
  ],
  "estimated_tokens": 13329
}
-->

# Durable State Update — Chapter 90

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 90. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 90. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 90,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 90,
    "continuity_sources": [90],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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
    "The party sells The Minotaur's Labyrinth byproducts and Magic Gems to the Administration.",
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild.",
    "Im Chunsoo is Sangdong Guild's A-rank Guild Master and founder, known as Frozen for his exceptional ice magic.",
    "Im Chunsoo learned that Changsoo transferred 8 billion won to two accounts, fired him, and began beating him with an ice club.",
    "Sangdong Guild's Team One Leader brought Changsoo to Im Chunsoo's office, which was closed to visitors for half a day.",
    "Im Changsoo transferred the promised four billion won to Jin Taekyung.",
    "Hayeon knows that Kim Jeonghee was secretly working at a restaurant and asked Taekyung not to find her.",
    "Kim Jeonghee is Taekyung and Hayeon's fifty-year-old mother and had worked in a restaurant kitchen for over a year.",
    "Taekyung's father died when a Gate opened downtown during the Great Cataclysm.",
    "Kim Jeonghee defended Taekyung against the restaurant owner's insults and curses.",
    "Taekyung arrived at the restaurant and called Kim Jeonghee Mom.",
    "Kim Jeonghee quit her restaurant kitchen job after the owner insulted and attacked Taekyung, then left with him.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Jin Taekyung is a C-rank Hunter rather than the F-rank Hunter the restaurant owner believed him to be; Im Changsoo confirmed Taekyung received four billion won.",
    "Taekyung can use the Jin Family's Cultivation Technique to perform Circulate Qi for Healing on other people.",
    "Hayeon and Kim Jeonghee recovered substantially after receiving Circulate Qi for Healing from Taekyung.",
    "Taekyung's reality and Murim Inventories are separate.",
    "Hayeon learned that Taekyung earned four billion won from the previous day's raid and asked whether she could drop out of school."
  ],
  "continuity_sources": [
    89
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved.",
    "Whether Hayeon will actually drop out of school remains unresolved."
  ],
  "safe_through": 89,
  "temporary_decisions": [
    "Use Frozen for 프로즌 and preserve the tiger-father/dog-son wordplay in 호부견자.",
    "Use ajumma for 아줌마 with an explanatory footnote.",
    "Retain goshiwon with an explanatory footnote.",
    "Use Minsu for 민수 as the short form of Kim Minsu.",
    "Render 운기요상 as Circulate Qi for Healing.",
    "Render 하급 포션 as Lesser Potion."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 임창수    | **Im Changsoo**   |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 88
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 85
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Former Ares Guild Team Leader; reawakened Hunter publicly classified as C-rank; leader and employer of Team 1, the Peace Guild’s E-rank Gate party
- **Personality:** Calm, observant, practical, and decisive under pressure
- **Voice:** Polite and measured in ordinary conversation; clipped and commanding during combat
- **Relationships:** Hires Jin Taekyung as a porter and leads him, Im Kkeokjeong, and three veteran E-rank Hunters through an E-rank Gate

## Korean source

```text
＃90화



“일주일 동안 휴가요?”

- 네. 들으신 그대롭니다.

그날 저녁에 걸려 온 최 팀장의 전화는 뜻밖이었다.

일주일이나 휴가라니. 길드에 무슨 문제라도 생겼나?

생각이 거기까지 미치자 문득 걸리는 사실이 있었다.

“저, 혹시 상동 길드랑 트러블이 생긴 건 아니죠?”

- 상동 길드요?

“아니 왜, 임창수 문제 때문에…….”

- 아, 그 문제는 신경 쓰지 않으셔도 됩니다. 길드 하우스 리모델링이 일주일 뒤에 끝난다고 해서요.

아무 일 없다니 다행이긴 한데. 길드 하우스 리모델링 때문에 레이드를 쉬는 경우도 있나?

‘일주일이나 쉰다니까 좋긴 한데.’

지난 7년간 앞만 보고 달려온 인생. 요즘 들어서는 무림과 현실까지 오가며 쉴 틈 없는 나날을 보내왔다.

솔직히 쉬고 싶…… 아니다. 이럴 때일수록 더욱 힘내서 일을 해야 한다. 나는 의지에 찬 목소리로 말했다.

“팀장님. 전 일하고 싶습니다.”

- 아, 휴가지만 급여는 정상적으로 나갈 겁니다.

“그럼 일주일 뒤에 뵙죠.”

- …….

“끊을게요. 저녁 먹으러 가야 해서.”

- ……네.

전화를 끊자 하연이가 종종걸음으로 다가와 공손히 고개를 숙였다.

“오라버니. 저녁 식사가 준비되었사옵니다.”

“……그 말투 소름 돋으니까 그만해 줄래?”

“반말 모드로 전환하려면 유료 결제가 필요하옵니다.”

“용돈 달라는 소리를 어렵게도 한다.”

신사임당 두 장을 내밀자 하연이가 씩 웃는다.

“엄마가 저녁 먹으래.”

“오, 메뉴 뭔데.”

“소불고기. 그리고 내가 끓인 콩나물국.”

“소불고기 맛있겠다.”

“콩나물국 맛있대. 엄마한테 칭찬받았어.”

“엄마표 소불고기는 배신하는 법이 없지. 늘 새로워, 최고야, 짜릿해.”

“…….”

잔뜩 열받은 여동생과 한 상 가득 차려진 엄마표 요리.

휴가가 별거냐. 집에서 실컷 먹고 자야겠다.



* * *



탁.

최민우는 전화가 끊긴 스마트폰을 내려놨다. 테이블을 가운데에 두고 앉아 있던 김 집사가 묻는다.

“뭐라고 하던가요?”

“안 그래도 걱정하고 있더군요. 상동 길드에 대해서.”

“보면 볼수록 재미있는 청년입니다. 생각 없이 행동하는 것 같으면서도 상황 파악이 빨라요.”

최민우는 길쭉한 손가락으로 테이블을 두드렸다.

갑자기 등장한 진태경의 존재는 시간이 좀 지난 지금도 여전히 수수께끼다.

처음 만났을 때는 성실한 F급 헌터 그 이상도 이하도 아니었던 그가, 어제는 혼자서 B급 게이트를 쓸어 버렸다.

‘점점 강해지고 있어.’

어제부로 의심이 확신으로 바뀌었다.

진태경은 점점 강해지고 있다. 그것도 매우 빠르게!

“진태경 씨 관련해서는 추가 정보가 없습니까?”

“예, 재확인을 거듭했지만 아무것도 나오지 않습니다.”

김 집사는 일 처리가 확실한 인물이다. 하지만 이번만큼은 경우가 다르다. 최민우는 신중하게 입을 뗐다.

“김 집사님.”

“예, 도련님.”

“혹시…… 3차 각성자의 사례를 찾아볼 수 있겠습니까?”

“네?”

김 집사의 눈썹이 움찔했다.

3차 각성자라니. 일평생 듣도 보도 못한 명칭이다. 만약 그런 헌터가 있었다면 아무도 ‘재각성’이라는 단어를 사용하지 않았을 것이다.

재각성은 그다음이 없기 때문에 재각성인 것이니까.

“도련님, 그건.”

난색을 표하려던 그때, 김 집사의 뇌리에 한 사람의 이름이 스쳤다.

‘진태경. 그 청년이라면 모르겠군.’

김 집사는 대격변을 온몸으로 겪은 산증인이다. 눈부신 전공을 세웠고 수많은 전투에 참전했다.

그러나 그의 시선에도 진태경은 특별했다.

‘그 움직임들…… 실로 대단했지.’

때로는 강하게, 혹은 유려하게, 효율적인 공수 전환과 나아갈 때와 물러설 때를 아는 타고난 전투 감각.

진태경의 싸움을 보고 있자면 압도적이라는 표현밖에 떠오르지 않았다.

‘3차 각성자라.’

시간은 걸리겠지만 충분히 알아볼 가치가 있다.

김 집사가 고개를 숙였다.

“알아보겠습니다.”

“고맙습니다. 아, 상동 길드 쪽 동향은 어떤가요?”

“감시원들을 풀었습니다. 아마 며칠 안에 대부분의 정보를 입수할 겁니다.”

임창수가 길드장실로 불려 가 개처럼 맞았다는 정보를 입수한 지 반나절도 되지 않았는데, 벌써 감시원들이 달라붙기 시작했다. 예상보다 빠른 움직임이다.

“목표는 진태경 씨겠군요.”

“주요 인물로 찍어 뒀을 겁니다. 일단은 길드 전체를 샅샅이 분석하겠지만요.”

“다른 길드원들은 어떻습니까?”

“혹시 미행이 붙을 수도 있으니 언질 정도는 해 두었습니다. 그런데…….”

김 집사가 멈칫하더니 덧붙였다.

“진태경 씨한테도 알려 줘야 하지 않겠습니까?”

“괜찮습니다. 전 오히려 상동 길드의 정보력이 우리보다 훨씬 뛰어났으면 하는 바람입니다.”

가장 알 수 없는 인물, 그리고 가장 많은 것이 드러나 있는 인물.

맑은 샘물을 보면서도 그 안에 무엇이 들어 있는지 볼 수가 없는 것과 같다.

최민우는 상동 길드의 힘을 빌려서라도 진태경의 정체에 근접하고 싶은 마음이었다.

“그보다, 상동 길드장이 화가 단단히 났나 봅니다.”

“그래도 많이 신중해진 것 같더군요. 예전 같았으면 진작 쳐들어와 난동을 피웠을 텐데.”

“아, 혹시?”

최민우의 반응에 김 집사가 웃으며 고개를 끄덕였다.

“상동 길드장과는 안면이 있습니다.”

“악연인가요?”

“글쎄요.”

김 집사의 웃음이 진해졌다.



* * *



“무슨 일로?”

이마가 번쩍번쩍 빛나는 부동산 아저씨의 물음에 내가 대답했다.

“집 좀 보려고요.”

“찾으시는 집이 월세? 전세? 아니면…….”

“매매요.”

“어이쿠, 젊은 사장님이셨네. 미안한데 잠시만 기다려 봐요. 내 이것만 처리하고 후딱 올게. 너무 급해서 참을 수가 있어야지.”

뭘 처리하나 했더니, 손에 화장지를 들고 있다.

다른 것도 아니고 그거면 빨리 처리하셔야지. 내가 고개를 끄덕이자 부동산 아저씨가 화장실로 후다닥 뛰어 들어갔다.

“소파에서 뭐라도 드시면서 기다리고 계세요. 탁자에 모카빵. 끄으으으읍.”

푸드득. 푸드드득.

“…….”

앞으로 모카빵은 못 먹겠군.

내심 한탄하며 소파에 몸을 기댔다. 이미 틀어져 있던 TV 화면에서는 대격변 관련 다큐멘터리가 흘러나오고 있었다.



- 꺄아아악!

- 콰과광! 펑!

- 긴급 속보입니다. 현재 전국 곳곳에서 정체불명의 현상들이 벌어지고 있습니다. 이에 정부는 현 시간부로 계엄령을 선포하였으며…….



비명을 지르며 흩어지는 사람들, 무너지는 건물과 솟구치는 화염, 대격변의 시작을 알리는 뉴스가 차례차례 스쳐 지나가고 미국 대통령의 초췌한 얼굴이 화면을 꽉 채웠다.



- 아직 저들의 정체를 파악하지 못했으나 한 가지는 확실합니다. 그들은 우리의 적입니다. 미합중국뿐만이 아닌 전 세계, 전 인류의 적입니다. 지금도 수많은 몬스터가 게이트를 통과해 지구를 침략하고 있습니다.



게이트(Gate).

게이트는 말 그대로 문을 뜻한다. 마왕 아스모데우스는 차원 저 너머에서 이 문을 열고 지구에 강림했다. 헤아릴 수 없이 많은 몬스터 군단과 함께.

‘그 후로는 교과서에 적힌 대로고.’

인류는 속수무책이었다. 도심지, 농촌, 산과 바다, 밀림……. 때와 장소를 가리지 않고 생성되는 게이트와 쏟아지는 괴물들이 살인과 파괴를 일삼았다.

게이트가 열린 후 ‘피의 일주일’이라 불리는 지옥 같은 시간이 끝났을 때, 사상자는 수천만에 달했고 재산 피해는 정확한 집계조차 내지 못할 정도였다.



- 대격변, 인류 역사상 가장 끔찍했던 10년의 역사.



자막과 함께 다큐멘터리가 중반에 접어들 때쯤 화장실 문이 벌컥 열렸다.

“휴, 이제 좀 살겠네.”

부동산 아저씨가 땀으로 번들거리는 이마를 닦으며 털썩 주저앉았다.

“오래 기다리게 해서 미안합니다. 매매 알아보신다고 했죠?”

“네.”

“혹시 다른 곳 들렀다가 오시는 길인가? 오는 길에 부동산 많았을 텐데.”

“아뇨, 여기가 처음이에요.”

“그으래요?”

눈동자를 굴리는 걸 보아하니 호구 잡을까 말까 고민 중인 모양이다. 나는 모른 척하며 쪽지를 내밀었다.

쪽지에는 미리 적어 온 주소지가 적혀 있었다.

“가급적이면 이쪽 매물로 보고 싶은데요.”

“이 주소지면…… 안전 구역인데?”

“네.”

“매매 맞죠? 아까 똥이 급해서 잘못 들었나?”

고개를 끄덕이자 아저씨의 눈이 슬쩍 위아래로 움직인다.

청바지에 흰 티셔츠. 시장에서 인터넷에서 주고 산 2만 원짜리 운동화. 누가 보더라도 결코 있어 보이는 차림은 아니다.

“혹시 직업이 어떻게 되시나?”

“게이트 뜁니다.”

“아, 헌터? 어쩐지. 젊은 분이 성공하셨네.”

아저씨의 얼굴에 웃음꽃이 활짝 피었다. 헌터는 대표적인 고수입 직종 중 하나다. 젊고 잘나가는 헌터들이 고가의 집과 차를 구매하는 것은 그리 드문 일이 아니다.

그가 한결 친절해진 말투로 물었다.

“시세는 대충 알아보셨어요?”

“오면서 인터넷으로 검색해 봤어요.”

“운 좋으시네. 안 그래도 매물이 좀 있긴 하거든요. 어디 보자…….”

아저씨가 몸이 달았는지 바쁘게 여기저기 전화를 걸기 시작한다.

끊고 다시 걸기를 반복하고 5분쯤 지났을까? 그가 스마트폰을 집어넣으며 내 쪽으로 돌아섰다.

“사장님한테 딱 맞는 매물을 찾았는데. 어떻게, 바쁘지 않으면 지금 가서 한번 보실래요?”

“그러죠, 뭐.”

휴가 중인 나로서는 거절할 이유가 없다. 내가 자리에서 일어나자 아저씨가 함박웃음을 지었다.



* * *



부우웅.

승용차 조수석에 앉아 스쳐 가는 풍경을 바라봤다. 줄지어 서 있는 단독 주택과 군데군데 자리한 상가, 놀이터와 학교.

“많이 변했네…….”

내 중얼거림에 아저씨가 슬쩍 곁눈질했다.

“여기 사시던 분이에요?”

“어릴 때요.”

중학교 3학년. 열여섯 살 때니까 지금으로부터 딱 11년 전이다. 이곳에서 태어나고 자랐으니 내게는 고향인 셈이다.

“여기가 10년 전쯤 재개발돼서 많이 바뀌었을 거예요. 원래 낡은 아파트 단지였는데 30분 거리에 협회 지부 세워진다니까 엎어 버린 거지.”

“그렇군요.”

이미 알고 있는 사실이다. 재개발 소식이 들리기가 무섭게 집값이 폭등했고, 몇억씩이나 오른 전세금을 감당할 수 없었던 우리는 이사를 결심했다.

‘아버지가 돌아가신 지 얼마 안 됐을 때였어.’

이사 전날 밤, 숨죽여 우시는 엄마의 모습을 봤다.

그곳이 부모님의 신혼집이었다는 이야기를 들은 건 그로부터 몇 년이나 지난 후였다.

“도착했어요.”

아저씨의 말에 정신을 차렸다. 문을 열고 나오자 마당이 깔린 단독 주택 한 채가 보인다.

“사장님이 말했던 주소가 여기예요. 마침 집주인도 없으니까 후딱 보고 나오자고.”

“아, 잠시만요.”

과거의 향수 때문일까? 낡은 아파트 단지는 이미 허물어지고 없지만 어딘지 모르게 친숙하다.

‘그래도…… 아주 바뀌진 않아서 다행이네.’

재개발을 거친 후에도 남아 있는 옛 풍경들이 있다. 감회에 젖어 주위를 둘러보는 내 모습에 아저씨가 입맛을 다셨다.

“오랜만에 오셔서 좋으신가 보네. 이참에 그냥 동네 한 바퀴 돌고 오실래요?”

“그래도 됩니까?”

“계약하실 거잖아. 아니에요?”

“아뇨. 맞습니다.”

이 집은 어떻게든 사야 한다.

피식 웃은 아저씨가 담배를 꺼내 들었다.

“그럼 편의 봐 드려야지, 동네 한 바퀴 도는 데 얼마나 걸린다고. 여기서 담배 한 대 피우고 있을 테니까 신경 쓰지 말고 다녀와요.”

가볍게 감사를 표한 후 천천히 걷기 시작했다.

‘이 길이 맞나?’

골목을 지나 어린 시절 자주 가던 슈퍼를 발견한 그 순간이었다.

“오빠 어릴 때 여기가 아지트였거든. 중학교 때 담배 막 피울 때 여기 할머니가 나이가 많아서…….”

슈퍼 앞에 주차된 번쩍거리는 외제 차. 대화를 나누던 한 쌍의 남녀가 나를 보고 멈칫했다.

아니, 정확히는 남자 쪽이 그랬다. 고개를 갸웃거리던 그가 내게 다가와 말했다.

“혹시 저 아세요?”
```

## Final English reading copy

```markdown
# Chapter 90

“A week off?”

“Yes. Exactly as you heard.”

Team Leader Choi’s call that evening had been unexpected.

A whole week off? Had something happened to the Guild?

When my thoughts reached that point, I suddenly remembered something.

“Uh, you didn’t have a problem with Sangdong Guild, did you?”

“Sangdong Guild?”

“I mean, because of the Im Changsoo situation…”

“Ah, you don’t need to worry about that. The Guild house remodeling is supposed to be finished in a week.”

It was a relief to hear that nothing had happened. But did people really stop raiding because of Guild house remodeling?

*It’s nice to hear I’m getting a whole week off.*

For the past seven years, I had lived with my eyes fixed straight ahead, running without rest. Lately, I had been going back and forth between the Murim and reality, spending my days without a moment to breathe.

Honestly, I wanted to re—no. This was precisely when I needed to work harder. I spoke in a voice filled with determination.

“Team Leader. I want to work.”

“Ah, but you’ll still receive your full salary during your vacation.”

“Then I’ll see you in a week.”

“……”

“I’m hanging up. I need to eat dinner.”

“…Yes.”

As soon as I ended the call, Hayeon came hurrying over and bowed politely.

“Oppa. The evening meal has been prepared.”

“……Could you stop speaking like that? It’s giving me goose bumps.”

“Switching to casual mode requires a paid purchase.”

“You make asking for allowance sound so complicated.”

When I held out two 50,000-won bills, Hayeon flashed a wide grin.

“Mom says dinner’s ready.”

“Oh, what’s on the menu?”

“Beef bulgogi. And bean sprout soup that I made.”

“Beef bulgogi sounds good.”

“Mom says my bean sprout soup is good. She praised me.”

“Mom’s homemade beef bulgogi never lets you down. It’s always fresh, the best, thrilling.”

“……”

My younger sister was thoroughly pissed off, and the table was covered with Mom’s cooking.

What was so special about vacation? I would eat and sleep to my heart’s content at home.

* * *

Tap.

Choi Minwoo set down his smartphone after ending the call. Butler Kim, seated across the table from him, asked,

“What did he say?”

“He was worried too. About Sangdong Guild.”

“The more I see of him, the more interesting that young man becomes. He seems to act without thinking, yet he’s quick to grasp the situation.”

Choi Minwoo tapped the table with his long fingers.

Even after some time had passed, the sudden appearance of Jin Taekyung remained a mystery.

When they had first met, Taekyung had seemed like nothing more or less than a diligent F-rank Hunter. Yet yesterday, he had single-handedly swept through a B-rank Gate.

*He’s getting stronger.*

As of yesterday, his suspicions had turned into certainty.

Jin Taekyung was getting stronger. And he was doing so incredibly fast.

“Is there no additional information about Jin Taekyung?”

“No. I’ve repeatedly reconfirmed everything, but nothing has turned up.”

Butler Kim was a man who handled his work thoroughly. But this time was different. Choi Minwoo carefully opened his mouth.

“Butler Kim.”

“Yes, Young Master.”

“Could you perhaps look for cases of Hunters who awakened a third time?”

“What?”

Butler Kim’s eyebrows twitched.

A third awakening? It was a term he had never heard or seen in his entire life. If a Hunter like that had existed, no one would have used the word *reawakening*.

A reawakening was called a reawakening because there was nothing after it.

“Young Master, that…”

Just as Butler Kim was about to express his difficulty, a name flashed through his mind.

*Jin Taekyung. If it’s that young man, who knows?*

Butler Kim was a living witness who had experienced the Great Cataclysm firsthand. He had accomplished brilliant feats and participated in countless battles.

Yet even to his eyes, Jin Taekyung was special.

*Those movements… They were truly remarkable.*

Sometimes forceful, sometimes fluid. His transitions between offense and defense were efficient, and he possessed an innate combat sense that told him when to advance and when to retreat.

When Butler Kim watched Jin Taekyung fight, the only word that came to mind was *overwhelming*.

*A third awakening, huh.*

It would take time, but it was worth investigating.

Butler Kim lowered his head.

“I’ll look into it.”

“Thank you. Ah, what are Sangdong Guild’s movements like?”

“They’ve deployed surveillance agents. They’ll probably obtain most of the information within a few days.”

It had not even been half a day since word came that Im Changsoo had been summoned to the Guild Master’s office and beaten like a dog, yet Sangdong Guild’s watchers had already latched on. They were moving faster than expected.

“The target is Jin Taekyung, then.”

“They must have marked him as a major figure. For now, they’ll analyze the entire Guild, though.”

“What about the other Guild members?”

“I’ve warned them in case someone follows them. But…”

Butler Kim hesitated before adding,

“Shouldn’t we tell Jin Taekyung as well?”

“It’s fine. In fact, I hope Sangdong Guild’s intelligence network is far better than ours.”

The person who was hardest to understand—and the person about whom the most had already been revealed.

It was like looking into a clear spring and still being unable to see what lay inside.

Choi Minwoo wanted to use Sangdong Guild’s power, if necessary, to get closer to Jin Taekyung’s true identity.

“More importantly, it seems Sangdong Guild’s Master is extremely angry.”

“He does seem much more cautious than before. If this were the past, he would have barged in and caused a scene by now.”

“Ah. Could it be?”

At Choi Minwoo’s reaction, Butler Kim smiled and nodded.

“I’m acquainted with Sangdong Guild’s Master.”

“An ill-fated relationship?”

“Who knows?”

Butler Kim’s smile deepened.

* * *

“What can I do for you?”

I answered the real estate agent, a man whose forehead shone brightly.

“I’d like to look at some houses.”

“Are you looking for a monthly rental? A jeonse lease? Or perhaps…”

“A house to buy.”

“Well, well. So you’re a young Boss. Sorry, but wait just a moment. Let me take care of this and I’ll be right back. It’s so urgent I can barely hold it.”

I wondered what he needed to take care of, then noticed the toilet paper in his hand.

If that was what he needed to take care of, he should hurry. When I nodded, the real estate agent dashed into the bathroom.

“Have something to eat while you wait on the sofa. There’s some mocha bread on the table. Gnnngh…”

Pfft. Pffft.

“……”

I wouldn’t be able to eat mocha bread ever again.

I lamented inwardly and leaned back against the sofa. On the television, which had already been turned on, a documentary about the Great Cataclysm was playing.

> “Aaaah!”
>
> “Crash! Boom!”
>
> “This is an emergency bulletin. Mysterious phenomena are currently occurring across the country. In response, the government has declared martial law effective immediately…”

People scattered while screaming, buildings collapsed, and flames shot into the sky. News reports announcing the beginning of the Great Cataclysm flashed by one after another, until the exhausted face of the American president filled the screen.

> “We have yet to determine their identity, but one thing is certain. They are our enemies. Not merely the enemies of the United States, but the enemies of the entire world and all of humanity. Even now, countless monsters are passing through Gates and invading Earth.”

Gate.

A Gate meant a door, quite literally. The Demon King Asmodeus had opened that door from beyond another dimension and descended upon Earth with an innumerable army of monsters.

*After that, it went exactly as written in the textbooks.*

Humanity had been helpless. Downtown areas, rural villages, mountains and seas, jungles… Gates appeared regardless of time or place, and the monsters pouring through them committed murder and destruction.

When the hellish period known as the Bloody Week ended after the Gates first opened, the casualties numbered in the tens of millions, while the property damage was so immense that it could not even be calculated accurately.

> The Great Cataclysm: The Ten Most Horrific Years in Human History.

By the time the documentary reached its midpoint alongside the caption, the bathroom door flew open.

“Whew. I feel alive again.”

The real estate agent plopped down after wiping his sweat-slick forehead.

“Sorry to keep you waiting. You said you were looking to buy, right?”

“Yes.”

“Did you happen to visit somewhere else before coming here? There must’ve been plenty of real estate offices on the way.”

“No, this is my first stop.”

“Really?”

Judging by the way his eyes rolled around, he seemed to be deciding whether or not to take me for a fool. I pretended not to notice and held out the note I had prepared.

It had the address written on it.

“I’d prefer to see the property at this address, if possible.”

“With this address… that’s a safe zone.”

“Yes.”

“You really said you wanted to buy, right? Did I hear you wrong because I had to take a dump so badly?”

When I nodded, the man’s eyes traveled subtly up and down.

Jeans and a white T-shirt. A pair of 20,000-won sneakers bought at a market or online. No matter how you looked at it, I was not dressed like someone wealthy.

“What do you do for a living?”

“I run Gates.”

“Oh, a Hunter? I thought so. You’re young and already successful.”

A bright smile blossomed across the man’s face. Hunters were one of the most prominent high-income professions. It was hardly unusual for young, successful Hunters to buy expensive houses and cars.

He asked in a much friendlier tone,

“Have you checked the market prices?”

“I searched online on the way here.”

“Then you’re in luck. There actually happen to be a few listings available. Let’s see…”

Perhaps he was excited by the prospect of a sale, because the man began making calls to one person after another.

He hung up and called again, repeating the process. About five minutes later, he put away his smartphone and turned toward me.

“I found a listing that’s perfect for you, Boss. If you’re not busy, would you like to go take a look right now?”

“Sure. Why not?”

Since I was on vacation, I had no reason to refuse. When I stood up, the man broke into a huge smile.

* * *

Vroom.

I sat in the passenger seat of the sedan and watched the scenery pass by. Detached houses stood in rows, shops dotted the streets here and there, and playgrounds and schools appeared along the way.

“It’s changed a lot…”

The man glanced at me.

“Did you used to live around here?”

“When I was young.”

I had been in my third year of middle school—sixteen years old—so it had been exactly eleven years since then. I had been born and raised here, so in a way, this was my hometown.

“This area was redeveloped about ten years ago, so it must look pretty different. It used to be an old apartment complex, but when they heard an Association branch was going to be built within thirty minutes of here, they tore the whole thing down.”

“I see.”

I already knew that. As soon as news of the redevelopment spread, housing prices skyrocketed. We could not afford the jeonse deposit, which had risen by hundreds of millions of won, so we decided to move.

*It was not long after my father died.*

On the night before we moved, I saw Mom crying silently.

It was several years later that I learned the place had been my parents’ newlywed home.

“We’re here.”

The man’s voice brought me back to myself. When I opened the door and stepped outside, I saw a detached house with a yard.

“This is the address you gave me, Boss. The owner happens to be out, so let’s take a quick look around and get going.”

“Ah, just a moment.”

Maybe it was because of the memories. The old apartment complex had already been demolished, but the area still felt strangely familiar.

*Still… I’m glad it hasn’t changed completely.*

Some traces of the old scenery remained even after the redevelopment. The real estate agent smacked his lips as he watched me look around, lost in nostalgia.

“You must be happy to be back after all this time. Why don’t you take a lap around the neighborhood while you’re at it?”

“Is that okay?”

“You’re going to sign the contract, right?”

“No. I mean, yes.”

This house was something I had to buy, no matter what.

The man let out a quiet laugh and took out a cigarette.

“Then I should accommodate you. It won’t take long to walk around the neighborhood. I’ll stay here and smoke while I wait, so don’t worry about me.”

After offering him a brief word of thanks, I began walking slowly.

*Is this the right way?*

I passed through an alley and found the supermarket I had often visited as a child.

“When I was a kid, this place was my hangout. Back when I smoked like crazy in middle school, the old lady here was so old that…”

A gleaming foreign car was parked in front of the supermarket. A man and woman who had been talking together stopped when they saw me.

No—the man was the one who stopped.

He tilted his head, then approached me and asked,

“Do you know me?”
```
